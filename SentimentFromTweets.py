# ==================== IMPORTS & CONFIG ====================
from itertools import combinations
import tweepy
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns


# Input phrases
word1 = "amafaranga ahwanye urugendo umugenzi yakoze"
word2 = "Distance Based Fare System kigali"

# Match threshold (e.g., 0.7 = 70%)
THRESHOLD = 0.7

# Max tweets to fetch per query
MAX_RESULTS = 100

# Initialize Twitter client and VADER
client = tweepy.Client(bearer_token=bearer_token)
sid = SentimentIntensityAnalyzer()

# QUERY BUILDING 
def get_2_word_phrases(word_list):
    return [' '.join(pair) for pair in combinations(word_list, 2)]

words_kinya = word1.lower().split()
words_eng  = word2.lower().split()

phrases_kinya = get_2_word_phrases(words_kinya)
phrases_eng   = get_2_word_phrases(words_eng)

qk = ' OR '.join(f'"{p}"' for p in phrases_kinya)
qe = ' OR '.join(f'"{p}"' for p in phrases_eng)

query_kinya = f"({qk}) -is:retweet -is:reply"
query_eng   = f"({qe}) lang:en -is:retweet -is:reply"

# FETCH & FILTER
def search_tweets(query):
    try:
        res = client.search_recent_tweets(
            query=query,
            tweet_fields=['created_at','public_metrics','lang','text'],
            max_results=MAX_RESULTS
        )
        return res.data or []
    except Exception as e:
        print("Error fetching tweets:", e)
        return []

def match_score(text, words):
    return sum(1 for w in words if w in text.lower()) / len(words)

def collect_and_filter(tweets, words, lang_tag):
    out = []
    for t in tweets:
        score = match_score(t.text, words)
        if score >= THRESHOLD:
            m = t.public_metrics
            out.append({
                "language": lang_tag,
                "date":     t.created_at,
                "text":     t.text,
                "likes":    m.get("like_count", 0),
                "retweets": m.get("retweet_count",0),
                "views":    m.get("impression_count",0)
            })
    return out

all_raw = []
all_raw += collect_and_filter(search_tweets(query_kinya), words_kinya, "kinya")
all_raw += collect_and_filter(search_tweets(query_eng),  words_eng,  "en")

df = pd.DataFrame(all_raw)
if df.empty:
    raise SystemExit("No tweets matched the threshold.")

# SENTIMENT SCORING
# Engagement-based: (likes + retweets) / views * 100
df["engagement_score"] = (df["likes"] + df["retweets"]) / df["views"].replace(0,1) * 100

# VADER for English, neutral fallback for others
def text_sentiment(row):
    if row["language"] == "en":
        return sid.polarity_scores(row["text"])["compound"] * 100
    else:
        return 0.0

df["text_score"]      = df.apply(text_sentiment, axis=1)
df["text_confidence"] = (df["text_score"].abs() / 100).clip(0,1)

# Weighted combination
df["final_score"] = (
    df["text_confidence"] * df["text_score"]
    + (1 - df["text_confidence"]) * df["engagement_score"]
)

# SAVE RESULTS
df = df.sort_values("final_score", ascending=False)
df.to_csv("tweets_sentiment.csv", index=False)
print("Saved detailed sentiment results to tweets_sentiment.csv")

# VISUALIZATIONS
plt.figure(figsize=(8,4))
sns.histplot(df["final_score"], bins=20, edgecolor='black')
plt.title("Distribution of Combined Sentiment Scores")
plt.xlabel("Final Sentiment Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,4))
sns.scatterplot(
    x="engagement_score", y="final_score",
    hue="language", data=df, alpha=0.7
)
plt.title("Sentiment vs. Engagement Rate")
plt.xlabel("Engagement Rate (%)")
plt.ylabel("Final Sentiment Score")
plt.legend(title="Language")
plt.tight_layout()
plt.show()

df["date_only"] = pd.to_datetime(df["date"]).dt.date
daily = df.groupby("date_only")["final_score"].mean().reset_index()
plt.figure(figsize=(8,4))
plt.plot(daily["date_only"], daily["final_score"], marker='o')
plt.title("Average Daily Sentiment Over Time")
plt.xlabel("Date")
plt.ylabel("Mean Sentiment Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

lang_avg = df.groupby("language")["final_score"].mean().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(x="language", y="final_score", data=lang_avg)
plt.title("Average Sentiment Score by Language")
plt.xlabel("Language")
plt.ylabel("Mean Sentiment Score")
plt.tight_layout()
plt.show()

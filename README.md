# Public Sentiment Analysis on Rwanda’s Distance-Based Transport Fare System

## Overview

This repository contains a comprehensive sentiment analysis project aimed at understanding public perception of Rwanda's recent shift from flat-rate to distance-based fare pricing in public transport. Through data collected from three key field locations and social media (Twitter), the analysis surfaces actionable insights and recommendations for policymakers.

## Background

In an effort to create a fairer and more sustainable public transport system, Rwanda transitioned to a distance-based fare model. While economically beneficial, the policy change has generated diverse reactions across social platforms, local communities, and commuter groups. This project explores these sentiments to help decision-makers gauge acceptance, address concerns, and correct potential misinformation.

## Data Sources

1. **Field Survey Data** (366 participants across three locations)

   * Karama Market (near ADHI houses): [Kaggle Dataset](https://www.kaggle.com/datasets/irakozekelly/karama)
   * Rafiki Club, Nyamirambo: [Kaggle Dataset](https://www.kaggle.com/datasets/irakozekelly/nyamirambo)
   * Remera Bus Station: [Kaggle Dataset](https://www.kaggle.com/datasets/irakozekelly/kacyiru/)

   > *Note: To verify responses, datasets include phone numbers for a subset of participants. Some entries represent second-hand responses provided on behalf of friends due to logistical constraints.*

2. **Social Media Data**

   * Tweets related to Rwanda’s transport fare policy: [Kaggle Dataset](https://www.kaggle.com/datasets/irakozekelly/tweets)

## Project Structure

```
├── data/                   # Raw and processed datasets
│   ├── field_karama.csv
│   ├── field_nyamirambo.csv
│   ├── field_remere.csv
│   └── tweets.csv
├── notebooks/              # Jupyter notebooks for EDA and modeling
│   └── sentiments_from_field_data.ipynb
├── src/                    # Source code for data processing and visualization
│   ├── preprocess.py
│   ├── sentiment_analysis.py
│   └── visualization.py
├── results/                # Figures, dashboards, and reports
│   ├── engagement_over_time.png
│   └── sentiment_summary.html
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## Methodology

1. **Data Ingestion & Cleaning**

   * Load Excel/CSV files; standardize column names and date formats.
   * Normalize language codes and handle missing or infinite values.

2. **Feature Engineering**

   * Compute engagement metrics (likes, retweets, and views ratios).
   * Perform sentiment analysis using TextBlob to derive polarity scores.

3. **Exploratory Data Analysis (EDA)**

   * Distribution of engagement and sentiment across locations and time.
   * Comparative analysis between field data and social media sentiment.

4. **Visualization & Dashboard**

   * Interactive plots (histograms, boxplots, line charts) to illustrate trends.
   * Exportable HTML dashboard summarizing key findings.

5. **Insights & Recommendations**

   * Identification of prevalent concerns, misinformation flags, and positive feedback.
   * Policy suggestions based on sentiment shifts over time and location.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/transport-fare-sentiment.git
   cd transport-fare-sentiment
   ```
2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

* Run notebooks in `notebooks/` for step-by-step analysis and visualization.
* Execute scripts in `src/` for automated preprocessing and figure generation:

  ```bash
  python src/preprocess.py --input data/field_karama.csv --output results/
  python src/visualization.py --input results/enriched_data.csv --output results/
  ```
* Open `results/sentiment_summary.html` in a browser to explore the interactive dashboard.

## Contributing

Contributions and feedback are welcome! Please submit issues or pull requests, ensuring:

* No plagiarism—properly cite any external code or data.
* Minimal reliance on AI-generated content; highlight any AI-assisted components.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

Irakoze Ntawigenga Kelly
Email: [irakoze.kelly@example.com](mailto:irakoze.kelly41@gmail.com)
LinkedIn: [https://www.linkedin.com/in/irakozekelly/]([https://www.linkedin.com/in/irakozekelly/](https://www.linkedin.com/in/irakoze-ntawigenga-kelly-bb194a287/))

---

*Prepared for the Rwanda Transport Fare Sentiment Hackathon*

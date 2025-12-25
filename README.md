# Customer Experience Analytics for Fintech Apps

## Business Objective
This project analyzes Google Play Store reviews for Ethiopian mobile banking applications
to understand customer sentiment, identify key pain points, and extract feature requests.
The goal is to provide actionable insights that help banks improve user experience,
retention, and satisfaction.

Banks analyzed:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

## Task 1: Data Collection and Preprocessing
- Collected Google Play Store reviews for three Ethiopian bank apps
- Minimum of 400 reviews per bank
- Removed duplicate and missing reviews
- Normalized review dates
- Cleaned review text for NLP tasks
- Saved processed data as CSV for downstream analysis

---

## Task 2: Sentiment and Thematic Analysis
- Applied lexicon-based sentiment analysis using VADER
- Generated sentiment scores and labels (positive, neutral, negative)
- Analyzed sentiment distribution by bank
- Extracted key themes and keywords using TF-IDF and rule-based grouping
- Identified major customer pain points and satisfaction drivers

---

## Task 3: PostgreSQL Data Storage
- Designed a relational PostgreSQL schema
- Created `banks` and `reviews` tables
- Inserted cleaned and enriched review data using Python
- Verified data integrity with SQL queries

---

## Task 4: Insights and Recommendations
- Compared sentiment trends across banks
- Identified key drivers (e.g., ease of use, fast navigation)
- Identified pain points (e.g., slow transfers, login errors, crashes)
- Generated visualizations to support findings
- Proposed data-driven recommendations for each bank

---

## Repository Structure

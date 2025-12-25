import psycopg2
import pandas as pd

# Load your CSV
df = pd.read_csv("../data/processed/reviews_with_sentiment.csv")

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="bank_reviews_db",      # your database name
    user="postgres",               # your PostgreSQL username
    password="mahi123",      # password you set during install
    host="localhost",
    port=5432
)
cur = conn.cursor()

# Insert banks (avoid duplicates)
banks = df[['bank_code', 'bank_name']].drop_duplicates()
for _, row in banks.iterrows():
    cur.execute("""
        INSERT INTO banks (bank_code, bank_name)
        VALUES (%s, %s)
        ON CONFLICT (bank_code) DO NOTHING;
    """, (row['bank_code'], row['bank_name']))

# Insert reviews
for _, row in df.iterrows():
    cur.execute("SELECT bank_id FROM banks WHERE bank_code=%s;", (row['bank_code'],))
    bank_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO reviews (bank_id, review_text, rating, review_date, sentiment)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        bank_id,
        row['review_text'],
        row['rating'],
        row['review_date'],
        row['sentiment']
    ))

# Commit and close
conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")

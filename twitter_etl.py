import tweepy
import pandas as pd
import os
from datetime import datetime
from config import BEARER_TOKEN, CSV_PATH

def run_twitter_etl():

    # ---------------- EXTRACT ----------------
    def extract_tweets(query="elon musk", max_results=11):
        client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        wait_on_rate_limit=True
    )


        response = client.search_recent_tweets(
            query=query,
            tweet_fields=["created_at", "public_metrics", "lang"],
            max_results=max_results
        )

        return response.data


    # ---------------- DEBUG PRINT ----------------
    def print_raw_tweets(tweets):
        print("\n🔹 RAW DATA FROM X API (Before Transform):\n")
        for t in tweets:
            print("Tweet ID:", t.id)
            print("Text:", t.text)
            print("Created At:", t.created_at)
            print("Metrics:", t.public_metrics)
            print("Language:", t.lang)
            print("-" * 60)


    # ---------------- TRANSFORM ----------------
    def transform_tweets(tweets):
        records = []
        for tweet in tweets:
            records.append({
                "tweet_id": tweet.id,
                "text": tweet.text,
                "created_at": tweet.created_at,
                "likes": tweet.public_metrics["like_count"],
                "retweets": tweet.public_metrics["retweet_count"],
                "language": tweet.lang,
                "ingested_at": datetime.utcnow()
            })
        return pd.DataFrame(records)


    # ---------------- LOAD ----------------
    def load_to_csv(df):
        os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
        df.to_csv("s3://dikshant-airflow-bucket/data.csv")


    # ---------------- MAIN ----------------
    def run_etl():
        tweets = extract_tweets()

        if tweets:
            # 🔴 PRINT BEFORE TRANSFORM
            print_raw_tweets(tweets)

            df = transform_tweets(tweets)
            load_to_csv(df)
            print("\n✅ Data saved to CSV")
        else:
            print("⚠️ No tweets found")


    if __name__ == "__main__":
        run_etl()

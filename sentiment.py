from google.cloud import language_v1
from tqdm import tqdm
import pandas as pd
import pickle
import time
import traceback
from transformers import pipeline
from ratelimit import limits, RateLimitException, sleep_and_retry

# Instantiates a client
# client = language_v1.LanguageServiceClient()

QUOTA_MIN = 550
ONE_MINUTE = 60


@sleep_and_retry
@limits(calls=QUOTA_MIN, period=ONE_MINUTE)
def get_sentiment_gcloud(text):
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment
    return sentiment

def checkpoint(obj=None):
    with open('sentiment_checkpoint.pickle', 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print("wrote to 'sentiment_checkpoint.pickle'")

if __name__ == "__main__":
    df = pd.read_parquet("./700077347251945472.parquet")
    succeed_idx = []
    sentiments = []
    failed_idx = []
    for i, text in enumerate(tqdm(df["content"])):
        try:
            sentiments.append(document_sentiment(text))
            succeed_idx.append(i)
        except Exception as e:
            print(traceback.format_exc())
            failed_idx.append(i)
        
        if i % (QUOTA_MIN) == 0:
            checkpoint({
                "succeed_idx": succeed_idx,
                "failed_idx": failed_idx,
                "sentiments": sentiments,
            })
        
    with open('sentiments.pickle', 'wb') as handle:
        pickle.dump(sentiments, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    # df["sentiments"] = sentiments
    # df.to_parquet("./700077347251945472_sentiments.parquet")
    
    
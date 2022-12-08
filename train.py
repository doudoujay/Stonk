from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd
import yfinance as yf
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

df = pd.read_parquet("700077347251945472_label_emoji100.parquet")
feats = ["stocktwits_score", "sentiment_score", "diretion_today", "content", "timestamp"] + list(top_100_emoji.keys())

df["stocktwits_score"] = df.stocktwits.apply(lambda x: 0 if x is None else (x[0]['score'] if x[0]['label'] == 'LABEL_1' else -x[0]['score']))
df["sentiment_score"] = df.pipe_sentiment_analysis.apply(lambda x: 0 if x is None else (x[0]['score'] if x[0]['label'] == 'POSITIVE' else -x[0]['score']))
final = df[df['diretion_today'].notna()][feats]
train_data = TabularDataset(final[:int(len(final) * 0.7)])
test_data = TabularDataset(final[int(len(final) * 0.7):])

predictor = TabularPredictor(label='diretion_today').fit(train_data=train_data)
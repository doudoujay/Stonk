# Stonk

```
Ji Ma jima@illinois.edu (Team Leader)
Mingqing Teng 	mt52@illinis.edu
Chien-Wei Chao	cwchao4@illinois.edu
```
Progress report
https://docs.google.com/document/d/1wk3C5U4qwzcBoktKgtSXMX1l6GoSqllvKtHn_o6e3Hs/edit

## Project Proposal 
https://docs.google.com/document/d/1wxmEypdi2GsSCXtskPlX0fHi7yWQZAgnANOVQr6qrF8/edit

## CMT Submission
https://docs.google.com/document/d/1XFvippp_jyiUUXpWsps4Geh5KsyZRkJq/edit

## Project Structure
### requirements
```
pip install -r requirements.txt
```

### Raw Data
Discord. Scrape last two years discord from atlas trading (A popular stock forum)
`700077347251945472.parquet`

### Data Prep & Data Pre Processing
```
alpha.py
ana.ipynb
label_gen.ipynb
```

For each user’s post, we will detect if a valid ticker is presented in the user's post by using Yahoo Finance’s API. Disregard any invalid records.
Disregard any record without the user's reactions. (emoji reactions are required)
Generate ground truth labels by using yahoo finance. Y_true. Which means that if a ticker up / down in a day (groundtruth)


### Feature Engineering
```
user_rank.ipynb
rank_emoji.py
sentiment.py
sentiment.ipynb
```

* Process embedding(vector) from roberta(NLP model) as one of the features.
* Use stocktwits and distilbert for sentiment analysis for each valid record’s user post.
* Process datetime information as day in week, hour in day, etc.
* Emoji reactions to one hot embedding.
* User popularity ranking. Will indicate if a record is from the top 50 / top 100 popular users or not. Bool feature.


### Model Training & Model Selection
Used autogluen. https://auto.gluon.ai/
`train.py` and `train.ipynb`

### Trained Model
`model.zip`

### Interactive UI App
Used gradio
https://gradio.app/

`cs410 project app.rar`
https://superstonk-app.herokuapp.com/


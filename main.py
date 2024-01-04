from openai import OpenAI
import pandas as pd
from finvizfinance.quote import finvizfinance
from finvizfinance.news import News

titolo = "TESLA"
stock = finvizfinance('tsla')
news_df = stock.ticker_news()

news_df.to_csv("qui.csv")

titles_df = news_df.Title
titles_df.to_csv("titoli.csv")

OPENAI_API_KEY = "KEY"
client = OpenAI(api_key=OPENAI_API_KEY)

intro = "ti fornisco in inglese una notizia di finanza e voglio una sentiment analisys del test a riguardo del titolo di " + titolo + " rappresentato con un valore reale compreso tra -1 e 1. VOGLIO SOLO ED ESCLUSIVAMETE IL NUMERO, NO PAROLE. "

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": intro}],
    stream=True,
)

i=0
while i<5:
    
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": intro + titles_df[i]}],
        stream=True,)
    print("\n", titles_df[i])    
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            #print(titles_df[i])
            print(chunk.choices[0].delta.content, end="")
                
    i+=1

import requests
from newspaper import Article
from newspaper import fulltext
from finvizfinance.quote import finvizfinance


def get_news(stock_sym): 
    stock = finvizfinance(stock_sym)
    news_df = stock.ticker_news()

    # news_df.to_csv("news.csv") # salva dataframe
    return news_df


def extract_text(url):
    html = requests.get(url).text
    text = fulltext(html)
    
    if len(text) < 200:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        
    return text
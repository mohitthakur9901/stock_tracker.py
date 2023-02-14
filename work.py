import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api="II3TPB3EHAOK4FR0"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"
news_api="22caa521a03146aca582bff669da9fa7"
my_email=
my_password=
para={
    "apikey":stock_api,
    "symbol":STOCK_NAME,
    "function":"TIME_SERIES_DAILY_ADJUSTED",

}

response=requests.get(url=STOCK_ENDPOINT,params=para)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
previous_data=data_list[0]
previous_closing=previous_data['4. close']
print(previous_closing)
# YESTERDAY CLOSING
day_before_data=data_list[1]
day_before_close=day_before_data['4. close']
print(day_before_close)
up_down=None
diffrence=round(float(previous_closing) - float(day_before_close))
if diffrence > 0 :
    up_down="💰"
elif diffrence < 0:
    up_down="⚠️"

percentage_diffrrence=abs(float(diffrence) / float(previous_closing) * 100)
print(percentage_diffrrence)

if percentage_diffrrence > 5:
    news_para = {
    "apiKey": news_api,
    "q": COMPANY_NAME
    }
    news=requests.get(url=NEWS_ENDPOINT,params=news_para)
    news.raise_for_status()
    news_data=news.json()["articles"]
    articles=news_data[:2]
    new_news_data=[f"{STOCK_NAME}:{up_down}{percentage_diffrrence}\nHEADLINE:{article['title']}, "
                   f"\n Brief:{article['description']}"for article in news_data]
    mail=smtplib.SMTP("smtp.gmail.com")
    mail.starttls()
    mail.login(user=my_email,password=my_password)
    mail.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:STOCK MARKET\n\n{new_news_data}")

































import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API=""
NEWS_API=""




    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "outputsize":"compact",
    "apikey":STOCK_API
}
news_params={
    "q":COMPANY_NAME,
    "apiKey":NEWS_API,
    "pageSize":3
}

response=requests.get(STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
stock_data=list(response.json()["Time Series (Daily)"].items())
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday=float(stock_data[0][1]["4. close"])
#TODO 2. - Get the day before yesterday's closing stock price
day_before=float(stock_data[1][1]["4. close"])
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff=abs(yesterday-day_before)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage=(diff/yesterday)*100
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage>1:
    print(f"get news {percentage}")
## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    # print(articles)
#TODO 9. - Send each article as a separate message via Twilio. 
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    for i in articles:
        message = client.messages \
                        .create(
                            body=f"TSLA:{'🔺up' if yesterday>day_before else '🔻down'} {int(percentage)}%\nHEADLINE:{i['title']}\nBRIEF:{i['content']}",
                            from_='',
                            to=''
                        )

        # print(message.sid)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


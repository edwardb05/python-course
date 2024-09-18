import requests
import datetime as dt
from newsapi import NewsApiClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
STOCK = ["TSLA","DIS","LSCC"]
COMPANY_NAME = ["Tesla Inc", "Disney", 'LSCC']
ALPHAVANTAGE_API_KEY = " B4PW58ELPEBT8D89"
NEWS_API_KEY = "4c1c6b72f1c041cf9cefc34fa8730af3"
GMAILEMAIL = "edpythontest123@gmail.com"
GMAILAPPPWD ="rtgg khgl vebo tuof"
EMAIL = os.getenv('MYEMAIL')

def getyesterdaydate(todaydate):
    # The given date string
    date_str = todaydate

    # Convert the string to a datetime object
    date_obj = dt.datetime.strptime(date_str, "%Y-%m-%d")

    # Subtract one day using timedelta
    day_before = date_obj - dt.timedelta(days=1)

    # Convert back to a string if needed
    day_before_str = day_before.strftime("%Y-%m-%d")
    return(day_before_str)

def getyesterdayclose(data, yesterdaydate):
    try:
        close = float(data["Time Series (Daily)"][yesterdaydate]["4. close"])
        return close
    except  KeyError:
        getyesterdayclose(getyesterdaydate(yesterdaydate))
       
    
def getdailychange(STOCK):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
    params = {
        "symbol": STOCK,
        "apikey": ALPHAVANTAGE_API_KEY
    }
    r = requests.get(url, params=params)
    data = r.json()
    todaydate = data["Meta Data"]["3. Last Refreshed"]
    yesterdaydate = getyesterdaydate(todaydate)
    todayclose = float(data["Time Series (Daily)"][todaydate]["4. close"])
    yesterdayclose = float( getyesterdayclose(data, yesterdaydate))
    change = ((todayclose - yesterdayclose)/(yesterdayclose))*100 # makes it a percent

    return(change)


def getnews(COMPANY_NAME):
    newsapi = NewsApiClient(api_key='4c1c6b72f1c041cf9cefc34fa8730af3')
    all_articles = newsapi.get_everything(
        q=COMPANY_NAME,
        from_param=getyesterdaydate(dt.datetime.now().strftime("%Y-%m-%d")),
        language='en',
        sort_by='relevancy',
        )
    if all_articles["totalResults"] >=3:
        resultsneeded = 3
    else:
        resultsneeded = all_articles["totalResults"]
    headlines= [article["title"] for article in all_articles["articles"][:resultsneeded]]
    desc = [article["description"] for article in all_articles["articles"][:resultsneeded]]
    return(headlines, desc)


def send_email(headlines, desc, change, stock):
    arrow = "🟢↑" if change >= 0 else "🔴↓"
    
    # Creating the email message object
    msg = MIMEMultipart()
    msg['From'] = GMAILEMAIL
    msg['To'] = EMAIL
    msg['Subject'] = f"{stock} {arrow}{change:.2f}%"
    
    # Constructing the message body
    body = f"This is news on {stock}:\n"
    for i in range(len(headlines)):
        body += f"\nHeadline: {headlines[i]}\nDescription: {desc[i]}\n\n"
    
    # Attach the body to the message and ensure it's UTF-8 encoded
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Sending the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Start secure connection
        connection.login(user=GMAILEMAIL, password=GMAILAPPPWD)
        connection.sendmail(
            from_addr=GMAILEMAIL, 
            to_addrs=EMAIL, 
            msg=msg.as_string()
        )
for i in range(len(STOCK)):
    change =getdailychange(STOCK[i])
    if abs(change)>= 1:
        headlines, desc = getnews(COMPANY_NAME[i])
        send_email(headlines,desc,change,STOCK[i])
    else: 
        print (f"no news for {STOCK[i]}")
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


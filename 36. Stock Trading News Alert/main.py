import smtplib
import requests
import secret

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


def generate_message(change_percentage: int, company_article: dict) -> str:
    if change_percentage < 0:
        direction = "🔻"
    else:
        direction = "🔺"
    msg = f"Subject:{STOCK_NAME}: {direction}{abs(change_percentage)}%\n\nHeadline: {company_article["title"]}\nBrief: {company_article["description"]}"
    return msg

def send_email(email: str, msg: str) -> None:
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=secret.my_email, password=secret.password)
        connection.sendmail(from_addr=secret.my_email, to_addrs=email, msg=msg)

def get_stock_data(company: str) -> tuple:
    API_URL="https://www.alphavantage.co/query"
    params = {
        "function":"TIME_SERIES_MONTHLY",
        "symbol": company,
        "datatype": "json",
        "apikey": secret.ALPHAVANTAGE_API_KEY
    }

    response = requests.get(API_URL, params=params, timeout=20)
    response.raise_for_status()

    return response.json()

def stock_price_change(company: str) -> bool:
    monthly_stock_data = get_stock_data(company)["Monthly Time Series"]

    stock_from_last_2_days = []

    for count, data in enumerate(monthly_stock_data.items()):
        if count > 1:
            break
        stock_from_last_2_days.append(data)
    
    date_to = stock_from_last_2_days[0][0]
    date_from = stock_from_last_2_days[1][0]

    close_price_to = float(stock_from_last_2_days[0][1]['4. close'])
    close_price_from = float(stock_from_last_2_days[1][1]['4. close'])
    
    change_percent = round(((close_price_from - close_price_to) / close_price_to ) * 100)
    return (date_from, date_to, change_percent)

def get_company_news(from_data: str, to_date: str, company: str) -> dict:
    API_URL="https://newsapi.org/v2/everything"
    params = {
        "q": company,
        "searchIn": "title",
        "language": "en",
        "form": from_data,
        "to": to_date,
        "sortBy": "popularity",
        "apiKey": secret.NEWS_API_KEY
    }

    response = requests.get(API_URL, params=params, timeout=20)
    response.raise_for_status()

    return response.json()

def get_company_top_articles(from_data: str, to_date: str, company: str, how_many: int) -> list:
    return get_company_news(from_data, to_date, company)["articles"][:how_many]

previous_day, day_before_previous, percent = stock_price_change(STOCK_NAME)

if percent > 1:
    articles = get_company_top_articles(previous_day, day_before_previous, COMPANY_NAME, 3)
    for article in articles:
        message = generate_message(percent, article)
        send_email(secret.to_email, message)

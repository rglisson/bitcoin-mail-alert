import requests
from bs4 import BeautifulSoup
import time
import os
import smtplib

url = "https://cryptowat.ch"
headers = {
    "User-Agents" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_SENDER = os.environ.get('EMAIL_SENDER')

def Check_price():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    price = soup.find_all("span", {"class":"price"})
    bitcoin = float(price[0].get_text())
    time.sleep(10)
    print(bitcoin)
    return bitcoin

def alert():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = 'Bitcoin price'
        body = 'Bitcoin price is now ' + str(last_price)
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_SENDER, msg)

while True:
    last_price = 11350.0
    if (last_price > Check_price()):
        alert()
        print(Check_price())
   # time.sleep(10)


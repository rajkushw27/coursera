import requests
from bs4 import BeautifulSoup
import smtplib


def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("rajkushwaha2705@gmail.com", "yntthiodulkwncar")

    subject = "Price Fell Down"
    global URL
    body = f'check the amazon link {URL}'

    msg = f'Subject: {subject}\n\n {body}'

    server.sendmail(
        "rajkushwaha2705@gmail.com",
        "rajkushwaha2705@gmail.com",
        msg
    )
    print("mail sent")


URL = 'https://www.amazon.in/Sony-WH-1000XM4-Cancelling-Headphones-Bluetooth/dp/B0863TXGM3/ref=sr_1_1?adgrpid=67315731764&dchild=1&ext_vrnc=hi&gclid=Cj0KCQjwssyJBhDXARIsAK98ITQJKqFcbGYH6DfwTZvXkTW9Z182q7cco-eUiDlDSQ23LwrFhZH0RsIaAnzCEALw_wcB&hvadid=398053963642&hvdev=c&hvlocphy=20471&hvnetw=g&hvqmt=e&hvrand=15982473760140431380&hvtargid=kwd-972690669745&hydadcr=18845_1972026&keywords=sony+headphone+xm4&qid=1630756421&sr=8-1'

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text().strip()

price = int(soup.find(id='priceblock_dealprice').get_text(
).strip().replace(',', '')[1:6])

if price > 20000:
    sendEmail()

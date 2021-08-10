import telebot
from bs4 import BeautifulSoup
import requests

counter = 1
url = f'https://www.wildberries.ru/catalog/28252553/detail.aspx?targetUrl=MS'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
bot = telebot.TeleBot('token')

while 1:
    urlnow = f'https://www.wildberries.ru/catalog/28252553/detail.aspx?targetUrl=MS'
    responsenow = requests.get(urlnow)
    soupnow = BeautifulSoup(responsenow.content, 'html.parser')
    counter += 1
    if soupnow.find_all('button', 'btn-main', 'hide') != soup.find_all('button', 'btn-main', 'hide'):
        send = 'В наличии'
        bot.send_message('telegram id', send)
        break
    if counter % 1800 == 0:
        bot.send_message('telegram id', 'Работаю')

bot.polling(none_stop=True)

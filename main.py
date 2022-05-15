import telebot
from googlesearch import search

bot = telebot.TeleBot('5278087741:AAENlRjw8_F2bdHaUsjgxxadSAS0cP6zVCU')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Salom. Men googledan ma\'lumot qidiruvchi botman.\n\nBiror so\'z kiriting: misol uchun [news]')
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    search_result = search(message.text, num_results=10)
    bot.send_message(message.chat.id, "Please wait / Iltimos kuting...")
    for result in search_result:
        bot.send_message(message.chat.id, result)
        
if __name__ == '__main__':
    bot.polling(none_stop=True)
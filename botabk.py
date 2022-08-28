import time
import requests
import telebot
from telebot import util
from telebot import types
from bs4 import BeautifulSoup
tokin = "5787009857:AAEjizv_TzKEKrqVTotUcu5FwiS0uBWpcB8" #tokin bot

def check_user(user_id):
    global tokin
    request = requests.get(
        f"https://api.telegram.org/bot{tokin}/getChatMember?chat_id=@SMOKA_28&user_id={user_id}"
    ).text
    if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
        return False
    else:
        return True
while True:
    try:
        bot = telebot.TeleBot(tokin)
        @bot.message_handler(commands=['start'])
        def welcome(message):
            name = message.from_user.username 
            ID = message.chat.id
            first = message.from_user.first_name
            channel = types.InlineKeyboardButton(
                text="Channel Developer ",
                url="https://t.me/SMOKA_28")
            if check_user(message.from_user.id):
                normal = types.InlineKeyboardButton(text="Normal Apps",callback_data="normal")
                hack = types.InlineKeyboardButton(text="Hacked Apps",callback_data="hack")
                programmer = types.InlineKeyboardButton(text="مراسلة المطور ",url="https://t.me/smoka28")
                Keyboards = types.InlineKeyboardMarkup()
                Keyboards.row_width = 1
                Keyboards.add(normal,hack,programmer)
                
                bot.send_photo(message.chat.id, 'https://ibb.co/TK6S8vJ', caption=f"""<strong>🌹| Hi  {message.from_user.first_name} 👋 \n Please choose one of the search sections  </strong>""" ,parse_mode='html', reply_markup=Keyboards)
            else:
                Keyboard = types.InlineKeyboardMarkup()
                Keyboard.row_width = 1
                Keyboard.add(channel)
                bot.reply_to(message,text=f"مرحبا {message.from_user.first_name} \n من فضلك اشترك بقناه المطور ثم حاول تشغيل البوت مجددا /start",reply_markup=Keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def bot_query_handler(call):
            if call.data == "normal":
                normal(call.message)
            elif call.data == "hack":
                hack(call.message)
            
        def normal(message):
            msg = bot.send_photo(message.chat.id, 'https://ibb.co/NT5RpCx', caption=f"""<strong>Enter the name of the normal app 🔎</strong>""" ,parse_mode='html')
            bot.register_next_step_handler(msg, run_watch)
            
            
        def run_watch(message):
        	global msg
        	msg = message.text
        	try:
	        	start = bot.send_message(message.chat.id,f'Searching.')
	        	time.sleep(0.5)
	        	bot.edit_message_text(text=f'Searching..',chat_id=int(message.chat.id),message_id=start.message_id)
	        	time.sleep(0.5)
	        	bot.edit_message_text(text=f'Searching...',chat_id=int(message.chat.id),message_id=start.message_id)
	        	re=requests.get(f"https://ar.uptodown.com/android/search/{msg}")
	        	soup = BeautifulSoup(re.text,"html.parser")
	        	getUrlAction = str(soup.find_all("div",{ "class":"item"}))
	        	bs = BeautifulSoup(getUrlAction,"html.parser")
	        	li = []
	        	lli = []
	        	for link in bs.findAll('a'):
	        		lin=(link.get("href"))
	        		li.append(lin)
	        	link=(li[0]+"/download")
	        	ree=requests.get(link)
	        	soup = BeautifulSoup(ree.text,"html.parser")
	        	getUrlAction = str(soup.find_all("div",{ "class":"button-group"}))
	        	bs = BeautifulSoup(getUrlAction,"html.parser")
	        	lit = []
	        	for link in bs.findAll('a'):
	        		lin=(link.get("href"))
	        		lli.append(lin)
	        	for i in bs:
	        		i=i.text
	        		lit.append(i)
	        	titl=(lit[1])
	        	title=titl.replace("تنزيل","").replace("مجانًا","").replace(" ","").replace("\n","")
	        	url=(lli[0])
	        	bot.edit_message_text(text=f'Searching.',chat_id=int(message.chat.id),message_id=start.message_id)
	        	bot.edit_message_text(text=f'Searching..',chat_id=int(message.chat.id),message_id=start.message_id)
	        	link = types.InlineKeyboardButton(text=title,url=url)
	        	Keyboards = types.InlineKeyboardMarkup()
	        	Keyboards.row_width = 1
	        	Keyboards.add(link)
	        	bot.send_photo(message.chat.id, 'https://ibb.co/VwwnwHh',parse_mode='html',reply_markup=Keyboards)
	        except:
	        	bot.send_message(message.chat.id,f"Sorry, I couldn't find your search ❗️")
        def hack(message):
            mssg = bot.send_photo(message.chat.id, 'https://ibb.co/njcypCN', caption=f"""<strong>Enter the name of the hacked app 🔎</strong>""" ,parse_mode='html')
            bot.register_next_step_handler(mssg, info1)
        def info1(message):
        	mssg = message.text
        	try:
	        	start = bot.send_message(message.chat.id,f'Searching.')
	        	time.sleep(0.5)
	        	bot.edit_message_text(text=f'Searching..',chat_id=int(message.chat.id),message_id=start.message_id)
	        	time.sleep(0.5)
	        	bot.edit_message_text(text=f'Searching...',chat_id=int(message.chat.id),message_id=start.message_id)
	        	re=requests.get(f"https://apkbaba.com/?s={mssg}")
	        	soup = BeautifulSoup(re.text,"html.parser")
	        	getUrlAction = str(soup.find_all("div",{ "class":"cont"}))
	        	bs = BeautifulSoup(getUrlAction,"html.parser")
	        	li = []
	        	lli = []
	        	for link in bs.findAll('a'):
	        		lin=(link.get("href"))
	        		li.append(lin)
	        	link=str(li[0])
	        	m=link.split("https://apkbaba.com/")[1]
	        	link2=("https://apkbaba.com/download/"+m)
	        	ree=requests.get(link2)
	        	s=(ree.text)
	        	titl=str(s.split('''display:none;">''')[1].split('''</span>''')[0]).replace("جاري التنزيل","")
	        	
	        	souup = BeautifulSoup(ree.text,"html.parser")
	        	for link in souup.findAll("a"):
	        		lin=(link.get("href"))
	        		if "up" in lin:
	        			lli.append(lin)
	        	linnk=(lli[0])
	        	bot.edit_message_text(text=f'Searching.',chat_id=int(message.chat.id),message_id=start.message_id)
	        	bot.edit_message_text(text=f'Searching..',chat_id=int(message.chat.id),message_id=start.message_id)
	        	link = types.InlineKeyboardButton(text=titl,url=linnk)
	        	Keyboards = types.InlineKeyboardMarkup()
	        	Keyboards.row_width = 1
	        	Keyboards.add(link)
	        	bot.send_photo(message.chat.id, 'https://ibb.co/VwwnwHh',parse_mode='html',reply_markup=Keyboards)
	        except:
	        	bot.send_message(message.chat.id,f"Sorry, I couldn't find your search ❗️")

        try:
            
            bot.polling(True)
        except Exception as ex:
            print(ex)
            telebot.logger.error(ex)
    except:
        continue
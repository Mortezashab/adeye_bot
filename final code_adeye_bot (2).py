# import telebot
# import time
from telebot import *
from telebot.types import*
from khayyam import*
from aiogram import *

API_TOKEN = '5976656437:AAFs9rTzCdWJHBvxQkykXvOaqSYqmHd2pPs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    time = JalaliDatetime.today().strftime('%A %d %B %Y')
    await message.reply(" امروز{}\n برای ادامه انتخاب کنید /help".format(time))

@dp.message_handler(commands=['help'])
async def sen_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True ,row_width=5  , one_time_keyboard=True)
    itembtn1 = types.KeyboardButton("زیارت عاشورا")
    itembtn2 = types.KeyboardButton("دعای عهد")
    itembtn3 = types.KeyboardButton("دعای عرفه")
    itembtn4 = types.KeyboardButton("دعای سماوات")
    itembtn5 = types.KeyboardButton("حدیث کساء")
    markup.add(itembtn1).add(itembtn2).add(itembtn3).add(itembtn4).add(itembtn5)
    await message.reply( "انتخاب کنید" , reply_markup = markup)


# @dp.message_handler(commands=['دعای عهد'])
# async def send_doaye_ahd(message):
#     link = 'https://bayanbox.ir/download/1408450609350107105/%D8%AF%D8%B9%D8%A7%DB%8C-%D8%B9%D9%87%D8%AF.pdf'
#     link2 = "https://www.erfan.ir/files/sound/mafatih/30_ahd_01.mp3"
#     await message.reply_document(document=link,caption='دعای عهد')
#     await message.reply_audio(audio=link2 , caption='صوت دعای عهد')


# @dp.message_handler(commands=['دعای عرفه'])
# async def send_duaye_arafe(message):
#     link = "https://salamdonya.com/assets/file/2021/07/dua-arafeh.pdf"
#     link2 = "https://dl.yasdl.com/user3/Behnam/2014/July/Media/Arafe-MosaviGhahar_YasDL.com.mp3"
#     await message.reply_document(document=link,caption='دعای عرفه')
#     await message.reply_document(document=link2,caption='صوت دعای عرفه')
    


# @dp.message_handler(commands=['دعای سماوات'])
# async def send_doaye_samavat(message):
#     link = 'https://salamdonya.com/assets/file/2021/05/doa-samat-ba-tarjomeh.pdf'
#     link2 = "https://www.erfan.ir/files/sound/mafatih/316_162_2.mp3"
#     await message.reply_document(document=link,caption="دعای سماوات")
#     await message.reply_document(document=link2,caption="دعای سماوات")


# @dp.message_handler(commands=['حدیث کساء'])
# async def send_hadis_kasa(message):
#     link = 'https://salamdonya.com/assets/file/2022/08/hadis-kisa-ba-tarjome.pdf'
#     link2 = "https://v.delgarm.com/mp3/804/2021/09/27/1632758036_S3nD3.mp3"
#     await message.reply_document(document=link,caption="حدیث کساء")
#     await message.reply_document(document=link2,caption="صوت حدیث کساء")


# @dp.message_handler(commands=['زیارت عاشورا'])
# async def send_zyarat_asura(message : types.Message):
#     link = "http://www.coca.ir/wp-content/uploads/2017/09/%D8%B2%DB%8C%D8%A7%D8%B1%D8%AA-%D8%B9%D8%A7%D8%B4%D9%88%D8%B1%D8%A7-pdf.pdf"
#     link2 = "https://files.namnak.com/aup/202004/224.mp3"
#     await message.reply_document(document=link,caption='زیارت عاشورا')
#     await message.reply_document(document=link2 , caption='صوت زیارت عاشورا')


@dp.message_handler()
async def asura(message: types.Message):
    
    
    if message.text == "زیارت عاشورا" or message.text.lower() == "zyarat asura" or message.text.lower() == "zyarat_asura" or message.text== 'عاشورا':

        link = "http://www.coca.ir/wp-content/uploads/2017/09/%D8%B2%DB%8C%D8%A7%D8%B1%D8%AA-%D8%B9%D8%A7%D8%B4%D9%88%D8%B1%D8%A7-pdf.pdf"
        link2 = "https://files.namnak.com/aup/202004/224.mp3"
        await message.reply_document(document=link,caption='زیارت عاشورا')
        await message.reply_document(document=link2 , caption='صوت زیارت عاشورا')
    
    
    elif message.text == "دعای عهد" or message.text.lower() == "doaye_ahd" or message.text.lower() == "doaye ahd" or message.text=='عهد':
        link = "https://salamdonya.com/assets/file/2021/07/dua-arafeh.pdf"
        link2 = "https://www.erfan.ir/files/sound/mafatih/30_ahd_01.mp3"
        await message.reply_document(document=link,caption='دعای عهد')
        await message.reply_document(document=link2 , caption='صوت دعای عهد')

    
    
    elif message.text == "دعای عرفه" or message.text.lower() == "duaye_arafe" or message.text.lower() == "duaye arafe" or message.text == 'عرفه':
        
        link = "https://salamdonya.com/assets/file/2021/07/dua-arafeh.pdf"
        link2 = "https://dl.yasdl.com/user3/Behnam/2014/July/Media/Arafe-MosaviGhahar_YasDL.com.mp3"
        await message.reply_document(document=link,caption="دعای عرفه")
        await message.reply_document(document=link2,caption="دعای عرفه")

    
    
    elif message.text == "حدیث کساء"or message.text=='حدیث کسا' or message.text.lower() == "hadis_kasa" or message.text.lower() == "hadis kasa" or message.text.lower() == "کسا" or message.text.lower() == "kasa" :
        link = 'https://salamdonya.com/assets/file/2022/08/hadis-kisa-ba-tarjome.pdf'
        link2 = "https://v.delgarm.com/mp3/804/2021/09/27/1632758036_S3nD3.mp3"
        await message.reply_document(document=link,caption='حدیث کسا')
        await message.reply_document(document=link2,caption="صوت حدیث کسا")
    
    
    elif message.text == "doaye_samavat" or message.text.lower() == "doaye samavat" or message.text.lower() == "دعای سماوات" or message.text == 'سماوات' or message.text.lower() == 'samavat':
        link = 'https://salamdonya.com/assets/file/2021/05/doa-samat-ba-tarjomeh.pdf'
        link2 = "https://www.erfan.ir/files/sound/mafatih/316_162_2.mp3"
        await message.reply_document(document=link,caption="دعای سماوات")
        await message.reply_document(document=link2,caption="دعای سماوات")

    elif message.text == 'سلام' or message.text.lower() == "salam" :
        await message.reply(text='سلام\nخوش امدید \nبرای استفاده از ربات می توانید ادعیه مورد نظر را سرچ کنید \nیا از /help استفاده کنید\n  ')
    
    else:
        
       await message.reply(text='خطایی پیش امده ! \n برای ادامه انتخاب کنید /help') 

           


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

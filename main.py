from config import TOKEN     # bu yerda tokenni(config.py fayillimizdan) chaqirib oldik
import logging 
from aiogram import Bot, Dispatcher, executor, types
from buttons import *      # bu yerda knopkalarimizni chaqirib oldik (buttons.py dan)
from aiogram.types import Message,CallbackQuery
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("<b>Tilni tanlang!</b>",parse_mode='HTML',reply_markup=til)

 

@dp.message_handler(text="🇺🇿 O'zbekcha")
async def uzbekcha_uchun(message: types.Message):
    await message.answer("<b>Manzilingizni kiriting!</b>",parse_mode='HTML',reply_markup=joy)


#buyurtma uchun

@dp.message_handler(text="Yunusobod")
async def buyr(message: types.Message):
    await message.answer("<b> Yunusobod tumani uchun buyurtma </b>",parse_mode = 'HTML',reply_markup = zakaz)

@dp.message_handler(text="Chilonzor")
async def buyr(message: types.Message):
    await message.answer("<b> Chilonzor tumani uchun buyurtma </b>",parse_mode = 'HTML',reply_markup = zakaz)    

@dp.message_handler(text="Olmozor")
async def buyr(message: types.Message):
    await message.answer("<b> Olmozor tumani uchun buyurtma </b>",parse_mode = 'HTML',reply_markup = zakaz)

@dp.message_handler(text="Sergili")
async def buyr(message: types.Message):
    await message.answer("<b> Sergili tumani uchun buyurtma </b>",parse_mode = 'HTML',reply_markup = zakaz)

@dp.message_handler(text="Yangobod")
async def buyr(message: types.Message):
    await message.answer("<b> Yangobod tumani uchun buyurtma </b>",parse_mode = 'HTML',reply_markup = zakaz)

@dp.message_handler(text="Yakkasaroy")
async def buyr(message: types.Message):
    await message.answer("<b> Yakkasaroy tumani uchun buyurtma </b>",parse_mode = 'HTML',reply_markup = zakaz)



#Menyu uchun

@dp.callback_query_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu) 

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu) 

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu) 

@dp.message_handler(text="buy")
async def men(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan birini tanlang </b>",parse_mode = 'HTML',reply_markup = menu)                            





# lavash uchun menu

@dp.callback_query_handler(text="lavash")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavash1.jpg','rb'),
        caption="""Lavashlar Menusi""",reply_markup = lavash_menyu1)
    await call.message.delete()                                                                    

@dp.callback_query_handler(text="lavash1")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavash2.jpg','rb'),
        caption="""Narxi: 19000 so'm💵
        Tarkibi""",reply_markup = lavash_menyu2)
    await call.message.delete()     

@dp.callback_query_handler(text="lavash2")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang \nSiz tanlagan Lavash: 🌯Classic mini lavash \nNarxi: 17000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = lavash_menyu3)

@dp.callback_query_handler(text="lavash3")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang \nSiz tanlagan Lavash: 🧀Pishloqli lavash \nNarxi: 20000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = lavash_menyu4)

@dp.callback_query_handler(text="lavash4")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang \nSiz tanlagan Lavash: 🧀Pishloqli mini lavash \nNarxi: 18000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = lavash_menyu5)

@dp.callback_query_handler(text="lavash5")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang \nSiz tanlagan Lavash: 🥖Tandir lavash \nNarxi: 20000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = lavash_menyu6)

@dp.callback_query_handler(text="lavash6")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang \nSiz tanlagan Lavash: 🥖Tandir pishloqli🧀 lavash \nNarxi: 21000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = lavash_menyu7)

@dp.callback_query_handler(text="lavash7")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang \nSiz tanlagan Lavash: 🌶Qalampirli lavash \nNarxi: 19000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = lavash_menyu8)




#burger_uchun_menu

@dp.callback_query_handler(text="burger")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/burger1.jpg','rb'),
        caption="""Burger Menusi""",reply_markup = burger_menu1)
    await call.message.delete()           

@dp.callback_query_handler(text="burger1")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/burger2.jpg','rb'),
        caption="""Narxi: 20000 so'm💵
Tarkibi: Non, kotlet, salat bargi, piyoz, tuzlangan bodring, pomidor, sous, moyonez
Miqdorini tanlang yoki kiriting!""",reply_markup = burger_menu2)
    await call.message.delete()

@dp.callback_query_handler(text="chiz")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/burger3.jpg','rb'),
        caption="""Narxi: 22000 so'm💵
Tarkibi: Non, kotlet, pishloq, salat bargi, piyoz, tuzlangan bodring, pomidor, sous, moyonez
Miqdorini tanlang yoki kiriting!""",reply_markup = burger_menu2)
    await call.message.delete() 


#shourma uchun menu


@dp.callback_query_handler(text="shourma")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma1.jpg','rb'),
        caption="""🌮Shourma Menusi""",reply_markup = shourma_menu1)
    await call.message.delete()


@dp.callback_query_handler(text="gush_shourma")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma2.jpg','rb'),
        caption="""🌮Mol go'shtli shourmani tanlang""",reply_markup = shourma_menu2)
    await call.message.delete() 


@dp.callback_query_handler(text="tov_shourma")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma3.jpg','rb'),
        caption="""🌮Tovuq go'shtli shourmani tanlang""",reply_markup = shourma_menu3)
    await call.message.delete() 


@dp.callback_query_handler(text="g_shourma")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma4.jpg','rb'),
        caption="""🌮Mol+qalampir go'shtli shourmani tanlang""",reply_markup = shourma_menu4)
    await call.message.delete() 

@dp.callback_query_handler(text="t_shourma")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma5.jpg','rb'),
        caption="""🌮Tovuq+qalampir go'shtli shourmani tanlang""",reply_markup = shourma_menu5)
    await call.message.delete()         



@dp.callback_query_handler(text="mini1")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma6.jpg','rb'),
        caption="""Narxi: 19000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu6)
    await call.message.delete() 


@dp.callback_query_handler(text="classic1")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma7.jpg','rb'),
        caption="""Narxi: 22000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu7)
    await call.message.delete()

@dp.callback_query_handler(text="mini2")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma8.jpg','rb'),
        caption="""Narxi: 18000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu8)
    await call.message.delete()    


@dp.callback_query_handler(text="classic2")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma9.jpg','rb'),
        caption="""Narxi: 20000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu9)
    await call.message.delete()

@dp.callback_query_handler(text="mini3")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma10.jpg','rb'),
        caption="""Narxi: 20000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu10)
    await call.message.delete()


@dp.callback_query_handler(text="classic3")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma11.jpg','rb'),
        caption="""Narxi: 23000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu11)
    await call.message.delete()


@dp.callback_query_handler(text="mini4")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma12.jpg','rb'),
        caption="""Narxi: 19000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu12)
    await call.message.delete()


@dp.callback_query_handler(text="classic4")
async def burger(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shourma13.jpg','rb'),
        caption="""Narxi: 22000 so'm💵
Tarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = shourma_menu13)
    await call.message.delete()






# Hod dog uchun menu

@dp.callback_query_handler(text="hod")
async def hoddog(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog1.jpg','rb'),
        caption="""🌭Hod-Dog Menu""",reply_markup = hoddog_menu1)
    await call.message.delete() 


@dp.callback_query_handler(text="clas1")
async def hoddog(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog2.jpg','rb'),
        caption="""🌭Hod-Dog Menu""",reply_markup = hoddog_menu2)
    await call.message.delete()


@dp.callback_query_handler(text="kar1")
async def hoddog(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🌭Hod-Dog Menu""",reply_markup = hoddog_menu3)
    await call.message.delete()

 
@dp.callback_query_handler(text="clas2")
async def hoddog(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog4.jpg','rb'),
        caption="""Narxi: 10000 so'm💵
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = hoddog_menu4)
    await call.message.delete()          

@dp.callback_query_handler(text="kar2")
async def hoddog(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog5.jpg','rb'),
        caption="""Narxi: 11000 so'm💵
Tarkibi: Kulcha,sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = hoddog_menu5)
    await call.message.delete()


@dp.callback_query_handler(text="clas3")
async def hoddog(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog6.jpg','rb'),
        caption="""Narxi: 13000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = hoddog_menu6)
    await call.message.delete()

@dp.callback_query_handler(text="kar3")
async def hoddog(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = hoddog_menu7)
    await call.message.delete()    

# Donar uchun menu


@dp.callback_query_handler(text="donar")
async def donar(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥙Donar Menu""",reply_markup = donar_menu1)
    await call.message.delete()



@dp.callback_query_handler(text="d_tovuq")
async def donar(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/donarg.jpg','rb'),
        caption="""Narxi: 20000 so'm💵
Tarkibi: Kulcha, Mol go'shti, sous,qovurilgan piyoz,pomidor,bodring. 
Miqdorini tanlang yoki kiriting!""",reply_markup = donar_menu2)
    await call.message.delete()

@dp.callback_query_handler(text="d_gusht")
async def donar(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/donart.jpg','rb'),
        caption="""Narxi: 18000 so'm💵
Tarkibi: Kulcha, Tovuq go'shti, sous,qovurilgan piyoz,pomidor,bodring. 
Miqdorini tanlang yoki kiriting!""",reply_markup = donar_menu3)
    await call.message.delete()    


# @dp.callback_query_handler(text="donar")
# async def burger(call:CallbackQuery):
#     await call.message.answer("<b>Donarni tanlang🥙 </b>",parse_mode = 'HTML',reply_markup = donar_menu1)

# @dp.callback_query_handler(text="d_tovuq")
# async def burger(call:CallbackQuery):
#     await call.message.answer("<b>Siz tanlagan donar: \nTovuqli Donar🥙 \nNarxi 19000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = donar_menu2)

# @dp.callback_query_handler(text="d_gusht")
# async def burger(call:CallbackQuery):
#     await call.message.answer("<b>Siz tanlagan donar: \nGo'shtli Donar🥙 \nNarxi 22000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = donar_menu3) 


# Sendvich Uchun menu


@dp.callback_query_handler(text="send")
async def sendvich(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvich1.jpg','rb'),
        caption="""🥪Sendvich Menu""",reply_markup = sendvich_menu1)
    await call.message.delete()


@dp.callback_query_handler(text="t_send1")
async def sendvich(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvich3.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Tostr non. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sendvich_menu2)
    await call.message.delete()


@dp.callback_query_handler(text="t_send2")
async def sendvich(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvich3.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sendvich_menu3)
    await call.message.delete()




# @dp.callback_query_handler(text="send")
# async def sendvich(call:CallbackQuery):
#     await call.message.answer("<b>Sendvichni tanlang🥪 </b>",parse_mode = 'HTML',reply_markup = sendvich_menu1)

# @dp.callback_query_handler(text="t_send1")
# async def sendvich(call:CallbackQuery):
#     await call.message.answer("<b>Siz tanlagan \nTuxumli Sendvich🍳🥪 \nNarxi: 17000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sendvich_menu2)

# @dp.callback_query_handler(text="t_send2")
# async def sendvich(call:CallbackQuery):
#     await call.message.answer("<b>Siz tanlagan \nTovuqli Sendvich🍗🥪 \nNarxi: 19000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sendvich_menu3)


#Desertlar uchun menu



@dp.callback_query_handler(text="desert")
async def desert(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🍰Desert Menu""",reply_markup = sendvich_menu1)
    await call.message.delete()

@dp.callback_query_handler(text="medovik")
async def desert(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = desert_menu2)
    await call.message.delete()


@dp.callback_query_handler(text="chizkey")
async def desert(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = desert_menu3)
    await call.message.delete()

@dp.callback_query_handler(text="q_pon")
async def desert(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = desert_menu4)
    await call.message.delete()

@dp.callback_query_handler(text="sh_pon")
async def desert(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = desert_menu5)
    await call.message.delete()



# @dp.callback_query_handler(text="desert")
# async def desert(call:CallbackQuery):
#     await call.message.answer("<b>Desertni tanlang🍰 </b>",parse_mode = 'HTML',reply_markup = desert_menu1)

# @dp.callback_query_handler(text="medovik")
# async def desert(call:CallbackQuery):
#     await call.message.answer("<b>Desertni tanlang🍰 \nSiz tanlagan desert: Asalli Medovik🧁 \nNarxi: 13000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = desert_menu2)

# @dp.callback_query_handler(text="chizkey")
# async def desert(call:CallbackQuery):
#     await call.message.answer("<b>Desertni tanlang🍰 \nSiz tanlagan desert: Chizkeyk🍰 \nNarxi: 12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = desert_menu3)

# @dp.callback_query_handler(text="q_pon")
# async def desert(call:CallbackQuery):
#     await call.message.answer("<b>Desertni tanlang🍰 \nSiz tanlagan desert: Qulupnayli Ponchik🍩 \nNarxi: 11000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = desert_menu4)

# @dp.callback_query_handler(text="sh_pon")
# async def desert(call:CallbackQuery):
#     await call.message.answer("<b>Desertni tanlang🍰 \nSiz tanlagan desert: Shkaladli Ponchik🍩 \nNarxi: 11000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = desert_menu5)            



# Ichimlik uchun menu


@dp.callback_query_handler(text="ichimlik")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥤Ichimlik Menu""",reply_markup = ichimlik_menu1)
    await call.message.delete()

@dp.callback_query_handler(text="pepsi")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥤Ichimlik Menu""",reply_markup = ichimlik_menu2)
    await call.message.delete()

@dp.callback_query_handler(text="suv")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥤Ichimlik Menu""",reply_markup = ichimlik_menu3)
    await call.message.delete()

@dp.callback_query_handler(text="sok")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥤Ichimlik Menu""",reply_markup = ichimlik_menu4)
    await call.message.delete()


@dp.callback_query_handler(text="choy")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥤Ichimlik Menu""",reply_markup = ichimlik_menu5)
    await call.message.delete()


@dp.callback_query_handler(text="kofe")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥤Ichimlik Menu""",reply_markup = ichimlik_menu6)
    await call.message.delete()

@dp.callback_query_handler(text="fresh")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥤Ichimlik Menu""",reply_markup = ichimlik_menu7)
    await call.message.delete()



@dp.callback_query_handler(text="pepsi1")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu8)
    await call.message.delete()


@dp.callback_query_handler(text="pepsi2")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu9)
    await call.message.delete()

@dp.callback_query_handler(text="pepsi3")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu10)
    await call.message.delete()

@dp.callback_query_handler(text="suv1")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu11)
    await call.message.delete()

@dp.callback_query_handler(text="suv2")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu12)
    await call.message.delete()           


@dp.callback_query_handler(text="sok1")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu13)
    await call.message.delete()


@dp.callback_query_handler(text="sok2")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu14)
    await call.message.delete()


@dp.callback_query_handler(text="sok3")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu15)
    await call.message.delete()


@dp.callback_query_handler(text="choy1")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu16)
    await call.message.delete()


@dp.callback_query_handler(text="choy2")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu17)
    await call.message.delete()


@dp.callback_query_handler(text="choy3")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu18)
    await call.message.delete()


@dp.callback_query_handler(text="kofe1")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu19)
    await call.message.delete()

@dp.callback_query_handler(text="kofe2")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu20)
    await call.message.delete()

@dp.callback_query_handler(text="kofe3")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu21)
    await call.message.delete()


@dp.callback_query_handler(text="kofe4")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu22)
    await call.message.delete()

@dp.callback_query_handler(text="kofe15")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu23)
    await call.message.delete()


@dp.callback_query_handler(text="fresh1")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu24)
    await call.message.delete()


@dp.callback_query_handler(text="fresh2")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu25)
    await call.message.delete()


@dp.callback_query_handler(text="fresh3")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu26)
    await call.message.delete()

@dp.callback_query_handler(text="fresh4")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu27)
    await call.message.delete()

@dp.callback_query_handler(text="fresh5")
async def ichimlik(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = ichimlik_menu28)
    await call.message.delete()

# @dp.callback_query_handler(text="ichimlik")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu1)

# @dp.callback_query_handler(text="pepsi")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu2)

# @dp.callback_query_handler(text="suv")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu3)

# @dp.callback_query_handler(text="sok")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu4)

# @dp.callback_query_handler(text="choy")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu5)

# @dp.callback_query_handler(text="kofe")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu6)

# @dp.callback_query_handler(text="fresh")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu7)                        




# @dp.callback_query_handler(text="pepsi1")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Pepsi-0.4L🥤 \nNarxi: 6000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu8)

# @dp.callback_query_handler(text="pepsi2")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Pepsi-0.5L🥤 \nNarxi: 8000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu9)

# @dp.callback_query_handler(text="pepsi3")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Pepsi-1.5L🥤 \nNarxi:12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu10)        


# @dp.callback_query_handler(text="suv1")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Gazlangan Suv-0.5L🥛 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu11)

# @dp.callback_query_handler(text="suv2")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Gazlanmagan Suv-0.5L🥛 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu12)


# @dp.callback_query_handler(text="sok1")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: 🍎Olmali Sok🧃🥤 \nNarxi:12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu13)

# @dp.callback_query_handler(text="sok2")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: 🍊Apelsinli Sok🧃 \nNarxi:12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu14)


# @dp.callback_query_handler(text="sok3")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: 🍑Shaftolili Sok🧃 \nNarxi:12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu15)


# @dp.callback_query_handler(text="choy1")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Ko'k Choy🍵 \nNarxi:12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu16)

# @dp.callback_query_handler(text="choy2")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Qora Choy🍵 \nNarxi:12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu17)

# @dp.callback_query_handler(text="choy3")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Limon Choy🍋🍵 \nNarxi:12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu18)


# @dp.callback_query_handler(text="kofe1")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Kapuchino☕ \nNarxi:9000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu19)

# @dp.callback_query_handler(text="kofe2")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Amerikano☕️ \nNarxi:8000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu20)

# @dp.callback_query_handler(text="kofe3")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Latte☕️ \nNarxi:10000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu21)

# @dp.callback_query_handler(text="kofe4")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Ekspresso☕️ \nNarxi:7000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu22)

# @dp.callback_query_handler(text="kofe5")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Sutli kofe☕️ \nNarxi:5000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu23)


# @dp.callback_query_handler(text="fresh1")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Issiq shokolad🍹 \nNarxi:15000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu24)

# @dp.callback_query_handler(text="fresh2")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Qulupnayli moxito🍹 \nNarxi:15000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu25)

# @dp.callback_query_handler(text="fresh3")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Banan va sutli kokteyl🍹 \nNarxi:15000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu26)

# @dp.callback_query_handler(text="fresh4")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Moxito🍹 \nNarxi:15000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu27)

# @dp.callback_query_handler(text="fresh5")
# async def ichimlik(call:CallbackQuery):
#     await call.message.answer("<b>Ichimliklarni tanlang🥤 \nSiz tanlagan Ichimlik: Shaftoli va malinali smuzi🍹 \nNarxi:15000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu28)



# Salat uchun menu


@dp.callback_query_handler(text="salat")
async def salat(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥗Salat Menu""",reply_markup = salat_menu1)
    await call.message.delete()


@dp.callback_query_handler(text="salat1")
async def salat(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = salat_menu2)
    await call.message.delete()

@dp.callback_query_handler(text="salat2")
async def salat(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = salat_menu3)
    await call.message.delete()

@dp.callback_query_handler(text="salat3")
async def salat(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = salat_menu4)
    await call.message.delete()


@dp.callback_query_handler(text="salat4")
async def salat(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = salat_menu5)
    await call.message.delete()


@dp.callback_query_handler(text="salat5")
async def salat(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = salat_menu6)
    await call.message.delete()


@dp.callback_query_handler(text="salat6")
async def salat(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = salat_menu7)
    await call.message.delete()



# @dp.callback_query_handler(text="salat")
# async def salat(call:CallbackQuery):
#     await call.message.answer("<b>Salatni tanlang🥗  </b>",parse_mode = 'HTML',reply_markup = salat_menu1)

# @dp.callback_query_handler(text="salat1")
# async def salat(call:CallbackQuery):
#     await call.message.answer("<b>Salatni tanlang🥗 \nSiz tanlagan Salat: Murskoy kapriz🥗 \nNarxi: 13000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = salat_menu2)

# @dp.callback_query_handler(text="salat2")
# async def salat(call:CallbackQuery):
#     await call.message.answer("<b>Salatni tanlang🥗 \nSiz tanlagan Salat: Sezar🥗 \nNarxi: 13000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = salat_menu3)    

# @dp.callback_query_handler(text="salat3")
# async def salat(call:CallbackQuery):
#     await call.message.answer("<b>Salatni tanlang🥗 \nSiz tanlagan Ananas va tovuqli salat🥗 \nNarxi: 13000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = salat_menu4)

# @dp.callback_query_handler(text="salat4")
# async def salat(call:CallbackQuery):
#     await call.message.answer("<b>Salatni tanlang🥗 \nSiz tanlagan Salat: Sabzavotli yengil salat🥗 \nNarxi: 13000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = salat_menu5)

# @dp.callback_query_handler(text="salat5")
# async def salat(call:CallbackQuery):
#     await call.message.answer("<b>Salatni tanlang🥗 \nSiz tanlagan Salat: Bodring va brinzali salat🥗 \nNarxi: 13000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = salat_menu6)

# @dp.callback_query_handler(text="salat6")
# async def salat(call:CallbackQuery):
#     await call.message.answer("<b>Salatni tanlang🥗 \nSiz tanlagan Salat: Shanxay salati🥗 \nNarxi: 13000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = salat_menu7)




# Sous uchun menu


@dp.callback_query_handler(text="sous")
async def sous(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🥫Sous Menu""",reply_markup = sous_menu1)
    await call.message.delete()


@dp.callback_query_handler(text="sous1")
async def sous(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sous_menu2)
    await call.message.delete()


@dp.callback_query_handler(text="sous2")
async def sous(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sous_menu3)
    await call.message.delete()


@dp.callback_query_handler(text="sous3")
async def sous(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sous_menu4)
    await call.message.delete()


@dp.callback_query_handler(text="sous4")
async def sous(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sous_menu5)
    await call.message.delete()

@dp.callback_query_handler(text="sous5")
async def sous(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sous_menu6)
    await call.message.delete()


@dp.callback_query_handler(text="sous6")
async def sous(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = sous_menu7)
    await call.message.delete()





# @dp.callback_query_handler(text="sous")
# async def sous(call:CallbackQuery):
#     await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_marsous_menu1@dp.callback_query_handler(text="sous1")
# async def sous(call:CallbackQuery):
#     await call.message.answer("<b>Sousni tanlang🥫 \nSiz tanlagan Sous: Sirli🧀 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sous_menu2)

# @dp.callback_query_handler(text="sous2")
# async def sous(call:CallbackQuery):
#     await call.message.answer("<b>Sousni tanlang🥫 \nSiz tanlagan Sous: Chili🌶 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sous_menu3)    

# @dp.callback_query_handler(text="sous3")
# async def sous(call:CallbackQuery):
#     await call.message.answer("<b>Sousni tanlang🥫 \nSiz tanlagan Sous: Chesnokli🧄 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sous_menu4)

# @dp.callback_query_handler(text="sous4")
# async def sous(call:CallbackQuery):
#     await call.message.answer("<b>Sousni tanlang🥫 \nSiz tanlagan Sous: Mayanez🥫 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sous_menu5)

# @dp.callback_query_handler(text="sous5")
# async def sous(call:CallbackQuery):
#     await call.message.answer("<b>Sousni tanlang🥫 \nSiz tanlagan Sous: Garchitsa🥫 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sous_menu6)

# @dp.callback_query_handler(text="sous6")
# async def sous(call:CallbackQuery):
#     await call.message.answer("<b>Sousni tanlang🥫 \nSiz tanlagan Sous: Ketchup🍅 \nNarxi: 3000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = sous_menu7)



# Garnir uchun menu


@dp.callback_query_handler(text="garnir")
async def garnir(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog3.jpg','rb'),
        caption="""🍟Garnir Menu""",reply_markup = gar_menu1)
    await call.message.delete()


@dp.callback_query_handler(text="gar1")
async def garnir(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = gar_menu2)
    await call.message.delete()


@dp.callback_query_handler(text="gar2")
async def garnir(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = gar_menu3)
    await call.message.delete()

@dp.callback_query_handler(text="gar3")
async def garnir(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = gar_menu4)
    await call.message.delete()

@dp.callback_query_handler(text="gar4")
async def garnir(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog7.jpg','rb'),
        caption="""Narxi: 15000 so'm💵
Tarkibi: Kulcha, 2ta sosiska,ketchup, chili va xantal,qovurilgan piyoz. 
Miqdorini tanlang yoki kiriting!""",reply_markup = gar_menu5)
    await call.message.delete()            


# @dp.callback_query_handler(text="garnir")
# async def garnir(call:CallbackQuery):
#     await call.message.answer("<b>Garnirni tanlang🍟 </b>",parse_mode = 'HTML',reply_markup = gar_menu1)

# @dp.callback_query_handler(text="gar1")
# async def garnir(call:CallbackQuery):
#     await call.message.answer("<b>Garnirni tanlang🍟 \nSiz tanlagan Garnir:Kartoshka Free🍟 \nNarxi: 10000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = gar_menu2)

# @dp.callback_query_handler(text="gar2")
# async def garnir(call:CallbackQuery):
#     await call.message.answer("<b>Garnirni tanlang🍟 \nSiz tanlagan Garnir:Kartoshka Derevenskiy🍟 \nNarxi: 12000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = gar_menu3)

# @dp.callback_query_handler(text="gar3")
# async def garnir(call:CallbackQuery):
#     await call.message.answer("<b>Garnirni tanlang🍟 \nSiz tanlagan Garnir:Gruch🍚 \nNarxi: 8000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = gar_menu4)

# @dp.callback_query_handler(text="gar4")
# async def garnir(call:CallbackQuery):
#     await call.message.answer("<b>Garnirni tanlang🍟 \nSiz tanlagan Garnir:Jo'xori🌽 \nNarxi: 8000 so'm💵 </b>",parse_mode = 'HTML',reply_markup = gar_menu5)



################################################################################################################################################################################

# lavash_uchun_ortga_knopkalar

@dp.callback_query_handler(text="back1")
async def nazad5(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang</b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="back2")
async def nazad5(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu1)

@dp.callback_query_handler(text="back3")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu1)

@dp.callback_query_handler(text="back4")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu1)

@dp.callback_query_handler(text="back5")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu1)

@dp.callback_query_handler(text="back1")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu1)

@dp.callback_query_handler(text="back7")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu1)

@dp.callback_query_handler(text="back8")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu1)



# burger_uchun_nazad

@dp.callback_query_handler(text="back20")
async def burger_nazad(call:CallbackQuery):
    await call.message.answer("<b>Burgerni tanlang </b>",parse_mode = 'HTML',reply_markup = menu)


@dp.callback_query_handler(text="back21")
async def burger_nazad1(call:CallbackQuery):
    await call.message.answer("<b>Burgerni tanlang </b>",parse_mode = 'HTML',reply_markup = burger_menu1)



#shourma uchun nazad knopkasi

@dp.callback_query_handler(text="back22")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = menu)


@dp.callback_query_handler(text="back23")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu1)


@dp.callback_query_handler(text="back24")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu1)


@dp.callback_query_handler(text="back25")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu1)

@dp.callback_query_handler(text="back26")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu1)        

@dp.callback_query_handler(text="back27")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu2)        

@dp.callback_query_handler(text="back28")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu2)        

@dp.callback_query_handler(text="back29")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu3)        

@dp.callback_query_handler(text="back30")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu3)        

@dp.callback_query_handler(text="back31")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu4)        

@dp.callback_query_handler(text="back32")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu4)        

@dp.callback_query_handler(text="back33")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu5)        

@dp.callback_query_handler(text="back34")
async def shourma_nazad(call:CallbackQuery):
    await call.message.answer("<b>Shourmani tanlang </b>",parse_mode = 'HTML',reply_markup = shourma_menu5)        


# Hod-dog uchun nazad knopkalar



@dp.callback_query_handler(text="back35")
async def burger(call:CallbackQuery):
    await call.message.answer("<b>Hod-dogni tanlang </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="back36")
async def burger(call:CallbackQuery):
    await call.message.answer("<b>Hod-dogni tanlang </b>",parse_mode = 'HTML',reply_markup = hoddog_menu1)

@dp.callback_query_handler(text="back37")
async def burger(call:CallbackQuery):
    await call.message.answer("<b>Hod-dogni tanlang </b>",parse_mode = 'HTML',reply_markup = hoddog_menu1)

@dp.callback_query_handler(text="back38")
async def burger(call:CallbackQuery):
    await call.message.answer("<b>Hod-dogni tanlang </b>",parse_mode = 'HTML',reply_markup = hoddog_menu2)            

@dp.callback_query_handler(text="back39")
async def burger(call:CallbackQuery):
    await call.message.answer("<b>Hod-dogni tanlang </b>",parse_mode = 'HTML',reply_markup = hoddog_menu2)            

@dp.callback_query_handler(text="back40")
async def burger(call:CallbackQuery):
    await call.message.answer("<b>Hod-dogni tanlang </b>",parse_mode = 'HTML',reply_markup = hoddog_menu3) 

@dp.callback_query_handler(text="back41")
async def burger(call:CallbackQuery):
    await call.message.answer("<b>Hod-dogni tanlang </b>",parse_mode = 'HTML',reply_markup = hoddog_menu3) 

#Donar uchun nazad knopkalar

@dp.callback_query_handler(text="back42")
async def donar(call:CallbackQuery):
    await call.message.answer("<b>Donarni tanlang </b>",parse_mode = 'HTML',reply_markup = menu)


@dp.callback_query_handler(text="back43")
async def donar(call:CallbackQuery):
    await call.message.answer("<b>Donarni tanlang </b>",parse_mode = 'HTML',reply_markup = donar_menu1)    

@dp.callback_query_handler(text="back44")
async def donar(call:CallbackQuery):
    await call.message.answer("<b>Donarni tanlang </b>",parse_mode = 'HTML',reply_markup = donar_menu1)    


# Sendvich uchun nazad knopkalar

@dp.callback_query_handler(text="back45")
async def donar(call:CallbackQuery):
    await call.message.answer("<b>Donarni tanlang </b>",parse_mode = 'HTML',reply_markup = menu)    

@dp.callback_query_handler(text="back46")
async def donar(call:CallbackQuery):
    await call.message.answer("<b>Donarni tanlang </b>",parse_mode = 'HTML',reply_markup = sendvich_menu1)   

@dp.callback_query_handler(text="back47")
async def donar(call:CallbackQuery):
    await call.message.answer("<b>Donarni tanlang </b>",parse_mode = 'HTML',reply_markup = sendvich_menu1)    


#desert uchun nazad knopka


@dp.callback_query_handler(text="back48")
async def desert(call:CallbackQuery):
    await call.message.answer("<b>Desertni tanlang🍰 </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="back49")
async def desert(call:CallbackQuery):
    await call.message.answer("<b>Desertni tanlang🍰 </b>",parse_mode = 'HTML',reply_markup = desert_menu1)

@dp.callback_query_handler(text="back50")
async def desert(call:CallbackQuery):
    await call.message.answer("<b>Desertni tanlang🍰 </b>",parse_mode = 'HTML',reply_markup = desert_menu1)

@dp.callback_query_handler(text="back51")
async def desert(call:CallbackQuery):
    await call.message.answer("<b>Desertni tanlang🍰 </b>",parse_mode = 'HTML',reply_markup = desert_menu1)

@dp.callback_query_handler(text="back52")
async def desert(call:CallbackQuery):
    await call.message.answer("<b>Desertni tanlang🍰 </b>",parse_mode = 'HTML',reply_markup = desert_menu1)            



# Ichimlik uchun nazad knopkalar


@dp.callback_query_handler(text="back53")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="back54")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu1)

@dp.callback_query_handler(text="back55")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu1)

@dp.callback_query_handler(text="back56")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu1)

@dp.callback_query_handler(text="back57")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu1)

@dp.callback_query_handler(text="back58")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu1)

@dp.callback_query_handler(text="back59")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu1)

@dp.callback_query_handler(text="back60")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu2)

@dp.callback_query_handler(text="back61")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu2)    

@dp.callback_query_handler(text="back62")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu2)

@dp.callback_query_handler(text="back63")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu3)

@dp.callback_query_handler(text="back64")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu3)

@dp.callback_query_handler(text="back65")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu4)

@dp.callback_query_handler(text="back66")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu4)

@dp.callback_query_handler(text="back67")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu4)

@dp.callback_query_handler(text="back68")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu5)

@dp.callback_query_handler(text="back69")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu5)

@dp.callback_query_handler(text="back70")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu5)

@dp.callback_query_handler(text="back71")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu6)

@dp.callback_query_handler(text="back72")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu6)

@dp.callback_query_handler(text="back73")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu6)

@dp.callback_query_handler(text="back74")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu6)

@dp.callback_query_handler(text="back75")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu6)

@dp.callback_query_handler(text="back76")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu7)

@dp.callback_query_handler(text="back77")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu7)

@dp.callback_query_handler(text="back78")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu7)

@dp.callback_query_handler(text="back79")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu7)

@dp.callback_query_handler(text="back80")
async def ichimlik(call:CallbackQuery):
    await call.message.answer("<b>Ichimliklarni tanlang🥤 </b>",parse_mode = 'HTML',reply_markup = ichimlik_menu7)



# Salat uchun nazad knopkalar


@dp.callback_query_handler(text="back81")
async def salat(call:CallbackQuery):
    await call.message.answer("<b>Salatni tanlang🥗 </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="back82")
async def salat(call:CallbackQuery):
    await call.message.answer("<b>Salatni tanlang🥗 </b>",parse_mode = 'HTML',reply_markup = salat_menu1)

@dp.callback_query_handler(text="back83")
async def salat(call:CallbackQuery):
    await call.message.answer("<b>Salatni tanlang🥗 </b>",parse_mode = 'HTML',reply_markup = salat_menu1)

@dp.callback_query_handler(text="back84")
async def salat(call:CallbackQuery):
    await call.message.answer("<b>Salatni tanlang🥗 </b>",parse_mode = 'HTML',reply_markup = salat_menu1)

@dp.callback_query_handler(text="back85")
async def salat(call:CallbackQuery):
    await call.message.answer("<b>Salatni tanlang🥗 </b>",parse_mode = 'HTML',reply_markup = salat_menu1)

@dp.callback_query_handler(text="back86")
async def salat(call:CallbackQuery):
    await call.message.answer("<b>Salatni tanlang🥗 </b>",parse_mode = 'HTML',reply_markup = salat_menu1)

@dp.callback_query_handler(text="back87")
async def salat(call:CallbackQuery):
    await call.message.answer("<b>Salatni tanlang🥗 </b>",parse_mode = 'HTML',reply_markup = salat_menu1)



# Sous uchun nazad knopkalar


@dp.callback_query_handler(text="back88")
async def sous(call:CallbackQuery):
    await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="back89")
async def sous(call:CallbackQuery):
    await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_markup = sous_menu1)

@dp.callback_query_handler(text="back90")
async def sous(call:CallbackQuery):
    await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_markup = sous_menu1)

@dp.callback_query_handler(text="back91")
async def sous(call:CallbackQuery):
    await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_markup = sous_menu1)

@dp.callback_query_handler(text="back92")
async def sous(call:CallbackQuery):
    await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_markup = sous_menu1)

@dp.callback_query_handler(text="back93")
async def sous(call:CallbackQuery):
    await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_markup = sous_menu1)

@dp.callback_query_handler(text="back94")
async def sous(call:CallbackQuery):
    await call.message.answer("<b>Sousni tanlang🥫 </b>",parse_mode = 'HTML',reply_markup = sous_menu1)



# Garnir uchun nazad knopkalar

@dp.callback_query_handler(text="back95")
async def garnir(call:CallbackQuery):
    await call.message.answer("<b>Garnirni tanlang🍟 </b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="back96")
async def garnir(call:CallbackQuery):
    await call.message.answer("<b>Garnirni tanlang🍟 </b>",parse_mode = 'HTML',reply_markup = gar_menu1)

@dp.callback_query_handler(text="back97")
async def garnir(call:CallbackQuery):
    await call.message.answer("<b>Garnirni tanlang🍟 </b>",parse_mode = 'HTML',reply_markup = gar_menu1)

@dp.callback_query_handler(text="back98")
async def garnir(call:CallbackQuery):
    await call.message.answer("<b>Garnirni tanlang🍟 </b>",parse_mode = 'HTML',reply_markup = gar_menu1)

@dp.callback_query_handler(text="back99")
async def garnir(call:CallbackQuery):
    await call.message.answer("<b>Garnirni tanlang🍟 </b>",parse_mode = 'HTML',reply_markup = gar_menu1)









########################################################################################################################################################################################









  



@dp.message_handler(text="🇷🇺 Руссуий")
async def ruscha_uchun(message: types.Message):
    await message.answer("<b>Здравствуйте! \n\nДля заказа нажмите кнопку Menyu📕 </b>",parse_mode='HTML',reply_markup=menyu2)

    
@dp.message_handler(text="🇬🇧 England")
async def england_uchun(message: types.Message):
    await message.answer("<b>Hello</b>",parse_mode='HTML')    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
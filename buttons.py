from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

til = ReplyKeyboardMarkup(
	keyboard=[
		
		[		
				KeyboardButton(text="🇺🇿 O'zbekcha")
		],
		[		
				KeyboardButton(text="🇷🇺 Руссуий")
		],
		[		
				KeyboardButton(text="🇬🇧 England")
		],
	],
	resize_keyboard=True
)

joy = ReplyKeyboardMarkup(
	keyboard=[
		[		
				KeyboardButton(text="Yunusobod"),
				KeyboardButton(text="Chilonzor")
		],
		[		
				KeyboardButton(text="Olmozor"),
				KeyboardButton(text="Sergili")
		],		
		[		
				KeyboardButton(text="Yangobod"),
				KeyboardButton(text="Yakkasaroy")
		],
				
	],
	resize_keyboard=True
)

zakaz = InlineKeyboardMarkup(
	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Buyurtma",callback_data = "buy")
		],
	],
)

menu = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
				InlineKeyboardButton(text="🌯Lavash",callback_data="lavash"),
				InlineKeyboardButton(text="🍔Burger",callback_data="burger")
		],
		[
				InlineKeyboardButton(text="🌮 Shourma",callback_data="shourma"),
				InlineKeyboardButton(text="🌭Hod-Dog",callback_data="hod")
		],		
		[
				InlineKeyboardButton(text="🥙Donar",callback_data="donar"),
				InlineKeyboardButton(text="🥪Sendvich",callback_data="send")
		],
		[
				InlineKeyboardButton(text="🍰Desertlar",callback_data="desert"),
				InlineKeyboardButton(text="🥤Ichimliklar",callback_data="ichimlik")
		],
		[
				InlineKeyboardButton(text="🥗Salatlar",callback_data="salat"),
				InlineKeyboardButton(text="🥫Souslar",callback_data="sous")
		],
		[
				InlineKeyboardButton(text="🍟Garnir",callback_data="garnir")
		],
	
	],

)


lavash_menyu1 = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
				InlineKeyboardButton(text="🌯Classic lavash",callback_data = "lavash1"),
				InlineKeyboardButton(text = "🌯Classic mini lavash",callback_data = "lavash2")
		],
		[
				InlineKeyboardButton(text="🧀Pishloqli lavash",callback_data = "lavash3"),
				InlineKeyboardButton(text="🧀Pishloqli mini lavash",callback_data = "lavash4")
		],
		[
				InlineKeyboardButton(text="🥖Tandir lavash",callback_data = "lavash5"),
				InlineKeyboardButton(text="🥖Tandir pishloqli🧀 lavash",callback_data = "lavash6")
		],
		[
				InlineKeyboardButton(text="🌶Qalampirli lavash",callback_data = "lavash7"),
		],				
		
		[
				InlineKeyboardButton(text="⬅️Orqaga",callback_data = "back1"),
		],
	],

)

lavash_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back2')
		],
	],
)

lavash_menyu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "b1"),InlineKeyboardButton(text = "2",callback_data = "b2"),InlineKeyboardButton(text = "3",callback_data = "b3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "b4"),InlineKeyboardButton(text = "5",callback_data = "b5"),InlineKeyboardButton(text = "6",callback_data = "b6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "b7"),InlineKeyboardButton(text = "8",callback_data = "b8"),InlineKeyboardButton(text = "...",callback_data = "b9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back3')
		],
	],
)

lavash_menyu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back4')
		],
	],
)

lavash_menyu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back5')
		],
	],
)


lavash_menyu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back6')
		],
	],
)

lavash_menyu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back7')
		],
	],
)

lavash_menyu8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back8')
		],
	],
)

#burger_uchun_knopkalar

burger_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Gamburger🍔",callback_data="burger1"),
				InlineKeyboardButton(text ="Chizburger🍔",callback_data="chiz")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back20")
		],
	],
)

burger_menu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back21')
		],
	],
)

burger_menu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back211')
		],
	],
)




#shourma_uchun_knopkalar


shourma_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Mol go'shti shourma🌮",callback_data="gush_shourma"),
				InlineKeyboardButton(text ="Tovuq go'shti shourma🌮",callback_data="tov_shourma")
		],
		[
				InlineKeyboardButton(text ="Mol go'shti shourma🌮+qalampir🌶",callback_data="g_shourma"),
				InlineKeyboardButton(text ="Tovuq go'shti shourma🌮+qalampir🌶",callback_data="t_shourma")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back22")
		],
	],
)



shourma_menu2 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Mini shourma🌮",callback_data="mini1"),
				InlineKeyboardButton(text ="Classic shourma🌮",callback_data="classic1")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back23")
		],
	],
)


shourma_menu3 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Mini shourma🌮",callback_data="mini2"),
				InlineKeyboardButton(text ="Classic shourma🌮",callback_data="classic2")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back24")
		],
	],
)

shourma_menu4 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Mini shourma🌮",callback_data="mini3"),
				InlineKeyboardButton(text ="Classic shourma🌮",callback_data="classic3")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back25")
		],
	],
)

shourma_menu5 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Mini shourma🌮",callback_data="mini4"),
				InlineKeyboardButton(text ="Classic shourma🌮",callback_data="classic4")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back26")
		],
	],
)

shourma_menu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back27')

		],
	],
)
shourma_menu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back28')
		],
	],
)

shourma_menu8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back29')
		],
	],
)

shourma_menu9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back30')

		],
	],
)

shourma_menu10 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back31')
		],
	],
)

shourma_menu11 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back32')
		],
	],
)

shourma_menu12 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back33')

		],
	],
)

shourma_menu13 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back34')
		],
	],
)




# hod dog uchun knopkalar


hoddog_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Classic 🌭Hod-Dog",callback_data="clas1"),
				InlineKeyboardButton(text ="Korolevskiy 🌭Hod-Dog",callback_data="kar1")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back35")
		],
	],
)


hoddog_menu2 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Classic 🌭Hod-Dog",callback_data="clas2"),
				InlineKeyboardButton(text ="Classik qalampir🌶 🌭Hod-Dog",callback_data="kar2")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back36")
		],
	],
)

hoddog_menu3 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Korolevskiy 🌭Hod-Dog",callback_data="clas3"),
				InlineKeyboardButton(text ="Korolevckiy qalampir🌶 🌭Hod-Dog",callback_data="kar3")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back37")
		],
	],
)

hoddog_menu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back38')
		],
	],
)

hoddog_menu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back39')
		],
	],
)

hoddog_menu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back40')
		],
	],
)

hoddog_menu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back41')
		],
	],
)





donar_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Tovuqli Donar🥙",callback_data="d_tovuq"),
				InlineKeyboardButton(text ="Go'shtli Donar🥙",callback_data="d_gusht")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back42")
		],
	],
)

donar_menu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back43')
		],
	],
)


donar_menu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back44')
		],
	],
)



# Sendvich uchun knopkalar

sendvich_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Tuxumli Sendvich🍳🥪",callback_data="t_send1"),
				InlineKeyboardButton(text ="Tovuqli Sendvich🍗🥪",callback_data="t_send2")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back45")
		],
	],
)


sendvich_menu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back46')
		],
	],
)



sendvich_menu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back47')
		],
	],
)



# Desertlar uchun knopkalar


desert_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Medovik Asalli🧁",callback_data="medovik"),
				InlineKeyboardButton(text ="Chizkeyk🍰",callback_data="chizkey")
		],
		[
				InlineKeyboardButton(text ="Ponchik qulupnayli🍩",callback_data="q_pon"),
				InlineKeyboardButton(text ="Ponchik shkaladli🍩",callback_data="sh_pon")
		],
		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back48")
		],
	],
)

desert_menu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back49')
		],
	],
)

desert_menu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back50')
		],
	],
)

desert_menu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back51')
		],
	],
)

desert_menu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back52')
		],
	],
)



ichimlik_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Pepsi🥤",callback_data="pepsi"),
				InlineKeyboardButton(text ="Suv🥛",callback_data="suv"),
				InlineKeyboardButton(text ="Sok🧃",callback_data="sok")
		],
		[
				InlineKeyboardButton(text ="Choy🍵",callback_data="choy"),
				InlineKeyboardButton(text ="Kofe☕️",callback_data="kofe")
		],
		[
				InlineKeyboardButton(text ="🍹Fresh🍹",callback_data="fresh")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back53")
		],
	],
)

ichimlik_menu2 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Pepsi-0.4L🥤",callback_data="pepsi1"),
				InlineKeyboardButton(text ="Pepsi-0.5L🥤",callback_data="pepsi2")
		],
		[
				InlineKeyboardButton(text ="Pepsi-1.5L🥤",callback_data="pepsi3")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back54")
		],
	],
)

ichimlik_menu3 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Gazlangan Suv-0.5L🥛",callback_data="suv1"),
				InlineKeyboardButton(text ="Gazlanmagan Suv-0.5L🥛",callback_data="suv2")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back55")
		],
	],
)


ichimlik_menu4 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="🍎Olmali Sok🧃",callback_data="sok1"),
				InlineKeyboardButton(text ="🍊Apelsinli Sok🧃 ",callback_data="sok2")
		],
		[
				InlineKeyboardButton(text ="🍑Shaftolili Sok🧃",callback_data="sok3")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back56")
		],
	],
)


ichimlik_menu5 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Ko'k Choy🍵",callback_data="choy1"),
				InlineKeyboardButton(text ="Qora Choy🍵",callback_data="choy2")
		],
		[
				InlineKeyboardButton(text ="Limon Choy🍋🍵",callback_data="choy3")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back57")
		],
	],
)


ichimlik_menu6 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Kapuchino☕️",callback_data="kofe1"),
				InlineKeyboardButton(text ="Amerikano☕️",callback_data="kofe2")
		],
		[
				InlineKeyboardButton(text ="Latte☕️",callback_data="kofe3"),
				InlineKeyboardButton(text ="Ekspresso☕️",callback_data="kofe4")
		],
		[
				InlineKeyboardButton(text ="Sutli kofe☕️",callback_data="kofe5")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back58")
		],
	],
)


ichimlik_menu7 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Issiq shokolad🍹",callback_data="fresh1"),
				InlineKeyboardButton(text ="Qulupnayli moxito🍹",callback_data="fresh2")
		],
		[
				InlineKeyboardButton(text ="Banan va sutli kokteyl🍹",callback_data="fresh3"),
				InlineKeyboardButton(text ="Moxito🍹",callback_data="fresh4")
		],
		[
				InlineKeyboardButton(text ="Shaftoli va malinali smuzi🍹",callback_data="fresh5")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back59")
		],
	],
)

ichimlik_menu8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back60')
		],
	],
)

ichimlik_menu9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back61')
		],
	],
)

ichimlik_menu10 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back62')
		],
	],
)

ichimlik_menu11 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back63')
		],
	],
)

ichimlik_menu12 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back64')
		],
	],
)

ichimlik_menu13 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back65')
		],
	],
)

ichimlik_menu14 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back66')
		],
	],
)

ichimlik_menu15 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back67')
		],
	],
)

ichimlik_menu16 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back68')
		],
	],
)

ichimlik_menu17 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back69')
		],
	],
)

ichimlik_menu18 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back70')
		],
	],
)

ichimlik_menu19 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back71')
		],
	],
)

ichimlik_menu20 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back72')
		],
	],
)

ichimlik_menu21 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back73')
		],
	],
)

ichimlik_menu22 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back74')
		],
	],
)

ichimlik_menu23 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back75')
		],
	],
)

ichimlik_menu24 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back76')
		],
	],
)

ichimlik_menu25 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back77')
		],
	],
)

ichimlik_menu26 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back78')
		],
	],
)

ichimlik_menu27 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back79')
		],
	],
)

ichimlik_menu28 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back80')
		],
	],
)




# Slatlar uchun knopkalar


salat_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Murskoy kapriz🥗",callback_data="salat1"),
				InlineKeyboardButton(text ="Sezar🥗",callback_data="salat2"),
		],
		[
				InlineKeyboardButton(text ="Ananas va tovuqli salat🥗",callback_data="salat3"),
				InlineKeyboardButton(text ="Sabzavotli yengil salat🥗",callback_data="salat4")
		],
		[
				InlineKeyboardButton(text ="Bodring va brinzali salat🥗",callback_data="salat5"),
				InlineKeyboardButton(text ="Shanxay salati🥗",callback_data="salat6")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back81")
		],
	],
)

salat_menu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back82')
		],
	],
)

salat_menu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back83')
		],
	],
)

salat_menu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back84')
		],
	],
)

salat_menu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back85')
		],
	],
)

salat_menu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back86')
		],
	],
)

salat_menu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back87')
		],
	],
)




# Souslar uchun knopkalar


sous_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Sirli🧀",callback_data="sous1"),
				InlineKeyboardButton(text ="Chili🌶",callback_data="sous2"),
		],
		[
				InlineKeyboardButton(text ="Chesnokli🧄",callback_data="sous3"),
				InlineKeyboardButton(text ="Mayanez🥫",callback_data="sous4")
		],
		[
				InlineKeyboardButton(text ="Garchitsa🥫",callback_data="sous5"),
				InlineKeyboardButton(text ="Ketchup🍅",callback_data="sous6")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back88")
		],
	],
)


sous_menu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back89')
		],
	],
)

sous_menu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back90')
		],
	],
)

sous_menu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back91')
		],
	],
)

sous_menu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back92')
		],
	],
)

sous_menu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back93')
		],
	],
)

sous_menu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back94')
		],
	],
)



# Garnir uchun knopkalar


gar_menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	
		[
				InlineKeyboardButton(text ="Kartoshka Free🍟",callback_data="gar1"),
				InlineKeyboardButton(text ="Kartoshka Derevenskiy🍟",callback_data="gar2"),
		],
		[
				InlineKeyboardButton(text ="Gruch🍚",callback_data="gar3"),
				InlineKeyboardButton(text ="Jo'xori🌽",callback_data="gar4")
		],

		[
				InlineKeyboardButton(text ="⬅️Orqaga",callback_data="back95")
		],
	],
)


gar_menu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back96')
		],
	],
)

gar_menu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back97')
		],
	],
)

gar_menu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back98')
		],
	],
)


gar_menu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back99')
		],
	],
)
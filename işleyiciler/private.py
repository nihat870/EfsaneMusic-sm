from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://i.ibb.co/khRz42f/Turkish-Voice.jpg",
                caption=(f"""**Merhaba {message.from_user.mention} 🎵\nBen {bot}!\nSesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [Talia Müzik 🎙️](https://t.me/Sohbetdestek).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna Ekle ❱ ➕", url=f"https://t.me/Efsanestar_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Taliamusicasistant"
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbet", url="https://t.me/Sohbetskyfall"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇹🇷", url=f"https://t.me/Sohbetdestek"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
       mesaj bekliyoruz . answer_text ( " ❗ Not:\n Botun aktivite için şu yetkiye ihtiyacı vardır:\n- Mesaj çalışması ile yetkisi,\n- Bağlantı yetkisine yetkisi,\n- Sesli Sohbeti yönetme yetkisi." ,reply_markup=InlineKeyboardMarkup(

             [

                 [

                     InlineKeyboardButton(

                         "Sahib 🇦🇿", url="https://t.me/nihat_33")

                 ],

                 [

                     InlineKeyboardButton(

                         "️🔄 Geri", callback_data="cbbilgi")

                 ] 

             ]

         )

         )

@Client.on_callback_query(filters.regex("admin"))

async def admin(_, query: CallbackQuery):

    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün əmr menyusu 🤩\n\n ▶️ /resume - Musiqi oxutmağa davam et\n ⏸️ /durdur - Oxuyan musiqini dayandır\n 🔄 /atla - Sıraya alınmış musiqiyə keç\n ⏹ /skip - Musiqi oxumanı dayandır\n 🔼 /promote - Botun sadəcə yönətici üçün olan əmrlərini istifadə üçün istifadəçiyə yetki ver\n 🔽 /demote - Botun yönətici əmrlərini istifadə edən istifadəçinin yetkisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur.\n\n</b>""",

    reply_markup=InlineKeyboardMarkup(

             [

                 [

                     InlineKeyboardButton(

                         "Sahib 🇦🇿", url="https://t.me/nihat_33")

                 ],

                 [

                     InlineKeyboardButton(

                         "️🔄 Geri", callback_data="cbbilgi")

                 ] 

             ]

         )

         )

@Client.on_callback_query(filters.regex("cbstart"))

async def cbstart(_, query: CallbackQuery):

    await query.edit_message_text(f"""Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yönətim yetki verib, Asistanı qrupa əlavə edin.\n\nSahibim👉  [NIHAT](https://t.me/nihat_33)""",

         reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/SM_mmusic_bot?startgroup=true"

                    )

                ],

                [

                    InlineKeyboardButton(

                        "🔊 Asistan", url="https://t.me/SM_music2_bot"

                    ),

                    InlineKeyboardButton(

                        "Support 💬", url="https://t.me/Ay_isigi_sohbet"

                    )

                ],

                [

                    InlineKeyboardButton(

                        "🧩 Əmrlər" , callback_data= "cbbilgi"

                    ),

                    InlineKeyboardButton(

                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/Fake_love_33"

                    )

                ]

                

           ]

        ),

    )
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 Herkes için komutlar", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Adminler için komutlar", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menü🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Mahoaga")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Herkes için Komutlar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Yönetici Komutları",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Geliştirici", url="https://t.me/Mahoaga")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun herkes için komut menüsü 😉\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Mahoaga")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Mahoaga")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Merhaba {query.from_user.mention} 🎵\nBen {bot}!\nSesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [Talia Müzik 🎙️](https://t.me/Sohbetdestek).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna Ekle ❱ ➕", url=f"https://t.me/Efsanestar_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Taliamusicasistant"
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbet", url="https://t.me/Sohbetskyfall"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇹🇷", url=f"https://t.me/Sohbetdestek"
                    )
                ]
                
           ]
        ),
    )

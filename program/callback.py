# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **xoş gəlmisiniz [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Telegramda səsli söhbətdə musiqi ifa etmək və video yayımı üçün kodlaşdırılmışam!**

💡 **» Mənim həddindən çox əmrim var. Əmrlərə baxmaq üçün Əmrlər 📚 düyməsinə vur!**

🔖 **Əgər botu qrupuna qoşmaq istəyirsənsə ❔ Quraşdırılma baxa bilərsən.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Gurupa əlavə et ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❔Quraşdırma❔", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Əmirlər", callback_data="cbcmds"),
                    InlineKeyboardButton("👨🏻‍💻 Sahibim", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Rəsmi Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Rəsmi Kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Nexus MMC", url="https://t.me/NEXUS_MMC"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⚙️ QURULUM QAYDASI:**

1.) **First, qrupunuza əlavə edin.**
2.) **Sonra məni admin et və anonim admindən başqa bütün icazələri ver.**
3.) **Daha sonra admin siyahısını yeniləmək üçün qrupa /yenile yazın..**
4.) **@{ASSISTANT_NAME} qrupunuza əlavə edin və ya/userbotjoin yazın özü gəlsin.**
5.) **Musiqi oxutmağa başlamazdan əvvəl səsli söhbəti yandırın..**

📌 **Assistant səsli söhbətə qoşulmayıbsa, səsli söhbətin aktiv olub olmadığına əmin olun və ya /leave yazın, sonra yenidən /add yazın..**


⚡ 𝙽𝚎𝚡𝚞𝚜 𝙱𝚘𝚝 {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri qayıt", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **» Mənim əmrlərimin siyahısına baxmaq və izahlarını oxumaq üçün aşağıdakı butona basın !**

⚡ 𝙽𝚎𝚡𝚞𝚜 𝙱𝚘𝚝 {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin əmirləri", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo əmirləri", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 BSadə əmirlər", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Geri", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Sadə əmrlər bunlardır

» /play (musiqi adı) - Səsli söhbətdə musiqi oxudur
» /stream (link) - Səslidə canlı açılır
» /vplay (video adı) - Səslidə video açır
» /vstream - Səslidə canlı radio açır
» /playlist - Playlisti göstərir
» /video (ad) - Videonu youtubedən yükləyir
» /song (ad) - Musiqini youtubedən yükləyir
» /lyric (musiqi adı) - Musiqi sözlərini tapır
» /search (ad) - Axtaris edir

» /ping - Ping statusu göstərir
» /uptime - İşləmə vaxtını göstərir
» /alive - Botun aktiv olduğunu yoxlayın

⚡️ 𝙽𝚎𝚡𝚞𝚜 𝙱𝚘𝚝 {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Admin əmrləri

» /saxla - Pause verir
» /dayandır - Davam edir
» /kec - Növbəti musiqiyə keçir
» /durdur - Musiqini bitirir
» /sessiz - Asistanı səssizə alır
» /sesiac - Asistanın səsini açır
» /volume 1-200 - Səs səviyyəsi qeyd edin
» /yenile - Admin listi yeniləyin
» /userbotjoin - Asistanı qrupa dəvət edin
» /userbotleave - Asistanı qrupdan çıxarın

⚡️ 𝙽𝚎𝚡𝚞𝚜 𝙱𝚘𝚝 {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Sudo əmrləri

» /rmw - Raw faylları silin
» /rmd - Datanı təmizləyin
» /sysinfo - Sistemə baxın
» /restart - Botu yenidən başladın
» /leaveall - Asistantı bütün qruplardan çıxarın

⚡ 𝙽𝚎𝚡𝚞𝚜 𝙱𝚘𝚝 {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()

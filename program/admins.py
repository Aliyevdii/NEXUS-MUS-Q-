from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Geri qayıt", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 Cıxış", callback_data="cls")]]
)


@Client.on_message(command(["yenile", f"yenile@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ Bot **düzgün yenidən yükləndi !**\n ✅ **Admin siyahısı** **yeniləndi !**"
    )


@Client.on_message(command(["kec", f"kec@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• Menu", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="• Cıxış", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ hal hazırda heç nə oynamır")
        elif op == 1:
            await m.reply("✅ Növbələr **boşdur.**\n\n**• istifadəçi robotu səsli çatı tərk edir**")
        elif op == 2:
            await m.reply("🗑️ **Növbələr silinir**\n\n**• istifadəçi robotu səsli söhbəti tərk edir**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **Növbəti treki keçdi.**\n\n🏷 **Ad:** [{op[0]}]({op[1]})\n💭 **Gurup:** `{chat_id}`\n💡 **Status:** 'oynayır'\n🎧 **Sorğu ilə:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **mahnı növbədən silindi:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["durdur", f"durdur@{BOT_USERNAME}", "durdur", f"durdur@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ İstifadəçi robotu video çatdan ayrıldı.")
        except Exception as e:
            await m.reply(f"🚫 **xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **heç nə yayımlanmır**")


@Client.on_message(
    command(["saxla", f"saxla@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
                "⏸ **İzləmə dayandırıldı.**\n\n• **Yayımı davam etdirmək üçün**\n» /saxla əmrindən istifadə edin."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **axında heç nə**")


@Client.on_message(
    command(["dayandır", f"dayandır@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **İzləmə davam etdirildi.**\n\n• **Yayımı dayandırmaq üçün**\n» /dayandır əmrindən istifadə edin."
            )
        except Exception as e:
            await m.reply(f"🚫 **xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **axında heç nə**")


@Client.on_message(
    command(["sessiz", f"sessiz@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **Userbot səsi söndürüldü.**\n\n• **İstifadəçi robotunun səsini açmaq üçün**\n» /sessiz əmrindən istifadə edin."
            )
        except Exception as e:
            await m.reply(f"🚫 **xətar:**\n\n`{e}`")
    else:
        await m.reply("❌ **axında heç nə**")


@Client.on_message(
    command(["sesiac", f"sesiac@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **Userbot səsi açıldı.**\n\n• **İstifadəçi robotunun səsini söndürmək üçün**\n» /sesiac əmrindən istifadə edin."
            )
        except Exception as e:
            await m.reply(f"🚫 **xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **axında heç nə**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("siz Anonim Adminsiniz !\n\n» admin hüquqlarından istifadəçi hesabına qayıdın.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 yalnız bu düyməyə toxuna bilən səsli söhbətləri idarə etmək icazəsi olan admin !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ yayım dayandırıldı", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **xəta:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ hazırda heç nə yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ the streaming has resumed", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **this streaming has ended**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 userbot succesfully muted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 userbot succesfully unmuted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **volume set to** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **nothing in streaming**")

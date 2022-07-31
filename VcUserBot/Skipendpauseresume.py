from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from VcUserBot.helpers.decorators import authorized_users_only
from VcUserBot.helpers.handlers import skip_current_song, skip_item
from VcUserBot.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["skip", "هات اللي بعدو", "غير"], prefixes=f"{HNDLR}"))
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**🙄لا يوجد شيء في قائمة الانتظار للتخطي!**")
        elif op == 1:
            await m.reply("**😩قائمة انتظار فارغة ، ترك الدردشة الصوتية**")
        else:
            await m.reply(
                f"**⏭ تم تخطي** \n**🎧 يتم التشغيل** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ إزالة الأغاني التالية من قائمة الانتظار: -**"
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
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["end", "stop", "وقف",], prefixes=f"{HNDLR}"))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**😐تـم انـهـاء الـمـحـادثـة الـصـوتـيـة.**")
        except Exception as e:
            await m.reply(f"**خطأ** \n`{e}`")
    else:
        await m.reply("**كسمكو بجد بقاا مقولنا مفيش حاجه شغاله 🤨. !**")


@Client.on_message(filters.command(["pause", "شد ميوت"], prefixes=f"{HNDLR}"))
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ متوقف مؤقتًا.**\n\n• لاستئناف التشغيل ، استخدم الأمر » {HNDLR}سيرة ذاتية"
            )
        except Exception as e:
            await m.reply(f"**خطأ** \n`{e}`")
    else:
        await m.reply("**🤨قولنا مفيش حاجه شغاله احا بقا.!**")


@Client.on_message(filters.command(["resume", "فك ميوت"], prefixes=f"{HNDLR}"))
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ مستأنف**\n\n• لإيقاف التشغيل مؤقتًا ، استخدم الأمر » {HNDLR}وقفة**"
            )
        except Exception as e:
            await m.reply(f"**خطأ** \n`{e}`")
    else:
        await m.reply("**🙄 مفيش حاجه شغاله دا انتو تجيبو المرض!**")

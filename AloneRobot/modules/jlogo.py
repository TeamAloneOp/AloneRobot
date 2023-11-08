import glob
import io
import os
import random

import requests
from PIL import Image, ImageDraw, ImageFont
from AloneRobot.modules.nightmode import button_row
from AloneRobot import BOT_USERNAME, OWNER_ID,BOT_NAME, SUPPORT_CHAT, telethn
from AloneRobot.events import register

LOGO_LINKS = [
    "https://te.legra.ph/file/7345fd37e2ed393b37643.jpg",
    "https://te.legra.ph/file/5ced2c3542ef0662fd6e2.jpg",
]


@register(pattern="^/jlogo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id != OWNER_ID and not quew:
        await event.reply(
            "`ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟᴏɢᴏ ʙᴀʙᴇ​ !`\n`Example /logo <alone>`"
        )
        return
    pesan = await event.reply("**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ​...**")
    try:
        text = event.pattern_match.group(1)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = glob.glob("./AloneRobot/resources/fonts/UrbanJungleDEMO.otf")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 120)
        bbox= draw.textbbox((0,0),text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        h += int(h * 0.21)
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "alone.png"
        img.save(fname, "png")
        await telethn.send_file(
            event.chat_id,
            file=fname,
            caption=f"""━━━━━━━{BOT_NAME}━━━━━━━

☘️ ʟᴏɢᴏ ᴄʀᴇᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ☘️
◈──────────────◈
🔥 ᴄʀᴇᴀᴛᴇᴅ ʙʏ : @{BOT_USERNAME}
━━━━━━━{BOT_NAME}━━━━━━━""",buttons=button_row
)
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await event.reply(f"ᴇʀʀᴏʀ {e}, ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ @{SUPPORT_CHAT} ")


__mod_name__ = "Jʟᴏɢᴏ"

__help__ = """
@{BOT_USERNAME} ᴄᴀɴ ᴄʀᴇᴀᴛᴇ sᴏᴍᴇ ʙᴇᴀᴜᴛɪғᴜʟ ᴀɴᴅ ᴀᴛᴛʀᴀᴄᴛɪᴠᴇ ʟᴏɢᴏ ғᴏʀ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘɪᴄs.


❍ /jlogo (Text) *:* ᴄʀᴇᴀᴛᴇ ᴀ ʟᴏɢᴏ ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ᴠɪᴇᴡ.
"""

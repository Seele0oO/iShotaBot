import re

from pyrogram import Client, filters, ContinuePropagation
from pyrogram.types import Message

from defs.bilibili import b23_extract, video_info_get, binfo_image_create
from defs.button import gen_button, Button


@Client.on_message(filters.incoming & ~filters.edited &
                   filters.regex(r"av(\d{1,12})|BV(1[A-Za-z0-9]{2}4.1.7[A-Za-z0-9]{2})|b23.tv"))
async def bili_resolve(client: Client, message: Message):
    """
        解析 bilibili 链接
    """
    video_info = None
    if "b23.tv" in message.text:
        message.text = await b23_extract(message.text)
    p = re.compile(r"av(\d{1,12})|BV(1[A-Za-z0-9]{2}4.1.7[A-Za-z0-9]{2})")
    video_number = p.search(message.text)
    if video_number:
        video_number = video_number.group(0)
        if video_number:
            video_info = await video_info_get(video_number)
    if video_info:
        if video_info["code"] == 0:
            image = binfo_image_create(video_info)
            await message.reply_photo(image,
                                      quote=True,
                                      reply_markup=gen_button(
                                          [Button(0, "Link", "https://b23.tv/" + video_info["data"]["bvid"])]))
    raise ContinuePropagation

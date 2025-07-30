from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Initialize bot
app = Client(
    "free_batch_bot",
    api_id=29907731,  # Replace with your API ID
    api_hash="8f59d632cb374705cfdee46ac17cc3cd",  # Replace with your API Hash
    bot_token="7439280676:AAETvxLH5DJX02Z3A4nLcUTiFbhIYV2iRTM"  # Replace with your bot token
)

# /start command
@app.on_message(filters.command("start"))
async def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Free Batch Rakesh Sir", url="https://t.me/+rE1hkV_MD_M4ZTNl")],
        [InlineKeyboardButton("Aarush", url="https://t.me/AarushNetX")]
    ])

    await message.reply_text(
        "**🎓 Welcome to the Free Batch Bot!**\n\n"
        "Free Batch Rakesh Sir WITH FORWARD ON \nhttps://t.me/+iBX0Aq0hUs43NmY1\n\nTap below to access your batch",
        reply_markup=keyboard
    )

# Run the bot
app.run()

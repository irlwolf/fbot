from bot import Bot  # Ensure Bot is imported correctly
import pyrogram

# If you absolutely need to set MIN_CHANNEL_ID, you can do it here
pyrogram.utils.MIN_CHANNEL_ID = -1002452376610

if __name__ == "__main__":
    bot = Bot()  # Ensure Bot is instantiated correctly
    bot.run()  # Run the bot

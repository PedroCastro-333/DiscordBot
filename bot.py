from decouple import config
from discord.ext import commands


bot = commands.Bot(['.', '!'])

@bot.event
async def on_ready():
    print("Bot ligado!")

def load_cog(bot):
    bot.load_extension('manager')
    bot.load_extension('commands.caule')
    bot.load_extension('commands.runas2')

load_cog(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)


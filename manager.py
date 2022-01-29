from discord.ext import commands

def setup(bot):
    bot.add_cog(Manager(bot))


class Manager(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
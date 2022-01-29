from discord.ext import commands
from discord import Client
from PIL import Image
def setup(bot):
    bot.add_cog(Runa(bot))


class Runa(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="runa")
    async def runas (self,  ctx, champ):
        resposta = f'https://www.leagueofgraphs.com/pt/champions/runes/{champ}'

        await ctx.send(f'A runa de {champ} é {resposta}')


import discord
from discord import guild
from discord.ext import commands
from discord import Client
from PIL import Image
from discord.file import File
import os, shutil


def setup(bot):
    bot.add_cog(Runa(bot))


class Runa(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="runa")
    async def runas (self,  ctx, champ):
        img_path = os.path.join(f'.\\commands\\src\\runas\\')
        img = img_path+f'{champ}.jpg'
        await ctx.send(f'A runa com maior porcentagem de vitória para {champ} é ', file=discord.File(img))


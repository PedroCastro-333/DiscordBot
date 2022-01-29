from discord.ext import commands
def setup(bot):
    bot.add_cog(Caule(bot))


class Caule(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="caule")
    async def caule (self, ctx):
        resposta = f'''
───────────────────────────
    ──▄▄▀▀█────────▄▄▀▀█──────
   █▒░░▄░█─────▄█▒░░▄░█─────
   ▒▀▀▀▄▄▀───▄▀▒▀▀▀▄▄▀─────
   █▒░░░█──█▒░░░░▄▀───────
   █▒░░░█─█▒░░░░▄▀────────
   █▒░░░█▒█░░░░█──────────
   █▒▒▒▒▒▒▀▒▒▒▒▒░▀▀▄▄──────
   ██▒▒▒▒▒░░░░░░░░░░▀▀▄▄───
   ███▓▓▒▒▒▀▀▀█▄▒▒░░░█░░▀▀▄
   ▓██▓▒▒▒▒▒▒▒▒▒█▀▀▄▄█▒░▄░█
   ▓▓█▓▒▒▒▒▒▒▓▒▒█░░░░▀▀▄▄ █░
   ░▒▒▀▀▄▄▄▄█▄▄▀░░░░░░░░───'''

        await ctx.send(resposta)
        print(ctx.author._roles)


import random

from discord.ext import commands

#constructor
class gamble_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

   #dice command 
    @commands.command()
    async def roll(self,ctx):
        n = random.randint(1,6)
        await ctx.send(n)

    #coinflip command
    @commands.command()
    async def coinflip(self,ctx):
        n = random.randint(1,2)
        await ctx.send(n)




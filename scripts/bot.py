import discord
import random
from discord.ext import commands
from image_cog import image_cog
from music_cog import music_cog
from gamble_cog import gamble_cog

Bot = commands.Bot(command_prefix="$")

Bot.add_cog(image_cog(Bot))
Bot.add_cog(music_cog(Bot))
Bot.add_cog(gamble_cog(Bot))

@Bot.command()
async def say(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)

token = ""

with open("token.txt") as file:
    token = file.read()

Bot.run(token)
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.slash_command(name="test", description="test command")
async def test(ctx):
    await ctx.send("test")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "test":
        await message.channel.send("test")

    



bot.run("MTE1MjI0MjA0MjkyNDE3NTQxMg.Ga0pX2.1eb-Lewmd1t-GdVE-NFb7iEX6Zn_mO366vhbaM")
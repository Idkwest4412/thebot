from discord.ext import commands
import discord

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command() #This is a testing command that will send "Test command works!" in the chat!
    async def test(self, ctx):
        await ctx.send("Test command works!")

async def setup(client):
    await client.add_cog(Test(client))

from discord.ext import commands
from discord import app_commands
import discord

import os

from Bot.Krusty import Krusty
from Bot.errors import *


class Balloons(commands.Cog):

    def __init__(self, bot: Krusty):
        self.bot = bot

    @app_commands.command(name="balloons", description="What does this do ?")
    async def balloons(self, interaction):
        await interaction.response.send_message(os.getenv('FROM_COMMAND'), ephemeral=True)

    @app_commands.command(name="get_balloons", description="(WIP) permission issues")
    @app_commands.describe(balloons="the balloons you want to get")
    async def get_balloons(self, interaction, balloons: discord.Role):
        await interaction.response.send_message("You already have this role", ephemeral=True)




async def setup(bot: Krusty):
    await bot.add_cog(Balloons(bot), guild=discord.Object(id=int(os.getenv('CTF_GUILD_ID')))

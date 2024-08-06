from discord.ext import commands
from discord import app_commands
import discord

import os

from Bot.Krusty import Krusty


class Flag(commands.Cog):

    def __init__(self, bot: Krusty):
        self.bot = bot

    @app_commands.command(name="get_flag", description="What does this do ?")
    async def get_flag(self, interaction):
        await interaction.response.send_message(os.getenv('FROM_COMMAND'), ephemeral=True)



async def setup(bot: Krusty):
    await bot.add_cog(Flag(bot), guild=discord.Object(id=1258573665964916867))

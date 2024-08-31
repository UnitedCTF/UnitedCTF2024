import discord
from discord.ext import commands
from discord import app_commands

import os

from Krusty import Krusty


class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sync", description="Sync the commands")
    async def sync(self, interaction):
        if str(interaction.user.id) == os.getenv('OWNER_ID'):
            await interaction.response.send_message(f"Syncing commands ", ephemeral=True)
            for guild in self.bot.guilds:
                await self.bot.tree.sync(guild=guild)
            await interaction.edit_original_response(content=f"Synced commands")


async def setup(bot: Krusty):
    await bot.add_cog(Utils(bot), guild=discord.Object(id=int(os.getenv('CTF_GUILD_ID'))))

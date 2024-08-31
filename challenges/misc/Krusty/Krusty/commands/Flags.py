import asyncio
import sys

from discord.ext import commands
from discord import app_commands
import discord

import os
from PIL import Image, ImageDraw
import subprocess

from Krusty import Krusty
from Krusty.errors import *


class Flag(commands.Cog):

    def __init__(self, bot: Krusty):
        self.bot = bot

    @app_commands.command(name="get_flag", description="What does this do ?")
    async def get_flag(self, interaction):
        await interaction.response.send_message(os.getenv('FROM_COMMAND'), ephemeral=True)

    @app_commands.command(name="get_role", description="(WIP) permission issues")
    @app_commands.describe(role="the role you want to get")
    async def get_role(self, interaction, role: discord.Role):
        guild = interaction.guild
        ctf_channel: discord.TextChannel = None
        privileged: discord.Role = None
        unprivileged: discord.Role = None
        for channel in guild.channels:
            if channel.name == 'what-is-this':
                ctf_channel = channel
        for r in guild.roles:
            if r.name == 'participant-2024':
                if ctf_channel.overwrites_for(r).read_messages:
                    privileged = r
                else:
                    unprivileged = r

        if privileged is None:
            raise SetupError("No privileged role found")

        if role == privileged:
            await interaction.user.remove_roles(unprivileged)
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Wait... What ?", ephemeral=True)
            async with interaction.channel.typing():
                await asyncio.sleep(2)
            await interaction.followup.send("You already have this role...", ephemeral=True)
            async with interaction.channel.typing():
                await asyncio.sleep(2)
            await interaction.followup.send("Well, if anything changed please dont pay attention to it",
                                            ephemeral=True)
        elif role in interaction.user.roles:
            await interaction.response.send_message("You already have this role", ephemeral=True)
        else:
            raise FakeError(f"get_role with role {role.name}")



async def setup(bot: Krusty):
    await bot.add_cog(Flag(bot), guild=discord.Object(id=int(os.getenv('CTF_GUILD_ID'))))

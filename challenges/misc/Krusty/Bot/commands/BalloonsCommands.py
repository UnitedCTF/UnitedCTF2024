import random
import sqlite3

from discord.ext import commands
from discord import app_commands
import discord

import os

from Bot.Krusty import Krusty
from Bot.errors import *
from Bot.data.Controller.PlayerController import PlayerController

from Bot.errors.DataModelErrors import NotFoundError, AlreadyExistsError


class Balloons(commands.Cog):

    def __init__(self, bot: Krusty):
        self.bot = bot

    @app_commands.command(name="balloon_buy", description="Buy a new balloon")
    @app_commands.describe(secret="The secret password to obtain the secret balloon")
    async def balloons_buy(self, interaction, secret: str = None):
        await interaction.response.defer(ephemeral=True)
        if secret:
            conn = sqlite3.connect('./data/db/' + str(interaction.guild_id) + '.db')
            cursor = conn.cursor()

            data = cursor.execute(f"SELECT * FROM players WHERE players.id = '{secret}' AND players.name = 'Krusty';")
            if data.fetchone() is None:
                await interaction.followup.send("You are not allowed to buy this balloon", ephemeral=True)
            else:
                cursor.close()
                conn.close()
                answer = "You bought the secret balloon !\n"
                answer += ("```\n"
                           "  emoji  |  points | description\n"
                           "---------|---------|- \n"
                           "   🚩    |  100    |"+os.getenv("SECRET_BALLOON"))
                await interaction.followup.send(answer, ephemeral=True)
                player_controller = PlayerController(interaction.guild_id)
                player = player_controller.get_player(interaction.user.id, interaction.user.name)
                player_controller.give_balloon(player.id, "??", 100, "THE SECRET BALLOON")
                try:
                    int(secret)
                except ValueError:
                    pass
                else:
                    await interaction.user.send("This was not the intended solution but GG still")
                finally:
                    return
        with open('./emojis_list', "r", encoding='utf-8') as emojis_file:
            emojis = emojis_file.readline().split(',')
        player_controller = PlayerController(interaction.guild_id)
        try:
            player = player_controller.get_player(interaction.user.id, interaction.user.name)
        except NotFoundError:
            await interaction.followup.send(
                "You are not registered as a player yet ! Use </register:1277792495832662120> to register",
                ephemeral=True)
        else:
            choosen = random.choice(emojis)
            print(player.id)
            player_controller.give_balloon(player.id, choosen, random.randint(1, 37), "A balloon")
        await interaction.followup.send("You bought a balloon", ephemeral=True)

    @app_commands.command(name="see_balloons", description="See someone's balloons")
    @app_commands.describe(player="The name of the player you want to see the balloons of")
    async def see_balloons(self, interaction, player: str):
        await interaction.response.defer(ephemeral=True)
        player = player.lower()
        try:
            # unsafe query
            conn = sqlite3.connect('./data/db/' + str(interaction.guild_id) + '.db')
            cursor = conn.cursor()
            data = cursor.execute(
                f"SELECT emoji, points FROM balloons JOIN players ON balloons.possessed_by = players.id WHERE players.name = '{player}';")
            balloons_data = data.fetchall()
            cursor.close()
            conn.close()
        except sqlite3.OperationalError as e:
            await interaction.user.send("DEBUG MODE : " + str(e))
        else:
            answer = ("Here are " + player + "'s balloons :\n"
                                             "```\n"
                                             "  emoji  |  points | description\n"
                                             "---------|---------|- \n"
                      )
            for balloon in balloons_data:
                answer += "|".join([str(i).center(8) for i in balloon]) + "\n"
            answer += "```"

            await interaction.followup.send(answer, ephemeral=True)

    @app_commands.command(name="register", description="Register as a player")
    async def register(self, interaction):
        await interaction.response.defer(ephemeral=True)
        player_controller = PlayerController(interaction.guild_id)
        try:
            player = player_controller.create_player(interaction.user.id, interaction.user.name)
            print(player)
        except AlreadyExistsError:
            await interaction.followup.send("You are already registered as a player", ephemeral=True)
        else:
            await interaction.followup.send("You are now registered as a player", ephemeral=True)


async def setup(bot: Krusty):
    await bot.add_cog(Balloons(bot), guild=discord.Object(id=int(os.getenv('CTF_GUILD_ID'))))

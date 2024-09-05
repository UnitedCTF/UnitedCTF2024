import random
import sqlite3

from discord.ext import commands
from discord import app_commands
import discord

import os

from Krusty import Krusty
from Krusty.errors import *
from Krusty.data.Controller.PlayerController import PlayerController

from Krusty.errors.DataModelErrors import NotFoundError, AlreadyExistsError


class Balloons(commands.Cog):

    def __init__(self, bot: Krusty):
        self.bot = bot

    @app_commands.command(name="balloon_buy", description="Buy a new balloon")
    @app_commands.describe(secret="The secret password to obtain the secret balloon")
    async def balloons_buy(self, interaction, secret: str = None):
        await interaction.response.defer(ephemeral=True)
        player_controller = PlayerController(interaction.guild_id)
        try:
            player = player_controller.get_player(interaction.user.id, interaction.user.name)
        except NotFoundError:
            await interaction.followup.send(
                "You are not registered as a player yet ! Use </balloon_register:1279538522025365613> to register",
                ephemeral=True)
        else:
            if secret:
                conn = sqlite3.connect('./Krusty/data/db/' + str(interaction.guild_id) + '.db')
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
                    answer += "```\nCAUTION : This balloon will stored as <CENSORED> in your inventory\n"
                    await interaction.followup.send(answer, ephemeral=True)
                    player = player_controller.get_player(interaction.user.id, interaction.user.name)
                    player_controller.give_balloon(player.id, "🚩", 100, "<CENSORED>")
                    try:
                        int(secret)
                    except ValueError:
                        pass
                    else:
                        await interaction.user.send("This was not the intended solution but GG still")
                    finally:
                        return
            else:
                with open('./emojis_list', "r", encoding='utf-8') as emojis_file:
                    emojis = emojis_file.readline().split(',')

                    chosen = random.choice(emojis)
                    print(player.id)
                    player_controller.give_balloon(player.id, chosen, random.randint(1, 37), "A balloon")
                await interaction.followup.send("You bought a balloon", ephemeral=True)

    @app_commands.command(name="balloon_see", description="See someone's balloons")
    @app_commands.describe(player="The name of the player you want to see the balloons of")
    async def balloon_see(self, interaction, player: str):
        await interaction.response.defer(ephemeral=True)
        player = player.lower()
        query = f"SELECT emoji, points FROM balloons JOIN players ON balloons.possessed_by = players.id WHERE players.name = '{player}';"
        try:
            # unsafe query
            conn = sqlite3.connect('./Krusty/data/db/' + str(interaction.guild_id) + '.db')
            cursor = conn.cursor()
            data = cursor.execute(query)
            balloons_data = data.fetchall()
            cursor.close()
            conn.close()
        except sqlite3.OperationalError as e:
            await interaction.user.send("DEBUG MODE : " + str(e)+"\n This happend during the query : "+query)
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

    @app_commands.command(name="balloon_register", description="Register as a player")
    async def balloon_register(self, interaction):
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

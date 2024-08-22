from discord.ext import commands
from discord import app_commands
import discord

import os

current_choice = ["Main Menu"]
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="You want help ? I'm here for that !")
    async def help(self, interaction):
        view = HelpChooser(interaction)
        await view.start()


class HelpChooser(discord.ui.View):
    message: discord.Message
    interaction: discord.Interaction
    embeds = {
        "initial": discord.Embed(
            title="Krusty help page",
            description="Hey !\n"
                        "You asked for some help ?\n"
                        "Try to select one of the category to have some more information about it\n"
                        "\n"
                        "Here are some links useful for the UnitedCTF:\n"
                        "[UnitedCTF](https://unitedctf.ca/) | [The 2024 CTF](https://ctf.unitedctf.ca/)"
            , color=discord.Color.blurple()
        ),
        "tips": discord.Embed(
            title="Tips and tricks for ctf",
            description="Here are some tips and tricks for the CTF:\n"
                        "1. Don't give up\n"
                        "2. Try to understand the challenge\n"
                        "3. Don't hesitate to ask for help\n"
                        "4. Don't forget to have fun !"
            , color=discord.Color.blurple()
        ),
        "commands": discord.Embed(
            title="Commands",
            description="Here are some commands you can use:\n"
                        "\n"
                        "\n"
                        ""
            , color=discord.Color.blurple()
        )
    }

    def __init__(self, interaction):
        super().__init__()
        self.message = None
        self.interaction = interaction
        global current_choice

    @discord.ui.select(placeholder=current_choice[0],
                       options=[
                           discord.SelectOption(label="Main Menu", value="initial"),
                           discord.SelectOption(label="Tips and tricks for ctf", value="ctf"),
                           discord.SelectOption(label="Commands", value="commands")
                       ])
    async def select_callback(self, interaction, select):
        print(select.values)
        if select.values[0] == "ctf":
            current_choice[0] = "Tips and tricks for ctf"
            await self.interaction.edit_original_response(embed=self.embeds["tips"])

        elif select.values[0] == "commands":
            current_choice[0] = "Commands"
            await self.interaction.edit_original_response(embed=self.embeds["commands"])
        else:
            current_choice[0] = "Main Menu"
            await self.interaction.edit_original_response(embed=self.embeds["initial"])
        await interaction.response.defer()

    async def interaction_check(self, interaction):
        return interaction.user.id == self.interaction.user.id

    async def on_timeout(self):
        await self.interaction.edit(view=None)

    async def on_error(self, interaction, error, item):
        await interaction.response.send_message("An error occured")
        raise error

    async def start(self):
        self.message = await self.interaction.response.send_message(embed=self.embeds["initial"], view=self)


async def setup(bot):
    await bot.add_cog(Help(bot), guild=discord.Object(id=int(os.getenv('CTF_GUILD_ID'))))

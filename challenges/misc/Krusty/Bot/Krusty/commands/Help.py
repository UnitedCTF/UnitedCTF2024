from discord.ext import commands
from discord import app_commands
import discord
from discord.app_commands import Choice
import os

current_choice = ["Main Menu"]


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="You want help ? I'm here for that !")
    @app_commands.describe(language="The language you want the help to be in")
    @app_commands.choices(language=[
        Choice(name="English", value="en"),
        Choice(name="Francais", value="fr")
    ])
    async def help(self, interaction, language:Choice[str]="en"):
        view = HelpChooser(interaction, language)
        await view.start()


class HelpChooser(discord.ui.View):
    message: discord.Message
    interaction: discord.Interaction

    embeds: dict
    en_embeds = {
        "initial": discord.Embed(
            title="Krusty help page",
            description="Hey !\n"
                        "You asked for some help ?\n"
                        "Try to select one of the category to have some more information about it\n"
                        "\n"
                        "Here are links about the UnitedCTF:\n"
                        "[UnitedCTF](https://unitedctf.ca/) | [The 2024 CTF](https://ctf.unitedctf.ca/)"
            , color=discord.Color.blurple()
        ),
        "tips": discord.Embed(
            title="Tips and tricks for ctf",
            description="Here are some tips and tricks for the CTF:\n"
                        "1. Don't give up\n"
                        "2. Try to understand the challenge\n"
                        "3. Don't hesitate to ask for help\n"
                        "4. Don't forget to have fun !\n"
                        "\n"
                        "Some websites that might help you along your journey:\n"
                        "[Hacktricks](https://book.hacktricks.xyz/) | [CTF101](https://ctf101.org/)"
            , color=discord.Color.blurple()
        ),
        "commands": discord.Embed(
            title="Commands",
            description="""Here are some commands you can use:
            
</help:1279538522025365610> `language` : Get help, language can be `English` or `Francais`

__-----------------------------**Balloons**-----------------------------__
</balloon_register:1279538522025365613> : Join the balloon game ! Who will have the most balloons at the end ?
</balloon_buy:1279538522025365611> `secret` (Optional) : Buy a new balloon ! (A secret balloon can be obtain with the correct password)
</balloon_see:1279538522025365612> `player` : Check your (and other's) progression !



__-----------------------------**Dev Notes**-----------------------------__
/balloon_see : ! Fix display !
~~/get_role `role`~~ : deactivated [ Need to be careful on permission issues ]"""
            , color=discord.Color.blurple()
        )
    }
    fr_embeds = {
        "initial": discord.Embed(
            title="Page d'aide Krusty",
            description="Salut !\n"
                        "Tu as demandé de l'aide ?\n"
                        "Essaie de sélectionner une des catégories pour obtenir plus d'informations à ce sujet\n"
                        "\n"
                        "Voici les liens du UnitedCTF:\n"
                        "[UnitedCTF](https://unitedctf.ca/) | [Le CTF 2024](https://ctf.unitedctf.ca/)"
            , color=discord.Color.blurple()
        ),
        "tips": discord.Embed(
            title="Astuces et conseils pour le CTF",
            description="Voici quelques astuces et conseils pour le CTF:\n"
                        "1. Ne baisse pas les bras\n"
                        "2. Essaie de comprendre le défi\n"
                        "3. N'hésite pas à demander de l'aide\n"
                        "4. N'oublie pas de t'amuser !\n"
                        "\n"
                        "Quelques sites web qui pourraient t'aider au cours de ton aventure:\n"
                         "[Hacktricks](https://book.hacktricks.xyz/) | [CTF101](https://ctf101.org/)"
            , color=discord.Color.blurple()
        ),
        "commands": discord.Embed(
            title="Commandes",
            description="""Voici quelques commandes que vous pouvez utiliser :

</help:1279538522025365610> `language` : Obtenez de l'aide, la langue peut être `English` ou `Francais`

__-----------------------------**Ballons**-----------------------------__
</balloon_register:1279538522025365613> : Rejoignez le jeu de ballon ! Qui aura le plus de ballons à la fin ?
</balloon_buy:1279538522025365611> `secret` (Optionnel) : Achetez un nouveau ballon ! (Un ballon secret peut être obtenu avec le bon mot de passe)
</balloon_see:1279538522025365612> `player` : Regarde ta progression ! (Ou celle des autres)


__---------------------------**Notes de Dev**--------------------------__
/balloon_see : ! Corrigez l'affichage !
~~/get_role `role`~~ : désactivé [ Besoin d'être prudent sur les questions de permissions ]"""
            , color=discord.Color.blurple()
        )
    }
    

    def __init__(self, interaction, language):
        super().__init__()
        self.message = None
        self.interaction = interaction
        self.embeds = self.en_embeds if language == "en" else self.fr_embeds
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
        self.clear_items()

    async def on_error(self, interaction, error, item):
        await interaction.response.send_message("An error occured")
        raise error

    async def start(self):
        self.message = await self.interaction.response.send_message(embed=self.embeds["initial"], view=self)


async def setup(bot):
    await bot.add_cog(Help(bot), guild=discord.Object(id=int(os.getenv('CTF_GUILD_ID'))))

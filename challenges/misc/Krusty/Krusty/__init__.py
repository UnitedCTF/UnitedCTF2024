import discord
from discord.ext import commands

import dotenv
import os

commands_ext = (
    'Krusty.commands.Utils',
    'Krusty.commands.Flags',
    'Krusty.commands.Help',
    'Krusty.commands.BalloonsCommands',
)


async def setup_guild_for_ctf(guild: discord.Guild):
    roles = guild.roles
    ctf_roles = []
    privileged_members = []
    ctf_channel: discord.TextChannel = None

    for role in roles:
        if role.name == 'participant-2024':
            ctf_roles.append(role)

    # reset the roles to be safe with knowledge of those who got the privileged role
    if len(ctf_roles) != 0:
        for channel in guild.channels:
            if channel.name == 'what-is-this':
                ctf_channel = channel
        for role in ctf_roles:
            if ctf_channel.overwrites_for(role).read_messages:
                privileged_members = role.members
            await role.delete()

    # create the roles and the channel
    privileged = await guild.create_role(name='participant-2024', mentionable=False)
    unprivileged = await guild.create_role(name='participant-2024', mentionable=False)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, view_channel=False),
        privileged: discord.PermissionOverwrite(read_messages=True, read_message_history=True, view_channel=True,
                                                send_messages=False),
        unprivileged: discord.PermissionOverwrite(read_messages=False, view_channel=False)
    }
    if ctf_channel is not None:
        await ctf_channel.edit(overwrites=overwrites)
    else:
        ctf_channel = await guild.create_text_channel('what-is-this', overwrites=overwrites)
        # send the message to the channel
        await ctf_channel.send(os.getenv('CTF_CHANNEL_MESSAGE'))

    # give the privileged role to the members who had it before
    for member in privileged_members:
        await member.add_roles(privileged)

    # give the unprivileged role to everyone else
    for member in guild.members:
        if member not in privileged_members:
            await member.add_roles(unprivileged)

    # create a


class Krusty(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all()
        )
        self.remove_command('help')
        dotenv.load_dotenv()

    async def on_ready(self):
        for guild in self.guilds:
            self.tree.clear_commands(guild=guild)
            await setup_guild_for_ctf(guild)
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        Test_Guild = self.get_guild(int(os.getenv('CTF_GUILD_ID')))
        for ext in commands_ext:
            await self.load_extension(ext)
        print('Syncing commands in guild ' + Test_Guild.name)
        await self.tree.sync(guild=Test_Guild)
        print('Changing status')
        await self.change_presence(
            activity=discord.CustomActivity(name='......... Use /help to get help ...... ' + os.getenv("IN_ACTIVITY"),
                                            emoji='🤡'))
        print('Krusty is ready')

    async def on_member_join(self, member):
        # the self check is not necessary, but it includes a self in the method, so it is not flagged as a potential
        # static method
        if member.guild.id == int(os.getenv('CTF_GUILD_ID')) and member.id != self.user.id:
            await member.add_roles(discord.utils.get(member.guild.roles, name='participant-2024'))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()






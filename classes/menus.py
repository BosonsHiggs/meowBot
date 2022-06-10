import discord
from discord.ext import commands
from discord import app_commands

TEST_GUILD = PRIVATE_GUILD_ID_HERE
class Menus(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.ctx_menu = (
            app_commands.ContextMenu(
                name='Msg command 1',
                callback=self.hello_command,
                guild_ids=[TEST_GUILD]
            ),

            app_commands.ContextMenu(
            name='User command 1',
            callback=self.show_command,
            guild_ids=[TEST_GUILD]
            )
        )
        for _ctx_menu in self.ctx_menu:
            self.bot.tree.add_command(_ctx_menu,  guild=discord.Object(TEST_GUILD))

    async def cog_unload(self) -> None:
        for _ctx_menu in self.ctx_menu:
            self.bot.tree.remove_command(_ctx_menu.name, type=_ctx_menu.type)

    @app_commands.checks.has_permissions(ban_members=True)
    async def hello_command(self, interaction: discord.Interaction, message: discord.Message) -> None:
        await interaction.response.send_message('hello...')

    @app_commands.checks.has_permissions(ban_members=True)
    async def show_command(self, interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
        await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Menus(bot))
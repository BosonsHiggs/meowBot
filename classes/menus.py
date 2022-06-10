import discord
from discord.ext import commands
from discord import app_commands

TEST_GUILD = GUILD_ID_HERE
class Menus(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name='Cool Command Name',
            callback=self.hello_command,
            guild_ids=[TEST_GUILD]
        )
        self.bot.tree.add_command(self.ctx_menu,  guild=discord.Object(id=TEST_GUILD))

    async def cog_unload(self) -> None:
        self.bot.tree.remove_command(self.ctx_menu.name, type=self.ctx_menu.type)

    @app_commands.checks.has_permissions(ban_members=True)
    async def hello_command(self, interaction: discord.Interaction, message: discord.Message) -> None:
        await interaction.response.send_message('hello...')

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Menus(bot))
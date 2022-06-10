import discord
from discord.ext import commands
from discord import app_commands
from typing import Union, List, Optional, Literal
from discord.ui import Modal, TextInput

from classes.applications import MyModal, GeneralButton

class Users(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot: commands.Bot = bot

  ##Groups
  @commands.has_permissions(administrator = False)
  @commands.hybrid_group(name="add")
  async def add_command(self, ctx: commands.Context):
    if ctx.invoked_subcommand is None:
      await ctx.send(f'Error! Error in add_command!', ephemeral=True)

  ##Commands
  @commands.cooldown(1, 10, commands.BucketType.guild)
  @add_command.command(name="newform", brief="Moderation・create a new form!")
  async def newform_command(
      self, 
      ctx: commands.Context,
      ):
    await ctx.defer()
    user1 = ctx.author
    messageid = ctx.message.id
    field = []

    ##Button
    emojis = ('✅')
    styles = tuple(discord.ButtonStyle.green for emoji in emojis)
    labels = tuple(None for emoji in emojis)
    urls = tuple(None for emoji in emojis)
    
    ##Modal: max 5 questions
    field.append(("Name", 'Your name here...', discord.TextStyle.long, 300, True))
    field.append(("Phone", 'Your phone number here...', discord.TextStyle.short, 10, True))
    field.append(("Email1", 'Your Email here...', discord.TextStyle.short, 30, True))
    field.append(("Email2", 'Your Email here...', discord.TextStyle.short, 30, True))
    field.append(("Email3", 'Your Email here...', discord.TextStyle.short, 30, True))

    myModal = MyModal("Job", "123456789", None, field)
    view = GeneralButton(emojis, labels, urls, styles, user1, False, True, messageid, myModal)
    
    #await ctx.interaction.response.send_modal(myModal)
    await ctx.send(content="Press!", view=view)

  @commands.hybrid_command(name="fruits")
  async def fruits_command(self, ctx:commands.Context, fruits: str):
    await ctx.interaction.response.send_message(f'Your favourite fruit seems to be {fruits}')

  @fruits_command.autocomplete('fruits')
  async def fruits_autocomplete(
    ctx: commands.Context,
    namespace: app_commands.Namespace,
    current: str
  ) -> List[app_commands.Choice[str]]:
    fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
    return [
      app_commands.Choice(name=fruit, value=fruit)
      for fruit in fruits if current.lower() in fruit.lower()
    ]
    
async def setup(bot: commands.Bot) -> None:
  TEST_GUILD = GUILD_ID_HERE
  #global sync
  #await bot.add_cog(Admins(bot))
  #Local sync
  await bot.add_cog(Users(bot), guilds=bot.get_guild(TEST_GUILD))
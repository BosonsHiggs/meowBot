#from os import write
import discord, asyncio
from discord.ext import commands
from discord import app_commands

initial_extensions = [
        'classes.menus',
        'classes.users'
        ]

TEST_GUILD = GUILD_ID_HERE

#intents = discord.Intents.all()
intents = discord.Intents(
    bans=True,
    dm_messages =True,
    dm_reactions=True,
    dm_typing=True,
    emojis=True,
    emojis_and_stickers=True,
    guild_messages=True,
    guild_reactions=True,
    guild_typing=True,
    guilds=True,
    integrations=True,
    invites=True,
    members=True,
    messages=True,
    message_content=True,
    presences=False,
    reactions=True,
    typing=True,
    voice_states=True,
    webhooks=True
    )


  ##############################
  ##                          ##
  ##       COMMANDS.BOT       ##
  ##                          ##
  ##############################
class MyBot(commands.Bot):
  def __init__(self, *, intents: discord.Intents, application_id: int):
    super().__init__(command_prefix="..", intents=intents, application_id=application_id)

  ##############################
  ##                          ##
  ##         SETUP_HOOK       ##
  ##                          ##
  ##############################
  async def setup_hook(self):
    for extension in initial_extensions:
      print(f'Loading module {extension}...')
      await self.load_extension(extension)			
    print('Modules loaded successfully!')

    ##Global sync
    #await self.tree.sync()

    ##Local sync
    await self.tree.sync(guild=self.get_guild(TEST_GUILD))


  ##############################
  ##                          ##
  ##         EVENTS           ##
  ##                          ##
  ##############################

  #Called when an Invite is created.
  async def on_invite_create(self, invite):
    #await check_invites(invite.guild)
    if invite.guild is None: return

    pass

  #Called when an Invite is deleted.
  
  async def on_invite_delete(self, invite):
    if invite.guild is None: return
    pass

  #### Remove as reações novas e antigas
  
  async def on_raw_reaction_remove(self, payload):
    try:
      channel_id = payload.channel_id
      channel = self.get_channel(channel_id)
    except:
      pass

    try:
      guild_id = payload.guild_id
      guild = self.get_guild(guild_id)
    except:
      pass
    try:
      user_id = payload.user_id
      user = guild.get_member(user_id)
    except:
      pass
      
    try:
      message_id = payload.message_id
      #message = channel.fetch_message(message_id)
    except:
      pass


    pass

  #### Pega as reações novas e antigas
  
  async def on_raw_reaction_add(self, payload):
    if payload is None: return
    
    pass
  
  async def on_message(self, message: discord.Message) -> None:
    if message.guild is None: return

    pass
    await self.process_commands(message)


  #### EVENTOS
  #### BAN MEMBER EVENT
  
  async def on_member_ban(self, guild, member):
    if guild is None or member is None: return
    
    pass
  
  async def on_member_join(self, member):
    if (member is None) or (member.guild is None): return
    pass

  
  async def on_member_remove(self, member):
    if (member is None) or (member.guild is None): return

    pass

  async def on_command_error(self, ctx: commands.Context, error: commands.CommandError) -> None:
    if (ctx is None) or ctx.guild is None: return
    if error is None: return

    guild = ctx.guild
    guild_id = guild.id
    channel = ctx.channel
    author = ctx.author

    pass
  
  async def on_guild_join(self, guild):
    if guild is None: return

    pass
  
  async def on_guild_remove(self, guild):
    guild_ids = []
    flag_1 = True

    if guild is None: return
    
    pass

  
  async def on_guild_role_create(self, role):
    guild = role.guild
    guild_id = guild.id

    if role is None: return

    pass
  
  
  async def on_guild_role_delete(self, role):
    guild = role.guild
    guild_id = guild.id
    
    pass
  
  
  async def on_guild_role_update(self, before, after):
    guild = after.guild
    
    if guild is None: return

    pass
  

  #Chamado com um servidor é atualizado: nome do canal, topicos, permissoes
  
  async def on_guild_channel_update(self, before, after):
    guild = after.guild

    if guild is None: return

    pass

  #Chamado quando um canal é criado
  
  async def on_guild_channel_create(self, channel):
    guild = channel.guild

    if guild is None: return

    pass
  
  #Chamado quando um canal é deletado
  
  async def on_guild_channel_delete(self, channel):
    guild = channel.guild

    if guild is None: return

    pass


  ##############################
  ##                          ##
  ##         ON_READY         ##
  ##                          ##
  ##############################
  async def on_ready(self) -> None:
    g = '```\n'
    g+=f'{self.user.name}\n'
    g+=f'ID: {self.user.id}\n'
    g+=f'SUCCESSFULLY LOGGED IN!\n'
    g+=f'```'

    print(g)

    
bot = MyBot(intents=intents, application_id=BOT_ID_HERE)

##############################
##                          ##
##           MAIN           ##
##                          ##
##############################

async def main():
  async with bot:
    await bot.start("TOKEN")

asyncio.run(main())

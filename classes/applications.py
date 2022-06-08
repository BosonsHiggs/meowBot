import discord
import traceback
from discord.ext import commands
from discord import app_commands
from discord.ui import Modal, TextInput


########################################
########                     ###########
########        MODALS       ###########
########                     ###########
########################################
# Defines a custom Modal with questions
# that user has to answer. The callback function
# of this class is called when the user submits the modal
class MyModal(Modal):
	def __init__(self, title:str=None, custom_id:str=None, timeout:int=None, *args) -> None:
		super().__init__(timeout=timeout, title=title, custom_id=custom_id)

		for form in args[0]:
			self.add_item(
							TextInput(
								label = form[0],
								placeholder = form[1],
								style = form[2],
								max_length = form[3],
								required = form[4]
							)
						)


	async def on_submit(self, interaction: discord.Interaction):
		await interaction.response.send_message(f"Submitting form! Wait!... {self.children[0].value}, {self.children[1].value}")

	async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
		await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

## Botões e listas
########################################
########                     ###########
########       BOTÕES        ###########
########                     ###########
########################################

class Button(discord.ui.Button["GeneralButton"]):
	def __init__(self, emoji, label, urls, style, return_, x: int, y: int, author, cont_custom, enable:bool=None, stop_:bool=True, modal:Modal=None):
		super().__init__(style=style, emoji=emoji, label=label, url=urls, row=y, custom_id=cont_custom)
		
		self.emoji = emoji
		self.label = label
		self.style = style
		self.return_ = return_
		self.author = author
		self.url = urls
		self.enable = enable
		self.custom_id = cont_custom
		self.stop_ = stop_
		self.modal = modal
		
	async def callback(self, interaction: discord.Interaction):
		assert self.view is not None
		view: GeneralButton = self.view

		self.disabled = self.enable
		self.label = self.label
		self.style = self.style
		self.url = self.url
		view.disable = self.enable
		
		#await interaction.response.send_message('waiting...', delete_after=1)
		#await interaction.response.defer(ephemeral=True)

		"""if str(self.emoji) == "🎟️" and self.modal is None:
			await interaction.response.defer(ephemeral=True)
			guild_id = interaction.guild_id
			channel = interaction.channel
			guild = interaction.guild
			author = interaction.user

			await newticket(guild, channel, author, interaction)"""
		if self.modal is not None:
			await interaction.response.send_modal(self.modal)
			return
		else:
			await interaction.response.defer()
			
		view.value = self.return_
		view.interaction = interaction
		if self.stop_: view.stop()

class GeneralButton(discord.ui.View):
	def __init__(self, 
				emoji:str=None, 
				label:str=None, 
				urls:str=None, 
				style:discord.ButtonStyle=None, 
				author:discord.Member=None, 
				enable:bool=True, 
				stop:bool=True, 
				messageid:int=None,
				modal:Modal = None
	):
		super().__init__(timeout=None)
		self.label = label
		self.style = style
		self.emoji = emoji
		self.urls = urls
		self.enable = enable
		self.stop_ = stop
		self.messageid	= messageid
		self.modal = modal
		
		#self.value = None
		
		cont_x = 0
		cont_y = 0
		cont_custom = 0
		for a in range(len(style)):
			if urls[a] is not None:
				self.add_item(Button(self.emoji[a], self.label[a], self.urls[a], self.style[a], a, cont_x, cont_y, None, None, self.enable, self.stop_, self.modal))
			else:
				if self.messageid is None:
					self.add_item(Button(self.emoji[a], self.label[a], self.urls[a], self.style[a], a, cont_x, cont_y, author, str(cont_custom), self.enable, self.stop_, self.modal))
				else:
					self.add_item(Button(self.emoji[a], self.label[a], self.urls[a], self.style[a], a, cont_x, cont_y, author, str(self.messageid), self.enable, self.stop_, self.modal))

			cont_custom+=1
			cont_x+=1

			if cont_x == 5: 
				cont_x = 0
				cont_y +=1
import discord 
from discord.ext import commands
import os
import datetime
import time
from pytz import timezone
from datetime import datetime
import jishaku
from keep_alive import keep_alive
keep_alive()


client = commands.Bot(command_prefix=".", intents = discord.Intents.all(), owner_ids = [918956960571879437])
token = os.environ["token"]
timestamp = datetime.now()
logging_channel_id = 990309743555915866
user_id = 918956960571879437
client.remove_command('help')

@client.event
async def on_ready():
  await client.load_extension("jishaku")
  await client.load_extension("cogs.spy")
  await client.load_extension("cogs.nevermore")
  await client.load_extension('cogs.timer')
  await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name= f'Watching Over Outcasts !', url= 'https://youtube.com/shorts/buKaBN3dliw?feature=share'))
  print(f''' LOGGED IN AS {client.user}''')




if __name__ == '__main__':
  client.run(token)

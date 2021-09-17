# module imports
import discord
import os
import json

# cmd/event imports
from commands import cmds
from triggers import events
from groups import support

# import keep-alive
from server import keep_alive



botcf = json.load(open('botconfig.json'))



client = discord.Client()
TOKEN = os.environ['TOKEN']
prefix = botcf['prefix']


# runs on bot-login
@client.event
async def on_ready():
  print(f"{client.user.name} is online!")
  return



# runs on msg receive
@client.event
async def on_message(message):
  cmdRun = False
  eventRun = False
  
  if message.author.bot or message.author == client.user:
    return
  
  
  
  # will attempt to run an event if no cmd trigger was found
  if not message.content.lower().startswith(prefix):
    for event in events:
      if message.content == event.trigger:
        await event.run([client, message, prefix])
        eventRun = True
        pass
      elif event.trigger == "*":
        eventRun = await event.run([client, message, prefix])
        pass
    return
  
  
  
  # creates arr of each word in msg and separates cmd trigger from cmd args
  msg_arr = message.content.split(" ")
  cmd_arr = msg_arr[0].split(prefix)
  cmd_name = str(cmd_arr[1])
  args = []
  try:
    args = msg_arr[1:]
    pass
  except:
    pass
  
  
  
  # will attempt to run requested cmd
  if not eventRun:
    if not message.content.lower().startswith(prefix): return
    if cmd_name != "help":
      for cmd in cmds:
        if cmd_name == cmd.name:
          await cmd.run([client, message, args, prefix])
          cmdRun = True
      if not cmdRun: await message.reply(f"{cmd_name} is not a command!")
    else: await support.arr[0].run([client, message, args, prefix])
  return



# bot login and server start
keep_alive()
client.run(TOKEN)
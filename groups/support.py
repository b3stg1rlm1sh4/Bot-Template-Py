import discord
import json
from utils import Command
from commands import cmds

botcf = json.load(open("botconfig.json"))



async def help_func(client, message, args, prefix):
  embed = discord.Embed(color = message.author.roles[-1].color)
  embed.set_author(name="Command support!", icon_url=client.user.avatar_url)
  embed.set_footer(text = "Test commands are unlisted here", icon_url = message.guild.icon_url)
  
  out = ""
  if len(args) == 0:
    out = f"• fun"
    embed.description = out
    pass
  elif args[0].lower() == "fun":
    for cmd in cmds:
      if cmd.group == "fun":
        out = out + f"{cmd.name} ~ {cmd.details}\nexample ~ `{cmd.example}`\ngroup ~ {cmd.group}\n"
        pass
  
  embed.description = out
  
  if embed.description != "":
    await message.channel.send(embed=embed)
    pass
  else:
    await message.reply("that category doesn't exist!")
    pass
  
  try:
    await message.delete()
    canDel = True
  except:
    pass
  
  return



_help = Command("help", "provides command support", "support", f"{botcf['prefix']}help", help_func)



arr = [_help]
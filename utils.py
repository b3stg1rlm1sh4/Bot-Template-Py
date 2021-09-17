class Command:
  def __init__(self, name:str, details:str, group:str, example:str, func):
    self.name = name
    self.details = details
    self.group = group
    self.example = example
    self.func = func
  async def run(self, args):
    # 0:Discord.Client, 1:Discord.Message, 2:args[], 3:str(prefix)
    await self.func(args[0], args[1], args[2], args[3])



class Event:
  def __init__(self, trigger:str, func):
    self.trigger = trigger
    self.func = func
  async def run(self, args):
    # 0:Discord.Client, 1:Discord.Message, 2:str(prefix)
    await self.func(args[0], args[1], args[2])
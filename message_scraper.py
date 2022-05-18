import discord
import pandas as pd

client = discord.Client()

def is_good_message(msg):
  if len(msg.content.split()) < 4 or len(msg.content.split()) > 200:
    return False
  elif msg.content.startswith("<:") or msg.content.startswith("<@") or msg.content.startswith("https") or msg.content.startswith("-"): 
    return False
  elif msg.content.startswith(";;"):
    return False
  elif msg.author.name not in ["tree.", "Niick", "Alan", "jaden", "Jason4Hear"]:
    return False
  else:
    return True


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  elif message.author.name != 'Niick':
    return
  elif message.content.startswith("_"):
    cmd = message.content.split()[0].replace("_","")
    if len(message.content.split()) > 1:
      parameters = message.content.split()[1:]
    
    if cmd == "scan":
      data = pd.DataFrame(columns=['content', 'author'])
      await message.channel.send("Scanning...")
      #function to check if message is a command call
      def is_command (msg):
        if len(msg.content) == 0:
          return False
        elif msg.content.split()[0] == "scan":
          return True
        else: 
          return False
      
      async for msg in message.channel.history(limit=None):

        if msg.author != client.user:
          if not is_command(msg) and is_good_message(msg):
            data = data.append({'content': msg.content,
                                'author': msg.author.name}, 
                                ignore_index= True)
            
    file_location = "./data_court.csv"
    data.to_csv(file_location)
    await message.channel.send("Done Scanning")

client.run("OTU1ODQ1MDM1ODY4NDM4NjE5.YjnmDw.GDWp5che8sto3sOQ7eCfiNrz0cw")


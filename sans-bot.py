import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

from discord.utils import MAX_ASYNCIO_SECONDS

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="끔찍한 시간을 보내고싶어?"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
  msg = message.content
  if(msg == '!와' or msg == '!WA' or msg == "!wa"):
      await message.channel.send('https://tenor.com/view/sans-undertale-dance-gif-12730380')

client.run(client.run(os.environ['token']))
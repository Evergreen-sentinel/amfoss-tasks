import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content=True

url='https://www.espncricinfo.com/live-cricket-score'

html= requests.get(url)

s=BeautifulSoup(html.content, 'html.parser')

results = s.find(class_='ds-p-0')
team_1=results.find_all('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3')
a=team_1[0].text
team_2=results.find_all('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
b=team_2[0].text
score_1=results.find_all('strong', class_='ds-text-typo-mid3')
c=score_1[0].text
score_2=results.find_all('strong', class_="")
d=score_2[0].text


client = discord.Client(intents=intents)
bot=commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print('Logged in')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!score'):
        await message.channel.send('Team 1: '+a+'\n')
        await message.channel.send('Score 1: '+c+'\n')
        await message.channel.send('Team 2: '+b+'\n')
        await message.channel.send('Score 1: '+d+'\n')




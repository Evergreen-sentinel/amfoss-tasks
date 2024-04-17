import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content=True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def score(ctx):
    try:
        url = "https://www.espncricinfo.com/live-cricket-score"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        matches = soup.select('div[class="match-score-block"]')

        for match in matches:
            team_names = match.select('.ds-text-tight-m.ds-font-bold.ds-capitalize.ds-truncate')
            if len(team_names) == 2:
                team_1 = team_names[0].text.strip()
                team_2 = team_names[1].text.strip()
                score = match.select('.ds-text-compact-s.ds-text-typo.ds-text-right.ds-whitespace-nowrap')
                if len(score) == 2:
                    score_1 = score[0].text.strip()
                    score_2 = score[1].text.strip()
                    await ctx.send(f"{team_1} vs {team_2}: {score_1} - {score_2}")
                    break
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")



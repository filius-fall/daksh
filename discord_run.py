import os
import discord
import subprocess
from discord.ext import commands
from dotenv import load_dotenv

# from test_script import open_edit
from youtube_downlodaer import video_download,audio_download,twitch_vod_download
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")


load_dotenv()
DISCORD_FOLDER = os.getenv("DOWNLOAD_PATH")
bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx):
    # print("LKJKLJLK")
    # open_edit()
    await ctx.send("OPenes")

@bot.command()
async def youtube_video(ctx,link, res):
    path = DISCORD_FOLDER
    
    video_download(path, link, res)
    await ctx.send("Download started check your folder for the file")

@bot.command()
async def remote(ctx,link,res):
    if res.lower() == '720p':
        res = '-f 22'
    elif res.lower() == "best":
        res = "-f 'bestvideo+bestaudio'"
    else:
        res = ""
    download_link = "yt-dlp" + " " + res + " " + link
    process = subprocess.Popen(['ansible','Indra','-m','shell','-a',download_link],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout)
    await ctx.send("Downloaded................")

bot.run(DISCORD_TOKEN)
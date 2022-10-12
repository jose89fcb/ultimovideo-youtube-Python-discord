import discord
from discord.ext import commands
import json
import requests
 


bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
Api_key_Youtube = ""  #Conseguir Api Key de youtube: https://console.cloud.google.com/
Id_Canal_Youtube = "UC1s7u4KXpKD1MBCvOVuZCQg" #IR al canal de vuestro Youtube favorito
url_youtube = "https://www.youtube.com/watch?v="

@bot.command()
async def hola(ctx): #Comando a decir
    

    response = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={Api_key_Youtube}&channelId={Id_Canal_Youtube}&part=snippet,id&order=date&maxResults=20")

    video = response.json()["items"][0]["snippet"]["title"]
    id_video_youtube = response.json()["items"][0]["id"]["videoId"]


    await ctx.send(f'{video}\n\n{url_youtube}{id_video_youtube}') #Mensaje que dira el bot
 
 

 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications
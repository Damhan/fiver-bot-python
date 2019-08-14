#Work with Python 3.6
import discord
from selenium import webdriver
import time

TOKEN = 'NjExMTQxNzgzMTc0MjUwNTI2.XVPgQQ.ubshJmHdwrcmTmuNiJrNyx1ZrXQ'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        driver = webdriver.Chrome()
        robloxUrl = "https://www.roblox.com/games/?SortFilter=default&TimeFilter=0"
        # browser.get(robloxUrl)

        driver.get(robloxUrl)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        # sleep for 30s
        time.sleep(5)
        images = driver.find_elements_by_class_name("game-card-thumb")
        channel = client.get_channel(604025309418881056)
        for image in images:
            if image.get_attribute('src'):
                await channel.send(image.get_attribute('src'))
                print(image.get_attribute('src'))

        
        with open('myimage.PNG', 'rb') as picture:
            await channel.send(file=discord.File('myimage.PNG'))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
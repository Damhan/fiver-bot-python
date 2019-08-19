import discord
from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

##
##CHANGE THIS TO YOUR TOKEN
##
TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    # Make sure bot doesn't reply to itself.
    if message.author == client.user:
        return

    if message.content.startswith('!thumbnails'):
        ##CHANGE THIS TO THE CHANNEL ID YOU WANT
        ##THUMBNAILS TO GO TO
        channel = client.get_channel()
        tokens = message.content.split(" ")
        options = webdriver.ChromeOptions()
        
        if len(tokens) > 1:
            count=int(tokens[1])
            options.add_argument('headless')
            options.add_argument("window-size=1920,1080")
            driver = webdriver.Chrome(options=options)
            robloxUrl = "https://www.roblox.com/games/?SortFilter=default&TimeFilter=0"

            
            #Get our Roblox Games Page, Scroll down, and wait two seconds
            #This allows the thumbnails to be populated via javascript.
            driver.get(robloxUrl)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            time.sleep(2)
            images = driver.find_elements_by_class_name("game-card-thumb")


            #Go until we run out of images or
            #until we reach the specified amount
            counter = 0
            for image in images:
                print(counter)
                if counter == count:
                    counter = 0
                    break
                else:
                    if image.get_attribute('src'):
                        counter += 1
                        await channel.send(image.get_attribute('src'))
                        print(image.get_attribute('src'))
                
            driver.close()
            print("Closing Driver")
        else:
            await channel.send("You must specify how many, eg: !roblox 10")
        
        
    if message.content.startswith('!ads'):
        ##
        ##CHANGE THIS ID TO CHANNEL ID YOU WANT AD1 TO GO TO
        channel1 = client.get_channel(611273506939994153)
        html = urlopen('https://www.roblox.com/user-sponsorship/1')
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('rbxcdn.com')})
        for image in images: 
            await channel1.send(image['src']+'\n')

        ##
        ##CHANGE THIS ID TO CHANNEL ID YOU WANT AD2 TO GO TO
        channel2 = client.get_channel(611273517945585664)
        html = urlopen('https://www.roblox.com/user-sponsorship/2')
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('rbxcdn.com')})
        for image in images: 
            await channel2.send(image['src']+'\n')

        ##
        ##CHANGE THIS ID TO CHANNEL ID YOU WANT AD3 TO GO TO
        channel3 = client.get_channel(611273525428486144)
        html = urlopen('https://www.roblox.com/user-sponsorship/3')
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('rbxcdn.com')})
        for image in images: 
            await channel3.send(image['src']+'\n')



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
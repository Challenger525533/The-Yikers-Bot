import discord
import random
import time

client = discord.Client()
myserver = discord.Guild.id
count_file = open('./number.txt', 'r')
count = int(count_file.readline())
print(count)
count_file.close()
#verypreviousAuthor = 0
#previousAuthor = 0
startBotActivity = discord.Game("The Most Dangerous Game")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=startBotActivity)
    previousAuthor = 0

@client.event
async def on_message(message):
    print("New Message Detected")
   # global verypreviousAuthor
   # global previousAuthor
    global count
    global count_file
    count = count + 1
    count_file = open('/home/container/number.txt', 'w')
    count_file.write(str(count))
    count_file.close()
    if message.channel.id == 672867381609103390:
        print("right channel")
       # myuser = message.author
        if message.content != "Yikes":
            print("content is not yikes")
            await message.delete()
       # elif previousAuthor == message.author.id:
        #    print("Author matching")
         #   await message.delete()
        else:
            print("I should be clear!")
         #   verypreviousAuthor = previousAuthor
         #   previousAuthor = message.author.id
            await client.change_presence(status=discord.Status.online, activity=discord.Game("with " + str(count) + " Yikes"))

    @client.event
    async def on_message_delete(message):
        print("Deleted Message Detected")
        global verypreviousAuthor
        global previousAuthor
        global count
        global count_file
        if message.channel.id == 672867381609103390:
            print("right channel")
         #   if (previousAuthor != verypreviousAuthor):
          #      previousAuthor = verypreviousAuthor
            count = count - 1
        count_file = open('/home/container/number.txt', 'w')
        count_file.write(str(count))
        count_file.close()
        await client.change_presence(status=discord.Status.online, activity=discord.Game("with " + str(count) + " Yikes"))
    
    @client.event
    async def on_message_edit(oldmessage, newmessage):
        print("Edited message detected")
        global verypreviousAuthor
        global previousAuthor
        global count
        if newmessage.channel.id == 672867381609103390:
            print("right channel")
            if newmessage.content != "Yikes":
                await newmessage.delete()
        await client.change_presence(status=discord.Status.online, activity=discord.Game("with " + str(count) + " Yikes"))


client.run(INSERT_TOKEN_HERE)

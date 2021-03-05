import json

import discord
import os
import random
from discord import member
from discord.ext import commands
from discord import ChannelType
from discord.ext.commands import Bot
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')


#@commands.Cog.listener()
#async def on_member_join(self, member):
#    await self.client.get_channel(793252653975076945).send(f'{member} has joined the server!')
#    print(f'{member} has joined the server.')

#@client.event
#async def on_member_remove(member):
#    print(f'{member} has left the server.')

@client.command(pass_context=True)
async def roll(ctx, d=6):
    username = ctx.message.author.name
    num = random.randint(1, d)
    if d == 20 and num == 20:
        await ctx.send(f'{username} rolled a natural 20 on a d20!')
    elif d == 20 and num == 1:
        await ctx.send(f'{username} rolled a natural 1 on a d20!')
    else:
        await ctx.send(f'{username} rolled a d{d} and got {num}')

@client.command(pass_context=True)
async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send(f'hello, {username}')

@client.command(pass_context=True,aliases=['8ball'])
async def _8ball(ctx, *, question):
    username = ctx.message.author.name
    responses = ['As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.']
    await ctx.send(f'{username} asked the question: {question}\nAnswer: {random.choice(responses)}')

@client.command(pass_context=True)
async def teams(ctx, amount=2):

    # sends message indicating must be in voice channel
    if(ctx.message.author.voice is None):
        return await ctx.send('You need to be in a voice channel to use this command.')

    # grabs voice channel  of user
    voice_channel = ctx.message.author.voice.channel

    # grabs voice channel by id
    VC = discord.utils.get(ctx.guild.channels, id=voice_channel.id)

    #initialize variable to track if other channels have members, assumes false
    otherChannelsHasMembers = False

    #iterates through each channel in the server
    for channel in ctx.message.guild.channels:
        #checks if the channel is a voice channel AND not the author's voice channel AND if there are members in it
        if channel.type == ChannelType.voice and channel != voice_channel and channel.members != []:
            otherChannelsHasMembers = True
            break

    #prints the Channel Name only if there are people in other voice channels
    if otherChannelsHasMembers == True:
        await ctx.send(VC)

    #declares full list and adds all users in VC to list
    fulllist = []
    for user in VC.members:
        if user.nick is None:
            fulllist.append(user.name)
        else:
            fulllist.append(user.nick)

    #shuffles list
    random.shuffle(fulllist)

    #split list into desired amount
    groupedlist = [fulllist[i::amount] for i in range(amount)]
    num = 1
    for x in groupedlist:
        team = ", ".join(x)
        await ctx.send(f"Team {num}: {team}")
        num += 1

@client.command(pass_context=True)
async def cheers(ctx):
    await ctx.send('DRINK UP BITCHES!')

@client.command(pass_context=True)
async def get_members(ctx, role_name):
    role = discord.utils.find(
        lambda r: r.name == role_name, ctx.guild.roles)
    if role is None:
        await ctx.send(f"{role_name} does not exist!")
        return
    roleList = []
    for user in ctx.guild.members:
        if role in user.roles:
            if user.nick is None:
                roleList.append(user.name)
            else:
                roleList.append(user.nick)
    if roleList == []:
        await ctx.send(f"No members in that role!")
    else:
        join_string = ", ".join(roleList)
        await ctx.send(f"List of members in {role}: {join_string}")







f = open('config.json')
data = json.load(f)
client.run(data['token'])


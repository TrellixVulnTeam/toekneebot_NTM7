import json

import discord
import os
import random
from discord import member
from discord.ext import commands
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
async def champselect(ctx):
    username = ctx.message.author.name
    champions = ['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie',
                 'Aphelios','Ashe','Aurelion Sol','Azir','Bard','Blitzcrank',
                 'Brand','Braum','Caitlyn','Camille','Cassiopeia','ChoGath',
                 'Corki','Darius','Diana','Dr. Mundo','Draven','Ekko','Elise',
                 'Evelynn','Ezreal','Fiddlesticks','Fiora','Fizz','Galio',
                 'Gangplank','Garen','Gnar','Gragas','Graves','Hecarim',
                 'Heimerdinger','Illaoi','Irelia','Ivern','Janna','Jarvan IV',
                 'Jax','Jayce','Jhin','Jinx','KaiSa','Kalista','Karma','Karthus',
                 'Kassadin','Katarina','Kayle','Kayn','Kennen','KhaZix','Kindred',
                 'Kled','KogMaw','LeBlanc','Lee Sin','Leona','Lillia','Lissandra',
                 'Lucian','Lulu','Lux','Malphite','Malzahar','Maokai','Master Yi',
                 'Miss Fortune','Mordekaiser','Morgana','Nami','Nasus','Nautilus',
                 'Neeko','Nidalee','Nocturne','Olaf','Orianna','Ornn','Pantheon',
                 'Poppy','Pyke','Qiyana','Quinn','Rakan','Rammus','RekSai','Rell',
                 'Renekton','Rengar','Riven','Rumble','Ryze','Samira','Sejuani','Senna',
                 'Seraphine','Sett','Shaco','Shen','Shyvana','Singed','Sion','Sivir',
                 'Skarner','Sona','Soraka','Swain','Sylas','Syndra','Tahm Kench','Taliyah',
                 'Talon','Taric','Teemo','Thresh','Tristana','Trundle','Tryndamere','Twisted Fate',
                 'Twitch','Udyr','Urgot','Varus','Vayne','Veigar','VelKoz','Vi','Viktor','Vladimir',
                 'Volibear','Warwick','Wukong','Xayah','Xerath','Xin Zhao','Yasuo','Yone','Yorick',
                 'Yuumi','Zac','Zed','Ziggs','Zilean','Zoe','Zyra',]
    await ctx.send(f'{username} should play {random.choice(champions)}')

@client.command(pass_context=True)
async def teams(ctx, amount=2):

    # sends message indicating must be in voice channel
    if(ctx.message.author.voice is None):
        return await ctx.send('You need to be in a voice channel to use this command.')

    # grabs voice channel id of user
    voice_channel_id = ctx.message.author.voice.channel.id
    #voice_state = ctx.message.author.voice

    #grabs voice channel by id
    VC = discord.utils.get(ctx.guild.channels,id=voice_channel_id)
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

    await ctx.send(groupedlist)


async def cheers(ctx):
    await ctx.send('DRINK UP BITCHES!')

f = open('config.json')
data = json.load(f)
client.run(data['token'])


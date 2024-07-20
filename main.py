import discord 
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has started fighting against pedos')

@bot.event
async def on_member_join(member: discord.Member):
    ###chanellid should be written like this 0000000 not '0000000', this also aplies for the mbm .id
    channel = bot.get_channel(channelid)
    if member.id == mbm.id:
        await member.ban()
        await channel.send(f'Known pedo' + member.mention + ' has been banned')
    
    ###for every id you get copy the code and change the member.id

bot.run('token')

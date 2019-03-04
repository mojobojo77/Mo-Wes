import discord
from discord.ext import commands
import asyncio
from itertools import cycle

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


status = ['FUNCTION CHECK....', 'GETTING THAT DUB.....', 'DESTROYING E-G']



async def change_status():
    await bot.wait_until_ready()
    msg = cycle(status)


    while not bot.is_closed:
        current_status = next (msg)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(60)



@bot.command
async def creatorinfo():
    embed = discord.Embed(
        title = 'Bot Creator',
        description = 'This Bot was made by Mohammed.I or also known (in discord) as YEETBOI',
        Color= discord.Color.Blue()
    )
    embed.set_footer(text='Some info about the creator:')
    embed.set_image(url='https://i.redd.it/6ipk5ua5ch611.png')
    embed.set_thumbnail(url='https://storage.pixteller.com/designs/designs-images/2018-11-05/08/epic-gamer-moment-1-5be0915fb50bb.png')
    embed.set_author(name= 'TheGamer2020#2173',
    icon_url= 'https://pics.me.me/yeet-36468345.png' )
    embed.add_field(name='Description', value='THANK YOU FOR USING THIS BOT! :)', inline=False)


    await bot.say(embed=embed)

 



@bot.command(pass_context=True)
async def help(ctx):
    author= ctx.message.author
    
    
    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Commands')
    embed.add_field(name='Commands:', value='.creatorinfo,.help,.ping,.lit,.clear, More coming!!!', inline=False)

    await bot.send_message(author, embed=embed)









  





@bot.event 
async def on_ready():

      print ("Welcome Back Master")
      print ("I am running on" + bot.user.name)
      print ("With the ID:" + bot.user.id)
      
   
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping! x9999")
    print("YOU HAVE PINGED!!!!")

  

@bot.command()
async def echo (*args):
    output = ''
    for word in args:
        output+=word
        output+= ''
        await bot.say(output)

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
        await bot.delete_message(messages)
        await bot.say('Messages deleted.')


@bot.event
async def on_message_delete(message):
    author = message.author
    content= message.content
    channel = message.channel
    await bot.send_message(channel, '{}: {}'.format(author,content))

@bot.command()
async def on_message(message):
    print('A user has sent a message')
    await bot.process_commands(message)


@bot.event 
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name= 'UNKNOWN GOD')
    await bot.add_roles(member, role)


@bot.command(pass_context=True)
async def lit(ctx):
    await bot.say(":100: It sure is!! ")
    print("YOU ARE LIT")


@bot.command(pass_context=True)
async def botinfo(ctx):
    embed = discord.Embed(title="Creator",description="Mohammed.I,Luis and Mohammed.R",color=0x00ff00)
    embed.set_footer(text="This is our first bot so it is very basic ,meant for a school project")
    embed.set_author(name="Mo Wes Bot Info")
    await bot.say(embed=embed)



@bot.command(pass_context=True)
async def creatorinfo():
    embed = discord.Embed(
        title = 'Bot Creator',
        description = 'This Bot was made by Mohammed.I or also known (in discord) as YEETBOI',
        colour= discord.Colour.blue()
    )
    embed.set_footer(text='Some info about the creator:')
    embed.set_image(url='https://i.redd.it/6ipk5ua5ch611.png')
    embed.set_thumbnail(url='https://storage.pixteller.com/designs/designs-images/2018-11-05/08/epic-gamer-moment-1-5be0915fb50bb.png')
    embed.set_author(name= 'TheGamer2020#2173',
    icon_url= 'https://pics.me.me/yeet-36468345.png' )
    embed.add_field(name='Description', value='THANK YOU FOR USING THIS BOT! :)', inline=False)
    embed.add_field(name='ANOTHER message', value='This is a school project so sorry for the bad excution for the bot', inline=True)
    embed.add_field(name='Last message', value='My discord is YEETBOI#2173', inline=True)



    await bot.say(embed=embed)







bot.loop.create_task(change_status())
bot.run("NTQyMjI3MDk5NzA1MTQ3Mzky.D0RlpQ.Iw6SnI1ZG1SMLCMT9vX1fBJUK7I")


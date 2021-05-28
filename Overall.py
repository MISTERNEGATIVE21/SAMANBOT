import discord
import random
from discord.ext import commands

client = commands.Bot (command_prefix ="%")

@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.idle, activity= discord.Activity(type= discord.ActivityType.playing, name="%help"))
    print('Bot is online')

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def info(ctx):
    await ctx.send("Hey, glad to see you, I am Suman's Bot")

@client.command()
async def ILoveYou(ctx):
    await ctx.send("I love you too")


@client.command()
async def Engineering(ctx):
    embed = discord.Embed(title='EVERYTHING IS AN ENGINEERING', description='Engineering is the use of scientific principles to design and build machines, structures, and other items, including bridges, tunnels, roads, vehicles, and buildings.')
    embed.set_footer(text='This is a footer.')
    embed.set_image(url='https://d3jh33bzyw1wep.cloudfront.net/s3/W1siZiIsIjIwMTkvMDEvMTYvMTEvNDYvNTQvMzA1L3BleGVscy1waG90by01NDY4MTkuanBlZyJdXQ' )
    embed.set_thumbnail (url='https://www.yacht.nl/binaries/page-hd/content/gallery/yacht/header-images/professionals/expats/career-opportunities-engineering-for-expats.jpg' )
    embed.set_author(name='Suman Dey',icon_url = 'https://static.thenounproject.com/png/302770-200.png')
    embed.add_field(name='Computer Science Engineering', value = 'Computer Science & Engineering (CSE) is an academic program at many universities which comprises scientific and engineering aspects of computing. CSE is also a term often used in Europe to translate the name of engineering informatics academic programs.', inline = True)
    embed.add_field(name='Electronics Engineering', value ='Electronic engineering is an electrical engineering discipline which utilizes nonlinear and active electrical components (such as semiconductor devices, especially transistors and diodes) to design electronic circuits, devices, integrated circuits and their systems. ' , inline = True)
    embed.add_field(name='Electrical Engineering', value = 'Electrical engineering is an engineering discipline concerned with the study, design and application of equipment, devices and systems which use electricity, electronics, and electromagnetism. It emerged as an identifiable occupation in the latter half of the 19th century after commercialization of the electric telegraph, the telephone, and electrical power generation, distribution and use.', inline = False)
    embed.add_field(name='Mechanical Engineering', value = 'Mechanical engineering is an engineering branch that combines engineering physics and mathematics principles with materials science to design, analyze, manufacture, and maintain mechanical systems.[1] It is one of the oldest and broadest of the engineering branches.', inline = True)
    embed.add_field(name='Civil Engineering', value = 'Civil engineering is a professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment, including public works such as roads, bridges, canals, dams, airports, sewerage systems, pipelines, structural components of buildings, and railways.', inline = False)
    embed.add_field(name='Aerospace Engineering', value = 'Aerospace engineering is the primary field of engineering concerned with the development of aircraft and spacecraft.[3] It has two major and overlapping branches: aeronautical engineering and astronautical engineering. Avionics engineering is similar, but deals with the electronics side of aerospace engineering.', inline = True)
    embed.add_field(name='Chemical Engineering', value = 'Chemical engineering is a certain type of engineering which deals with the study of operation and design of chemical plants as well as methods of improving production. Chemical engineers develop economical commercial processes to convert raw material into useful products.' , inline = True)

    await ctx.send(embed=embed)



@client.command()
async def slap(ctx):
    await ctx.send("আমি একটি শিশুকে চড় মারব না")


@client.command()
async def goodnight(ctx):
    await ctx.send("Good Night Sweety, Sweet Dreams :new_moon_with_face:")

@client.command()
async def goodmorning(ctx):
    await ctx.send("Very Good Morning Sweety, Have a great day!")


@client.command()
async def sayambhu(ctx):
    await ctx.send("Sayambhu is a **GANDU**")

@client.command()
async def shujash(ctx):
    await ctx.send("Please don't call me Shujash, call me **RAKHI**")

@client.command()
async def suman(ctx):
    await ctx.send("He is a very good boi. Afterall he is my creator and my owner. I love him so much.")

@client.command()
async def bej(ctx):
    await ctx.send("Bej is a very good boi. He is a piro coder. My owner is learning how to develop me from him. I love him also.")

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def wishus1(ctx):
    await ctx.send("**বিদায় রাগিণী বাজিয়ে গেল জীর্ণ পুরাতন বর্ষ,নববর্ষ নিয়ে আসবে সবরকমের হর্ষ। শুভ নববর্ষের শুভেচ্ছা!**")

@client.command()
async def wishus2(ctx):
    await ctx.send("**আজ এই শুভ দিনে কত খুশি, কত সাজ। আজ এই শুভ দিনে ভুলে যাও সব কাজ। শুভ নববর্ষ!**")

@client.command()
async def Ask(ctx,*,question):
    responses = ['As I see it', 
                'Yes.',
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
                'Outlook not so good',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.',
                'Loading...',
                'Wait...',
                'Thinking...',
                'May be yes.',
                'May be no.',
                'Who are you, to asking me this question?',  
                'Go and faak yourself'            
                ]
    await ctx.send (f'**Question**: {question}\n**Answer**: {random.choice(responses)} ')



@client.event
async def on_ready():
    print("Bot Is Ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
async def toss(ctx):
    
    type = random.randint(1,2)
    if type == 2:
        embed = discord.Embed(title='**HEADS**')
        embed.set_thumbnail (url="https://qph.fs.quoracdn.net/main-qimg-3a556d0d96025c086d37f29cf9bd73ea")
    else :
         embed = discord.Embed(title='**TAILS**')
         embed.set_thumbnail (url="https://qph.fs.quoracdn.net/main-qimg-148ae81e6fe0500e130fb547026a9b26")

    await ctx.send(embed=embed)



@client.command()
async def rolldice(ctx):
    
    type = random.randint(1,5)
    if type == 1:
        embed = discord.Embed(title='**ONE[1]**')
        embed.set_thumbnail (url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJH4Rn1b88KbD31SCyFo89fMwJetAoH7ElLvEpOVZn2Gb9wMTnINnaVRTXiUmUU0Jh_vE&amp;usqp=CAU")
    
    if type == 2:
        embed = discord.Embed(title='**TWO[2]**')
        embed.set_thumbnail (url="https://www.media4math.com/sites/default/files/library_asset/images/MathClipArt--Single-Die-with-2-Showing.png")
    
    if type == 3:
        embed = discord.Embed(title='**THREE[3]**')
        embed.set_thumbnail (url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkegCjwqOfG3WOvIfoEXz9tvP6bjU_l_DXq5riPTCsPhTLNt131tgXGqHuPa-AJ4a2gdU&amp;usqp=CAU")
    
    if type == 4:
        embed = discord.Embed(title='**FOUR[4]**')
        embed.set_thumbnail (url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtwoIaQplQf1TEJiwHdJ3KexW-SQwB7fb5wt8NWuWdHLF9qIKff6z9aVBE-5v1WbfXXHA&amp;usqp=CAU")
    
    if type == 5:
        embed = discord.Embed(title='**FIVE[5]**')
        embed.set_thumbnail (url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx0I71jj0pt2W9FlMHzkJsnqFQGmNZcILlTEK9vzwut4M791ePqIGRG1drcww33GrJ2PQ&amp;usqp=CAU")
    
    if type == 6:
         embed = discord.Embed(title='**SIX[6]**')
         embed.set_thumbnail (url="https://slm-assets.secondlife.com/assets/5844708/view_large/White%206.jpg")

    await ctx.send(embed=embed)





client.run ("ODI0MzcxODY3MzA5MTc4OTAw.YFuaIQ.BH1iYXisNS0TkBWYQD3u6JClSoE")
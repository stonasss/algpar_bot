import os
from dotenv import load_dotenv
load_dotenv()
BOT_KEY = os.getenv('DISCORD_TOKEN')

import discord
from discord.ext import commands
permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True
bot = commands.Bot(command_prefix=".", intents=permissions)

@bot.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
    res = num1 + num2
    await ctx.reply(f'A soma de {num1} com {num2} resulta em {res}.')
    
@bot.command()
async def falar(ctx:commands.Context, *,sentence):
    await ctx.send(sentence)
    
@bot.command()
async def oi(ctx:commands.Context):
    my_embed = discord.Embed(title='Olá amigo!', description="tamo junto")
    
    image = discord.File('images/pngtree-beagle-dog-the-rock-star-with-sunglasses-png-image_10272754.png', 'image.png')
    my_embed.set_image(url='attachment://image.png')
    
    thumb = discord.File('images/opera_QnhgkiiIvL.png', 'thumb.png')
    my_embed.set_thumbnail(url='attachment://thumb.png')
    
    my_embed.set_footer(text='Divirta-se!')
    
    my_embed.color = discord.Color.blurple()
    await ctx.reply(files=[image, thumb], embed=my_embed)

@bot.event
async def on_guild_channel_create(channel:discord.abc.GuildChannel):
    await channel.send(f'Novo canal criado: {channel.name}!')
    
@bot.event
async def on_member_join(member:discord.Member):
    channel = bot.get_channel(1309221885728522270)
    my_embed = discord.Embed(title=f'Bem-vindo, {member.display_name}!', description='Feliz de te ver por aqui, amigo.')

    my_embed.set_thumbnail(url=member.avatar)
    
    my_embed.set_footer(text='Qualquer coisa chama!')
    
    my_embed.color = discord.Color.dark_orange()
    await channel.send(embed=my_embed)

@bot.event
async def on_ready():
    print("Estou online!")
    
bot.run(BOT_KEY)
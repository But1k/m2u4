import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def help(ctx):
    print(f'Список команд'
          f'mem'
          f'Выдает любой мем с сервера'
          f'help'
          f'команда для изучения функций'
          f'igra'
          f'начинает игру орел или решка'
          f'plusi'
          f'какие могут быть плюсы от ухода за природой')
    
@bot.command()
async def plusi(ctx):
    print(f'1: При собирании мусора и сдачи его на переработку вы будете получать деньги'
          f'2: В вашем городе, поселке, деревне станет на много чище и приятнее'
          f'3: Появленее одежды разной новой одежды')

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

images = ['mem1.jpg', 'mem2.jpg','mem3.jpg']
print(os.listdir('images'))

@bot.command()
async def mem(ctx):
    print(random.choice(images))

@bot.command()
async def igra(ctx):
    print("Добро пожаловать в игру 'Орел и решка'")

    podbr=int(input("Сколько раз хотите подбросить монету?"))
    raz=0
    orel=0
    rejka=0

    while raz<podbr:   
        pir=random.randint(1,2)
        raz+=1
    if pir==1:
        orel+=1
    elif pir==2:
        rejka+=1

print("Орел выпал",orel,"раз")

print("Решка выпала",rejka,"раз")



bot.run('MTE1NTE2ODQ1MjY0Mjg3NzU3Mg.GHsfo2.BrIvmcPUs8O0FiJ2e32O6ESAQ0CFZ6SKJeg6mY')
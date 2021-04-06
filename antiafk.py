
import random, os, time, colorama
from colorama import Fore
from discord.ext import commands
c = Fore.CYAN
re = Fore.RESET
g = Fore.GREEN
R = Fore.RED
lr = Fore.LIGHTRED_EX
b = Fore.LIGHTBLACK_EX

colorama.init()
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

os.system(f'title [Welcome To Skadaddle Anti Afk Check] - V1')

n = ["look at what this goof said","yikes he tried","oxy is so lazy","imagine being as bad as qud","yeah okay get anti afked kid","aww so sad","yikes good luck checking me","your mom is dead and u failed XD"]





def clear():
    os.system('cls')

def skad():
    print(f'''
                                 {re}♥♥♥♥♥♥  ♥♥♥    ♥♥ ♥♥      ♥♥♥♥♥♥ ♥♥   ♥♥  ♥♥♥♥♥  ♥♥♥    ♥♥ 
                                {b}♥♥    ♥♥ ♥♥♥♥   ♥♥ ♥♥     ♥♥      ♥♥   ♥♥ ♥♥   ♥♥ ♥♥♥♥   ♥♥ 
                                {lr}♥♥    ♥♥ ♥♥ ♥♥  ♥♥ ♥♥     ♥♥      ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥ ♥♥ ♥♥  ♥♥ 
                               {lr} ♥♥    ♥♥ ♥♥  ♥♥ ♥♥ ♥♥     ♥♥      ♥♥   ♥♥ ♥♥   ♥♥ ♥♥  ♥♥ ♥♥ 
                                {R} ♥♥♥♥♥♥  ♥♥   ♥♥♥♥ ♥♥      ♥♥♥♥♥♥ ♥♥   ♥♥ ♥♥   ♥♥ ♥♥   ♥♥♥♥{re}
Made by skadaddle with <3                                                                    
''')
skad()

token = input(f'{R}[{re}--{R}] {R}Token{re}:{R} ')

@client.event
async def on_ready():
    clear()
    skad()
    os.system(f'title [Skadaddle] {client.user.name}#{client.user.discriminator} Authorized - Protected in {len(client.guilds)} Guilds')

@client.event
async def on_message(message):
    p = ["look at what this goof said","yikes he tried","oxy is so lazy","imagine being as bad as qud","yeah okay get anti afked kid","aww so sad","yikes good luck checking me","your mom is dead and u failed XD"]
    o = f'title [Skadaddle] Just Bodied {message.author} In {message.channel} - Msg: [{message.content}] Blocked'
    r = ["can't touch me :rolling_eyes: :heart:","yes daddy? :flushed:",f"<@!{message.author.id}>  suck my dick","stop it cutie :rolling_eyes:",f"this nigga <@!{message.author.id}> love's me ong",f"look at this dick rider named <@!{message.author.id}>","lol nice try","good luck next time","can't check me","stop trying kiddo",f"your my son <@!{message.author.id}> :joy:",f"lmao dumb kid really saying ''{message.content}''","stop tryna afk check me :skull:",f'<@!{message.author.id}> what do u want skid stop saying "{message.content}"']
    n = f'[{R}{time.strftime("%I:%M:%S")}{re}] ({message.author.id}) [{message.author}] {random.choice(p)} [{g}{message.content}{re}] in [{R}{message.channel}{re}]'
    if "afk check" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
            
    elif f"<@!{client.user.id}>" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
    elif f"test" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
    elif "focus son" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
            
    elif f"<@!{client.user.id}> afk check" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
            
    elif f"afk check <@!{client.user.id}>" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
            
    elif f"wake up" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
    elif f"quit sleeping" in message.content.lower():
        await message.channel.send(f"{random.choice(r)}")
        print(n)
        os.system(o)
    
if __name__ == '__main__':
    client.run(token, bot=False)

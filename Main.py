class SELFBOT():
    __linecount__ = 3602
    __version__ = 3.1

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, codecs, webbrowser, re, humor_langs, asyncpraw, urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging, nekos, art, concurrent.futures

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from colorama import Fore
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
import random
import pyperclip
from urllib.parse import quote
from decimal import Decimal, getcontext

ctypes.windll.kernel32.SetConsoleTitleW(f"[ST'S COOL SELFBOT v{SELFBOT.__version__}]")

with open('data/config.json') as f:
    config = json.load(f)

token = config['token']
password = config['password']
prefix = config['prefix']

giveaway_sniper = config['giveaway_sniper']
slotbot_sniper = config['slotbot_sniper']
nitro_sniper = config['nitro_sniper']['nitro_sniper']
open_in_browser = config['nitro_sniper']['open_in_browser']
send_in_channel = config['nitro_sniper']['send_in_channel']
message_logger = config['message_logger']['message_logger']
say_in_chat = config['message_logger']['say_in_chat']
respond_hi = config['respond_hi']
ping_back = config['ping_back']
repeat_message = config['repeat_message']['repeat_message']
repeat_commands = config['repeat_message']['repeat_commands']

tts_language = config['tts_language']
cat_key = config['cat_key']
weather_key = config['weather_key']
cuttly_key = config['cuttly_key']
ipkey = config['ip_key']

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
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

    print(f'''{Fore.RESET}

                              _   _               _  __ _           _   
                          ___| |_( )__   ___  ___| |/ _| |__   ___ | |_ 
                         / __| __|/ __| / __|/ _ \ | |_| '_ \ / _ \| __|
                         \__ \ |_ \__ \ \__ \  __/ |  _| |_) | (_) | |_ 
                         |___/\__||___/ |___/\___|_|_| |_.__/ \___/ \__|





{Fore.CYAN}! Thank you for using st's cool selfbot v{SELFBOT.__version__} 
{Fore.CYAN}! Logged in as: {Fore.WHITE} {stselfbot.user.name}#{stselfbot.user.discriminator} {Fore.CYAN} ID: {Fore.WHITE}{stselfbot.user.id}   
{Fore.CYAN}! Prefix: {Fore.WHITE}{prefix}
{Fore.CYAN}! Commands: {Fore.WHITE}247 + some features!

{Fore.CYAN}! Giveaway sniper: {Fore.WHITE}{giveaway}
{Fore.CYAN}! Nitro sniper: {Fore.WHITE}{nitro}
{Fore.CYAN}! Slotbot sniper: {Fore.WHITE}{slotbot}
    ''' + Fore.RESET)


def Clear():
    os.system('cls')


Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file" + Fore.RESET)
    else:
        token = config.get('token')
        try:
            stselfbot.run(token)
            os.system(f'title (stselfbot Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
            os.system('pause >NUL')

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

async def do_tts(text):
    tts = gTTS(text, lang='en')
    tts.save('data/tts.mp3')
    with open('data/tts.mp3', 'rb') as f:
        audio_data = f.read()
    return audio_data

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'data/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar) + '\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

async def getPost(ctx, subredditName, tempList):
    async with asyncpraw.Reddit(
    client_id="wRoZ9305CMPrv8g0k2-y9A",
    client_secret="vLs5wzsivo58cWQgCeptsWSKXU-W1Q",
    user_agent="python.discord.bot:discord.bot.sending.images:v1:(by u/stitoooobote)",
    ) as reddit:
        await reddit.user.me()
        if len(tempList) == 0:
            subreddit = await reddit.subreddit(subredditName)
            await subreddit._fetch()
            async for post in subreddit.new(limit=10):
                if post.url.endswith(('.jpg', '.png', '.jpeg', '.gif')) or "imgur" in post.url:
                    tempList.append(post.url)
        randUrl = random.choice(tempList)
        tempList.remove(randUrl)
        await ctx.send(randUrl)
        return tempList


colorama.init()
stselfbot = commands.Bot(command_prefix=prefix, self_bot=True)
stselfbot.remove_command('help')

@tasks.loop(minutes=30)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: " + value + "$ USD",
        url="https://www.twitch.tv/imstcool",
    )
    await stselfbot.change_presence(activity=btc_stream)


@stselfbot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command" + Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}" + Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image" + Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}" + Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message" + Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}" + Fore.RESET)

def FindUrl(string):
    if "discord.gift" or "discord.com/gift" in string:
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, string)
        return [x[0] for x in url]

async def embedGen(ctx, author, title, description, image, randomthingcauseimtoolazytoeditallofthefunctioncallsyee = None):
    url = f"https://embed.rauf.workers.dev/?author={quote(author)}&title={quote(title)}&description={quote(description)}&color=570000&image={image}"
    full = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ " + url
    if len(full) > 1999:
        full = url
    if len(full) > 1999:
        res = f"**{author}** \n __{title}__ \n {description} \n {image}"
        stringLength = len(res)
        max_index = 1800
        firstStringToSend = res[0:max_index]
        await ctx.send(firstStringToSend)
        index = max_index
        while index < (stringLength - max_index) and index > 0: 
            secondIndex = index + max_index
            posted_string = res[index:secondIndex]
            await ctx.send(posted_string)
            index = index + max_index
        posted_string = res[index:stringLength]
        await ctx.send(posted_string)
        return "st's cool selfbot :3!!!"
    return full

@stselfbot.event
async def on_message_delete(message):
    if message_logger:
        if not message.author == stselfbot.user:
            msg = f'**{message.author}** has deleted the message:\n {message.content}'
            await message.channel.send(msg)
            print(msg)
            if say_in_chat:
                await message.channel.send(msg)

@stselfbot.event
async def on_message_edit(before, after):
    await stselfbot.process_commands(before)
    await stselfbot.process_commands(after)
    if message_logger:
        if not before.author == stselfbot.user:
            msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
            print(msg)
            if say_in_chat:
                await before.channel.send(msg)

@stselfbot.event
async def on_message(message):
    if message.author == stselfbot.user:
        if (message.content).startswith("blacklistchannel"):
            print(message.channel.id)
            await message.delete()
            print(f"The discord channel with an id of {message.channel.id} has been added to the blacklist.")
            print("You can edit this blacklist if you understand json and can check which discord channel is each id (say <@#[id]> in discord) in the blacklistedchannels.txt file.")
            blacklistedc = open("data/blacklistedchannels.txt", "w")
            blacklistedc.write(str(message.channel.id) + "\n") 
            blacklistedc.close()
        if (message.content).startswith("setnitrochannel"):
            config["nitro_sniper"]["specified_channel"] = str(message.channel.id)
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
            print(f"{Fore.CYAN}[Set Nitro channel]: {Fore.WHITE}Set the nitro sniper channel to {message.channel.id}")
    elif not message.author == stselfbot.user:
        if respond_hi:
            if message.content == "hi":
                await message.channel.send("hi")
        if ping_back:
            if str(stselfbot.user.id) in message.content:
                await message.channel.send(f"<@{message.author.id}>")
        if repeat_message:
            blacklistedc = open("data/blacklistedchannels.txt", "r")
            readblc = blacklistedc.read()
            if not str(message.channel.id) in readblc:
                if not (message.content).startswith(prefix):
                    if respond_hi:
                        if message.content != "hi":
                            try:
                                await message.channel.send(message.content)
                            except:
                                pass
                    elif ping_back:
                        if str(stselfbot.user.id) not in message.content:
                            try:
                                await message.channel.send(message.content)
                            except:
                                pass
                    else:
                        try:
                            await message.channel.send(message.content)
                        except:
                            pass
                elif repeat_commands:
                    if respond_hi:
                        if message.content != "hi":
                            try:
                                await message.channel.send(message.content)
                            except:
                                pass
                    elif ping_back:
                        if str(stselfbot.user.id) not in message.content:
                            try:
                                await message.channel.send(message.content)
                            except:
                                pass
                    else:
                        try:
                            await message.channel.send(message.content)
                        except:
                            pass
            blacklistedc.close()
        if nitro_sniper:
            if "discord.gift" in message.content:
                for url in FindUrl(message.content):
                    print(f"{Fore.GREEN}[NITRO] {Fore.WHITE} FOUND NITRO GIFT LINK IN A MESSAGE: {url}" + Fore.RESET)
                    if 'https://' in str(url):
                        if 'discord.gift' in str(url):
                            nitrocode = url[20:]
                        elif 'discord.com/gift' in str(url):
                            nitrocode = url[24:]
                    elif 'https://' not in str(url):
                        if 'discord.gift' in str(url):
                            nitrocode = url[12:]
                        elif 'discord.com/gift' in str(url):
                            nitrocode = url[16:]
                    else:
                        print("COULDNT GET NITROCODE FROM URL. TRY TO CLAIM IT YOURSELF.")
                        return
                    checkUrl = f'https://discord.com/api/v9/entitlements/gift-codes/{nitrocode}?with_application=false'
                    r = requests.get(checkUrl)
                    r = str(r.content)

                    Headers = {
                    'Authorization': token
                    }
                    try:
                        jsonThing = r.strip("''")
                        jsonThing = jsonThing[2:]
                        r = json.loads(jsonThing)
                        if 'redeemed' in str(r).lower():
                            if r['redeemed'] == False:
                                if open_in_browser:
                                    for url in FindUrl(message.content):
                                        webbrowser.open(url)
                                if send_in_channel:
                                    channelint = int(config["nitro_sniper"]["specified_channel"])
                                    channel = stselfbot.get_channel(channelint)
                                    await channel.send(url)
                                print("not redeemed")
                                print(r['store_listing']['sku']['name'])
                                try:
                                    q = requests.post(
                                    f"https://discord.com/api/v9/entitlements/gift-codes/{nitrocode}/redeem",
                                    headers=Headers).json()
                                    if "method not allowed" in str(q['message']).lower():
                                        print("COULDNT CLAIM NITRO, PLEASE TRY TO CLAIM IT YOURSELF")
                                    elif "you are being rate limited" in str(q['message']).lower():
                                        print("YOU ARE BEING RATE LIMITED, PLEASE TRY TO CLAIM IT YOURSELF")
                                    elif "unkown gift" in str(q['message']).lower():
                                        print("THE NITRO GIFT LINK IS NOT WORKING.")
                                    elif "this gift has been redeemed" in str(q['message']).lower():
                                        print("THE NITRO GIFT HAS ALREADY BEEN REDEEMED")
                                    elif "unauthorized" in str(q['message']).lower():
                                        print(
                                        "EITHER YOUR TOKEN BROKE OR SOMETHING ELSE BROKE, JUST TRY TO REDEEM IT MANUALLY"
                                    )
                                    elif "you need to verify your" in str(q['message']).lower():
                                        print(
                                        "YOU NEED TO VERIFY YOUR EMAIL ON YOUR DISCORD ACCOUNT TO AUTO CLAIM NITRO"
                                    )
                                    else:
                                        print("SUCCESSFULLY CLAIMED THE GIFT")
                                except Exception as e:
                                    print(e)
                            else:
                                print("NITRO CODE HAS ALREADY BEEN REDEEMED")
                        else:
                            print("THE NITRO CODE ISNT AN ACTUAL VALID GIFT")
                    except Exception as e:
                        print(e)
                        if '"redeemed": false' in r:
                            print("NITRO CODE IS MOST LIKELY VALID AND NOT REDEEMED! THERE WAS A JSON ERROR, MEANING I CANNOT TELL YOU WHICH NITRO THIS IS, BUT I WILL STILL TRY TO AUTOCLAIM IT")
                        try:
                            q = requests.post(
                            f"https://discord.com/api/v9/entitlements/gift-codes/{nitrocode}/redeem",
                            headers=Headers).json()
                            if "method not allowed" in str(q['message']).lower():
                                print("COULDNT CLAIM NITRO, PLEASE TRY TO CLAIM IT YOURSELF")
                            elif "you are being rate limited" in str(q['message']).lower():
                                print("YOU ARE BEING RATE LIMITED, PLEASE TRY TO CLAIM IT YOURSELF")
                            elif "unkown gift" in str(q['message']).lower():
                                print("THE NITRO GIFT LINK IS NOT WORKING.")
                            elif "this gift has been redeemed" in str(q['message']).lower():
                                print("THE NITRO GIFT HAS ALREADY BEEN REDEEMED")
                            elif "unauthorized" in str(q['message']).lower():
                                print(
                                "EITHER YOUR TOKEN BROKE OR SOMETHING ELSE BROKE, JUST TRY TO REDEEM IT MANUALLY"
                            )
                            elif "you need to verify your" in str(q['message']).lower():
                                print(
                                "YOU NEED TO VERIFY YOUR EMAIL ON YOUR DISCORD ACCOUNT TO AUTO CLAIM NITRO"
                            )
                            else:
                                print("SUCCESSFULLY CLAIMED THE GIFT")
                        except Exception as e:
                            print(e)
        if slotbot_sniper:
            if message.author.id == 346353957029019648:
                if "Someone just dropped their wallet in this channel" in message.content:
                    await asyncio.sleep(0.3)
                    await message.channel.send("~grab")
                    print(f"{Fore.GREEN}[SLOTBOT] {Fore.WHITE} SNIPED A SLOTBOT WALLET DROP" + Fore.RESET)
        if giveaway_sniper:
            if message.author.bot:
                if "winner" in str(message.content).lower() or "giveaway" in str(message.content).lower() or "ends" in str(message.content).lower() or "hosted" in str(message.content).lower() or "entries" in str(message.content).lower():
                    await asyncio.sleep(5)
                    messageComponents = message.components
                    if "button" in str(messageComponents).lower():
                        for component in message.components:
                            if isinstance(component, discord.ActionRow):
                                for button in component.children:
                                    if isinstance(button, discord.Button):
                                        await button.click()
                                        break
                    messageReactions = message.reactions
                    if len(messageReactions) == 0 and "button" not in str(messageComponents).lower():
                        return
                    else:
                        i = 0
                        for msgReaction in messageReactions:
                            i += 1
                            print(f"{msgReaction} is the reaction on the 'giveaway' message. Please check the message out.")
                        if i == 1:
                            await message.add_reaction(msgReaction)
                    print(f"{Fore.GREEN}[GIVEAWAY] {Fore.WHITE}FOUND A GIVEAWAY IN: {message.guild.name} CHANNEL: {message.channel}" + Fore.RESET)
                for Embed in message.embeds:
                    if "winner" in str(Embed.description).lower() or "giveaway" in str(Embed.description).lower() or "ends" in str(Embed.description).lower() or "hosted" in str(Embed.description).lower() or "entries" in str(Embed.description).lower():
                        await asyncio.sleep(5)
                        messageComponents = message.components
                        if "button" in str(messageComponents).lower():
                            for component in message.components:
                                if isinstance(component, discord.ActionRow):
                                    for button in component.children:
                                        if isinstance(button, discord.Button):
                                            await button.click()
                                            break
                        messageReactions = message.reactions
                        if len(messageReactions) == 0 and "button" not in str(messageComponents).lower():
                            return
                        else:
                            i = 0
                            for msgReaction in messageReactions:
                                i += 1
                                print(f"{msgReaction} is the reaction on the 'giveaway' message. Please check the message out.")
                            if i == 1:
                                await message.add_reaction(msgReaction)
                        print(f"{Fore.GREEN}[GIVEAWAY] {Fore.WHITE}FOUND A GIVEAWAY IN: {message.guild.name} CHANNEL: {message.channel}" + Fore.RESET)

    await stselfbot.process_commands(message)

@stselfbot.event
async def on_connect():
    Clear()
    startprint()

@stselfbot.event
async def on_ready():
    Clear()
    startprint()

@stselfbot.command()
async def clear(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Clear]''' + Fore.RESET)
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')

@stselfbot.command()
async def genname(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Genname]''' + Fore.RESET)
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@stselfbot.command()
async def google(ctx, *, message):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Google]''' + Fore.RESET)
    q = urlencode({"q": message})
    await ctx.send(f'<https://www.google.com/search?{q}>')

@stselfbot.command()
async def randomaddress(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Randomaddress], note that this is just a "fun" command, the address is nowhere close to being real.''' + Fore.RESET)
    r = requests.get("https://random-data-api.com/api/v2/addresses").json()
    await ctx.send(f'''Address: {r['street_address']}, {r['city']}, {r['country']}, {r['zip_code']}''')

@stselfbot.command()
async def weather(ctx, *, city):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Weather]''' + Fore.RESET)
    if weather_key == 'weather key':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file" + Fore.RESET)
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
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city" + Fore.RESET)
        except:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}" + Fore.RESET)

@stselfbot.command(aliases=['shorten'])
async def cuttly(ctx, *, link):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cuttly]''' + Fore.RESET)
    if cuttly_key == 'cuttly key':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file, I'll still use a free keyless api to shorten your link." + Fore.RESET)
        r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
        await ctx.send(f'shortened: {r}')
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
                await ctx.send("shortened: " + new)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}" + Fore.RESET)

@stselfbot.command()
async def cat(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cat]''' + Fore.RESET)
    if cat_key == 'cat key':
        i = random.randrange(1, 10)
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file. I can still send a cat image from a free keyless api. Warning - it might be shitty" + Fore.RESET)
        if i < 4:
            r = requests.get("https://some-random-api.ml/animal/cat").json()
            await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))
        else:
            await ctx.send(nekos.cat())
    else:
        try:
            r = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}").json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command()
async def dog(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dog]''' + Fore.RESET)
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))

@stselfbot.command()
async def kiss(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Kiss]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/kiss").json()
    url = await embedGen(ctx, f"{ctx.author.name} is giving you a little kiss, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def lick(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lick]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/lick").json()
    url = await embedGen(ctx, f"{ctx.author.name} is licking you, {user.name}!", "", "st's cool selfbot :3!!", r['image'], "")
    await ctx.send(url)

@stselfbot.command()
async def hug(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Hug]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/hug").json()
    url = await embedGen(ctx, f"{ctx.author.name} just hugged you very aggresively, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def baka(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Baka]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/baka").json()
    await ctx.send(str(r["results"][0]["url"]))

@stselfbot.command()
async def cry(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cry]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/cry").json()
    url = await embedGen(ctx, f"{ctx.author.name} is crying!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def poke(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Poke]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/poke").json()
    url = await embedGen(ctx, f"{ctx.author.name} just poked you really hard, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def smug(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Smug]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/smug").json()
    url = await embedGen(ctx, f"{ctx.author.name} is in a smug mood ;)!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def slap(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Slap]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/slap").json()
    url = await embedGen(ctx, f"{ctx.author.name} just gave you an extremely harsh slap, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def tickle(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tickle]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/tickle").json()
    url = await embedGen(ctx, f"{ctx.author.name} is tickling you, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def pat(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pat]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/pat").json()
    url = await embedGen(ctx, f"{ctx.author.name} is giving you a little pat on the head, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def laugh(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Laugh]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/laugh").json()
    url = await embedGen(ctx, f"{ctx.author.name} is laughing at this!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)
    
@stselfbot.command()
async def feed(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Feed]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/feed").json()
    url = await embedGen(ctx, f"{ctx.author.name} is feeding you.. something..;), {user.name}", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def cuddle(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cuddle]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/cuddle").json()
    url = await embedGen(ctx, f"{ctx.author.name} is cuddling you, {user.name}..", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def highfive(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Highfive]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/highfive").json()
    url = await embedGen(ctx, f"{ctx.author.name} is giving you a highfive, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def happy(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Happy]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/happy").json()
    url = await embedGen(ctx, f"{ctx.author.name} is happy!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def sleep(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Sleep]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/sleep").json()
    url = await embedGen(ctx, f"{ctx.author.name} is sleeping!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def handhold(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Handhold]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/handhold").json()
    url = await embedGen(ctx, f"{ctx.author.name} is holding your hand, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def bite(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bite]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/bite").json()
    url = await embedGen(ctx, f"{ctx.author.name} just bit you, {user.name}!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def wave(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Wave]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/wave").json()
    url = await embedGen(ctx, f"{ctx.author.name} is waving with their hand!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def thumbsup(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Thumbs up]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/thumbsup").json()
    url = await embedGen(ctx, f"{ctx.author.name} is giving a thumbs up!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def stare(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stare]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/stare").json()
    url = await embedGen(ctx, f"{ctx.author.name} is staring at you... 😐", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def blush(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blush]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/blush").json()
    url = await embedGen(ctx, f"{ctx.author.name} is blushing! 😳", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def nom(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Nom]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/nom").json()
    url = await embedGen(ctx, f"{ctx.author.name} is making loud nom sounds..", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def think(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Think]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/think").json()
    url = await embedGen(ctx, f"{ctx.author.name} is thinking...🤔", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def pout(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pout]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/pout").json()
    await ctx.send(str(r["results"][0]["url"]))

@stselfbot.command()
async def facepalm(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Face palm]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/facepalm").json()
    url = await embedGen(ctx, f"{ctx.author.name} is face palming...🤦", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def wink(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Wink]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/wink").json()
    url = await embedGen(ctx, f"{ctx.author.name} is winking at you! 😉", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def shoot(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Shoot]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/shoot").json()
    url = await embedGen(ctx, f"{ctx.author.name} just fucking SHOT you, {user.name}!!! 🤠", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def nope(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Nope]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/nope").json()
    url = await embedGen(ctx, f"{ctx.author.name} is saying no...", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def nod(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Nod]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/nod").json()
    url = await embedGen(ctx, f"{ctx.author.name} is nodding!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")    
    await ctx.send(url)

@stselfbot.command()
async def punch(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Punch]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/punch").json()
    url = await embedGen(ctx, f"{ctx.author.name} just fucking PUNCHED you, {user.name}!!!! 🤜", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def dance(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dance]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/dance").json()
    url = await embedGen(ctx, f"{ctx.author.name} is dancing with you, {user.name}..", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def shruggif(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Shruggif]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/shrug").json()
    url = await embedGen(ctx, f"{ctx.author.name} doesn't know.", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def bored(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bored]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/bored").json()
    url = await embedGen(ctx, f"{ctx.author.name} is bored...", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def kick(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Kick]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/kick").json()
    url = await embedGen(ctx, f"{ctx.author.name} just fucking KICKED you, {user.name}!!!! 🦵", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def yeet(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Yeet]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/yeet").json()
    url = await embedGen(ctx, f"{ctx.author.name} just yeeted!", "", "st's cool selfbot :3!!", r['results'][0]['url'], "")
    await ctx.send(str(r["results"][0]["url"]))

@stselfbot.command()
async def husbando(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Husbando]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/husbando").json()
    await ctx.send(str(r["results"][0]["url"]))

@stselfbot.command()
async def kitsune(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Kitsune]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/kitsune").json()
    await ctx.send(str(r["results"][0]["url"]))

@stselfbot.command(aliases=['4k', 'uhd'])
async def fourk(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [4k]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/4k").json()
    await ctx.send(str(r['image']))

@stselfbot.command(aliases=['blowjob'])
async def bj(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blowjob]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/bj").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def boobs(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Boobs]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/boobs").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def cum(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cum]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/cum").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def feet(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Feet]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/feet").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def hentai(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Hentai]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/hentai").json()
    await ctx.send(str(r['image']))

@stselfbot.command()
async def yaoi(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Yaoi]''' + Fore.RESET)
    r = requests.get("https://nekobot.xyz/api/image?type=yaoi").json()
    await ctx.send(str(r['message']))
    
@stselfbot.command()
async def wallpapers(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Wallpapers]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/wallpapers").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def spank(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Spank]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/spank").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def gasm(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [gasm]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/gasm").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def lesbian(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lesbian]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/lesbian").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def lewd(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lewd]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/lewd").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def pussy(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pussy]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/pussy").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def animalears(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Animal ears]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/animalears").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def bellevid(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bellevid]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/bellevid").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def gif(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Gif]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/gif").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def anal(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Anal]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/anal").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def holo(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Holo]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/holo").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def waifu(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Waifu]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/waifu").json()
    await ctx.send(str(r["results"][0]["url"]))
    
@stselfbot.command()
async def foxgirl(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Foxgirl]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/foxgirl").json()
    await ctx.send(str(r['image']))
    
@stselfbot.command()
async def belle(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Belle]''' + Fore.RESET)
    r = requests.get("http://api.nekos.fun:8080/api/belle").json()
    await ctx.send(str(r['image']))

@stselfbot.command()
async def neko(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Neko]''' + Fore.RESET)
    r = requests.get("https://nekos.best/api/v2/neko").json()
    await ctx.send(str(r["results"][0]["url"]))

@stselfbot.command()
async def hneko(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Hneko]''' + Fore.RESET)
    r = requests.get("https://nekobot.xyz/api/image?type=hneko").json()
    await ctx.send(str(r['message']))

@stselfbot.command()
async def paizuri(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Paizuri]''' + Fore.RESET)
    r = requests.get("https://nekobot.xyz/api/image?type=paizuri").json()
    await ctx.send(str(r['message']))

@stselfbot.command()
async def fox(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Fox]''' + Fore.RESET)
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image (sts cool selfbot kid)", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))

@stselfbot.command()
async def bird(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bird]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/animal/bird').json()
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))

@stselfbot.command()
async def kangaroo(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Kangaroo]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/animal/kangaroo').json()
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))

@stselfbot.command()
async def koala(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Koala]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/animal/koala').json()
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))

@stselfbot.command()
async def panda(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Panda]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/animal/panda').json()
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))

@stselfbot.command()
async def raccoon(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Raccoon]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/animal/raccoon').json()
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))

@stselfbot.command()
async def redpanda(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Red Panda]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/animal/red_panda').json()
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["image"]))

@stselfbot.command()
async def whale(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Whale]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/img/whale').json()
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", r["link"]))

@stselfbot.command()
async def animequote(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Anime Quote]''' + Fore.RESET)
    r = requests.get('https://some-random-api.ml/animu/quote').json()
    await ctx.send(await embedGen(ctx, r['character'], r['anime'], f"{r['sentence']} \n \n st's cool selfbot :3!!!", ""))

@stselfbot.command()
async def blue(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blue]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/blue?avatar={user.avatar}'))

@stselfbot.command()
async def blurple(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blurple]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/blurple?avatar={user.avatar}'))

@stselfbot.command()
async def blurple2(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blurple2]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/blurple?avatar={user.avatar}'))

@stselfbot.command()
async def brightness(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Brightness]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/brightness?avatar={user.avatar}'))

@stselfbot.command()
async def green(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Green]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/green?avatar={user.avatar}'))

@stselfbot.command(aliases=['grayscale'])
async def greyscale(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Greyscale]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/greyscale?avatar={user.avatar}'))

@stselfbot.command(aliases=['invertgrayscale'])
async def invertgreyscale(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Invert & Greyscale]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/invertgreyscale?avatar={user.avatar}'))

@stselfbot.command()
async def red(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Red]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/red?avatar={user.avatar}'))

@stselfbot.command()
async def sepia(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Sepia]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/sepia?avatar={user.avatar}'))

@stselfbot.command()
async def threshold(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Threshold]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/filter/threshold?avatar={user.avatar}'))

@stselfbot.command()
async def lyrics(ctx, *, song: str):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lyrics]''' + Fore.RESET)
    r = requests.get(f'https://some-random-api.ml/others/lyrics?title={quote(song)}').json()
    await ctx.send(await embedGen(ctx, r['title'], r['author'], r['lyrics'], r['thumbnail']['genius']))

@stselfbot.command()
async def bisexualborder(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bisexual border]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/bisexual?avatar={user.avatar}'))

@stselfbot.command()
async def blur(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blur]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/blur?avatar={user.avatar}'))

@stselfbot.command()
async def circle(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Circle]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/circle?avatar={user.avatar}'))

@stselfbot.command()
async def heart(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Heart]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/heart?avatar={user.avatar}'))

@stselfbot.command()
async def horny(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Horny]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/horny?avatar={user.avatar}'))

@stselfbot.command()
async def itssostupid(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [It's so stupid]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/its-so-stupid?avatar={user.avatar}'))

@stselfbot.command()
async def jpg(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Jpg]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/jpg?avatar={user.avatar}'))

@stselfbot.command()
async def lesbianborder(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lesbian border]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/lesbian?avatar={user.avatar}'))

@stselfbot.command()
async def lgbtborder(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [LGBT border]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/lgbt?avatar={user.avatar}'))

@stselfbot.command()
async def lied(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lied]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(f'https://some-random-api.ml/canvas/misc/lied?avatar={user.avatar}&username={user.name}')

@stselfbot.command()
async def noblank(ctx, *, text: str):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [No blank?]''' + Fore.RESET)
    await ctx.send(f"https://some-random-api.ml/canvas/misc/nobitches?no=no%20{quote(text)}%3F")

@stselfbot.command()
async def nonbinaryborder(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Non binary border]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/nonbinary?avatar={user.avatar}'))

@stselfbot.command()
async def pansexualborder(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pansexual border]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/pansexual?avatar={user.avatar}'))

@stselfbot.command()
async def pixelate(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pixelate]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/pixelate?avatar={user.avatar}'))

@stselfbot.command()
async def simpcard(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Simp card]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/simpcard?avatar={user.avatar}'))

@stselfbot.command()
async def spin(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Spin]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/spin?avatar={user.avatar}'))

@stselfbot.command(aliases=['dvd'])
async def tonikawa(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tonikawa]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/tonikawa?avatar={user.avatar}'))

@stselfbot.command()
async def transborder(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Trans border]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/misc/transgender?avatar={user.avatar}'))

@stselfbot.command()
async def youtubecomment(ctx, user: discord.User, *, text: str):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Youtube comment]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(f"https://some-random-api.ml/canvas/misc/youtube-comment?username={user.name}&avatar={user.avatar}&comment={quote(text)}")

@stselfbot.command()
async def comrade(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Comrade]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/overlay/comrade?avatar={user.avatar}'))

@stselfbot.command()
async def pride(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pride]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/overlay/gay?avatar={user.avatar}'))

@stselfbot.command()
async def glass(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Glass]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/overlay/glass?avatar={user.avatar}'))

@stselfbot.command()
async def jail(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Jail]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/overlay/jail?avatar={user.avatar}'))

@stselfbot.command()
async def passed(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Passed]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/overlay/passed?avatar={user.avatar}'))

@stselfbot.command()
async def triggered(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Triggered]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/overlay/triggered?avatar={user.avatar}'))

@stselfbot.command()
async def wasted(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Wasted]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    await ctx.send(await embedGen(ctx, "st's cool selfbot :3!!!", "", "", f'https://some-random-api.ml/canvas/overlay/wasted?avatar={user.avatar}'))

@stselfbot.command()
async def binaryencode(ctx, *, text: str):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Binary encode]''' + Fore.RESET)
    r = requests.get(f'https://some-random-api.ml/others/binary?encode={quote(text)}').json()
    await ctx.send(await embedGen(ctx, r['binary'], "Binary encode", "st's cool selfbot :3!!!", ""))

@stselfbot.command()
async def binarydecode(ctx, *, text: str):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Binary decode]''' + Fore.RESET)
    r = requests.get(f'https://some-random-api.ml/others/binary?decode={quote(text)}').json()
    await ctx.send(await embedGen(ctx, r['text'], "Binary decode", "st's cool selfbot :3!!!", ""))

@stselfbot.command()
async def catboy(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Catboy]''' + Fore.RESET)
    r = requests.get('https://api.catboys.com/img').json()
    await ctx.send(r['url'])

catgirlList = []

@stselfbot.command()
async def catgirl(ctx):
    global catgirlList
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Catgirl]''' + Fore.RESET)
    catgirlList = await getPost(ctx, "catgirls", catgirlList)

femboyList = []

@stselfbot.command()
async def femboy(ctx):
    global femboyList
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Femboy]''' + Fore.RESET)
    femboyList = await getPost(ctx, "femboyhentai", femboyList)

@stselfbot.command()
async def encode(ctx, *args):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Base 64 encode]''' + Fore.RESET)
    string = ' '.join(args)
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff) - 1]
    await ctx.send(encoded_stuff)

@stselfbot.command()
async def decode(ctx, *args):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Base 64 decode]''' + Fore.RESET)
    string = ' '.join(args)
    strOne = (string).encode("ascii")
    pad = len(strOne) % 4
    strOne += b"=" * pad
    encoded_stuff = codecs.decode(strOne.strip(), 'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff) - 1]
    await ctx.send(decoded_stuff)

@stselfbot.command()
async def encrypt(ctx, *args):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Rot 13 encode]''' + Fore.RESET)
    string = ' '.join(args)
    encoded_stuff = codecs.encode(string, 'rot_13')
    await ctx.send(encoded_stuff)

@stselfbot.command()
async def decrypt(ctx, *args):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Rot 13 decode]''' + Fore.RESET)
    string = ' '.join(args)
    decoded_stuff = codecs.decode(string, 'rot_13')
    await ctx.send(decoded_stuff)

@stselfbot.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Geoip]''' + Fore.RESET)
    if ipkey == "ip key":
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}extreme-ip-lookup.com API key has not been set in the config.json file" + Fore.RESET)
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}?key={ipkey}')
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
    try:
        await ctx.send(embed=em)
    except:
        x = " "
        for field in fields:
            if field['value']:
                name=field['name']
                value=field['value']

                x = x + f'{name}: {value} \n'
        url = await embedGen(ctx, f"IP lookup", "st's cool selfbot :3!!", f"{x}", "", "")
        await ctx.send(url)

@stselfbot.command()
async def pingweb(ctx, website=None):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pingweb]''' + Fore.RESET)
    if website is None:
        pass
    else:
        r = 0
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)

@stselfbot.command()
async def trumptweet(ctx, *message: str):  
    await ctx.message.delete()
    message = "%20".join(message)
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tweet]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={message}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def tweet(ctx, username: str, *, message: str):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tweet]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def clyde(ctx, *message: str):  
    await ctx.message.delete()
    message = "%20".join(message)
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Clyde]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={message}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def changemymind(ctx, *message: str):  
    await ctx.message.delete()
    message = "%20".join(message)
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Change my mind]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={message}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def kannafy(ctx, *message: str):  
    await ctx.message.delete()
    message = "%20".join(message)
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Kannafy]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={message}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def fact(ctx, *message: str):  
    await ctx.message.delete()
    message = "%20".join(message)
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Fact]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=fact&text={message}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def putin(ctx, *args):
    await ctx.message.delete()
    secondPart = False
    top = ""
    bottom = ""
    args = "%20".join(args)
    for char in args:
        if char == ",":
            secondPart = True
            continue
        if secondPart:
            bottom = f"{bottom}%20{char}"
        else:
            top = f"{top}%20{char}"
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Putin]''' + Fore.RESET)
    await ctx.send(f"https://apimeme.com/meme?meme=Vladimir-Putin&top={top}&bottom={bottom}")

@stselfbot.command()
async def drake(ctx, *args):
    await ctx.message.delete()
    secondPart = False
    top = ""
    bottom = ""
    args = "%20".join(args)
    for char in args:
        if char == ",":
            secondPart = True
            continue
        if secondPart:
            bottom = f"{bottom}%20{char}"
        else:
            top = f"{top}%20{char}"
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Putin]''' + Fore.RESET)
    await ctx.send(f"https://apimeme.com/meme?meme=Drake-Bad-Good&top={top}&bottom={bottom}")

@stselfbot.command()
async def spongebobsad(ctx, *args):
    await ctx.message.delete()
    secondPart = False
    top = ""
    bottom = ""
    args = "%20".join(args)
    for char in args:
        if char == ",":
            secondPart = True
            continue
        if secondPart:
            bottom = f"{bottom}%20{char}"
        else:
            top = f"{top}%20{char}"
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Putin]''' + Fore.RESET)
    await ctx.send(f"https://apimeme.com/meme?meme=Spongebob-Coffee&top={top}&bottom={bottom}")

@stselfbot.command()
async def iphonex(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [IPhoneX]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={str(user.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def whowouldwin(ctx, user1: discord.User, user2: discord.User = None):
    await ctx.message.delete()
    if user2 is None:
        user2 = ctx.author
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Who would win]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={str(user1.avatar)}&user2={str(user2.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def ship(ctx, user1: discord.User, user2: discord.User = None):
    await ctx.message.delete()
    if user2 is None:
        user2 = ctx.author
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Ship]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=ship&user1={str(user1.avatar)}&user2={str(user2.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def awooify(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Awooify]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={str(user.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def captcha(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Captcha]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={str(user.avatar)}&username={str(user.name)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def lolice(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lolice]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=lolice&url={str(user.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def trap(ctx, user1: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Trap]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=trap&name={str(user1.name)}&author={str(ctx.author.name)}&image={str(user1.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def deepfry(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Deepfry]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=deepfry&image={str(user.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def blurpify(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bluripfy]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=blurpify&image={str(user.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def magik(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Magik]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={str(user.avatar)}&intensity=1").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def trash(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Trash]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={str(user.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def stickbug(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stickbug]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=stickbug&url={str(user.avatar)}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def phcomment(ctx, user: discord.User, *message: str):
    await ctx.message.delete()
    message = "%20".join(message)
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pornhub comment]''' + Fore.RESET)
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={str(user.avatar)}&text={message}&username={user.name}").json()
    await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", res['message'], ""))

@stselfbot.command()
async def pornhub(ctx, left: str, right: str):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pornhub logo]''' + Fore.RESET)
    await ctx.send(f"https://logohub.appspot.com/{left}-{right}.png")

@stselfbot.command()
async def revav(ctx, user: discord.User = None):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Reverse search pfp]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar}")
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(f"google reverse search - https://lens.google.com/uploadbyurl?url={user.avatar}")
            await ctx.send(f"yandex reverse search - https://yandex.com/images/search?source=collections&&url={user.avatar}&rpt=imageview")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command()
async def img(ctx, *, search: str):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Img]''' + Fore.RESET)
    await ctx.send(f"https://yandex.com/images/search?text={quote(search)}")

@stselfbot.command()
async def qrcode(ctx, *, text: str):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [QR Code]''' + Fore.RESET)
    await ctx.send(f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={quote(text)}")

@stselfbot.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [pfp]''' + Fore.RESET)
    if user.avatar == None:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}SPECIFIED USER DOESN'T HAVE A CUSTOM PROFILE PICTURE." + Fore.RESET)
    else:
        await ctx.send(await embedGen(ctx, f"st's cool selfbot :3!!", f"", "", user.avatar, ""))

@stselfbot.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Roleinfo]''' + Fore.RESET)
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    roleinfocool = f'''
        Name: {role.name}
        Role ID: {role.id}
        Users: {users}
        Mentionable: {role.mentionable}
        Hoist: {role.hoist}
        Position: {role.position}
        Managed: {role.managed}
        Creation Date: {created_on}
        '''
    try:
        await ctx.send(await embedGen(ctx, f"Role info", f"st's cool selfbot :3!!", roleinfocool, "", ""))
    except:
        await ctx.send(roleinfocool)
    print(f'''{Fore.CYAN} {roleinfocool}''' + Fore.RESET)

@stselfbot.command()
async def whois(ctx, *, user: discord.Member = None):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Whois]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    userroles = "No Roles"
    if len(user.roles) > 1:
        role_string = ' | '.join([r.name for r in user.roles][1:])
        userroles = "Roles [{}]: ".format(len(user.roles) - 1), role_string
        userroles = str(userroles).strip("()'',")
        userroles = userroles.replace("', '", " ")
    whoiscool = f'''
    General info:
    Name: {user.name}
    Tag: {user.name}#{user.discriminator}
    ID: {str(user.id)}
    Creation: {user.created_at.strftime(date_format)}
    Status: {str(user.raw_status)}

    Server info:
    Joined: {user.joined_at.strftime(date_format)}
    Join position: {str(members.index(user) + 1)}
    {userroles}
    '''
    await ctx.send(await embedGen(ctx, f"Whois", f"st's cool selfbot :3!!", whoiscool, user.avatar, ""))


@stselfbot.command()
async def combine(ctx, name1, name2):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Combine]''' + Fore.RESET)
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    combinecool = f'''
    Combined names: {ship}
    Names: {name1} + {name2}
    '''
    await ctx.send(await embedGen(ctx, f"Combine", f"st's cool selfbot :3!!", combinecool, "", ""))

@stselfbot.command(name='1337-speak', aliases=['1337speak', '1377'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [1337 speak]''' + Fore.RESET)
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@stselfbot.command(aliases=['dvwl'])
async def devowel(ctx, *, text):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Devowel]''' + Fore.RESET)
    dvl = text.replace('a', '').replace('A', '').replace('e', '') \
        .replace('E', '').replace('i', '').replace('I', '') \
        .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@stselfbot.command()
async def blank(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Blank]''' + Fore.RESET)
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        with open('data/transparent.png', 'rb') as f:
            try:
                await stselfbot.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
                await stselfbot.change_presence(activity=None, status=discord.Status.offline)
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.User):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pfpsteal]''' + Fore.RESET)
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        with open('data/stolen.png', 'wb') as f:
            r = requests.get(user.avatar, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        try:
            Image.open('data/stolen.png').convert('RGB')
            with open('data/stolen.png', 'rb') as f:
                await stselfbot.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Setpfp]''' + Fore.RESET)
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        with open('data/pfp.png', 'wb') as f:
            r = requests.get(url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    try:
        Image.open('data/pfp.png').convert('RGB')
        with open('data/pfp.png', 'rb') as f:
            await stselfbot.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command(aliases=['steal-profile'])
async def stealprofile(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Steal profile]''' + Fore.RESET)
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        with open('data/pfp.png', 'wb') as f:
            r = requests.get(user.avatar, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    try:
        Image.open('data/pfp.png').convert('RGB')
        with open('data/pfp.png', 'rb') as f:
            await stselfbot.user.edit(password=password, username=user.name, avatar=f.read())
    except discord.HTTPException as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command()
async def saveprofile(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Save profile]''' + Fore.RESET)
    with open('data/savedprofiles.json', 'r') as f:
        data = json.load(f)
    data['username'] = str(ctx.author.name)
    with open('data/pfp.png', 'wb') as f:
            r = requests.get(ctx.author.avatar, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    with open('data/pfp.png', 'rb') as f:
        files = {'files[]': f}
        response = requests.post("https://up1.fileditch.com/upload.php", files=files).json()
    data['avatar'] = str(response['files'][0]['url'])
    with open('data/savedprofiles.json', 'w') as f:
        json.dump(data, f)

@stselfbot.command()
async def animatedaboutme(ctx, *, args):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Animated about me]''' + Fore.RESET)
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        bioList = args.split(', ')
        i = 0
        while True:
            bio = bioList[i]
            await stselfbot.user.edit(password=password, bio=bio)
            i += 1
            if i > len(bioList) - 1:
                i = 0
            await asyncio.sleep(60)

@stselfbot.command()
async def animatedstatus(ctx, sleep: int = 30, *, args):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Animated status]''' + Fore.RESET)
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        bioList = args.split(', ')
        i = 0
        while True:
            bio = bioList[i]
            await stselfbot.change_presence(activity=discord.CustomActivity(name=bio))
            i += 1
            if i > len(bioList) - 1:
                i = 0
            await asyncio.sleep(sleep)

@stselfbot.command()
async def loadprofile(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Load profile]''' + Fore.RESET)
    if password == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        with open('data/savedprofiles.json', 'r') as q:
            data = json.load(q)
        with open('data/pfp.png', 'wb') as f:
            r = requests.get(data['avatar'], stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    try:
        Image.open('data/pfp.png').convert('RGB')
        with open('data/pfp.png', 'rb') as f:
            await stselfbot.user.edit(password=password, username=data['username'], avatar=f.read())
    except discord.HTTPException as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.User = None):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dick]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(await embedGen(ctx, f"{user.name}'s Dick size", f"8{dong}D", "st's cool selfbot :3!!", ""))

@stselfbot.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Change hypesquad]''' + Fore.RESET)
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
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@stselfbot.command()
async def backupserver(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Backup server]''' + Fore.RESET)
    await stselfbot.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in stselfbot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                await asyncio.sleep(3)
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
async def destroy(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Destroy]''' + Fore.RESET)
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
    for _i in range(50):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(50):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@stselfbot.command()
async def dmall(ctx, *, message):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dmall]''' + Fore.RESET)
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)
            await user.send(message)
        except:
            pass

@stselfbot.command()
async def massban(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Massban]''' + Fore.RESET)
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

@stselfbot.command()
async def masskick(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Masskick]''' + Fore.RESET)
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass

@stselfbot.command()
async def massrole(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Massrole]''' + Fore.RESET)
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return

@stselfbot.command()
async def masschannel(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Masschann]''' + Fore.RESET)
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@stselfbot.command()
async def delchannels(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Delchann]''' + Fore.RESET)
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@stselfbot.command()
async def delroles(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Delroles]''' + Fore.RESET)
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@stselfbot.command()
async def massunban(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Massunban]''' + Fore.RESET)
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@stselfbot.command()
async def spam(ctx, amount: int, *, message):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Spam]''' + Fore.RESET)
    for _i in range(amount):
        await ctx.send(message)

@stselfbot.command()
async def dm(ctx, user: discord.User, *, message):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dm]''' + Fore.RESET)
    try:
        await user.send(message)
    except:
        pass

@stselfbot.command()
async def sessions(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Sessions]''' + Fore.RESET)
    for Session in stselfbot.sessions:
        print(f"Operating system of the session: {Session.os}, The client of the session {Session.client}")

@stselfbot.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Getcolor]''' + Fore.RESET)
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    await ctx.send(file=discord.File(file, 'color.png'))

@stselfbot.command(aliases=['shorten2'])
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tinyurl]''' + Fore.RESET)
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    await ctx.send(f'shortened: {r}')

@stselfbot.command(aliases=['rainbow-role'])
async def rainbow(ctx, role: discord.Role):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Rainbow]''' + Fore.RESET)
    while True:
        randcolor = RandomColor()
        await role.edit(colour=randcolor)
        await asyncio.sleep(10)

@stselfbot.command(name='8ball')
async def _ball(ctx, *, question):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [8Ball]''' + Fore.RESET)
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
    url = await embedGen(ctx, f"8ball question: {question}", f"Answer: {answer}", "st's cool selfbot :3!!", "https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png", "")
    await ctx.send(url)

@stselfbot.command(name='8balldiff')
async def _balldiff(ctx, *question):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [8Ball different]''' + Fore.RESET)
    question = " ".join(question)
    r = requests.get("https://api.catboys.com/8ball").json()
    url = await embedGen(ctx, f"8ball question: {question}", f"Answer: {r['response']}", "st's cool selfbot :3!!", r['url'], "")
    await ctx.send(url)

@stselfbot.command()
async def dice(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Dice]''' + Fore.RESET)
    r = requests.get("https://api.catboys.com/dice").json()
    while r['url'] == None:
        r = requests.get("https://api.catboys.com/dice").json()
    await ctx.send(await embedGen(ctx, f"Rolled a dice! Landed on {r['response']}", "", "st's cool selfbot :3!!", r['url']))

@stselfbot.command(aliases=['slots', 'bet'])
async def slot(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Slots]''' + Fore.RESET)
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"{a} {b} {c}"
    if (a == b == c):
        await ctx.send(await embedGen(ctx, f"Slot machine", f"{slotmachine} All matchings, you won, {ctx.author.name}!", "st's cool selfbot :3!!", ""))
    elif (a == b) or (b == c):
        await ctx.send(await embedGen(ctx, f"Slot machine", f"{slotmachine} 2 in a row, you won, {ctx.author.name}!", "st's cool selfbot :3!!", ""))
    else:
        await ctx.send(await embedGen(ctx, f"Slot machine", f"{slotmachine} No match, you lost, {ctx.author.name}!", "st's cool selfbot :3!!", ""))

@stselfbot.command()
async def joke(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Joke]''' + Fore.RESET)
    headers = {
        "Accept": "application/json"
    }
    r = requests.get("https://icanhazdadjoke.com", headers=headers).json()
    await ctx.send(r["joke"])

@stselfbot.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Autobump]''' + Fore.RESET)
    count = 0
    while True:
        try:
            count += 1
            channel = stselfbot.get_channel(ctx.channel.id)
            async for command in channel.slash_commands(query="bump"):
                if command.application.id == 302050872383242240:
                    await command()
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump info: sent {count} bump(s) so far' + Fore.RESET)
            await asyncio.sleep(7230)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)    

@stselfbot.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [tts]''' + Fore.RESET)
    audio_data = await do_tts(message)
    with io.BytesIO(audio_data) as f:
        await ctx.send(file=discord.File(f, filename='tts.mp3'))

@stselfbot.command()
async def caps(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Caps]''' + Fore.RESET)
    message = message.upper()
    await ctx.send(message)

@stselfbot.command(aliases=['guildicon', 'servericon'])
async def serverlogo(ctx, guildid = None):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Server logo]''' + Fore.RESET)
    if guildid == None:
        guildid = ctx.guild.id
    guild = stselfbot.get_guild(int(guildid))
    await ctx.send(await embedGen(ctx, f"Server logo", "", "st's cool selfbot :3!!", guild.icon))

@stselfbot.command(aliases=['guildbanner'])
async def serverbanner(ctx, guildid = None):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Server banner]''' + Fore.RESET)
    if guildid == None:
        guildid = ctx.guild.id
    guild = stselfbot.get_guild(int(guildid))
    if guild.banner == None:
        print(f'''{Fore.RED}[ERROR] {Fore.YELLOW}Server doesn't have a banner''' + Fore.RESET)
        return
    await ctx.send(await embedGen(ctx, f"Server banner", "", "st's cool selfbot :3!!", guild.banner))

@stselfbot.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Backup]''' + Fore.RESET)
    print(stselfbot.friends)
    for friend in stselfbot.friends:
        friendlist = (friend.user.name) + '#' + (friend.user.discriminator)
        with open('data/Friends.txt', 'a+', encoding='utf-8') as f:
            f.write(friendlist + "\n")
    for block in stselfbot.blocked:
        blocklist = (block.user.name) + '#' + (block.user.discriminator)
        with open('data/Blocked.txt', 'a+', encoding='utf-8') as f:
            f.write(blocklist + "\n")

@stselfbot.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [First message]''' + Fore.RESET)
    if channel is None:
        channel = ctx.channel
    async for message in channel.history(limit=1, oldest_first=True):
        first_message = message
        break
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send("first message - " + f"{first_message.jump_url}")

@stselfbot.command()
async def owofy(ctx, *args):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Owofy]''' + Fore.RESET)
    string = ' '.join(args)
    owofiedString = humor_langs.owofy(string)
    await ctx.send(owofiedString)

@stselfbot.command()
async def abc(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Abc]''' + Fore.RESET)
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@stselfbot.command(aliases=['bitcoin'])
async def btc(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Btc]''' + Fore.RESET)
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    await ctx.send(await embedGen(ctx, f'Bitcoin Price:\nUSD: {str(usd)}$ \nEUR: {str(eur)}€', "", "st's cool selfbot :3!!", ""))

@stselfbot.command(aliases=['ethereum'])
async def eth(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Eth]''' + Fore.RESET)
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    await ctx.send(await embedGen(ctx, f'Ethereum Price:\nUSD: {str(usd)}$ \nEUR: {str(eur)}€', "", "st's cool selfbot :3!!", ""))

@stselfbot.command()
async def topic(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Topic]''' + Fore.RESET)
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@stselfbot.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Wyr]''' + Fore.RESET)
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = f'Would you rather\n{qa}\n{qor}\n{qb}'
    await ctx.send(em)

@stselfbot.command()
async def ascii(ctx, *, text):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Ascii]''' + Fore.RESET)
    r = art.text2art(text)
    if len('```' + r + '```') > 2000:
        print("Generated ascii text is too long to send!")
        return
    thingy = f"```{r}```"
    await ctx.send(thingy)

@stselfbot.command()
async def uptime(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Uptime]''' + Fore.RESET)
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    print(f'''{Fore.CYAN} {uptime}''' + Fore.RESET)
    await ctx.send(f'`' + uptime + '`')

@stselfbot.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Purge]''' + Fore.RESET)
    async for message in ctx.channel.history(limit=amount):
        try:
            await message.delete()
        except:
            pass

@stselfbot.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Groupleaver]''' + Fore.RESET)
    for channel in stselfbot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@stselfbot.command(aliases=['cmds', 'commands'])
async def help(ctx):
    await ctx.message.delete()
    webbrowser.open("https://stiscool.cu.ma/selfbot/cmds.html")
    print(f'''

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}General Commands

{Fore.BLUE}cls {Fore.LIGHTBLACK_EX}- Clears console
{Fore.BLUE}help {Fore.LIGHTBLACK_EX}- Shows this
{Fore.BLUE}id {Fore.LIGHTBLACK_EX}- Sends Their ID In The Console
{Fore.BLUE}logout {Fore.LIGHTBLACK_EX}- Logs you out the selfbot
{Fore.BLUE}restart {Fore.LIGHTBLACK_EX}- Restarts the selfbot
{Fore.BLUE}uptime {Fore.LIGHTBLACK_EX}- Shows how long the selfbot has been online and working

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Text Stuff

{Fore.BLUE}1337-speak {Fore.LIGHTBLACK_EX}- Translates your message to 1337 language
{Fore.BLUE}abc {Fore.LIGHTBLACK_EX}- Sends the whole abecedary in a single message
{Fore.BLUE}ascii {Fore.LIGHTBLACK_EX}- Makes your message ascii/fancy
{Fore.BLUE}bold {Fore.LIGHTBLACK_EX}- Returns the message but **bold**
{Fore.BLUE}caps {Fore.LIGHTBLACK_EX}- Make your message CAPS
{Fore.BLUE}clear {Fore.LIGHTBLACK_EX}- Spam the chat with invisible messages
{Fore.BLUE}decode {Fore.LIGHTBLACK_EX}- Decode a string from base64 to regular text
{Fore.BLUE}decrypt {Fore.LIGHTBLACK_EX}- Decrypt a string from rot13 to regular text
{Fore.BLUE}devowel {Fore.LIGHTBLACK_EX}- Devowels your message
{Fore.BLUE}dm (user) (message) {Fore.LIGHTBLACK_EX}- Sends a message to the specified user
{Fore.BLUE}edit {Fore.LIGHTBLACK_EX}- edits all your messages
{Fore.BLUE}empty {Fore.LIGHTBLACK_EX}- Sends a empty message
{Fore.BLUE}encode {Fore.LIGHTBLACK_EX}- Encode a string to base64 ascii
{Fore.BLUE}encrypt {Fore.LIGHTBLACK_EX}- Encrypt a string to rot13
{Fore.BLUE}everyone {Fore.LIGHTBLACK_EX}- Glitched way to mention everyone in a server
{Fore.BLUE}get-hwid {Fore.LIGHTBLACK_EX}- Prints your hwid in the console
{Fore.BLUE}lenny {Fore.LIGHTBLACK_EX}- Sends: ( ͡° ͜ʖ ͡°)
{Fore.BLUE}reverse {Fore.LIGHTBLACK_EX}- Reverses ur message
{Fore.BLUE}secret {Fore.LIGHTBLACK_EX}- Returns the message but hidden ||hidden||
{Fore.BLUE}shrug {Fore.LIGHTBLACK_EX}- Sends: ¯\_(ツ)_/¯
{Fore.BLUE}spam {Fore.LIGHTBLACK_EX}- Sends the specified message that amount of times
{Fore.BLUE}stoptextppl {Fore.LIGHTBLACK_EX}- Stops textppl
{Fore.BLUE}tableflip {Fore.LIGHTBLACK_EX}- Sends: (╯°□°）╯︵ ┻━┻
{Fore.BLUE}textppl {Fore.LIGHTBLACK_EX}- Sends random messages to a channel for example while you're afk
{Fore.BLUE}tts {Fore.LIGHTBLACK_EX}- Send that message in .wav format, like an audio
{Fore.BLUE}unflip {Fore.LIGHTBLACK_EX}- Sends: ┬─┬ ノ( ゜-゜ノ)

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Guild, User Stuff

{Fore.BLUE}animatedaboutme {Fore.LIGHTBLACK_EX}- Cycles through specified about me's in your about me (can be buggy and slow), split the about me's with a comma
{Fore.BLUE}animatedstatus {Fore.LIGHTBLACK_EX}- Cycles through specified statuses in your status, split the statuses with a comma
{Fore.BLUE}av {Fore.LIGHTBLACK_EX}- Shows Your or mentioned users Avatar!
{Fore.BLUE}backupserver {Fore.LIGHTBLACK_EX}- Copies guild channels, categories, voice channels and makes them in a new one (backs it up)
{Fore.BLUE}banner {Fore.LIGHTBLACK_EX}- Shows mentioned users banner
{Fore.BLUE}blank {Fore.LIGHTBLACK_EX}- Turns your name and profile picture blank
{Fore.BLUE}first-message {Fore.LIGHTBLACK_EX}- Get the first message in that channel
{Fore.BLUE}genname {Fore.LIGHTBLACK_EX}- Generate a random name based on the server members
{Fore.BLUE}group-leaver {Fore.LIGHTBLACK_EX}- Leaves all the groups you're in
{Fore.BLUE}pfpsteal {Fore.LIGHTBLACK_EX}- Allows you to steal mentioned user profile picture
{Fore.BLUE}purge {Fore.LIGHTBLACK_EX}- Deletes your messages based on the amount you specify
{Fore.BLUE}readall {Fore.LIGHTBLACK_EX}- Marks all your messages as read, except DM
{Fore.BLUE}revav {Fore.LIGHTBLACK_EX}- Reverse avatar the mentioned user profile picture
{Fore.BLUE}role-hexcode {Fore.LIGHTBLACK_EX}- Displays the hexcode of the specified role
{Fore.BLUE}roleinfo {Fore.LIGHTBLACK_EX}- Display some info about the specified role
{Fore.BLUE}saveprofile {Fore.LIGHTBLACK_EX}- Saves a currently used profile picture and username
{Fore.BLUE}loadprofile {Fore.LIGHTBLACK_EX}- Loads a saved profile picture and username
{Fore.BLUE}serverbanner {Fore.LIGHTBLACK_EX}- Sends the server banner
{Fore.BLUE}serverlogo {Fore.LIGHTBLACK_EX}- Sends the server logo
{Fore.BLUE}sessions {Fore.LIGHTBLACK_EX}- Shows your accounts running sessions
{Fore.BLUE}setpfp {Fore.LIGHTBLACK_EX}- Set the specified url as profile picture
{Fore.BLUE}steal-all-pfp {Fore.LIGHTBLACK_EX}- Steal all the pfps in the server
{Fore.BLUE}stealprofile {Fore.LIGHTBLACK_EX}- Steals a users pfp and username
{Fore.BLUE}whois {Fore.LIGHTBLACK_EX}- Displays discord information of the mentioned user

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Fun Stuff

{Fore.BLUE}8ball {Fore.LIGHTBLACK_EX}- Answers your question
{Fore.BLUE}8balldiff {Fore.LIGHTBLACK_EX}- Answers your question, but different...
{Fore.BLUE}911 {Fore.LIGHTBLACK_EX}- Funny little animation haha
{Fore.BLUE}auto-bump {Fore.LIGHTBLACK_EX}- Automatically bump server to disboard.org
{Fore.BLUE}backupf {Fore.LIGHTBLACK_EX}- Backup your friends and blocked users name and discrim
{Fore.BLUE}calcpi {Fore.LIGHTBLACK_EX}- Calculates the value of pi to the specified amount of decimal places
{Fore.BLUE}calcprime {Fore.LIGHTBLACK_EX}- Calculates the value of primes up to the specified number
{Fore.BLUE}combine {Fore.LIGHTBLACK_EX}- Combines the two names together
{Fore.BLUE}cuttly {Fore.LIGHTBLACK_EX}- Shorten your link
{Fore.BLUE}dice {Fore.LIGHTBLACK_EX}- Rolls a dice
{Fore.BLUE}dick {Fore.LIGHTBLACK_EX}- Display the mentioned user dick size
{Fore.BLUE}get-color {Fore.LIGHTBLACK_EX}- Generates an image of a color that you specify
{Fore.BLUE}google {Fore.LIGHTBLACK_EX}- Use google search engine to look up something
{Fore.BLUE}img {Fore.LIGHTBLACK_EX}- Searches for an image on yandex
{Fore.BLUE}jerkoff {Fore.LIGHTBLACK_EX}- Funny emoji man creaming haha
{Fore.BLUE}junknick {Fore.LIGHTBLACK_EX}- long junk nickname
{Fore.BLUE}minesweeper {Fore.LIGHTBLACK_EX}- Play minesweeper in the discord chat
{Fore.BLUE}nitro {Fore.LIGHTBLACK_EX}- Generate a random nitro code
{Fore.BLUE}pingstreak {Fore.LIGHTBLACK_EX}- Pings mentioned user every 2-6 seconds
{Fore.BLUE}pp(User) {Fore.LIGHTBLACK_EX}- Does a funny little pp length command
{Fore.BLUE}qrcode {Fore.LIGHTBLACK_EX}- Generates a qr code from text
{Fore.BLUE}rainbow {Fore.LIGHTBLACK_EX}- Cycle colors in the role you specify
{Fore.BLUE}randomaddress {Fore.LIGHTBLACK_EX}- Generates a random address
{Fore.BLUE}slot {Fore.LIGHTBLACK_EX}- Play slot machine in the discord chat
{Fore.BLUE}stopstreak {Fore.LIGHTBLACK_EX}- Stops pinging mentioned user every 2-6 seconds
{Fore.BLUE}tinyurl {Fore.LIGHTBLACK_EX}- Shorten your link
{Fore.BLUE}weather {Fore.LIGHTBLACK_EX}- Lookup weather for the specified city

{Fore.YELLOW}Text Stuff

{Fore.BLUE}advice {Fore.LIGHTBLACK_EX}- Gives advice
{Fore.BLUE}animequote {Fore.LIGHTBLACK_EX}- Sends a random quote from an anime
{Fore.BLUE}joke {Fore.LIGHTBLACK_EX}- Drops a random joke in the chat
{Fore.BLUE}lyrics {Fore.LIGHTBLACK_EX}- Send lyrics of a song in the chat
{Fore.BLUE}oneshot {Fore.LIGHTBLACK_EX}- Sends a line of lyrics one by one of One Shot by King Ferran
{Fore.BLUE}owofy {Fore.LIGHTBLACK_EX}- Owofies your message
{Fore.BLUE}pack {Fore.LIGHTBLACK_EX}- Funny message roasts haha
{Fore.BLUE}topic {Fore.LIGHTBLACK_EX}- Start a random topic to keep the chat going
{Fore.BLUE}wyr {Fore.LIGHTBLACK_EX}- Start a 'what would you rather' topic in the chat

{Fore.YELLOW}Image Stuff

{Fore.BLUE}awooify {Fore.LIGHTBLACK_EX}- Puts a users pfp on a catgirls face
{Fore.BLUE}bird {Fore.LIGHTBLACK_EX}- Random bird image
{Fore.BLUE}bisexualborder {Fore.LIGHTBLACK_EX}- Add a bisexual flag border to a users pfp
{Fore.BLUE}blue {Fore.LIGHTBLACK_EX}- Make a users pfp blue
{Fore.BLUE}blur {Fore.LIGHTBLACK_EX}- Make a users pfp blurred
{Fore.BLUE}blurpify {Fore.LIGHTBLACK_EX}- Blurpifies a users pfp
{Fore.BLUE}blurple {Fore.LIGHTBLACK_EX}- Make a users pfp blurple
{Fore.BLUE}blurple2 {Fore.LIGHTBLACK_EX}- Make a users pfp blurple
{Fore.BLUE}brightness {Fore.LIGHTBLACK_EX}- Make a users pfp brighter
{Fore.BLUE}captcha {Fore.LIGHTBLACK_EX}- Puts a users pfp on a captcha
{Fore.BLUE}cat {Fore.LIGHTBLACK_EX}- Random cat image
{Fore.BLUE}changemymind {Fore.LIGHTBLACK_EX}- Generates a change my mind image with text
{Fore.BLUE}circle {Fore.LIGHTBLACK_EX}- Make a users pfp circular
{Fore.BLUE}clyde {Fore.LIGHTBLACK_EX}- Generates a clyde message image
{Fore.BLUE}comrade {Fore.LIGHTBLACK_EX}- Put a communism scythe and hammer overlay on a users pfp
{Fore.BLUE}deepfry {Fore.LIGHTBLACK_EX}- Deepfries a users pfp
{Fore.BLUE}dog {Fore.LIGHTBLACK_EX}- Random dog image
{Fore.BLUE}drake {Fore.LIGHTBLACK_EX}- Generates a drake good or bad image
{Fore.BLUE}fact {Fore.LIGHTBLACK_EX}- Generates an image of the fact on a paper getting held
{Fore.BLUE}fox {Fore.LIGHTBLACK_EX}- Random fox image
{Fore.BLUE}glass {Fore.LIGHTBLACK_EX}- Put a glass overlay on a users pfp
{Fore.BLUE}green {Fore.LIGHTBLACK_EX}- Make a users pfp green
{Fore.BLUE}greyscale {Fore.LIGHTBLACK_EX}- Make a users pfp grey
{Fore.BLUE}heart {Fore.LIGHTBLACK_EX}- Make a users pfp a heart
{Fore.BLUE}horny {Fore.LIGHTBLACK_EX}- Put users pfp on a horny ID card image thing funny haha
{Fore.BLUE}invergreyscale {Fore.LIGHTBLACK_EX}- Make a users pfp inverted grey
{Fore.BLUE}iphonex {Fore.LIGHTBLACK_EX}- Puts a users pfp on an iphone x screen
{Fore.BLUE}itssostupid {Fore.LIGHTBLACK_EX}- Put users pfp on a it's stupid meme
{Fore.BLUE}jail {Fore.LIGHTBLACK_EX}- Put a jail overlay on a users pfp
{Fore.BLUE}jpg {Fore.LIGHTBLACK_EX}- Convert a users pfp to a jpg
{Fore.BLUE}kangaroo {Fore.LIGHTBLACK_EX}- Random kangaroo image
{Fore.BLUE}kannafy {Fore.LIGHTBLACK_EX}- Generates a kanna image with the text
{Fore.BLUE}koala {Fore.LIGHTBLACK_EX}- Random koala image
{Fore.BLUE}lesbianborder {Fore.LIGHTBLACK_EX}- Put a lesbian flag border to a users pfp
{Fore.BLUE}lgbtborder {Fore.LIGHTBLACK_EX}- Put an lgbt flag border to a users pfp
{Fore.BLUE}lied {Fore.LIGHTBLACK_EX}- Put a users pfp and name on some lied thing idk
{Fore.BLUE}lolice {Fore.LIGHTBLACK_EX}- Puts a users pfp on a lolice chef saying something
{Fore.BLUE}magik {Fore.LIGHTBLACK_EX}- Adds a magik effect to a users pfp
{Fore.BLUE}milanaham {Fore.LIGHTBLACK_EX}- Sends a random picture of Milana Hametova from my WebAPI
{Fore.BLUE}noblank {Fore.LIGHTBLACK_EX}- Sends a no bitches meme thing where you can edit "bitches" to anything you want
{Fore.BLUE}nonbinaryborder {Fore.LIGHTBLACK_EX}- Put a nonbinary flag border to a users pfp
{Fore.BLUE}panda {Fore.LIGHTBLACK_EX}- Random panda image
{Fore.BLUE}pansexualborder {Fore.LIGHTBLACK_EX}- Put a pansexual flag border to a users pfp
{Fore.BLUE}passed {Fore.LIGHTBLACK_EX}- Put a mission passed overlay on a users pfp
{Fore.BLUE}phcomment {Fore.LIGHTBLACK_EX}- Generates a pornhub comment with a users pfp and name and defined text
{Fore.BLUE}pixelate {Fore.LIGHTBLACK_EX}- Pixelate a users pfp
{Fore.BLUE}pornhub {Fore.LIGHTBLACK_EX}- Generates a pornhub logo image with left and right text
{Fore.BLUE}pride {Fore.LIGHTBLACK_EX}- Put a pride flag overlay on a users pfp
{Fore.BLUE}putin {Fore.LIGHTBLACK_EX}- Generates a putin top bottom text image
{Fore.BLUE}raccoon {Fore.LIGHTBLACK_EX}- Random raccoon image
{Fore.BLUE}red {Fore.LIGHTBLACK_EX}- Make a users pfp red
{Fore.BLUE}redpanda {Fore.LIGHTBLACK_EX}- Random redpanda image
{Fore.BLUE}sepia {Fore.LIGHTBLACK_EX}- Add a sepia effect to a users pfp
{Fore.BLUE}ship {Fore.LIGHTBLACK_EX}- Generates a ship image with two pfps
{Fore.BLUE}simpcard {Fore.LIGHTBLACK_EX}- Put a users pfp on a simp card
{Fore.BLUE}spin {Fore.LIGHTBLACK_EX}- Make a users pfp spin
{Fore.BLUE}spongebobsad {Fore.LIGHTBLACK_EX}- Generates a spongebob sad in a cafe top bottom text image
{Fore.BLUE}stickbug {Fore.LIGHTBLACK_EX}- Generates a stickbug video from a users pfp
{Fore.BLUE}threshold {Fore.LIGHTBLACK_EX}- Add a threshold effect to a users pfp
{Fore.BLUE}tonikawa {Fore.LIGHTBLACK_EX}- Put a users pfp on a thing tonikawa is holding
{Fore.BLUE}transborder {Fore.LIGHTBLACK_EX}- Put a transgender flag border to a users pfp
{Fore.BLUE}trap {Fore.LIGHTBLACK_EX}- Generates a trap card with the users pfp
{Fore.BLUE}trash {Fore.LIGHTBLACK_EX}- Generates a trash anime girl Japan meme with a users pfp
{Fore.BLUE}triggered {Fore.LIGHTBLACK_EX}- Put a triggered overlay on a users pfp
{Fore.BLUE}trumptweet {Fore.LIGHTBLACK_EX}- Generates a trump tweet image
{Fore.BLUE}tweet {Fore.LIGHTBLACK_EX}- Generates a tweet image
{Fore.BLUE}wasted {Fore.LIGHTBLACK_EX}- Put a wasted overlay on a users pfp
{Fore.BLUE}whale {Fore.LIGHTBLACK_EX}- Random whale image
{Fore.BLUE}whowouldwin {Fore.LIGHTBLACK_EX}- Generates a who would win meme image with two pfps
{Fore.BLUE}youtubecomment {Fore.LIGHTBLACK_EX}- Make a fake youtube comment

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Emotions

{Fore.BLUE}animalears {Fore.LIGHTBLACK_EX}- Random animalears [Anime]
{Fore.BLUE}baka {Fore.LIGHTBLACK_EX}- Random baka [Anime]
{Fore.BLUE}bite {Fore.LIGHTBLACK_EX}- Random biting gif
{Fore.BLUE}blush {Fore.LIGHTBLACK_EX}- Random blushing gif
{Fore.BLUE}bored {Fore.LIGHTBLACK_EX}- Random bored gif
{Fore.BLUE}catboy {Fore.LIGHTBLACK_EX}- Random catboy img
{Fore.BLUE}cry {Fore.LIGHTBLACK_EX}- Random crying gif
{Fore.BLUE}cuddle {Fore.LIGHTBLACK_EX}- Random cuddle gif
{Fore.BLUE}dance {Fore.LIGHTBLACK_EX}- Random dancing gif
{Fore.BLUE}facepalm {Fore.LIGHTBLACK_EX}- Random facepalming gif
{Fore.BLUE}feed {Fore.LIGHTBLACK_EX}- Random feeding gif
{Fore.BLUE}foxgirl {Fore.LIGHTBLACK_EX}- Random foxgirl [Anime]
{Fore.BLUE}gasm {Fore.LIGHTBLACK_EX}- Random gasm [Anime]
{Fore.BLUE}handhold {Fore.LIGHTBLACK_EX}- Random hand holding gif
{Fore.BLUE}happy {Fore.LIGHTBLACK_EX}- Random happy gif
{Fore.BLUE}highfive {Fore.LIGHTBLACK_EX}- Random highfive gif
{Fore.BLUE}hug {Fore.LIGHTBLACK_EX}- Random hugging gif
{Fore.BLUE}husbando {Fore.LIGHTBLACK_EX}- Random husbando gif
{Fore.BLUE}kick {Fore.LIGHTBLACK_EX}- Random kicking gif
{Fore.BLUE}kiss {Fore.LIGHTBLACK_EX}- Random kissing gif
{Fore.BLUE}kitsune {Fore.LIGHTBLACK_EX}- Random kitsune gif
{Fore.BLUE}laugh {Fore.LIGHTBLACK_EX}- Random laughing gif
{Fore.BLUE}lick {Fore.LIGHTBLACK_EX}- Random licking gif
{Fore.BLUE}neko {Fore.LIGHTBLACK_EX}- Random neko [Anime]
{Fore.BLUE}nod {Fore.LIGHTBLACK_EX}- Random nodding gif
{Fore.BLUE}nom {Fore.LIGHTBLACK_EX}- Random nom gif
{Fore.BLUE}nope {Fore.LIGHTBLACK_EX}- Random nope gif
{Fore.BLUE}pat {Fore.LIGHTBLACK_EX}- Random pat gif
{Fore.BLUE}poke {Fore.LIGHTBLACK_EX}- Random poking gif
{Fore.BLUE}pout {Fore.LIGHTBLACK_EX}- Random pout gif
{Fore.BLUE}punch {Fore.LIGHTBLACK_EX}- Random punching gif
{Fore.BLUE}shoot {Fore.LIGHTBLACK_EX}- Random shooting gif
{Fore.BLUE}shruggif {Fore.LIGHTBLACK_EX}- Random shrugging gif
{Fore.BLUE}slap {Fore.LIGHTBLACK_EX}- Random slapping gif
{Fore.BLUE}sleep {Fore.LIGHTBLACK_EX}- Random sleeping gif
{Fore.BLUE}smug {Fore.LIGHTBLACK_EX}- Random smug gif
{Fore.BLUE}stare {Fore.LIGHTBLACK_EX}- Random staring gif
{Fore.BLUE}think {Fore.LIGHTBLACK_EX}- Random thinking gif
{Fore.BLUE}thumbsup {Fore.LIGHTBLACK_EX}- Random thumbsup gif
{Fore.BLUE}tickle {Fore.LIGHTBLACK_EX}- Random tickling gif
{Fore.BLUE}waifu {Fore.LIGHTBLACK_EX}- Random waifu [Anime]
{Fore.BLUE}wallpapers {Fore.LIGHTBLACK_EX}- Random wallpaper
{Fore.BLUE}wave {Fore.LIGHTBLACK_EX}- Random waving gif
{Fore.BLUE}wink {Fore.LIGHTBLACK_EX}- Random winking gif
{Fore.BLUE}yeet {Fore.LIGHTBLACK_EX}- Random yeeting gif

{Fore.RED}NSFW Stuff

{Fore.BLUE}anal {Fore.LIGHTBLACK_EX}- Random anal [Anime]
{Fore.BLUE}belle {Fore.LIGHTBLACK_EX}- Random belle deplhine picture
{Fore.BLUE}bellevid {Fore.LIGHTBLACK_EX}- Random belle delphine video
{Fore.BLUE}blowjob, bj {Fore.LIGHTBLACK_EX}- Random blowjob gif [Anime]
{Fore.BLUE}boobs {Fore.LIGHTBLACK_EX}- Random boobs [Anime]
{Fore.BLUE}catgirl {Fore.LIGHTBLACK_EX}- Random catgirl [Most likely not anime]
{Fore.BLUE}cum {Fore.LIGHTBLACK_EX}- Random cum gif [Anime]
{Fore.BLUE}feet {Fore.LIGHTBLACK_EX}- Random feet [Anime]
{Fore.BLUE}femboy {Fore.LIGHTBLACK_EX}- Random femboy [Anime]
{Fore.BLUE}fourk, 4k {Fore.LIGHTBLACK_EX}- Random 4K image
{Fore.BLUE}gif {Fore.LIGHTBLACK_EX}- Random NSFW gif
{Fore.BLUE}hentai {Fore.LIGHTBLACK_EX}- Random hentai [Anime]
{Fore.BLUE}hneko {Fore.LIGHTBLACK_EX}- Random hentai neko [Anime]
{Fore.BLUE}holo {Fore.LIGHTBLACK_EX}- Random holo [Anime]
{Fore.BLUE}lesbian {Fore.LIGHTBLACK_EX}- Random lesbian [Anime]
{Fore.BLUE}lewd {Fore.LIGHTBLACK_EX}- Random lewd image [Anime]
{Fore.BLUE}paizuri {Fore.LIGHTBLACK_EX}- Random paizuri gif/image [Anime]
{Fore.BLUE}pussy {Fore.LIGHTBLACK_EX}- Random pussy gif [Anime]
{Fore.BLUE}spank {Fore.LIGHTBLACK_EX}- Random ass spanking gif [Anime]
{Fore.BLUE}yaoi {Fore.LIGHTBLACK_EX}- Random yaoi gif/image [Anime]

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Doxxing stuff

{Fore.BLUE}address {Fore.LIGHTBLACK_EX}- Generates fake address based on the text you specify
{Fore.BLUE}geoip {Fore.LIGHTBLACK_EX}- Display various information about the IP
{Fore.BLUE}pingweb {Fore.LIGHTBLACK_EX}- Pings a website

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Streaming

{Fore.BLUE}btc {Fore.LIGHTBLACK_EX}- Display current Bitcoin price
{Fore.BLUE}btcstream {Fore.LIGHTBLACK_EX}- Stream current btc price
{Fore.BLUE}changeactivity [name (streaming, watching, listening)] [text to say] {Fore.LIGHTBLACK_EX}-Adds an activity that you specify with that message onto your profile
{Fore.BLUE}eth {Fore.LIGHTBLACK_EX}- Display current Ethereum price
{Fore.BLUE}hypesquad {Fore.LIGHTBLACK_EX}- Allows you to change your hypesquad
{Fore.BLUE}stopactivity {Fore.LIGHTBLACK_EX}- Stops all the streams, plays and listen activities

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.YELLOW}Nuking

{Fore.BLUE}delchannels {Fore.LIGHTBLACK_EX}- Delete all the channels
{Fore.BLUE}delroles {Fore.LIGHTBLACK_EX}- Delete all the roles
{Fore.BLUE}destroy {Fore.LIGHTBLACK_EX}- Ban, delete roles, delete channels, edit guild info, mass create channels All in one!
{Fore.BLUE}dmall {Fore.LIGHTBLACK_EX}- Messages every user in that guild
{Fore.BLUE}massban {Fore.LIGHTBLACK_EX}- Ban all the users in that guild
{Fore.BLUE}masschannel {Fore.LIGHTBLACK_EX}- Mass create channels
{Fore.BLUE}masskick {Fore.LIGHTBLACK_EX}- Kick all the users in that guild
{Fore.BLUE}massrole {Fore.LIGHTBLACK_EX}- Mass create role
{Fore.BLUE}massunban {Fore.LIGHTBLACK_EX}- Unban every member
''')

@stselfbot.command()
async def oneshot(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [One Shot]''' + Fore.RESET)
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
              "king ferran out", ]
    for i in lyrics:
        await ctx.send(i)
        await asyncio.sleep(2)

@stselfbot.command()
async def pack(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Pack]''' + Fore.RESET)
    await ctx.send(
        'You used OBS studio just to screen-record yourself beating the roblox tower of hell obby and you failed on a lava jump trash ass nigga')
    await asyncio.sleep(1)
    await ctx.send(
        'Thats why you had a friend for 3 years on roblox that was a girl and when you asked her out on adopt me she reset and disconnected from the game dumb ass nigga fuck is you talkin bout')
    await asyncio.sleep(1)
    await ctx.send(
        'thats why yo grandma is addicted to masturbating to sea weed water while she sips coffe with syrup in it nasty ass nigga')
    await asyncio.sleep(1)
    await ctx.send(
        'Nigga you literally have a modded version of GTA 5 and whenever you get into arguments with citizens boy ya character just start using shadow clone jutsu without using any hand signs boy you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send(
        'uhuh nigga ya mother is a level 10 warrior nigga and she trains zobies to clip her toe nails with safety sizzors boy you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send(
        'nigga you woke up and saw juice wrld and thought he came back from the dead only to find out you got killed by a cross eyed frog the day before you stupid ass nigga')
    await asyncio.sleep(1)
    await ctx.send(
        'What boy you survived a plane crash in south africa and as soon as you got out the plane you just took a 2 hour long shit behind a tree my nigga you ugly as shit')
    await asyncio.sleep(1)
    await ctx.send(
        'nigga but tell me why you the only nigga thats built like a half retarded turanchula boy you got 7 eyes and 4 legs boy')
    await asyncio.sleep(1)
    await ctx.send(
        'i saw you throwing it back for mr krabs you got 3 dabloons and a krabby patty to go hell nah you got sexually harrassed by a math workbook hell nah nigga caught yo dumbass doing the electric zoo with that nigga ed from goodburger because yall found a cockroach nope nigga your grandma got backhanded by angry mall cop over a bottle of listerine and mechanical parts from fortnite nasty neck nigga like shit you got sexually seduced by a radioactive shit spitting cow when you overtalked him with the indian scammer headset')
    await asyncio.sleep(1)
    await ctx.send(
        '“ratio” took you 4 tries to spell it correctly retarded dyslexic ugly lookin peice of banana flavored cheese dirty ass boy, you got shit stains on your forehead my nigga shutcho dumb ass up boi you shoved a boiled egg up your ass at 4am while playing with hot wheels dirty ass boy you eat your fingers for breakfast my nigga shutcho dumb ass up')
    await asyncio.sleep(1)
    await ctx.send(
        'danggg… that shit was ass my nigga shutcho oompa loopa from charlie and the chocolate factory lookin ass boy you started doing fortnite emotes after you got an a on your report card weird ass nigga I hit a 360 on yo grandma in real life and she landed in the gulag dumb ass boy shutcho lame ass up boy they call you “lil inched” at school because your dick is -1 cm long my nigga shut yo dumb ass up boy')
    await asyncio.sleep(1)
    await ctx.send(
        'im sorry.. 💔 but that shit was ass my nigga you down bad too knowing what shreks tits look like anyways shut yo dumb ass up boi you stupid as shit your grandma got instant cancer after taking a gaze at your face for more than 10 seconds and she died a week later stupid ass bitch “Say sum” - :nerd: shutcho “Mom, I’m ready for school!” you stuffed 10 pairs of dildos in your backpack to give to your classmates outside behind the slides dirty nigga shutcho dumb ass up “when pinocchio lies his nose grows” he told you, you got no hoes and nothing happened bitch ass nigga shutcho dumb ass misfigured nose  broken upperlip disabled pony ride lookin ass nigga after lookin at your moms titties I caught ebola shutcho dumb ass up')
    await asyncio.sleep(1)
    await ctx.send(
        'boy shut yo dumb ass up, with your android with a despicable me phone case dirty ass boy you wipe your ass with a pack of toothpaste bitch ass boy you look like a gangster with extra long toothpicks coming outcha ass they call you “Lil Toothy” bitch ass boy I smacked your grandma into a deep state and she turned into a soundcloud rapper you brush your teeth with a ethernet cable nigga I hit you with a slice of sweaty pizza and you started playing geometry dash dumb ass boy if you don’t get your harry potter gacha life mosquito joycon nipple cosplaying as franklin the turtle but emo 🖤 dumb ass boyy cricket wireless using ass boy toaster strudel wireless zoo electric tomato with potato skin lookin ass boy you arabian seastar shut the fuck up blowing some dude in the back of the alley with a fork and knife for 3 nickels and a strawberry poptart fat ass boy I went up to your grandpa with ptsd showed him the new call of duty and he had world war 2 flash backs bitch ass boy')
    await asyncio.sleep(1)
    await ctx.send(
        'you rage when your mom doesn’t let you  eat toaster strudels fat ass boi. you threw a bag of peanut shells at your mom and started rapping cod subtitles stupid ass boi. you got grounded for eating a bag of salt and pepper apple jacks at 3am in the morning outside in the cold listening to lil pump making gacha life music videos bitch ass boi')
    await asyncio.sleep(1)
    await ctx.send('tell me why yo ass built built a rocket league car boy')
    await asyncio.sleep(1)
    await ctx.send(
        'you weird as fuck boy ole ugly ass nigga tell me why yo gang bangin 93 year grandpa caught yo ass fucking a coconut with a rubix cube in yo mouth and grounded you from painting your nails weird ass boy')
    await asyncio.sleep(1)
    await ctx.send(
        'nigga you look like you try to fight tadpoles with yo weird ass boy tell me why i caught yo ugly ass pet frog with a 1737 durag on fucking yo pet snail weird ass boy')
    await asyncio.sleep(1)
    await ctx.send('nigga you bout ugly as shit boy yo head built like donkey kongs right nut ugly ass')
    await asyncio.sleep(1)
    await ctx.send(
        'you can not be talking to me right now nigga you reading all yo packs off your forehead in the mirror boy')
    await asyncio.sleep(1)
    await ctx.send(
        'tell me why yo ass broke yo tv tryna fight squidward weird ass nigga you bout ugly as shit boy with yo un funny ass')
    await asyncio.sleep(1)
    await ctx.send(
        'nigga i caught yo ass counting the pixels on yo tv to say you had 4k nigga.. wait.. no thats 4p headass boy you play gacha life HOOD EDITION and try to act gangster')
    await asyncio.sleep(1)
    await ctx.send(
        'boy i caught yo ass with a sharpened spongebob butter knife robbing a bass pro shop for fishing poles.')
    await asyncio.sleep(1)
    await ctx.send(
        'that shit was ass tell my why i caught you but ass naked solving a rubix cube while fucking a coconut. tell me why i caught you trying to create “super sauce” with your cum combined with sprite')
    await asyncio.sleep(1)
    await ctx.send(
        'you got your chain snatched at the suburban skate park by chester bennington and shia labeouf shut the fuck up nigga')
    await asyncio.sleep(1)
    await ctx.send(
        'Ths nigga ugly as shit you fat ass boy you been getting flamed by two donkeys when you walk to the store and one of them smacked you in the forehead fuckboy and then you go to come in with uh ???? and smacked you in the bootycheeks fuckboy you dirty as shit boy everytime you go to school nigga you get bullied by 10 white kids that say you gay behind the bus fuckboy suck my dick nigga unknown as shit nigga named nud you been getting hit by two frozen packs when you walk into the store fuckboy suck my dick unknown ass nigga named nud nigga you my son nigga hold on, ay creedo you can flame this nigga for me? Yeah im in this bitch fuck is you saying nigga my nigga')
    await asyncio.sleep(1)
    await ctx.send(
        'nigga mad as fuck cuz you got a hairline on yo armpit hairs you nasty bitch yo ass had to use yo internal keyboard to type yo high school english language arts essay cuz yo ass had an orgasms on you keyboard when you seen a, picture of cardi bs leaked titty pic after you clicked the link in yo best friends status on discord yo virgin ass nigga fuck is you talkin bitch bout you weak ass bitch made ass kangaroo neck ass cmon now gladiator chainsaw neck ass claustrophobic necklace wearing ass nigga yo step dad got a ancient katana named "storm-cutter" that shit soul bounded to cutting nothing but gold-fish crackers nigga you got out yo bed at 3 in the morning nigga u so retarded you tried doing a skyrim shout to yo fucking teacher and failed miserably then you proceeded to try morph into a retarded imperial and tried doing the calm power fuck is you talkin about nigga you got the most expensive skin on fortnite because epic games felt bad for you after yo hairline got pushed back 8 inches by a drunk barber nigga you ugly as shit.')
    await asyncio.sleep(1)
    await ctx.send(
        'Aight bruh shut ur dumbass up before i get to the packing on ur ass u nasty no neck built ass happy meal looking ass bvoy shut ur big booty ass up i caught ur dumbass cosplaying as ronald mcdonald till u got body slammed by a chicken nugget u nasty as boy after that u fell into a coma when u wake up u thought u was from lego ninja go u started saying ninja gooo u started smacking people on the streets with racoons till ur fatass got hungry u started eating them u said yea u got the yummy yuh yummy yuh ma yummy yuh u nasty ass boy cum in a bum cum in a son nasty ass bitch u bout dirty as shit boy i caught ur fatass in ur backyard belly dancing with cockroaches till u started dong the dream speedrun anthem they started speedrunning trying to kill the enderdragon u said minecraft was the best game in 2022 u enchanted ur body parts with efficiency 5 u became the fastest person on earth u started going on a big mac rampage eating every big mac u see fat neck built ass bitch u became depressed cus u got rejected 19 times in a row u got a charger and charged it into ur heart thinking it will fix ur depression like shit boy u thought u was michael jordan u started slamming basketballs into ur grandmas pussy u dirty ass bitch')
    await asyncio.sleep(1)
    await ctx.send(
        'that shit was so ass, tell me why I caught you with the queen of england eating premium edition cream cheese in a corner store with a nigga named pablo eating takis recording an asmr bedwars video in the background stupid ass nigga.')
    await asyncio.sleep(1)
    await ctx.send(
        'Bro you a whole new species NIGGA everytime it gets foggy you turn into a space demon fading away everytime somebody walks away 5 feet from u you disappear like a skinny black dude turning sideways in the dark oh nah nigga tell me why you the gay batman yo identity is sex lane you like to hate on black people and fight black and white flags instead of fighting crime Nigga how are you finna sit here and say your a boy AND girl do u got a dick or not, that will end the whole conversation and so of you niggas be like "im not a gender im other" nigga fuck do you mean theres only 2 genders your not fucking niel degrass tyson you dont know shit but how to make yourself look retarded Your mothers a whole creature from coraline my nigga i caught her ass transmutating herself into a chuthulu mythos creature. my guy tell me why when you woke up you saw your dad getting abducted by oompa loompas you nasty bitch , ong you was standing like “🧍🏻‍♂️” when your dad got jumped by aliens from men im black then turned into a box by a plasma ray my nigga, stfu before i smack tf outta you with roach spray and you start dissolving like my science project nasty ass nigga Nah bro you was deadass eating them rainbow air heads and u thought they gave u +1 LGBTQ boost to give off your statements on why LGBTQ is good shut cho dumbass up HUSH MODE HUSH MODE SAY SUM BITCH')
    await asyncio.sleep(1)
    await ctx.send(
        'yo FBI agent used instant transmission to yoliving room and stole all yo light bulbs dumb ass niggafuck is you saying you hideous ass iPhone 4 se screenprotector forehead ass niggacmon now lotion bottle neck ass long foot ass itchy toenail having ass nigga im onyo ass nigga I went to yo momma house and went to the bathroom and opened up themirror and saw 3 dildos and they all had sticky notes with names on them saying"Pussy Destroyer 1, 2 and 3" dumb ass nigga you ugly as fuck Ill smack yo mommawith a meat ball and she start breakdancing from the adrenaline rush bitch assnigga fuck is you saying to me bitch ass nigga yo mom was in Highschool walkingaround the halls and she tripped and fell and busted her chest open bitch ass boyfuck is you saying nigga you ugly as fuck fat neck ass picture frame neck ass BiClighter face ass acute triangle teeth shape ass nigga you spectacularly ugly asshit with yo Kapreson straw neck ass and speaking of kapreson straws, yo mom had akapreson straw and put it in her booty hole and that fat bitch got tired becauseher left arm alone weigh 700 pounds fat ass bitch nigga fuck is you talking aboutyou lame ass nigga yo father had a crush on Usain Bolt in 1944 while he was playingSaxiphone instrumentals in a doctors office flexing in front of all the patientswith knee cap problems bitch ass nigga you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send(
        'nigga you floss yo teeth with cockroach antennas your dad is best friends with fat albert “he ate his last bigmac” your just mad because spongebob killed your whole family with a spatula you is retarded you chew on rocks for fun head ass you is mentally retarded i caught you french kissing a cactus naked you have rubber bands on the bottom of your feet fat ass nigga yo ass is banned him from the middle east for assaulting a Palestinian with a Louis Vuitton water bottle boy nigga your balls are above your belly is button head ass nigga nigga  you went in the sewers bc you thought penny wise was gonna be there your dog got into an arguement with hannibal lecter yo pillow is made out of toilet paper with yo head ass when i was fucking your mom it started playing bart sim sim music nigga tell me why you drink water bottles with nothing in them your retarded dumb ass nigga you look like kung fu panda eating a breadstick head ass nigga your built like the a black thanos big body ass nigga shut yo fat ass up nigga you molested a chicken nigga i caught you and yo family begging for a Travis scott meal on the streets dumb ass fat ass nigga  nigga your retarded as shit nigga  you look like a emo clownfish nigga you is retarded nigga you have a mexican comb over nigga you looked in yo backyard and your pet dog was having a pool party with spiderman in a bottle of ranch nigga yo ass was beating yo meat with peroxide and Clorox wipes you nasty ass nigga yo ass is broke as shit because you spent 447 billion dollars on a Louis Vuitton pencil sharpener on the Roblox catalog yo ass has a dominus astro on roblox and you sold that shit for a mcdonald’s slushy machine dumbass nigga yo teacher ip banned you from the zoom class because you was showing off yo haircuts to the assistant principal for a homework pass dumbass nigga you barley have friends because you have policy when they come to your house you gotta take there eyelids cuz you don’t like niggas blinking at you')
    await asyncio.sleep(1)
    await ctx.send(
        'yo FBI agent used instant transmission to yoliving room and stole all yo light bulbs dumb ass niggafuck is you saying you hideous ass iPhone 4 se screenprotector forehead ass niggacmon now lotion bottle neck ass long foot ass itchy toenail having ass nigga im onyo ass nigga I went to yo momma house and went to the bathroom and opened up themirror and saw 3 dildos and they all had sticky notes with names on them saying"Pussy Destroyer 1, 2 and 3" dumb ass nigga you ugly as fuck Ill smack yo mommawith a meat ball and she start breakdancing from the adrenaline rush bitch assnigga fuck is you saying to me bitch ass nigga yo mom was in Highschool walkingaround the halls and she tripped and fell and busted her chest open bitch ass boyfuck is you saying nigga you ugly as fuck fat neck ass picture frame neck ass BiClighter face ass acute triangle teeth shape ass nigga you spectacularly ugly asshit with yo Kapreson straw neck ass and speaking of kapreson straws, yo mom had akapreson straw and put it in her booty hole and that fat bitch got tired becauseher left arm alone weigh 700 pounds fat ass bitch nigga fuck is you talking aboutyou lame ass nigga yo father had a crush on Usain Bolt in 1944 while he was playingSaxiphone instrumentals in a doctors office flexing in front of all the patientswith knee cap problems bitch ass nigga you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send(
        'stfu Im really boutta get to the flamin on yo ass stfu yo ass built like an atm looking ass nigga built like a sumo wrestler looking ass nigga I caught yo ass stealing the travis scott burgers from McDonalds oh u fat as hell bruh with yo greasy musty Dusty cheeseburger body having ass bruh thats it.. bro stfu dont get me started with yo crusty lip ass bruh I caught yo ass taking a shower in the community pool and using chlorine as soap u nasty as hell bruh yo ass cosplays as a discord admin thinking hes cool u dirty as hell,Shutcho ugly ass up bruh yo ass built like a deformed shrek 2.0 boi yo ass fat as hell fat neck ass fat triple chin having ass stfu bruh...  Shut ur ass up I can make that pussy whistle like the old spic commercial nigga thats it nigga stfu with yo ugly ass drake head as mr clean looking ass up bruh Im really boutta get to yo shit stained eyebrows having ass up bruh yo ass built like a beanbag with arms and legs stfu bruh,  fuck you bitch you nasty lookin asssloth take yo dee dee from dexter laboratory nasty ass giraffe built hoe bald headed ass bitch lookin like sumo from clarence cough drop ponytail ass hoe and you built like peter griffin from family guy big fat hippo ass bitch you look like gumball dad from amazing world of gumball fat ass hoe looking like edna gap having ass bitch you the fatass girl from alvin and the chipmunks talking about some “my precious” lookin like the donkey from shrek built ass green booger ass hoe lookin like penny wise with yo big ass forehead not even bitch you got a five head built like ursula from the little mermaid and lookin like yellow bird from elmo daffy duck lookin ass & lookin like the fat pig from chicKen little mojo mojo lookin ass wide face ass cross eyed hoe lookin like the bald guy from ed edd eddy lookin like doofenshmirtz from Phineas and ferb dorito head ass hoe pointy head ass bitch.')
    await asyncio.sleep(1)
    await ctx.send(
        "yo mom was bussin it back for that nigga sandy cheeks because she was gon give hera TI-84 calculator if she did it so she could conquor the world dumb ass nigga yomom created the letter O because she saw the moon and started meditating dumb assnigga she fell into sleep paralysis, and her sleep paralysis demon was a waterbattle, with the top off bitch ass boi fuck is you saying nigga you are a legendarypokemon trainer you beat Ash's pikachu by staring at his tail, dumb ass niggathat's why yo Auntie know the secret art of Spinjitsu, her ass can jump up in theair, kill 800 niggas, and fall back to the ground in 0.0004 seconds nigga yo auntiescary as shit fuck is you saying that's why yo granddad got assassinated by apoisonous venus fly trap in south dekota on top of a Ice Cream truck while he wascharging his chakra dumb ass nigga yo great grandma created basketball, because shepicked up a rock, and threw it through the middle of a lifesaver bitch ass niggayou stupid as fuck that's why yo granddad is an experienced agar.io player and hesolotricked Donald Trump and gained 439,543 mass and started giving away all hismass to everyone in the game with a number in they name dumb ass nigga yo mom wason a airplane, and she banged her head against the glass, broke the window, jumpedout, and landed on a trampoline and she bounced back up to the airplane, sat down,and pulled out a toolbox, and started fixing the airplane dumb ass nigga you stupidas fuck, fuck is you saying nigga you are horrible nigga yo granddad is the bestspace conservationist in the world nigga he made 84 couches, fit inside of abathroom dumb ass nigga fuck is you saying nigga you retarded as fuck yo girlfriendis Sakura so she beats the shit out of you whenever you don't acknowledge her dumbass nigga boy fuck is you saying nigga you quit gaming, becuz that nigga YBNNahmir, gave yo mom a cheeseburger, you saw that shit ain't have no meat on thatshit, yo ass awakened yo sharingan and put that nigga into Sleep")
    await asyncio.sleep(1)
    await ctx.send(
        "Nigga yo principal got emotional during a speach for all the freshmans boy, and hestarted loud micing the audience to get his point accross nigga 3/4th of theaudience walked out that bitch with hearing loss and ear barotrauma symptoms boyyou dumb as fuckNigga you was in a star wars roleplay game on roblox boy, and an administratorbanned you because you was roleplaying as Darth Vadar with a Jedi outft on niggayou dumb as fuckThat was ass nigga ya father raised you in an arabian desert boy you made a livingby training camals how to moon-walk nigga you stupid as fuckNigga ya mom was known back in 2018 because she was the best stripper in VRChat boyshe used to give discounts for her lapdances to whoever had the most expensive VRheadset nigga you stupid as fuckNigga that's why yo grandma gave you a life lesson on alcohol abuse boy, becauseshe caught you having a hangover inside of a bouncy house nigga you dumb as fuckNigga you tried to recreate the meatloaf from Johnny Test for a youtube video andgot 674 dislikes because you made them watch all 2 hours of the cooking processnigga you dumb as fuckNigga you met H2ODelirious in a GTA 5 Online server and he gave you a free farraribecause he felt bad that you died to a padestrian nigga you dumb as fuckNigga you was number 1 on the leaderboard in a agario server and got tricksplit bythe TYT clan nigga you stupid as shitNo nigga you ran away from home yesterday evening and got chased around yoneighborhood by an armadillo boy you stupid as fuckThat was ass nigga ya great great grandfather starred as the main antagonist in theMichael myers movie in 1981 boy you dumb as fuckNigga you was cutting yo toe nails and you was on the last toe and yo clippersbroke cuz yo toe nails got level 10 strength nigga")
    await asyncio.sleep(1)
    await ctx.send(
        "Nigga you literally have a signiature move in competitive pac-man tournaments boyand all you do is move your joy stick up and down 4 times and your pac-man justturns into a Pac-woman boy you dumb as fuck stop talking to meNo boy you literally have a special ability to control the temperature of tap waterjust by making contact with yo uvula nigga you're weird as fuck stop talking to meNigga you got hired to work with the teen titans just because you had the ultimateability to not shed tears when you cut onions nigga and they use you to makespecial meals nigga your retarded as shitNigga what you literally grew an instant boner when you was walking around in anabandoned jungle because yo horny ass thought the branches on the trees looked likeHorrible nigga that's why you and ya long lost puppy finally reunited witheachother for the first time in 6 years because you sold yo soul to the slender mandumb ass boy what are you talking about niggaNigga huh you just mad because the niggas that constructed your house were idiotsboy and they built a stair case in yo kitchen that went all the way through yo roofand into the clouds my nigga you dumb as shit you just mad cuz you aint got thestamina to climb that shit boyWhat boy you literally don't even drink Lemon-aid anymore because you deadassthought it was gonna give you lemon flavoured aids nigga you're actually dumb asfuck stop talking to meNigga you literally have a modded version of GTA 5 and whenever you get intoarguments with citizens boy ya character just start using shadow clone jutsuwithout using any hand signs boy you ugly as fuckNigga your family got mad and disowned you because you instantly win Monopolymatches because your negotiating skills are just too great boy what are you talkingaboutYou literally got hired by NASA because you had a special disease that allowed youto breath in space boy and 2 years later you took a DNA test and when you looked atthe feedback all you seen was you being 45.89% alien nigga")
    await asyncio.sleep(1)

@stselfbot.command(aliases=["stopstream", "stopplay", "stoplisten"])
async def stopactivity(ctx):
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stopactivity]''' + Fore.RESET)
    await ctx.message.delete()
    await stselfbot.change_presence(activity=None, status=discord.Status.dnd)

@stselfbot.command(aliases=["milanahametova", "milanah"])
async def milanaham(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Milana Hametova]''' + Fore.RESET)
    r = requests.get("https://stiscool.000webhostapp.com/webapi/milanahametova/get.php").json()
    await ctx.send(str(r['image']))

@stselfbot.command()
async def jerkoff(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Jerk off]''' + Fore.RESET)
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
    await message.edit(content='''
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
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [911]''' + Fore.RESET)
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
{abc}    :airplane::office: WATCH YO JET BRRO WATCH YO JET
''')
    await asyncio.sleep(2)
    await message.edit(content='''
        :exploding_head::skull::fire::fire_extinguisher:
        ''')

@stselfbot.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Minesweeper]''' + Fore.RESET)
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
async def id(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Id]''' + Fore.RESET)
    if user is None:
        user = ctx.author
    print(
        f'''[K]{Fore.BLUE} {user.name} user id is {user.id}, copied user id to your keyboard!''' + Fore.RESET)
    pyperclip.copy(f'''{user.id}''')

@stselfbot.command()
async def reverse(ctx, *, message):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Reverse]''' + Fore.RESET)
    message = message[::-1]
    await ctx.send(message)

@stselfbot.command()
async def shrug(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Shrug]''' + Fore.RESET)
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@stselfbot.command()
async def lenny(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Lenny]''' + Fore.RESET)
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@stselfbot.command()
async def tableflip(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Tableflip]''' + Fore.RESET)
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@stselfbot.command()
async def unflip(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Unflip]''' + Fore.RESET)
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@stselfbot.command()
async def bold(ctx, *, message):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Bold]''' + Fore.RESET)
    await ctx.send('**' + message + '**')

@stselfbot.command()
async def secret(ctx, *, message):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Secret]''' + Fore.RESET)
    await ctx.send('||' + message + '||')

@stselfbot.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Rolehexcode]''' + Fore.RESET)
    await ctx.send(f"{role.name} : {role.color}")

@stselfbot.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Gethwid]''' + Fore.RESET)
    print(f"HWID: {Fore.YELLOW}{hwid}" + Fore.RESET)

@stselfbot.command()
async def empty(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Empty]''' + Fore.RESET)
    await ctx.send(chr(173))

@stselfbot.command()
async def everyone(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Everyone]''' + Fore.RESET)
    await ctx.send('hey||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ @everyone')

@stselfbot.command()
async def logout(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Logout]''' + Fore.RESET)
    await stselfbot.logout()

@stselfbot.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Btcstream]''' + Fore.RESET)
    btc_status.start()

@stselfbot.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stealallpfp]''' + Fore.RESET)
    Dump(ctx)

@stselfbot.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cls]''' + Fore.RESET)
    Clear()
    startprint()

def time_convert(sec):
  sec = sec * 100000
  sec = round(sec)
  sec = sec / 100000
  ms = sec ** 100
  ms = ms % 100
  mins = sec // 60
  sec = sec % 60
  mins = mins % 60
  return (f"{int(mins)} minute(s) and {round(sec)} second(s) and {ms} miliseconds")

def calculate_pi(precision):
        getcontext().prec = precision
        res = Decimal(0)
        for i in range(precision):
            a = Decimal(1) / (16**i)
            b = Decimal(4) / (8 * i + 1)
            c = Decimal(2) / (8 * i + 4)
            d = Decimal(1) / (8 * i + 5)
            e = Decimal(1) / (8 * i + 6)
            r = a * (b - c - d - e)
            res += r
        return res

@stselfbot.command(aliases=['picalc', 'pi'])
async def calcpi(ctx, precision: int):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Calcpi]''' + Fore.RESET)
    if precision > 10000:
        precision = 10000
    elif precision == 1:
        await ctx.send("PI is 3")
        return
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Calculating pi, it will take a while.''' + Fore.RESET)
    t1 = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(calculate_pi, precision)
        while not future.done():
            await asyncio.sleep(1)
        res = future.result()
    dt = time.time() - t1
    endTime = time_convert(dt)
    res = str(res)
    stringLength = len(res)
    if stringLength <= 1999:
        await ctx.send(f"PI calculation took {endTime} and pi is {res}")
    else:
        max_index = 1800
        firstStringToSend = res[0:max_index]
        await ctx.send(f"PI calculation took {endTime} and pi is {firstStringToSend}")
        index = max_index
        while index < (stringLength - max_index): 
            secondIndex = index + max_index
            posted_string = res[index:secondIndex]
            await ctx.send(posted_string)
            index = index + max_index
        posted_string = res[index:stringLength]
        await ctx.send(posted_string)
    print(f"PI is {res}")

def primes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

@stselfbot.command(aliases=['primecalc', 'primes'])
async def calcprime(ctx, amount: int):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Calcprime]''' + Fore.RESET)
    t1 = time.time()
    q = ""
    for a in primes_sieve(int(amount)):
        q += f"{str(a)}, "
    dt = time.time() - t1
    print(q)
    print(f"Prime calculation took {time_convert(dt)}")
    stringLength = len(q)
    if stringLength <= 1999:
        await ctx.send(f"Prime calculation took {time_convert(dt)} and numbers are {q}")
    else:
        max_index = 1800
        firstStringToSend = q[0:max_index]
        await ctx.send(f"Prime calculation took {time_convert(dt)} and numbers are {firstStringToSend}")
        index = max_index
        while index < (stringLength - max_index): 
            secondIndex = index + max_index
            posted_string = q[index:secondIndex]
            await ctx.send(posted_string)
            index = index + max_index
        posted_string = q[index:stringLength]
        await ctx.send(posted_string)

@stselfbot.command()
async def youngsexy(ctx):
    young_dudes = [
    "https://tenor.com/view/hi-selfie-old-man-stare-serious-face-gif-17346629",
    "https://tenor.com/view/front-camera-selfie-what-old-man-gif-16684902",
    "https://tenor.com/view/tempranito-old-man-staring-gif-7973272",
    "https://tenor.com/view/old-man-front-cam-open-me-myself-and-i-black-and-white-gif-16411023",
    "https://tenor.com/view/black-gif-21508623",
    "https://tenor.com/view/black-gif-21481235",
    "https://tenor.com/view/black-man-staring-gif-22222579",
    "https://tenor.com/view/indian-man-rolls-eyes-funny-gorilla-gif-21725477",
    "https://cdn.discordapp.com/attachments/737379472625369169/1094020868432220220/image.png",
    "https://media.discordapp.net/attachments/570686290799099920/1094543031031562300/monkey.mp4"
    ]
    await ctx.send(random.choice(young_dudes))

@stselfbot.command(aliases=['markasread', 'ackall'])
async def readall(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Read all]''' + Fore.RESET)
    for UserGuild in stselfbot.guilds:
        readBool = False
        while not readBool:
            try:
                await UserGuild.ack()
                print(f"read all messages in {UserGuild.name}")
                await asyncio.sleep(10)
                readBool = True
            except:
                print("couldnt read due to rate limits")
                await asyncio.sleep(60)

@stselfbot.command()
async def changeactivity(ctx, typeOfIt, *text):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Change activity]''' + Fore.RESET)
    activityText = ' '.join(text)
    if typeOfIt.lower() == "streaming":
        theActivity = discord.Streaming(
            name=f"{activityText}",
            url="https://www.twitch.tv/imstcool",
        )
    elif typeOfIt.lower() == "playing":
        theActivity = discord.Game(
            name=f"{activityText}"
        )
    elif typeOfIt.lower() == "listening":
        theActivity = discord.Activity(
            type=discord.ActivityType.listening,
            name=f"{activityText}"
        )
    elif typeOfIt.lower() == "listening":
        theActivity = discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{activityText}"
        )    
    await stselfbot.change_presence(activity=theActivity)

@stselfbot.command()
async def nitro(ctx):  
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Nitro]''' + Fore.RESET)
    await ctx.send(Nitro())

realNitro = ["https://discord.gift/jrVPPaK7dB9HXawfPswz3uS9",
            "https://discord.gift/ZT9SjJmnZYmsydrwwwwJJC5A",
            "https://discord.gift/duHW5XPgE8AYsvWD2qCZ4EcH",
            "https://discord.gift/xD5eZY2aQFnaUwe9MYwkuzTE",
            "https://discord.gift/MFA9U7h44WnDBzmP5hkFyXjh",
            "https://discord.gift/6eyPp6m7NAfZ6dYn8TEZuRPG",
            "https://discord.gift/2UERBd9GxPqtXYKMXDYv9TF8",
            "https://discord.com/gifts/6eyPp6m7NAfZ6dYn8TEZuRPG",
            "https://discord.gift/EbnyrC9AT28mySmdpuwWTKA7"
]

@stselfbot.command()
async def realnitro(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Real Nitro]''' + Fore.RESET)
    await ctx.send(random.choice(realNitro))

@stselfbot.command()
async def edit(ctx, amount, *, textInput):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Edit]''' + Fore.RESET)
    async for message in ctx.channel.history(limit=int(amount)):
        try:
            await message.edit(content=textInput)
        except:
            pass

@stselfbot.command()
async def banner(ctx, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Banner]''' + Fore.RESET)
    if user == None:
        user = ctx.author
    user = await stselfbot.fetch_user(user.id)
    banner_url = user.banner
    if banner_url == None:
        print(f"{Fore.RED}[ERROR] {Fore.WHITE}User has no banner!" + Fore.RESET)
        return
    await ctx.send(await embedGen(ctx, f"{user.name}'s banner", "", "st's cool selfbot :3!!", banner_url))

@stselfbot.command()
async def stoptextppl(ctx):
    stoptextppl.has_been_called = True
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stop texting]''' + Fore.RESET)

stoptextppl.has_been_called = False

@stselfbot.command()
async def textppl(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Text people]''' + Fore.RESET)
    while True:
        cool123 = ['Hello!', "What's up guys?", 'Hi guys!', 'whats up chat', 'hey lol', 'hey chat']
        await ctx.send(random.choice(cool123))
        await asyncio.sleep(60)
        if stoptextppl.has_been_called:
            break

@stselfbot.command()
async def advice(ctx):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Advice]''' + Fore.RESET)
    r = requests.get('https://api.adviceslip.com/advice')
    await ctx.send(r.json()['slip']['advice'])

@stselfbot.command()
async def stopstreak(ctx):
    stopstreak.has_been_called = True
    pass
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Stopstreak]''' + Fore.RESET)

stopstreak.has_been_called = False

@stselfbot.command()
async def pingstreak(ctx, user: discord.User):
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Ping streak]''' + Fore.RESET)
    while True:
        timetosend = random.randint(3, 6)
        await ctx.send(user.mention)
        await asyncio.sleep(timetosend)
        print("sent ping in", timetosend, "seconds")
        if stopstreak.has_been_called:
            break

@stselfbot.command()
async def restart(ctx):
    await ctx.message.delete()
    print()
    print(f"{Fore.GREEN} Restarting the selfbot in 2 seconds!" + Fore.RESET)
    time.sleep(2)
    subprocess.call(["launch.bat"])
    sys.exit()

codeRegex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")
ready = False

if __name__ == '__main__':
    Init()

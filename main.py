import discord
import random
import json
import os
from keep_alive import keep_alive
import googletrans
from discord.ext import commands
import praw
import ffmpeg
import youtube_dl
import nacl

kugisaki = discord.Client()
kugisaki = commands.Bot(command_prefix="#")




reddit = praw.Reddit(client_id =os.getenv('id'),
                     client_secret=os.getenv('keyy'),
                     #u_name=os.getenv('namee'),
                     #pswdd=os.getenv('psed'),
                     user_agent="vivy" )
vivi = 1

@kugisaki.command()
async def LangList(ctx):
  await ctx.send("""'af' 'afrikaans'
  'sq' 'albanian'
   'am' 'amharic'
    'ar' 'arabic'
    'hy' 'armenian'
    'az' 'azerbaijani'
    'eu' 'basque'
    'be' 'belarusian'
    'bn' 'bengali'
    'bs' 'bosnian'
    'bg' 'bulgarian'
    'ca' 'catalan'
    'ceb' 'cebuano'
    'ny' 'chichewa'
    'zh-cn' 'chinese (simplified)'
    'zh-tw' 'chinese (traditional)'
    'co' 'corsican'
    'hr' 'croatian'
    'cs' 'czech'
    'da' 'danish'
    'nl' 'dutch'
    'en' 'english'
    'eo' 'esperanto'
    'et' 'estonian'
    'tl' 'filipino'
    'fi' 'finnish'
    'fr' 'french'
    'fy' 'frisian'
    'gl' 'galician'
    'ka' 'georgian'
    'de' 'german'
    'el' 'greek'
    'gu' 'gujarati'
    'ht' 'haitian creole'
    'ha' 'hausa'
    'haw' 'hawaiian'
    'iw' 'hebrew'
    'he' 'hebrew'
    'hi' 'hindi'
  """)

  await ctx.send(
    """
      'hmn' 'hmong'
    'hu' 'hungarian'
    'is' 'icelandic'
    'ig' 'igbo'
    'id' 'indonesian'
    'ga' 'irish'
    'it' 'italian'
    'ja' 'japanese'
    'jw' 'javanese'
    'kn' 'kannada'
    'kk' 'kazakh'
    'km' 'khmer'
    'ko' 'korean'
    'ku' 'kurdish (kurmanji)'
    'ky' 'kyrgyz'
    'lo' 'lao'
    'la' 'latin'
    'lv' 'latvian'
    'lt' 'lithuanian'
    'lb' 'luxembourgish'
    'mk' 'macedonian'
    'mg' 'malagasy'
    'ms' 'malay'
    'ml' 'malayalam'
    'mt' 'maltese'
    'mi' 'maori'
    'mr' 'marathi'
    'mn' 'mongolian'
    'my' 'myanmar (burmese)'
    'ne' 'nepali'
    'no' 'norwegian'
    'or' 'odia'
    'ps' 'pashto'
    'fa' 'persian'
    'pl' 'polish'
    'pt' 'portuguese'
    'pa' 'punjabi'
    'ro' 'romanian'
    'ru' 'russian'
    'sm' 'samoan'
    'gd' 'scots gaelic'
    'sr' 'serbian'
    'st' 'sesotho'
    'sn' 'shona'
    'sd' 'sindhi'
    'si' 'sinhala'
    'sk' 'slovak'
    'sl' 'slovenian'
    'so' 'somali'
    'es' 'spanish'
    'su' 'sundanese'
    'sw' 'swahili'
    'sv' 'swedish'
    'tg' 'tajik'
    'ta' 'tamil'
    'te' 'telugu'
    'th' 'thai'
    'tr' 'turkish'
    'uk' 'ukrainian'
    'ur' 'urdu'
    'ug' 'uyghur'
    'uz' 'uzbek'
    'vi' 'vietnamese'
    'cy' 'welsh'
    'xh' 'xhosa'
    'yi' 'yiddish'
    'yo' 'yoruba'
    'zu' 'zulu
    """
  )


@kugisaki.command(aliases=['anime'])
async def AnimeArt(ctx):
  async with ctx.typing():
    subreddit = reddit.subreddit("AnimeArt")
    all_subs = []
    top = subreddit.top(limit = 500)

    for submission in top:
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)


    url = random_sub.url

    em = discord.Embed()
    em.set_image(url = url )
    await ctx.send(embed = em)



@kugisaki.command(aliases=['meme'])
async def memes(ctx):
  async with ctx.typing():
    subreddit = reddit.subreddit("IndianDankMemes")
    all_subs = []
    top = subreddit.top(limit = 500)

    for submission in top:
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)


    url = random_sub.url

    em = discord.Embed()
    em.set_image(url = url )
    await ctx.send(embed = em)


@kugisaki.command()
async def memee(ctx):
  async with ctx.typing():
    subreddit = reddit.subreddit("Meme")
    all_subs = []
    top = subreddit.top(limit = 500)

    for submission in top:
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)


    url = random_sub.url

    em = discord.Embed()
    em.set_image(url = url )
    await ctx.send(embed = em)


@kugisaki.command(aliases=['nude'])
async def henati(ctx):
  async with ctx.typing():
    subreddit = reddit.subreddit("Hentai")
    all_subs = []
    top = subreddit.top(limit = 500)

    for submission in top:
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)


    url = random_sub.url

    em = discord.Embed()
    em.set_image(url = url )
    await ctx.send(embed = em)


@kugisaki.command(aliases=['nudes'])
async def echi(ctx):
  async with ctx.typing():
    subreddit = reddit.subreddit("Ecchi")
    all_subs = []
    top = subreddit.top(limit = 500)

    for submission in top:
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)


    url = random_sub.url

    em = discord.Embed()
    em.set_image(url = url )
    await ctx.send(embed = em)



@kugisaki.command()
async def test(ctx):
  async with ctx.channel.typing():
    await ctx.send("Command executed")




@kugisaki.command()
async def roles(ctx):
  await ctx.send("server roles-\n kamisama/神様/god-ANKIT\n Maō-sama/魔王様/demonLord-samudro and bhalu\n ningen/人間//human-EvryoneElse")

@kugisaki.command()
async def rules(ctx):
  await ctx.send("#####---RULES---##### \n 1) Imp rule be ready for sexy time \n 2) Nobody talk about 2 girl 1 cup video \n 3) Don't judge people , this is judgement free area \n 4) Banch0 jisne kartik ko faltu bola usko perma BAN ")

@kugisaki.command(aliases=['tr'])
async def translate(ctx, lang_to, *args):
    """
    Translates the given text to the language `lang_to`.
    The language translated from is automatically detected.
    """

    lang_to = lang_to.lower()
    if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
        raise commands.BadArgument("Invalid language to translate text to")

    text = ' '.join(args)
    translator = googletrans.Translator()
    text_translated = translator.translate(text, dest=lang_to).text
    await ctx.send(text_translated)


############################################################
####################---AUDIO_FEAUTRE___#####################
############################################################


@kugisaki.command()
async def playy(ctx):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='chillin')
  voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)
  await voiceChannel.connect()





@kugisaki.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            print("ok")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='chillin')
    await voiceChannel.connect()
    voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@kugisaki.command()
async def leave(ctx):
    voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@kugisaki.command()
async def pause(ctx):
    voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@kugisaki.command()
async def resume(ctx):
    voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@kugisaki.command()
async def stop(ctx):
    voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)
    voice.stop()











#######################################################################33
###################---list-----######################################3
############################################################3

name = [
    'gupta',
    'dog',
    'Gupta',
    'GUPTA',
    'dOG',
    'Dog',
]

cc = ['PARIVARIK', 'parivarik']
cc_reply = ['ja na chuttad', 'toh ab kya itni si baat pe gand maarega bc']

bh = ['bhalu', 'Bhalu', 'BHALU', 'Abhishek', 'ABHISHEK', 'abhishek']

vr = ['vridhi', 'VRIDHI', 'Vridhi', 'vridi', 'VRIDI', 'Vridi']
vr_reply = [
    'banchod  fir bhul gae tum esko', 'arey bancho h kya ye abhi tk',
    'he is busy snding insta reels'
]

name_reply = [
    'uske muh me lauda h vo busy h..',
    'he is busy sniffing his balls',
    'gand ke nashe kr rha h abhi vo',
    'bokachoda kha h',
    'apne hi muut pee rha h vo',
]
bh_reply = [
    'uske muh me lauda h vo busy h..', 'he is busy sniffing his balls',
    'gand ke nashe kr rha h abhi vo', 'bokachoda kha h', 'He is stalking Riya'
]

an = ['ankit', 'Ankit', 'ANKIT']

sas = [
    'aega koi', 'Aega', 'AEGA', 'GAME', 'game', 'Game', 'lodu', 'LODU', 'Ludo',
    'bakchodi', 'BAKCHODI', 'Bakchodi', 'bakchod', 'BAKCHOD', 'Bakchod'
    'Koi aa nhi rha kya aaj?', 'KOI AA ', 'Koi aa'
    'COME', 'Come', 'come', 'cum', 'Cum', 'CUM'
]

sas_reply = [
    "soo ja na bsdk", "kaam dhanda ni h tum pe", "cuming",
    'NOOOOOOOOOOOOOOOOOO', 'SEXXXX'
]

gali = [
    'bc', 'BC', 'bancho', 'BANCHO', 'banchod', 'bancho', 'Banchod', 'BANCHOD',
    'bokachoda', 'BOKACHODA', 'Bokachoda', 'lund', 'LUND', 'loda', 'Lund',
    'GAND', "Gand"
]


va=['vanshaj','vansh','Vanshaj','Vansh']
va_reply=['Vanshika mausi bol usse']
sa = ['Samudro', 'samudro']
sa_reply = ['yaahooo onii-sama', 'yamete kudasai captain-sama']

bot = [
    'bot', 'sexy_bot', 'Bot', 'SEXY', 'Bot', 'Sexy', 'BOT', 'sexy', '@sexy_bot'
]

bot_reply = [
    'kya chea trko...', 'aati kya khandala chikne', 'kya chea bancho trko',
    'yeasss', 'gand mara bokachoda',
    'i dont know wht u saying but i like sex ', 'i m watchinbg anal stuff DND'
]

vivy=['vivy','Vivy','VIVY','vivY']
vivy_reply=['YES! what can i do for you','did someone call me','wht u want asswipe','mera naam lene ki auakt h teri','bol be gandu','Tere gand ko hole smjhke maaru mai shot... Naam h mera vivy bot__bol ab kya chea']


ri = ['riya', 'RIYA', 'Riya']

ri_reply = [
    'arey shanti chli jaegi eske ate he', 'arey bol oi', 'arey chotu ki maa',
    'palnt animal ble h ye ', 'she in love with bhalu', 'bndRiya bol'
]

gm = ['pubg', 'Pubg', 'PUBG', 'ludo', 'Ludo']
gm_reply = [
    'pdh le bsdk', 'pehle sbka muh me leke naach ek baar',
    'apna kaam kr na bhadwe'
]

bb = ['moan']
bb_reply = ['vo muh me leta h uss time toh awaz nhi aata']

lol = ['naam', 'name']
lol_reply = [
    'Jugemu-jugemu Gokōnosurikire Kaijarisuigyo-no Suigyōmatsu Unraimatsu Fūraimatsu Kūnerutokoroni-sumutokoro Yaburakōjino-burakōji Paipopaipo-paiponoshūringan Shūringanno-gūrindai Gūrindaino-ponpokopīno-ponpokonāno Chōkyūmeino-chōsuke'
]

########################################################3
##############################################################3
##################################################################3

######################################################
#########################################################3
#3########################################################3


@kugisaki.event
async def on_ready():
    print('ONLIne as {0.user}'.format(kugisaki))





@kugisaki.event
async def on_message(message):
    await kugisaki.process_commands(message)
    if message.author == kugisaki.user:
        return
        

    msg = message.content

    if msg.startswith('$DEACTIVATE VIVI'):
        await message.channel.send('#--VIVI IS OFFLINE--#')
        await message.channel.send('#--password--#')
        
        
        
        global vivi
        vivi = 0

    if msg.startswith('$ACTIVATE VIVI'):
        await message.channel.send('#--VIVI IS ONLINE--#')

        vivi = 1

    if vivi == 1 :
        if msg.startswith('hi'):
            await message.channel.send('hey')

        #################---1
        if any(word in msg for word in gali):

            await message.channel.send(
                "######---PARIVARIK GROUP H YE KIRPYA KRKE GAND MASTI NA KRE---#########"
            )

        ##################---2

        if any(word in msg for word in vr):

            await message.channel.send(random.choice(vr_reply))

        ###############3-3

        if any(word in msg for word in sas):

            await message.channel.send(random.choice(sas_reply))

        ###############---4

        if msg.startswith('bakchodi'):
            await message.channel.send('arey bokachoda')

        ###############---5

        if msg.startswith('69'):
            await message.channel.send('shok badi cheez h')

        if msg.startswith('saxx' or 'sex'):
            await message.channel.send('ghante ke 100rs')

        if msg.startswith('Bol' or 'bol'):
            await message.channel.send(
                'jisne mujhe bulaya uske alawa sb bhosdiwale')

        if msg.startswith('shubham'):
            await message.channel.send('mutthal h saala')

        ###############---6
        if msg.startswith('Teri gaand' or 'tera gand'):
            await message.channel.send('muh me lega')

        if any(word in msg for word in an):
            await message.channel.send('he is watching hentai/sex stuff')

        #############-7

        #############--8

        if any(word in msg for word in name):

            await message.channel.send(random.choice(name_reply))

        #############--9

        if any(word in msg for word in bot):

            await message.channel.send(random.choice(bot_reply))

        ############-10

        if any(word in msg for word in ri):

            await message.channel.send(random.choice(ri_reply))

        ############-11

        if any(word in msg for word in bh):

            await message.channel.send(random.choice(bh_reply))

        if any(word in msg for word in bb):
            await message.channel.send(random.choice(bb_reply))

        #######-12

        if any(word in msg for word in sa):
            await message.channel.send(random.choice(sa_reply))

        ########-13
        if any(word in msg for word in gm):
            await message.channel.send(random.choice(gm_reply))

        ########-14
        if any(word in msg for word in lol):
            await message.channel.send(random.choice(lol_reply))

        ########-15
        if any(word in msg for word in cc):
            await message.channel.send(random.choice(cc_reply))
        
        ########-16
        if any(word in msg for word in vivy):
            await message.channel.send(random.choice(vivy_reply))
        ########-17
        if any(word in msg for word in va):
            await message.channel.send(random.choice(va_reply))

    else:
        return


keep_alive()

kugisaki.run(os.getenv('tk'))

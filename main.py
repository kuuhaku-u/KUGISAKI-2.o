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
import pyttsx3
import gtts  
from playsound import playsound  


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





########################################################################3
####################################################################3
###################################################################3



@kugisaki.command()
async def join(ctx):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='sexy_time')
  await voiceChannel.connect()
  voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)



@kugisaki.command()
async def spea(ctx):
  await ctx.send("This is a tts message", tts=True)


@kugisaki.command()
async def speak(ctx):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='sexy_time')
  await voiceChannel.connect()
  voice = discord.utils.get(kugisaki.voice_clients, guild=ctx.guild)
  voice.play(discord.FFmpegPCMAudio("hello.mp3"))
 

#######################################################################33
###################---list-----######################################3
############################################################3





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
                "######---PARIVARIK GROUP H YE ---#########"
            )

        ##################---2

        if any(word in msg for word in vr):

            await message.channel.send(random.choice(vr_reply))

        ###############3-3

        if any(word in msg for word in sas):

            await message.channel.send(random.choice(sas_reply))

        ###############---4

        

        ###############---5

      
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

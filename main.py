import discord
import random
import os
from keep_alive import keep_alive 

vivi = 0
kugisaki  = discord.Client()




#######################################################################33
###################---list-----######################################3
############################################################3

name = [
    'gupta', 'dog', 'Gupta', 'GUPTA', 
    'dOG', 'Dog',
]


cc = ['PARIVARIK','parivarik']
cc_reply = ['ja na chuttad','toh ab kya itni si baat pe gand maarega bc']


bh=['bhalu','Bhalu','BHALU','Abhishek','ABHISHEK','abhishek']

vr = ['vridhi', 'VRIDHI', 'Vridhi', 'vridi', 'VRIDI', 'Vridi']
vr_reply = [
    'banchod  fir bhul gae tum esko', 'arey bancho h kya ye abhi tk',
    'he is busy snding insta reels'
]

name_reply = [
    'uske muh me lauda h vo busy h..', 'he is busy sniffing his balls',
    'gand ke nashe kr rha h abhi vo', 'bokachoda kha h','apne hi muut pee rha h vo',
]
bh_reply = [
    'uske muh me lauda h vo busy h..', 'he is busy sniffing his balls',
    'gand ke nashe kr rha h abhi vo', 'bokachoda kha h','He is stalking Riya'
]

an=['ankit','Ankit','ANKIT']

sas = [
    'aega koi', 'Aega', 'AEGA', 'GAME', 'game', 'Game', 'lodu', 'LODU', 'Ludo','bakchodi','BAKCHODI','Bakchodi','bakchod','BAKCHOD','Bakchod'
    'Koi aa nhi rha kya aaj?', 'KOI AA ', 'Koi aa'
    'COME', 'Come', 'come', 'cum', 'Cum', 'CUM'
]

sas_reply = [
    "soo ja na bsdk", "kaam dhanda ni h tum pe", "cuming",
    'NOOOOOOOOOOOOOOOOOO', 'SEXXXX'
]

gali = [
    'bc', 'BC', 'bancho', 'BANCHO', 'banchod', 'bancho', 'Banchod', 'BANCHOD',
    'bokachoda', 'BOKACHODA', 'Bokachoda','lund','LUND','loda','Lund','GAND',"Gand"
]

sa = ['Samudro','samudro']
sa_reply = ['yaahooo onii-sama','yamete kudasai captain-sama']

bot = ['bot', 'sexy_bot','Bot','SEXY','Bot','Sexy','BOT', 'sexy', '@sexy_bot']


bot_reply = ['kya chea trko...','aati kya khandala chikne', 'kya chea bancho trko', 'yeasss', 'gand mara bokachoda','i dont know wht u saying but i like sex ','i m watchinbg anal stuff DND']


ri=['riya','RIYA','Riya']

ri_reply=['arey shanti chli jaegi eske ate he','arey bol oi','arey chotu ki maa','palnt animal ble h ye ','she in love with bhalu','bndRiya bol']

gm = ['pubg','Pubg','PUBG','ludo','Ludo']
gm_reply = ['pdh le bsdk', 'pehle sbka muh me leke naach ek baar','apna kaam kr na bhadwe']

bb = ['moan']
bb_reply = ['vo muh me leta h uss time toh awaz nhi aata']

lol = ['naam','name']
lol_reply = ['Jugemu-jugemu Gokōnosurikire Kaijarisuigyo-no Suigyōmatsu Unraimatsu Fūraimatsu Kūnerutokoroni-sumutokoro Yaburakōjino-burakōji Paipopaipo-paiponoshūringan Shūringanno-gūrindai Gūrindaino-ponpokopīno-ponpokonāno Chōkyūmeino-chōsuke']


########################################################3
##############################################################3
##################################################################3






@kugisaki.event
async def on_ready():
  print('ONLIne as {0.user}'.format(kugisaki))


@kugisaki.event
async def on_message(message):
  if message.author == kugisaki.user:
    return

  msg = message.content
  
  if msg.startswith('$ACTIVATE VIVI'):
    await message.channel.send('#--VIVI IS ONLINE--#')
    


  if msg.startswith('$DEACTIVATE VIVI'):
    await message.channel.send('#--VIVI IS OFFLINE--#')
    global vivi
    vivi=1



  if vivi==0:
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
                await message.channel.send('jisne mujhe bulaya uske alawa sb bhosdiwale')
                
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
              await message.channel.send (random.choice(sa_reply))
              
            ########-13
    if any(word in msg for word in gm):
              await message.channel.send (random.choice(gm_reply))
              
            ########-14
    if any(word in msg for word in lol):
              await message.channel.send (random.choice(lol_reply))
              
            ########-15
    if any(word in msg for word in cc):
                await message.channel.send(random.choice(cc_reply))


               

    


  else:
    return



keep_alive()

kugisaki.run(os.getenv('tk'))


  




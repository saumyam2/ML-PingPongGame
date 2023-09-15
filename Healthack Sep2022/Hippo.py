tkn = "MTAyMDQ2MzAyMjQ2NjE0MjI2MA.GeUwub.vWPdTk0bXKlywBVJXiOrDRUrYalJx5mbVI2uwM"
import interactions as inta
from interactions import ButtonStyle
import csv
import random as ran
from discord import Embed
bot = inta.Client(token=tkn)
weird_links = ["https://youtu.be/odADwWzHR24?t=23","https://youtu.be/RE3ttI6U4IU?t=202","https://youtu.be/RE3ttI6U4IU?t=202","https://youtu.be/0QXmmP4psbA","https://youtu.be/RE3ttI6U4IU?t=22","https://youtu.be/HneFe-mGPfI?t=60","https://youtu.be/CM_ZDGorTn8","https://youtu.be/B077Cn9wJ1A","https://youtu.be/EW06sG8EeHY","https://youtu.be/xsEJ6GeAGb0","https://youtu.be/J_ii4gs6niQ","https://youtu.be/D5dVoAWBOpQ","https://youtu.be/F0Z63hVvMUM","https://youtu.be/dxGU80Ny0JQ","https://youtu.be/ovysKeX-4Vo","https://youtu.be/jVA-tr_euKU","https://youtu.be/t5ECa0-MXxk","https://youtu.be/GN6FopLHVtk","https://youtu.be/BPaYNAXsNmE","https://youtu.be/WiTgn5QH_HU","https://youtu.be/Yv6US-yhPxM","https://youtu.be/7bkgWwRXkgk","https://youtu.be/cPQgG29pT_4","https://youtu.be/Upp2w3RYEww",""]
websites=["https://os.me/community/self/what-should-i-do-if-i-am-feeling-sad/","https://www.instagram.com/realdepressionproject/?hl=en","https://nimhans.ac.in/pssmhs-helpline/","https://www.thelivelovelaughfoundation.org/helpline","https://icallhelpline.org/","https://www.limitless.sg/talk?gclid=Cj0KCQjwvZCZBhCiARIsAPXbajvwTDGfuBRCIvW-rH8orlnUFwn1vFDdf73zPEutroXWfel1Bpi4Ra4aAjQgEALw_wcB","https://gng.org/seat-at-the-table/?utm_term=talk%20to%20someone&utm_campaign=Seat+At+The+Table&utm_source=adwords&utm_medium=ppc&hsa_acc=9691649620&hsa_net=adwords&hsa_grp=122260247700&hsa_ver=3&hsa_kw=talk%20","https://content.gng.org/mentalandemotionalwellbeingconvo?utm_term=mental%20health&utm_campaign=Seat_At_The_Table_Mental_Emotional_Wellbieng&utm_source=adwords&utm_medium=ppc&hsa_acc=9691649620&hsa_net=adwords&hsa_grp=146849857371&hsa_ver=3&hsa_kw=mental%20health&hsa_tgt=kwd-11488156&hsa_mt=b&hsa_ad=621261246406&hsa_src=g&hsa_cam=18307229191&gclid=Cj0KCQjwvZCZBhCiARIsAPXbajvjaDpgvAZhoA6rndFtPQwtOnSXJLUFxam-4IeRZFv2oDsGLa11J6saAjLNEALw_wcB","https://blog.gratefulness.me/20-affirmations-to-say-to-yourself-when-you-need-support/"]
@bot.event()
async def on_ready():
    print("Hippo-man Online")

@bot.command()
async def web(ctx:inta.CommandContext):
    button1 = inta.Button(
        style=ButtonStyle.SUCCESS,
        custom_id="yay",
        label=":D",
    )
    
    button2 = inta.Button(
        style =ButtonStyle.DANGER,
        custom_id='sed',
        label='-_-'
    )
    
    
    action_row = inta.ActionRow(components=[button1,button2])
    await ctx.send("Here's some satisfying and informative content for you!")
    await ctx.send(ran.choice(websites), components=action_row)
@bot.command()
async def video(ctx:inta.CommandContext):
    button1 = inta.Button(
        style=ButtonStyle.SUCCESS,
        custom_id="yay",
        label=":D",
    )
    
    button2 = inta.Button(
        style =ButtonStyle.DANGER,
        custom_id='sed',
        label='-_-'
    )
    
    
    action_row = inta.ActionRow(components=[button1,button2])
    await ctx.send("Here's some satisfying and informative content for you!")
    await ctx.send(ran.choice(weird_links), components=action_row)
@bot.command()
async def hello(ctx:inta.CommandContext):
    await ctx.send("Welcome to the community :) ")
    await ctx.author.send("**Kindly take this quick Personality test to understand yourself better >_<\n**https://www.16personalities.com/free-personality-test")

@bot.component("yay")
async def success_component(ctx:inta.ComponentContext):
    await ctx.send("Thank you for the upvote :smile:", ephemeral=True)
    
@bot.component("sed")
async def danger_component(ctx:inta.ComponentContext):
    await ctx.send("We are sorry to know you had a bad episode with us, we hope the next one will be better! :cry:", ephemeral=True)
    button1 = inta.Button(
        style=ButtonStyle.SUCCESS,
        custom_id="yay",
        label=":D",
    )
    
    button2 = inta.Button(
        style =ButtonStyle.DANGER,
        custom_id='sed',
        label='-_-'
    )
    action_row = inta.ActionRow(components=[button1,button2])
    await ctx.send("Here's some satisfying and informative content for you!")
    await ctx.send(ran.choice(weird_links), components=action_row)
bot.start()

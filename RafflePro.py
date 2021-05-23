import discord
from discord.ext import commands
import time
import os
from discord.utils import get 

mainbot = commands.Bot(command_prefix = "-")
mainbot.remove_command("help")


@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def send(ctx,*,channel_id):
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))
  
  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please type what would you like to send")


  msg = await mainbot.wait_for("message", check=check)

  msg = str(msg.content)

  if msg.lower().strip() == "stop":
    return

  
  await ctx.send(msg)

  time.sleep(1.5)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")

  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm.lower().strip() == "stop":
    return

  else:

    if msg_confirm == "yes":
      await ctx.send("sent to <#"+ channel_id + ">")
      await channel.send(msg) 


    else:
      await ctx.send("Reverted")
      return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def edit(ctx,*,channel_id):

    channel_id = channel_id.replace("#","").replace("<","").replace(">","")
    channel = mainbot.get_channel(int(channel_id))

    channelIdOfMessage = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

    await ctx.send("What is id of the message you would like to edit")

    responseMessageID = await mainbot.wait_for("message", check=check)
    responseMessageID = int(responseMessageID.content)


    await ctx.send("Please send the edited message")

    responseEditContent = await mainbot.wait_for("message", check=check)
    responseEditContent = str(responseEditContent.content)

    await ctx.send(responseEditContent)
    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")

    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()


    if msg_confirm == "yes":
        await ctx.send("Edited the message in <#"+ str(channel_id) + ">")

        msg = await channelIdOfMessage.fetch_message(responseMessageID)
        await msg.edit(content=responseEditContent)


    else:

        await ctx.send("Reverted")
        return
                
@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def sendlink(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()
  


  await ctx.send("What is the title of the embed?")


  msg = await mainbot.wait_for("message", check=check)
  msg = str(msg.content)


  await ctx.send("Please provide the file link")


  msg_link = await mainbot.wait_for("message", check=check)
  msg_link = str(msg_link.content)


  await ctx.send("Would you like an image? 'yes' to continue. Anything else will mean no images")


  msg_image_confirm = await mainbot.wait_for("message", check=check)
  msg_image_confirm = str(msg_image_confirm.content)


  embed=discord.Embed(title=msg, description=f"[Click here]({msg_link})")

  if msg_image_confirm.lower().strip() == "yes":
    await ctx.send("Please provide image link")

    msg_image = await mainbot.wait_for("message", check=check)
    msg_image = str(msg_image.content)
    
    
    embed.set_thumbnail(url = msg_image)

    await ctx.send(embed=embed)

    time.sleep(2)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

      await ctx.send("sent to <#"+ channel_id + ">")
      await channel.send(embed=embed) 
    
    
    else:

      await ctx.send("Reverted")
      return

  else:
    await ctx.send(embed=embed)
    time.sleep(2)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")

    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

      await ctx.send("sent to <#"+ channel_id + ">")
      await channel.send(embed=embed) 
    
    
    else:

      await ctx.send("Reverted")
      return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def raffle(ctx,*,channel_id):
  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please type what would you like to send")

  msg = await mainbot.wait_for("message", check=check)
  msg = str(msg.content)

  await ctx.send(msg)

  time.sleep(1.5)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")

  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm.lower().strip() == "stop":
    return

  else:

    if msg_confirm == "yes":
      await ctx.send("sent to <#"+ channel_id + ">")


      theMsg = await channel.send(msg) 
      await theMsg.add_reaction(u"\u2705")


    else:
      await ctx.send("Reverted")
      return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def jdsportsuk(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")

  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'JD Sports UK', description=f"**Region**\n :flag_gb:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://uploads.prod01.london.platform-os.com/instances/351/assets/images/store_images/JD%20Sports/JD%20Sports_2.jpg?updated=1587557520")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='- FCFS so enter ASAP\n- Add multiple emails to your paypal accounts\n- Utilise guest paypal checkout\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def jdsportsbe(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")

  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'JD Sports BE', description=f"**Region**\n :flag_be:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://uploads.prod01.london.platform-os.com/instances/351/assets/images/store_images/JD%20Sports/JD%20Sports_2.jpg?updated=1587557520")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='- FCFS so enter ASAP\n- Add multiple emails to your paypal accounts\n- Utilise guest paypal checkout\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def jdsportsfr(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")

  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'JD Sports FR', description=f"**Region**\n :flag_cp:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://uploads.prod01.london.platform-os.com/instances/351/assets/images/store_images/JD%20Sports/JD%20Sports_2.jpg?updated=1587557520")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='- FCFS so enter ASAP\n- Add multiple emails to your paypal accounts\n- Utilise guest paypal checkout\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def jdsportsnl(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")

  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'JD Sports NL', description=f"**Region**\n :flag_nl:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://uploads.prod01.london.platform-os.com/instances/351/assets/images/store_images/JD%20Sports/JD%20Sports_2.jpg?updated=1587557520")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='- FCFS so enter ASAP\n- Add multiple emails to your paypal accounts\n- Utilise guest paypal checkout\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def jdsportses(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")

  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'JD Sports ES', description=f"**Region**\n :flag_es:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://uploads.prod01.london.platform-os.com/instances/351/assets/images/store_images/JD%20Sports/JD%20Sports_2.jpg?updated=1587557520")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='- FCFS so enter ASAP\n- Add multiple emails to your paypal accounts\n- Utilise guest paypal checkout\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def jdsportsde(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")

  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'JD Sports DE', description=f"**Region**\n :flag_de:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://uploads.prod01.london.platform-os.com/instances/351/assets/images/store_images/JD%20Sports/JD%20Sports_2.jpg?updated=1587557520")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='- FCFS so enter ASAP\n- Add multiple emails to your paypal accounts\n- Utilise guest paypal checkout\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def footpatrol(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")

  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'Footpatrol', description=f"**Region**\n :flag_gb:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://m.footpatrol.com//skins/footpatrolgb-mobile/public/img/icons/app/favicon-192x192.png")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout\n:white_check_mark:Payment Hold')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Use each postcode once\n- Use local addresses to redirect with DPD\n- Utilise guest paypal checkout\n- Put the email you entered with as the guests checkout email\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def thehipstore(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'The Hip Store', description=f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://www.raffle-sneakers.com/wp-content/uploads/2020/03/thehiphopstore.jpg")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:white_check_mark:Paypal Checkout\n:white_check_mark:Payment Hold')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Use each postcode once\n- Use local addresses to redirect with DPD\n- Utilise guest paypal checkout\n- Put the email you entered with as the guests checkout email\n- Use random phone numbers')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def footpatrolinstorefr(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'Footpatrol Instore FR', description=f"**Region**\n :flag_fr:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://m.footpatrol.com//skins/footpatrolgb-mobile/public/img/icons/app/favicon-192x192.png")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x: Payment Hold')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Use multiple names\n- Use random phone numbers\n- Make typos in your name to increase entries (Risky)')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def footpatrolinstoreuk(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'Footpatrol Instore UK', description=f"**Region**\n :flag_gb: :handshake:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://m.footpatrol.com//skins/footpatrolgb-mobile/public/img/icons/app/favicon-192x192.png")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x: Payment Hold')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Use multiple names\n- Use random phone numbers\n- Make typos in your name to increase entries (Risky)')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def footshop(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")


  raffle_link = await mainbot.wait_for("message", check=check)
  raffle_link = str(raffle_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)


  embed=discord.Embed(title=f'Footshop', description=f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {raffle_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://media.glassdoor.com/sqll/1805993/footshop-squarelogo-1522228062767.png")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:white_check_mark: Instagrams \n:white_check_mark:Unique Cards')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Use each card once\n- Unique addresses\n- Spread your entries / high delays 800s')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def naked(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")


  raffle_link = await mainbot.wait_for("message", check=check)
  raffle_link = str(raffle_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)


  embed=discord.Embed(title=f'Naked', description=f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {raffle_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://pbs.twimg.com/profile_images/582179018419482624/RppHUjBa.jpg")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':white_check_mark: Accounts \n:white_check_mark: Instagrams \n:x:Unique Cards')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Add address to all accounts\n- Use girls names\n- Match the address of account to the one entered')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def stress(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")


  raffle_link = await mainbot.wait_for("message", check=check)
  raffle_link = str(raffle_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)


  embed=discord.Embed(title=f'Stress 95', description=f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {raffle_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://pbs.twimg.com/profile_images/1036960222663860229/9k17siNE_400x400.jpg")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':white_check_mark: Accounts \n:white_check_mark: Instagrams \n:x: Unique Cards \n:x: Pre payment')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Add address to all accounts\n- Use nordic names\n- Match the address of account to the one entered')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def bstn(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'BSTN', description=f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://www.raffle-sneakers.com/wp-content/uploads/2020/03/bstn.jpg")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x: Payment Hold')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 2 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Quality > Quantity\n- Confirm entries with same IP\n- Confirm entries ASAP\n- If you win, go for the same size in future with that specific profile')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def einhalb(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle link")


  raffle_link = await mainbot.wait_for("message", check=check)
  raffle_link = str(raffle_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)


  embed=discord.Embed(title=f'43 Einhalb', description=f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {raffle_link}\n\n**Closes**\n {close_time}")
  embed.set_thumbnail(url = "https://pbs.twimg.com/profile_images/434946346513354752/nxZQYUzE.jpeg")

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")
  embed.add_field(name='**Requirements** :pencil:', value=':x: Accounts \n:white_check_mark: Instagrams \n:x: Unique Cards \n:x: Pre payment')
  embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')  
  embed.add_field(name='**Tips** :pencil:', value='\n- Hard j!g addresses\n- Make paypal and email match\n- You can add the winning paypal to your account once you have won\n- The more entries the better')


  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def backdoorbottega(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f'Back Door Bottega',
        description=
        f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://scontent-bru2-1.xx.fbcdn.net/v/t31.18172-8/22519892_1556997187700219_79061155418646292_o.png?_nc_cat=105&ccb=1-3&_nc_sid=973b4a&_nc_ohc=3muoBQWdbVoAX-Lekok&_nc_ht=scontent-bru2-1.xx&oh=230acfa187731c75d5c525514acc99f9&oe=60AB60AD"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':white_check_mark: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :white_check_mark: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 2 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- Use each postcode once\n- Use each credit card once\n- Use random phone numbers'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def bigairlab(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f'Big Air Lab',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/773285214318362624/801592833072824330/unknown.png?width=470&height=416"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- Quality > Quantity\n- Use the data generator in the tools section on the bot for random birthdays\n- Use random phone numbers'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def cactusplantfleamarket(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f'Cactus Plant Flea Market',
        description=
        f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://i.pinimg.com/originals/0e/17/2f/0e172f159256ff1ec6c38871ceebd356.png"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- Quality > Quantity\n- Use random phone numbers'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def commonwealthph(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f'Commonwealth PH',
        description=
        f"**Region**\n :flag_ph:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/EP_NKvPtrDFqEgVD2YnVzSDWW47DQui3xQEk4kn1FUk/https/pbs.twimg.com/profile_images/1172057210173526016/ZqF2Ubob.jpg?width=360&height=360"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':white_check_mark: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 2 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- Quality > Quantity\n- Use philipine phone numbers'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def dsml(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' DSM London',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/m3KlO6LeFFZkxtmffGjG5KteMVm1neEbkkCDU9D2rc4/https/images-ext-1.discordapp.net/external/1E6p9ewNeVCSald6JolniLHnHAm2zYo6IgTWx2IHJz4/https/thedropdate-media.s3.amazonaws.com/uploads/2018/05/FEAT-IMAGE-25.png?width=495&height=495"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- Enter as fast a possible\n- Use random phone numbers\n- Use random addresses '
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def junkyard(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Junkyard',
        description=
        f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/5sS3CxkqyQDEIIRByO8wY6MSafhej8XfEYCA95uCZi4/https/pbs.twimg.com/profile_images/466571607469613056/9UyI0VXt_400x400.jpeg?width=360&height=360"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 2 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays '
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def maha(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Maha',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/-auB4DiZSa0RAWEJN-UEzapYdK6yJd0Vhqi9E-VJx0s/https/i4.sndcdn.com/avatars-XIAMNs5LPWV2iRwj-SNwa5A-t500x500.jpg?width=450&height=450"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity '
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def noirfonce(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Noirfonce',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/Y5JZEDceispymQ0tmCW8o55nGL52ad_nXARYtL1lO28/https/pbs.twimg.com/profile_images/732903169311813633/PGEXEQq7_400x400.jpg?width=360&height=360"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity '
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def obd(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' One Block Down',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/1x55MyqhwI5MHdcW-ZwQgcC2csso4Qrbrn17bjuvG_s/https/www.fashionsauce.com/img/stores/one-block-down.jpg?width=270&height=270"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity '
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def patta(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Patta',
        description=
        f"**Region**\n :flag_nl:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/NUrJRHXHQUh2CjooBweHNfy0AmMvJi-Zn7AidSSBVck/%3Fe%3D2159024400%26v%3Dbeta%26t%3DKbB26RZ_Idfh2jQAFpcIbAWa9vlP474seQG2vZcxwB8/https/media-exp1.licdn.com/dms/image/C4E0BAQHYB-iO4I6EbQ/company-logo_200_200/0/1519863796164?width=180&height=180"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 2 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity\n- use birthday generator in tools! '
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def prodirect(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Pro Direct',
        description=
        f"**Region**\n :flag_gb:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/773285214318362624/789618809002131486/AAUvwngWTyroOAzJGg2lVMEcHJaoE3Sh9Aq0RX-BKHqo1Qs900-c-k-c0x00ffffff-no-rj.png?width=676&height=676"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity\n- use birthday generator in tools! '
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def shuzulab(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Shuzu Lab',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/773285214318362624/808508656785948722/shuzu.png?width=202&height=202"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':white_check_mark: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def soft(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' SOTF',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/8k5RwUjcS2YTq2lJZ0WIatUVH4GfBhQFMYy9qCDbri0/%3Fq%3Dtbn%3AANd9GcS74zr7-OWnv9Fsj5qVkH0EsFSml4MUS4YwUA%26usqp%3DCAU/https/encrypted-tbn0.gstatic.com/images?width=202&height=202"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def streetmachine(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Street Machine',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/J5Z8hF3KFZSLOBLvrG84ydG0kYOqnvu7rlceNmHiwag/https/fizzymag.com/uploads/fizzypage/logo/14/streetmachine-streetwear-workwear.jpg?width=676&height=676"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':white_check_mark: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 2 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def thenextdoor(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' The Next Door',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/B2Nm2PCWHxcoSAYNGR1GXsDWVytSmuiCucAVS0Mo6A0/%3Fq%3Dtbn%3AANd9GcT2vdw6muZ3XE-XHnRHh91NcC1OkaJPhjfw9Q%26usqp%3DCAU/https/encrypted-tbn0.gstatic.com/images?width=202&height=202"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':white_check_mark: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def travisscott(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Travis Scott',
        description=
        f"**Region**\n :flag_us:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/dnsFDhg5J5T2DK8v06l_0SNPY1v4BxAScCb7KJamm7o/%3Fq%3Dtbn%3AANd9GcTrifsArCS7iUD1yGZNiXc1dFQvx_aDjXiU8w%26usqp%3DCAU/https/encrypted-tbn0.gstatic.com/images?width=226&height=181"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def tresbien(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' Tres Bien',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/mmH5-Cs1HYJqPd5WzqgrkusJGPMBhRtpfwKgrn3ZGMw/%3Fw%3D850/https/i0.wp.com/s3.store.hypebeast.com/media/wiki/fixtures/brand/Tr%25C3%25A8s%2520Bien.jpeg?width=676&height=676"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x: Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def voostore(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f'Voostore',
        description=
        f"**Region**\n :flag_eu:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/3F4vpsRWxzasnW2FqVom2ObBYhdztjr2e3C-qTsI_zE/https/pbs.twimg.com/profile_images/844221441008635906/Wsu_RxHZ.jpg?width=461&height=461"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:x: Instagrams \n:x: Paypal Checkout\n:x: Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def yme(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f' YME',
        description=
        f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/O3r4eGrVeR5SXoG1DpoKv_Yho99sGZ_UqAJHSrqxceI/https/pbs.twimg.com/profile_images/1063180550339477505/Eyracvns.jpg?width=461&height=461"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':white_check_mark: Accounts \n:white_check_mark: Instagrams \n:x: Paypal Checkout\n:x:Payment Hold\n :x: Credit Cards' 
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 3 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- use high delays\n- quality > quantity'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def kickz(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f'Kickz',
        description=
        f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://kickz.akamaized.net/media/images/landingpages/BUREAU-BORSCHE/KICKZ_400x200_Logo2000.jpg"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':x: Accounts \n:white_check_mark: Instagrams \n:white_check_mark:Paypal Checkout\n:white_check_mark:Payment Hold'
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- Use real address only\n- Utilise guest paypal checkout\n- Put the email you entered with as the guests checkout email\n- Use regional link'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return

@mainbot.command()
@commands.has_any_role('Owners', "Support")
async def kith(ctx, *, channel_id):

    await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

    channel_id = channel_id.replace("#", "").replace("<", "").replace(">", "")
    channel = mainbot.get_channel(int(channel_id))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
        ).strip()

    await ctx.send("Please provide the raffle link")

    stockx_link = await mainbot.wait_for("message", check=check)
    stockx_link = str(stockx_link.content)

    await ctx.send("Please provide the closing date and time")

    close_time = await mainbot.wait_for("message", check=check)
    close_time = str(close_time.content)

    embed = discord.Embed(
        title=f'Kith',
        description=
        f"**Region**\n :globe_with_meridians:\n\n**Raffle URL**\n {stockx_link}\n\n**Closes**\n {close_time}"
    )
    embed.set_thumbnail(
        url=
        "https://images-ext-2.discordapp.net/external/Mr6EBFMwG_69RYGvoLxdFrjrpsyuO_zDB0tQwUZuQqA/%3Fe%3D2159024400%26v%3Dbeta%26t%3DF-KqgYZerGxG2Bgmo5gKVEApxItmcKAjFwaCHc3_cVs/https/media-exp1.licdn.com/dms/image/C4E0BAQEkAAH_3b6sNw/company-logo_200_200/0/1519865047124?width=180&height=180"
    )

    embed.set_footer(
        text="Powered by RafflePro",
        icon_url=
        "https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png"
    )
    embed.add_field(
        name='**Requirements** :pencil:',
        value=
        ':white_check_mark: Accounts \n:x: Instagrams \n:x:Paypal Checkout\n:x:Payment Hold'
    )
    embed.add_field(name='**Raffle Tier :trophy:**', value='Tier 1 Raffle')
    embed.add_field(
        name='**Tips** :pencil:',
        value=
        '\n- Create accounts with random addresses\n-  Use UK, FR or DE addresses\n- If you win, you can change address'
    )

    time.sleep(2)

    await ctx.send(embed=embed)

    await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel"
                   )
    msg_confirm = await mainbot.wait_for("message", check=check)
    msg_confirm = str(msg_confirm.content).lower().strip()

    if msg_confirm == "yes":

        await ctx.send("sent to <#" + channel_id + ">")
        theMsg = await channel.send(embed=embed)
        await theMsg.add_reaction(u"\u2705")

    else:

        await ctx.send("Reverted")
        return
        
@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def newrelease(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the item name")


  item_name = await mainbot.wait_for("message", check=check)
  item_name = str(item_name.content)

  await ctx.send("Please provide the StockX link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide a PNG discord url of the item")

  img = await mainbot.wait_for("message", check=check)
  img = str(img.content)


  embed=discord.Embed(title=f'{item_name}', description = f"**Resell Value** :chart_with_upwards_trend: \n [StockX]({stockx_link})")
  embed.set_thumbnail(url = img)

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")

  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def randomrelease(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the item name")

  item_name = await mainbot.wait_for("message", check=check)
  item_name = str(item_name.content)

  await ctx.send("Please provide the StockX link")

  stockx_link = await mainbot.wait_for("message", check=check)
  stockx_link = str(stockx_link.content)

  await ctx.send("Please provide a PNG discord url of the item")

  img = await mainbot.wait_for("message", check=check)
  img = str(img.content)

  await ctx.send("Please provide the stores name")

  store = await mainbot.wait_for("message", check=check)
  store = str(store.content)

  await ctx.send("Please provide the stores image")

  store_img = await mainbot.wait_for("message", check=check)
  store_img = str(store_img.content)

  await ctx.send("Please provide the raffle link")

  raffle_link = await mainbot.wait_for("message", check=check)
  raffle_link = str(raffle_link.content)

  await ctx.send("Please provide the closing date and time")


  close_time = await mainbot.wait_for("message", check=check)
  close_time = str(close_time.content)

  embed=discord.Embed(title=f'{item_name}', description = f"**{store}**\n\n**Raffle Link**\n**{raffle_link}**\n\n**Resell Value** :chart_with_upwards_trend: \n [StockX]({stockx_link})")

  embed.set_thumbnail(url = store_img)
  embed.set_image(url = img)
  embed.add_field(name='**Closing Date**', value=close_time)

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")

  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def botstatus(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

  channel_id = channel_id.replace("#","").replace("<","").replace(">","")
  channel = mainbot.get_channel(int(channel_id))

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower().strip()

  await ctx.send("Please provide the raffle status")

  rafflestatus = await mainbot.wait_for("message", check=check)
  rafflestatus = str(rafflestatus.content)

  await ctx.send("Please provide the generator status")

  generatorstatus = await mainbot.wait_for("message", check=check)
  generatorstatus = str(generatorstatus.content)

  await ctx.send("Please provide the tool status")

  toolstatus = await mainbot.wait_for("message", check=check)
  toolstatus = str(toolstatus.content)

  embed=discord.Embed(title=f'RafflePro Feature Status', description = f"Here is the status of all Raffles / Generators / Tools")

  embed.add_field(name='**Raffle Status**', value=rafflestatus)
  embed.add_field(name='**Generator Status**', value=generatorstatus)
  embed.add_field(name='**Tool Status**', value=toolstatus)

  embed.set_footer(text="Powered by RafflePro",icon_url="https://cdn.discordapp.com/attachments/773644857004523530/773644903443464262/RafflePro4300.png")

  time.sleep(2)

  await ctx.send(embed=embed)

  await ctx.send("\n\nConfirm this by saying 'yes' anything else will cancel")
  msg_confirm = await mainbot.wait_for("message", check=check)
  msg_confirm = str(msg_confirm.content).lower().strip()

  if msg_confirm == "yes":

    await ctx.send("sent to <#"+ channel_id + ">")
    theMsg = await channel.send(embed=embed)
    await theMsg.add_reaction(u"\u2705")
    
    
  else:

    await ctx.send("Reverted")
    return

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def archiveChannel(ctx):
  channel = ctx.channel

  B = discord.utils.get(ctx.guild.channels, name= "archives")
  await ctx.channel.edit(category=B)

@mainbot.command()
@commands.has_any_role('Owners',"Support")
async def releasesChannel(ctx):
  channel = ctx.channel

  B = discord.utils.get(ctx.guild.channels, name= "Releases")
  await ctx.channel.edit(category=B)


raffle_links_eu = 773276599399219281
channelIds = [raffle_links_eu]
client = discord.Client()


@client.event
async def on_message(message):
    ping = get(message.guild.roles, name = 'Support')

    webhooks = message.embeds 
    wordsInEmbed = []
    if message.channel.id == raffle_links_eu:
        for webhook in webhooks:
            theWebhookMessage = webhook.to_dict()
            webhookValues = theWebhookMessage.values()

            for embed in webhookValues:
                if (type(embed) == list):

                    for field in embed:
                        fieldValues = field.values()

                    for text in fieldValues:
                        wordsInEmbed.append(text)

                else:
                    wordsInEmbed.append(embed)

    keywords = ['Footpatrol','Maha', 'NakedCPH', 'OneBlockDown' , 'Soto', 'Sotf', 'VooStore' , 'Kith', 'BSTN' , 'Big Air Lab', 'Noirfonce', 'TheNextDoor' , 'Très Bien' , '43Einhalb', 'YME', 'Stress95', 'JD Sports', 'Backdoor', 'Pro Direct', 'Patta']
  
    if any(word in keywords for word in wordsInEmbed):
        await message.channel.send(ping.mention)

token_test = "NzE0MDgzODU1MjU0MDI4MzA4.Xspgag.Uof1FspmtRqpQpHAnYboMZLyDXw"
token_RP = "NzA5OTQ0OTkwNzE2OTE5ODA4.XrtRyw.y8h1zgO-qg63x2d17dLkjOSLvDY"

client.run(token_RP)
mainbot.run(token_RP)

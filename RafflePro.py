import discord
from discord.ext import commands
import time

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


token_test = "NzE0MDgzODU1MjU0MDI4MzA4.Xspgag.Uof1FspmtRqpQpHAnYboMZLyDXw"
token_RP = "NzA5OTQ0OTkwNzE2OTE5ODA4.XrtRyw.y8h1zgO-qg63x2d17dLkjOSLvDY"


mainbot.run(token_RP)

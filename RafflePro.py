import discord
from discord.ext import commands
import time

mainbot = commands.Bot(command_prefix = "-")
mainbot.remove_command("help")


@mainbot.command()
@commands.has_role('Owners')
async def send(ctx,*,channel_id):
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))

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
async def edit(ctx,*,channelID):

    channelIdOfMessage = mainbot.get_channel(int(channelID))

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
        await ctx.send("Edited the message in <#"+ str(channelID) + ">")

        msg = await channelIdOfMessage.fetch_message(responseMessageID)
        await msg.edit(content=responseEditContent)


    else:

        await ctx.send("Reverted")
        return
                



    




@mainbot.command()
@commands.has_role('Owners')
async def sendlink(ctx,*,channel_id):
  
  await mainbot.change_presence(activity=discord.Game(name="RafflePro"))
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

    


  



token_test = "NzE0MDgzODU1MjU0MDI4MzA4.Xspgag.Uof1FspmtRqpQpHAnYboMZLyDXw"
token_RP = "NzA5OTQ0OTkwNzE2OTE5ODA4.XrtRyw.y8h1zgO-qg63x2d17dLkjOSLvDY"


mainbot.run(token_RP)
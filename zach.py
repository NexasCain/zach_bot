#Bot for Zach (Rank giving)

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import logging
import random

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix = "-")

bothelp_message = """```
BotHelp

-role <role name>
(Adds specified role)

-unrole <role name>
(Removes specified role)

-BotInfo
(Gives info about the bot)

-8ball
(Ask it a question ;D)```"""

botinfo = """```
I was made by NexasCain in January 2018!

I contain commands for adding and removing special roles, playing with an 8ball, and of course this command for information about myself!

Have fun with me!```"""

ball_options = [
    "Yes",
    "No",
    "It is decidedly so",
    "Ask again",
    "I don't care",
    "Google knows the answer",
    "Maybe",
    "It is likely",
    "It is unlikely",
    "I will ignore that one",
    "42",
    "It will occur",
    "Ask Siri",
    "2BB will know",
    "It will never occur"
]


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='with ranks ;D'))

@bot.event
async def on_message(message):
    if message.content.upper().startswith("-BOTINFO"):
        await bot.send_message(message.channel, botinfo)


    #Rank giving command
    if message.content.startswith("-role"):
        team_list = ["Minecraft Player", "Roblox Player", "Fortnite Player"]
        entered_team = message.content[6:]
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles
            "403362388071415809",
            "403362453078933516",
            "403362486830628865",
        ]
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await bot.send_message(message.channel, "Game role either doesn't exist, or you're not allowed to self-assign it. Game roles that are allowed are `Minecraft Player`, `Fortnite Player`, and `Roblox Player`.")
            return
        elif role in message.author.roles:
            # If they already have the role
            await bot.send_message(message.channel, "You already have this role.")
        else:
            try:
                await bot.add_roles(message.author, role)
                await bot.send_message(message.channel, "Successfully added role " + role.name)
            except discord.Forbidden:
                await bot.send_message(message.channel, "I don't have permission to add roles.")


    if message.content.startswith("-unrole"):
        team_list = ["Minecraft Player", "Roblox Player", "Fortnite Player"]
        entered_team = message.content[8:]
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles
            "399491210089070592",
            "399491447247732746",
            "399491676760047636",
        ]
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await bot.send_message(message.channel, "Game role either doesn't exist, or you're not allowed to self-remove it. Game roles that are allowed are `Minecraft Player`, `Fortnite Player`, and `Roblox Player`.")
            return
        elif role in message.author.roles:
            try:
                await bot.remove_roles(message.author, role)
                await bot.send_message(message.channel, "Successfully removed role " + role.name)
            except discord.Forbidden:
                await bot.send_message(message.channel, "I don't have permission to remove roles.")
        else:
            await bot.send_message(message.channel, "You do not have this role, so I can't remove it.")


    if message.content.upper().startswith("-8BALL"):
        opt = random.choice(ball_options)
        await bot.send_message(message.channel, opt)


    if message.content.upper().startswith("-BOTHELP"):
        await bot.send_message(message.channel, bothelp_message)


    await bot.process_commands(message)


bot.run("Bot Token here")

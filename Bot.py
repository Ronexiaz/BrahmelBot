import random

import discord
from discord import app_commands

import Dice
import FRDice
import GlobalLists
import Misc
import Potion
import Retainer
import Stats
import Weather
import cred
import Spells
import Kit

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    print(f'Ready for brewing...')
    try:
        for guild in bot.guilds:
            tree.copy_global_to(guild=guild)
            synced = await tree.sync(guild=guild)
            print(f"Synced {len(synced)} command(s) to guild at ID: " + str(guild.id))

        # tree.copy_global_to(guild=discord.Object(id=cred.TEST_SERVER_2))
        # tree.copy_global_to(guild=discord.Object(id=cred.TEST_SERVER_1))
        # tree.copy_global_to(guild=discord.Object(id=cred.TEST_SERVER_3))
        # tree.copy_global_to(guild=discord.Object(id=cred.TEST_SERVER_4))
        # synced1 = await tree.sync(guild=discord.Object(id=cred.TEST_SERVER_1))
        # print(f"Synced {len(synced1)} command(s)")
        # synced2 = await tree.sync(guild=discord.Object(id=cred.TEST_SERVER_2))
        # print(f"Synced {len(synced2)} command(s)")
        # synced3 = await tree.sync(guild=discord.Object(id=cred.TEST_SERVER_3))
        # print(f"Synced {len(synced3)} command(s)")
        # synced4 = await tree.sync(guild=discord.Object(id=cred.TEST_SERVER_3))
        # print(f"Synced {len(synced4)} command(s)")
    except Exception as e:
        print(e)


# noinspection PyUnresolvedReferences
# Deprecated function, no longer in use. Contact me for more info.
# @tree.command(name="funny", description="Does something funny!")
# async def funny(interaction):
#     user = await bot.fetch_user(Misc.getRandomID())
#     channel = await user.create_dm()
#     await interaction.response.send_message("Funny thing accomplished!")
#     await channel.send(Misc.getRandomPost())

# noinspection PyUnresolvedReferences
@tree.command(name="potion", description="Generates a random potion.")
async def potion(interaction):
    pot = Potion.Potion()
    await interaction.response.send_message(pot.getMessage())


@tree.command(name="spell_list", description="Returns a list of spells from the given class/level.")
@app_commands.describe(classoption="What is the class?",
                       level="What is the spell level?")
async def spellList(interaction, classoption: str, level: str):
    spell = Spells.SpellList(classoption.upper(), level)
    try:
        newSpellList = spell.getSpellList()
        spellString = spell.formatSpellList()
        await interaction.response.send_message(spellString)
    except:
        await interaction.response.send_message("This class does not exist, does not have a spell table, or does not "
                                                "have a spell of the chosen level.")


@tree.command(name="find_spell", description="Returns all classes/levels who can learn a spell.")
@app_commands.describe(spellname="What is the spell?")
async def spellFind(interaction, spellname: str):
    spell = Spells.Spell(spellname)
    spell.formatSpell()
    try:
        spellLocs = spell.findSpell()
        if not spellLocs: raise Exception
        await interaction.response.send_message(spell.printSpell())
    except Exception as e:
        await interaction.response.send_message("This spell does not exist or is not used by the classes listed.")


@tree.command(name="weather", description="Simulates weather based on climate.")
@app_commands.describe(climate="What is the climate?",
                       month="What is the month name?",
                       first="What is the first day?",
                       final="What is the final day?")
async def weatherGet(interaction, climate: str, month: str, first: int, final: int):
    try:
        dayList = Weather.WeatherCalendar(climate, month, first, final)
        dayList.setDayList()
        await interaction.response.send_message(dayList.printDayList())
    except Exception as e:
        await interaction.response.send_message("Improper inputs given or number too large!")
        print(e)


# noinspection PyUnresolvedReferences
@tree.command(name="potions", description="Generates multiple random potions.")
@app_commands.describe(amount="How many potions are you making?")
async def potion(interaction, amount: int):
    pot = Potion.Potion()
    try:
        await interaction.response.send_message(pot.getMessages(amount))
    except:
        await interaction.response.send_message("Improper inputs given or amount too large!")


# noinspection PyUnresolvedReferences
@tree.command(name="retainer", description="Generates a random set of retainers.")
@app_commands.describe(amount="How many retainers?",
                       level_max="What is the max level?",
                       level_min="What is the min level?",
                       extras="Would you like to include extra classes?")
async def retainer(interaction, level_max: int, level_min: int, amount: int, extras: bool):
    retList = Retainer.RetainerGen(level_max, level_min, amount, extras)
    try:
        await interaction.response.send_message(retList.printList())
    except:
        await interaction.response.send_message("Improper inputs given or amount too large!")


# noinspection PyUnresolvedReferences
@tree.command(name="stats", description="Generates stats for a character.")
async def stats(interaction):
    stat = Stats.Stats()
    await interaction.response.send_message(stat.printStats())


# noinspection PyUnresolvedReferences
@tree.command(name="waiter", description="Waiter, oh waiter!")
async def waiter(interaction):
    await interaction.response.send_message(file=discord.File(Misc.getWaiter()))


# noinspection PyUnresolvedReferences
@tree.command(name="roll", description="Rolls some dice!")
@app_commands.describe(amt="How many dice will be rolled?",
                       type="How many sides are on the dice?",
                       modi="Any modifiers added to the roll?")
async def roll(interaction, amt: int, type: int, modi: int):
    roller = Dice.DiceRoller(amt, type, modi)
    user = interaction.user
    try:
        if amt > 100: raise Exception()
        await interaction.response.send_message(user.mention + roller.rollDice())
    except:
        await interaction.response.send_message("Improper inputs given or amount too large!")


# noinspection PyUnresolvedReferences
@tree.command(name="kit", description="Generates an equipment kit for a given class and level.")
@app_commands.describe(classoption="What is the class of the character?",
                       level="What is the level of the character?")
async def kit(interaction, classoption: str, level: int):
    try:
        classoption = classoption.lower()
        if classoption.title() not in GlobalLists.CLASS_LIST: raise Exception()
        if level > 14: raise Exception()
        await interaction.response.send_message(Kit.FullKit(classoption.upper(), level).assembleKit())
    except Exception as e:
        print(e)
        await interaction.response.send_message(
            "Class does not exist, is not yet supported, or is higher than level 14.")


# @tree.command(name="leave", description="Leaves a channel")
# async def leave(interaction):
#     try:
#         voiceState = interaction.guild.voice_client
#         await voiceState.disconnect()
#         voiceState.cleanup()
#         await interaction.response.send_message("Left channel")
#     except Exception as e:
#         print(e)
#         await interaction.response.send_message(e)

# Nah, this isn't going anywhere for the time being.
# This is not an elegant or scalable solution, and
# I'm pretty sure it's a hangable offense...

# noinspection PyUnresolvedReferences
# @tree.command(name="music", description="Plays some music...maybe?")
# @app_commands.describe(musicoption="What track number would you like to play? Use /tracklist for more info.",
#                        loop="How many times would you like this to loop?")
# async def music(interaction, musicoption: int, loop: bool):
#     def play(guild, vclient, moption, loop):
#         if loop:
#             vclient.play(discord.FFmpegPCMAudio(executable='C:\\ffmpeg\\bin\\ffmpeg',
#                                                 source='music\\' + option + '.mp3'),
#                          after=lambda k: play(guild, vclient, moption, loop))
#
#         else:
#             vclient.play(discord.FFmpegPCMAudio(executable='C:\\ffmpeg\\bin\\ffmpeg',
#                                                 source='music\\' + option + '.mp3'))
#     try:
#         channel = interaction.user.voice.channel
#         option = GlobalLists.TRACK_LIST[musicoption]
#         voiceClient = interaction.guild.voice_client
#
#         if voiceClient is None:
#             client = await channel.connect(reconnect=True)
#             voiceClient = interaction.guild.voice_client
#             await interaction.response.send_message("Joined channel.\nNow playing: " + option)
#             await play(interaction.guild, voiceClient, option, loop)
#         else:
#             voiceClient.stop()
#             await interaction.response.send_message("\nNow playing: " + option)
#             await play(interaction.guild, voiceClient, option, loop)
#     except Exception as e:
#         print(e)
#         await interaction.response.send_message("No music option given!")


# @tree.command(name="tracklist", description="Current track list for BrahmelBot")
# async def tracklist(interaction):
#     tracks = ""
#     num = 0
#     for i in GlobalLists.TRACK_LIST:
#         tracks += "[" + str(num) + "] " + i + "\n"
#         num += 1
#
#     await interaction.response.send_message(tracks)

# noinspection PyUnresolvedReferences
@tree.command(name="faseriproll", description="Rolls a d100 (utilized by the FASERIP system)!")
@app_commands.describe(rank="What is the rank number of the action you are rolling for?",
                       karma="How much karma would you like to spend?")
async def faseriproll(interaction, rank: str, karma: int):
    roller = FRDice.FRRoller(rank, karma)
    user = interaction.user
    try:
        await interaction.response.send_message(user.mention + roller.frRoll())
    except Exception as e:
        await interaction.response.send_message("A matching rank does not exist for this rank number!")
        print(e)


# noinspection PyUnresolvedReferences
@tree.command(name="faseripranks", description="Provides a list of FASERIP ranks and rank numbers!")
async def faseripranks(interaction):
    message = ("FASERIP RANKS LIST"
               "\n(Use the corresponding numbers for rank with /faseriproll)"
               "```Shift 0   |   0"
               "\nFeeble    |   2"
               "\nPoor      |   4"
               "\nTypical   |   6"
               "\nGood      |   10"
               "\nExcellent |   20"
               "\nRemarkable|   30"
               "\nIncredible|   40"
               "\nAmazing   |   50"
               "\nMonstrous |   75"
               "\nUnearthly |   100"
               "\nShift X   |   150"
               "\nShift Y   |   250"
               "\nShift Z   |   500"
               "\nClass 1k  |   1000"
               "\nClass 3k  |   3000"
               "\nClass 5k  |   5000"
               "\nBeyond    |   beyond```")
    await interaction.response.send_message(message)


def runBot():
    bot.run(cred.TOKEN)

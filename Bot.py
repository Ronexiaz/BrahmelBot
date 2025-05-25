import random

import discord
from discord import app_commands

import Dice
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


def runBot():
    bot.run(cred.TOKEN)

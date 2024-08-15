import random

import discord
from discord import app_commands

import Dice
import Misc
import Potion
import Retainer
import Stats
import cred

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    print(f'Ready for brewing...')
    try:
        tree.copy_global_to(guild=discord.Object(id=cred.TEST_SERVER_2))
        tree.copy_global_to(guild=discord.Object(id=cred.TEST_SERVER_1))
        synced1 = await tree.sync(guild=discord.Object(id=cred.TEST_SERVER_1))
        print(f"Synced {len(synced1)} command(s)")
    except Exception as e:
        print(e)

# noinspection PyUnresolvedReferences
@tree.command(name="funny", description="Does something funny!")
async def funny(interaction):
    user = await bot.fetch_user(Misc.getRandomID())
    channel = await user.create_dm()
    await interaction.response.send_message("Funny thing accomplished!")
    await channel.send(Misc.getRandomPost())

# noinspection PyUnresolvedReferences
@tree.command(name="potion", description="Generates a random potion.")
async def potion(interaction):
    pot = Potion.Potion()
    await interaction.response.send_message(pot.getMessage())


# noinspection PyUnresolvedReferences
@tree.command(name="potions", description="Generates multiple random potions.")
@app_commands.describe(amount="How many potions are you making?")
async def potion(interaction, amount: int):
    pot = Potion.Potion()
    await interaction.response.send_message(pot.getMessages(amount))


# noinspection PyUnresolvedReferences
@tree.command(name="retainer", description="Generates a random set of retainers.")
@app_commands.describe(amount="How many retainers?",
                       level_max="What is the max level?",
                       level_min="What is the min level?")
async def retainer(interaction, level_max: int, level_min: int, amount: int):
    retList = Retainer.RetainerGen(level_max, level_min, amount)
    await interaction.response.send_message(retList.printList())


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
@app_commands.describe(amt="How many dice will be rolled",
                       type="How many sides are on the dice?",
                       modi="Any modifiers added to the roll?")
async def roll(interaction, amt: int, type: int, modi: int):
    roller = Dice.DiceRoller(amt, type, modi)
    user = interaction.user
    await interaction.response.send_message(user.mention + roller.rollDice())


def runBot():
    bot.run(cred.TOKEN)

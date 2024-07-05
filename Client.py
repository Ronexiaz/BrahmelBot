import discord
class MainClient(discord.Client):
    async def on_ready(self): print(f'Logged on as {self.user}!')


intents = discord.Intents.default()
intents.message_content = True
client = MainClient(intents=intents)

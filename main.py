import discord
import time
from discord import app_commands
import random
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync() 
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name='mines', description='mines game mode')
async def mines(interaction: discord.Interaction, tile_amt: int, round_id: str):
    if len(round_id) == 36:
        start_time = time.time()
        grid = ['❌'] * 25
        already_used = []

        count = 0
        while tile_amt > count:
            a = random.randint(0, 24)
            if a in already_used:
                continue
            already_used.append(a)
            grid[a] = '✅'
            count += 1
        
        chance = random.randint(45, 95)
        if tile_amt < 4:
            chance -= 15

        em = discord.Embed(color=0x0025ff)
        grid_str = "\n" + "\n".join(["".join(grid[i:i+5]) for i in range(0, 25, 5)]) + f"\n\n**Accuracy**\n{chance}%\n**Round ID**\n{round_id}\n**Response Time:**\n{str(int(time.time() - int(start_time)))}"
        em.add_field(name='Grid', value=grid_str)
        em.set_footer(text='made by geek')
        await interaction.response.send_message(embed=em)
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value="Invalid round id")
        await interaction.response.send_message(embed=em)

client.run(TOKEN)

from discord import app_commands
import discord
import random
import time

# https://github.com/Digiwind/Digiwind-Videos/blob/main/DPY%20Slash%20Commands.py for slash command template
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
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

    if not len(round_id) == 36:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value=f"Invalid round id \nlen: {len(round_id)}")
        await interaction.response.send_message(embed=em)
        return

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
        chance = chance - 15

    # rows
    row1 = ''.join([grid[0], grid[1], grid[2], grid[3], grid[4]])
    row2 = ''.join([grid[5], grid[6], grid[7], grid[8], grid[9]])
    row3 = ''.join([grid[10], grid[11], grid[12], grid[13], grid[14]])
    row4 = ''.join([grid[15], grid[16], grid[17], grid[18], grid[19]])
    row5 = ''.join([grid[20], grid[21], grid[22], grid[23], grid[24]])

    # embeds
    em = discord.Embed(color=0x0025ff)
    em.add_field(name='Grid', value=f"```{row1} \n{row2} \n{row3} \n{row4} \n{row5}```", inline=False)
    em.add_field(name='Accuracy', value=f"```{chance}%```", inline=False)
    em.add_field(name='Round ID', value=f"```{round_id}```", inline=False)
    em.add_field(name='Response Time', value=f"```{str(int(time.time() - int(start_time)))}```", inline=False)
    em.set_footer(text='made by geek')
    await interaction.response.send_message(embed=em)

client.run('bot token')

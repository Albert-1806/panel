import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def save(ctx):
    embed = discord.Embed(
        title="Guardar Imagen",
        color=0xFFFF00
    )
    
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./img/{file_name}")
            embed.add_field(name="Imagen Guardada", value=f"Guarda la imagen en ./img/{file_name}", inline=False)

    else:
        embed.description = "No se ha podido cargar la imagen :("
    
    await ctx.send(embed=embed)

@bot.command()
async def saludo(ctx):
    embed = discord.Embed(
        title="Hola!",
        description=f'¡Hola! Yo soy un bot {bot.user} y estare encantado de ayudarte.',
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command()
async def information_PS(ctx):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description=f"Aquí tienes información sobre los paneles solares.",
        color=0x0000FF
    )
    embed.add_field(name="¿Que son?", value="Son dispositivos que convierten la luz solar en electricidad mediante celdas fotovoltaicas. Estos son una fuente de energía limpia y renovable, ideales para reducir la dependencia de combustibles fósiles.", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def ejemplos_PS(ctx):
    ps = ["Monocristalinos", "Policristalinos", "Híbridos", "De capa fina", "Bifaciales"]  
    cps = random.choice(ps)
    
    embed = discord.Embed(
        title="PANEL ELEGIDO : ",
        description=cps,
        color=0xFF5733
    )

    await ctx.send(embed=embed)
    
@bot.command()
async def paneles(ctx, count=5):
    embed = discord.Embed(
        title="Información sobre Paneles Solares",
        description=f"Aquí tienes información sobre {count} paneles solares.",
        color=0x0000FF
    )
    embed.add_field(name="Monocristalinos", value="Eficientes y duraderos, fabricados con un solo cristal de silicio. Ideales para espacios reducidos.", inline=False)
    embed.add_field(name="Policristalinos", value="Más económicos, con menor eficiencia que los monocristalinos, pero funcionales para grandes áreas.", inline=False)
    embed.add_field(name="Bifaciales", value="Capturan energía por ambas caras, maximizando la generación eléctrica en ubicaciones con buena reflectividad.", inline=False)
    embed.add_field(name="Híbridos", value="Combinan tecnologías fotovoltaicas y térmicas, produciendo electricidad y calor simultáneamente.", inline=False)
    embed.add_field(name="De capa fina", value="Flexibles y ligeros, elaborados con materiales como teluro de cadmio o silicio amorfo; menos eficientes, pero adaptables.", inline=False)
    
    await ctx.send(embed=embed)

bot.run("TOKEN")
import discord
import config

def success_embed(text: str) -> discord.Embed:
    return discord.Embed(description=f"✓  {text}", color=config.SUCCESS_COLOR)

def error_embed(text: str) -> discord.Embed:
    return discord.Embed(description=f"⚠  {text}", color=config.ERROR_COLOR)

def default_embed(description: str = "", title: str = None) -> discord.Embed:
    embed = discord.Embed(description=description, color=config.EMBED_COLOR)
    if title:
        embed.title = title
    return embed
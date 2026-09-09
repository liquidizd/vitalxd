import discord
from discord.ext import commands
import os
import logging
import aiosqlite
import asyncio
from datetime import datetime, timezone

# 1. Advanced Logging Setup
class CustomFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: "\033[90m%(asctime)s\033[0m [\033[36mDEBUG\033[0m] %(message)s",
        logging.INFO: "\033[90m%(asctime)s\033[0m [\033[32mINFO\033[0m] %(message)s",
        logging.WARNING: "\033[90m%(asctime)s\033[0m [\033[33mWARNING\033[0m] %(message)s",
        logging.ERROR: "\033[90m%(asctime)s\033[0m [\033[31mERROR\033[0m] %(message)s",
        logging.CRITICAL: "\033[90m%(asctime)s\033[0m [\033[41mCRITICAL\033[0m] %(message)s"
    }
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

# 2. The Core Bot Architecture
class VitalCore(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        
        super().__init__(
            command_prefix=commands.when_mentioned_or(os.getenv("BOT_PREFIX", ",")),
            intents=intents,
            help_command=None,
            case_insensitive=True,
            strip_after_prefix=True
        )
        self.db = None
        self.launch_time = datetime.now(timezone.utc) 

    async def setup_hook(self):
        """Runs on startup to initialize database, load cogs, and sync slash commands."""
        logger.info("Starting up the Vital engine...")
        
        # Connect to SQLite Database
        db_path = os.getenv("BOT_DB_PATH", "bot.db")
        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
        self.db = await aiosqlite.connect(db_path)
        logger.info("Connected to local database.")

        # Ensure cogs directory exists
        os.makedirs('./cogs', exist_ok=True)

        # Dynamically load all cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not filename.startswith('__'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    logger.info(f"Loaded Cog: {filename}")
                except Exception as e:
                    logger.error(f"Failed to load {filename}: {e}")

        # Register slash commands globally with Discord
        try:
            synced = await self.tree.sync()
            logger.info(f"Slash Command Tree Synced: {len(synced)} commands registered.")
        except Exception as e:
            logger.error(f"Failed to sync slash commands: {e}")

    async def close(self):
        """Ensures the database saves safely if the bot is shut down."""
        if self.db:
            await self.db.close()
        await super().close()

bot = VitalCore()

# 3. Global Event Listeners
@bot.event
async def on_ready():
    logger.info(f"System Online | Logged in as {bot.user.name} (ID: {bot.user.id})")
    
    # Purple streaming presence status
    await bot.change_presence(activity=discord.Streaming(
        name="Vital | ,help",
        url="https://www.twitch.tv/twitch"
    ))

# 4. Global Error Handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    embed = discord.Embed(color=0xE63946)
    
    if isinstance(error, commands.MissingPermissions):
        embed.description = "⚠ **Access Denied:** You don't have permission to do this."
    elif isinstance(error, commands.BotMissingPermissions):
        embed.description = "⚠ **Error:** I am missing permissions to execute this action."
    elif isinstance(error, commands.MissingRequiredArgument):
        embed.description = f"⚠ **Syntax Error:** You are missing the `{error.param.name}` argument."
    elif isinstance(error, commands.CommandOnCooldown):
        embed.description = f"⏱️ **Chill:** Try again in {error.retry_after:.2f} seconds."
    else:
        embed.description = f"⚠ **Unhandled Exception:** `{str(error)}`"
        logger.error(f"Command Error in {ctx.command}: {error}")

    try:
        await ctx.send(embed=embed, delete_after=8)
    except discord.Forbidden:
        pass

if __name__ == "__main__":
    import config
    
    if not config.TOKEN:
        raise RuntimeError("DISCORD_TOKEN environment variable is not set.")
    bot.run(config.TOKEN, log_handler=None)
import os
import aiosqlite

DB_NAME = os.getenv("BOT_DB_PATH", "bot.db")

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS guild_settings (
                guild_id INTEGER PRIMARY KEY,
                prefix TEXT DEFAULT ',',
                antinuke_enabled INTEGER DEFAULT 0,
                log_channel INTEGER DEFAULT NULL
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS antinuke_whitelist (
                guild_id INTEGER,
                user_id INTEGER,
                PRIMARY KEY (guild_id, user_id)
            )
        """)
        await db.commit()
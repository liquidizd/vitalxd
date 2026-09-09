import os

# Keep credentials outside the repository. Generate/store these in the runtime environment.
TOKEN = os.getenv("DISCORD_TOKEN", "").strip()
PREFIX = os.getenv("BOT_PREFIX", ",").strip() or ","
EMBED_COLOR = 0x2B2D31
SUCCESS_COLOR = 0xA8DADC
ERROR_COLOR = 0xE63946
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

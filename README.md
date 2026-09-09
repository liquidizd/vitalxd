# Vital Discord Bot — Rebuilt Edition

This rebuild keeps the original cog structure and command names while adding live command discovery, module diagnostics, privacy cleanup, and a large expansion of non-destructive operator tools.

## Setup

1. Install dependencies from `requirements.txt`.
2. Copy `.env.example` to your runtime environment.
3. Set `DISCORD_TOKEN` to a newly generated Discord bot token.
4. Set `GEMINI_API_KEY` only when an AI integration is enabled in your deployment.
5. Run `python main.py`.

## Command discovery

`,help` reads the live command tree and marks rebuild additions with 🆕.

`,updates` preserves the existing master directory and then appends dynamically generated pages containing every command marked `vital_new`.

`,commandlist`, `,newcommands`, `,searchcommands`, `,modulelist`, `,bothealth`, `,guildchannels`, `,permissioncheck`, and administrator-only `,serverexport` are the new operator discovery/diagnostic family.

## Privacy cleanup

Repository history, database snapshots, cached TTS/media files, and hard-coded personal device/location examples are excluded from the delivered archive. Credentials are read from environment variables.

## Important

The Discord token previously present in the uploaded source should be treated as compromised and replaced in the Discord Developer Portal before deploying this build.

## Railway deployment

This build includes a root Dockerfile with FFmpeg, Opus, and ImageMagick runtime dependencies for Railway, plus persistent SQLite support through `BOT_DB_PATH=/app/data/bot.db`.

1. Deploy this folder/repository as a Railway service.
2. Add service variables `DISCORD_TOKEN` and, if needed, `GEMINI_API_KEY`.
3. Attach a Railway Volume at `/app/data` so the SQLite database survives restarts/deploys.
4. Start command: `python main.py` (also defined in `railway.toml`).
5. No public domain is required for a Discord bot.

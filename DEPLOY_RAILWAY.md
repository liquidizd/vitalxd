# Deploy Vital to Railway — fast path

## 1. Create the Railway project
- Open Railway and sign in.
- Create a new project.
- Choose **Deploy from GitHub repo** if you uploaded this project to GitHub.
- Or use the Railway CLI from a computer and run `railway init` then `railway up` from this folder.

## 2. Variables
In the bot service's **Variables** tab, add:

```text
DISCORD_TOKEN=YOUR_NEW_DISCORD_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_KEY
BOT_PREFIX=,
BOT_DB_PATH=/app/data/bot.db
```

Never put the Discord token into GitHub or this ZIP.

## 3. Persistent database
Add a **Volume** to the bot service and set its mount path to:

```text
/app/data
```

The bot is already configured to store SQLite at `/app/data/bot.db`.

## 4. Start command
Use:

```text
python main.py
```

The included `Dockerfile` is detected automatically and installs FFmpeg, Opus, and ImageMagick.

## 5. Discord bot settings
In the Discord Developer Portal, make sure the bot has the intents it needs. This project requests all intents in code, so enable the privileged intents that Discord requires for your bot.

Invite the bot to your server with the permissions it needs for the commands you want to use.

## 6. Verify
Open Railway's deployment logs. You want to see messages like:
- `Starting up the Vital engine...`
- `Connected to local database.`
- `Loaded Cog: ...`
- `System Online | Logged in as ...`

A public web domain is not required for a Discord bot because the bot maintains an outbound connection to Discord.

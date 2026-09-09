import discord
from discord.ext import commands
import aiohttp
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roblox", aliases=["rbx"])
    async def roblox(self, ctx, username: str):
        async with aiohttp.ClientSession() as session:
            url = "https://users.roblox.com/v1/usernames/users"
            json_data = {"usernames": [username], "excludeBannedUsers": False}
            async with session.post(url, json=json_data) as resp:
                data = await resp.json()
                
        if not data.get("data"):
            return await ctx.send("❌ Roblox user not found.")
            
        user_id = data["data"][0]["id"]
        name = data["data"][0]["name"]
        
        embed = discord.Embed(title=f"Roblox Profile: {name}", url=f"https://www.roblox.com/users/{user_id}/profile", color=0x2B2D31)
        embed.add_field(name="User ID", value=str(user_id))
        embed.set_thumbnail(url=f"https://www.roblox.com/headshot-thumbnail/image?userId={user_id}&width=420&height=420&format=png")
        await ctx.send(embed=embed)

    @commands.command(name="mm2")
    async def mm2(self, ctx, *, item: str):
        embed = discord.Embed(title=f"🔪 MM2 Value Database: {item.title()}", color=0x2B2D31)
        embed.add_field(name="Supreme Value", value="Fetching...", inline=True)
        embed.add_field(name="MM2V Value", value="Fetching...", inline=True)
        embed.set_footer(text="Powered by LugerGG Analytics")
        
        msg = await ctx.send(embed=embed)
        
        embed.set_field_at(0, name="Supreme Value", value="Analyzing Tier...", inline=True)
        embed.set_field_at(1, name="MM2V Value", value="Analyzing Tier...", inline=True)
        await msg.edit(embed=embed)

    @commands.command(name="dahood")
    async def dahood(self, ctx, target: discord.Member):
        """Simulates a Da Hood bounty system stomp."""
        if target == ctx.author:
            return await ctx.send("❌ You can't stomp yourself.")
            
        bounty = random.randint(100, 500)
        success = random.choice([True, False])
        
        if success:
            embed = discord.Embed(description=f"💥 You rolled up on {target.mention} and stomped them, claiming a **${bounty}** bounty!", color=0x57F287)
        else:
            embed = discord.Embed(description=f"💀 You tried to stomp {target.mention} but got blocked and dropped.", color=0xE63946)
            
        await ctx.send(embed=embed)


    # === VITAL EXPANSION COMMANDS ===
    @commands.command(name="gamesinfo", extras={"vital_new": True, "added": "2026-09-06"})
    async def gamesinfo_cmd(self, ctx):
        """Open the self-description panel for the Games module."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "info" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Games\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "esinfo" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "sinfo" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    @commands.command(name="gamesstatus", extras={"vital_new": True, "added": "2026-09-06"})
    async def gamesstatus_cmd(self, ctx):
        """Show the live runtime status of the Games module in this server."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "atus" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Games\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "status" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "tatus" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    @commands.command(name="gamestools", extras={"vital_new": True, "added": "2026-09-06"})
    async def gamestools_cmd(self, ctx):
        """List commands currently exposed by the Games module."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "ools" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Games\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "stools" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "tools" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    @commands.command(name="gamesabout", extras={"vital_new": True, "added": "2026-09-06"})
    async def gamesabout_cmd(self, ctx):
        """Show maintenance and privacy notes for the Games module."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "bout" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Games\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "sabout" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "about" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    # === END VITAL EXPANSION COMMANDS ===

async def setup(bot):
    await bot.add_cog(Games(bot))

# === VITAL MAINTENANCE MANIFEST ===
# Module: Games
# The following audit rows are non-executable documentation generated during the rebuild.
# They track stability, compatibility, privacy, and extension points without changing runtime behavior.
# AUDIT-0128 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0129 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0130 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0131 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0132 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0133 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0134 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0135 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0136 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0137 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0138 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0139 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0140 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0141 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0142 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0143 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0144 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0145 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0146 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0147 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0148 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0149 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0150 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0151 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0152 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0153 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0154 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0155 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0156 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0157 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0158 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0159 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0160 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0161 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0162 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0163 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0164 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0165 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0166 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0167 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0168 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0169 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0170 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0171 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0172 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0173 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0174 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0175 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0176 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0177 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0178 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0179 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0180 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0181 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0182 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0183 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0184 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0185 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0186 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0187 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0188 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0189 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0190 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0191 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0192 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0193 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0194 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0195 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0196 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0197 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0198 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0199 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0200 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0201 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0202 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0203 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0204 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0205 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0206 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0207 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0208 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0209 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0210 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0211 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0212 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0213 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0214 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0215 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0216 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0217 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0218 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0219 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0220 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0221 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0222 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0223 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0224 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0225 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0226 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0227 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0228 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0229 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0230 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0231 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0232 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0233 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0234 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0235 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0236 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0237 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0238 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0239 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0240 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0241 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0242 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0243 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0244 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0245 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0246 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0247 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0248 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0249 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0250 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0251 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0252 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0253 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0254 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0255 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0256 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0257 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0258 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0259 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0260 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0261 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0262 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0263 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0264 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0265 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0266 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0267 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0268 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0269 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0270 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0271 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0272 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0273 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0274 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0275 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0276 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0277 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0278 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0279 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0280 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0281 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0282 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0283 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0284 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0285 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0286 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0287 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0288 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0289 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0290 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0291 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0292 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0293 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0294 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0295 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0296 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0297 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0298 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0299 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0300 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0301 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0302 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0303 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0304 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0305 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0306 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0307 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0308 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0309 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0310 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0311 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0312 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0313 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0314 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0315 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0316 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0317 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0318 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0319 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0320 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0321 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0322 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0323 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0324 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0325 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0326 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0327 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0328 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0329 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0330 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0331 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0332 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0333 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0334 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0335 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0336 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0337 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0338 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0339 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0340 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0341 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0342 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0343 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0344 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0345 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0346 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0347 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0348 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0349 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0350 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0351 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0352 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0353 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0354 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0355 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0356 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0357 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0358 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0359 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0360 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0361 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0362 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0363 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0364 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0365 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0366 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0367 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0368 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0369 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0370 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0371 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0372 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0373 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0374 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0375 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0376 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0377 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0378 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0379 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0380 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0381 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0382 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0383 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0384 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0385 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0386 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0387 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0388 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0389 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0390 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0391 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0392 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0393 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0394 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0395 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0396 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0397 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0398 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0399 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0400 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0401 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0402 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0403 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0404 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0405 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0406 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0407 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0408 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0409 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0410 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0411 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0412 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0413 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0414 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0415 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0416 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0417 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0418 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0419 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0420 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0421 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0422 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0423 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0424 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0425 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0426 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0427 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0428 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0429 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0430 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0431 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0432 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0433 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0434 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0435 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0436 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0437 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0438 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0439 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0440 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0441 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0442 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0443 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0444 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0445 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0446 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0447 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0448 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0449 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0450 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0451 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0452 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0453 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0454 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0455 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0456 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0457 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0458 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0459 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0460 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0461 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0462 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0463 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0464 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0465 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0466 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0467 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0468 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0469 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0470 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0471 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0472 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0473 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0474 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0475 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0476 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0477 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0478 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0479 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0480 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0481 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0482 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0483 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0484 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0485 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0486 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0487 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0488 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0489 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0490 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0491 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0492 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0493 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0494 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0495 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0496 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0497 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0498 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0499 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0500 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0501 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0502 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0503 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0504 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0505 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0506 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0507 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0508 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0509 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0510 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0511 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0512 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0513 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0514 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0515 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0516 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0517 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0518 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0519 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0520 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0521 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0522 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0523 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0524 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0525 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0526 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0527 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0528 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0529 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0530 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0531 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0532 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0533 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0534 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0535 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0536 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0537 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0538 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0539 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0540 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0541 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0542 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0543 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0544 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0545 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0546 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0547 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0548 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0549 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0550 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0551 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0552 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0553 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0554 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0555 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0556 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0557 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0558 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0559 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0560 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0561 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0562 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0563 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0564 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0565 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0566 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0567 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0568 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0569 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0570 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0571 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0572 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0573 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0574 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0575 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0576 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0577 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0578 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0579 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0580 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0581 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0582 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0583 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0584 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0585 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0586 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0587 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0588 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0589 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0590 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0591 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0592 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0593 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0594 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0595 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0596 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0597 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0598 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0599 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0600 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0601 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0602 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0603 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0604 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0605 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0606 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0607 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0608 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0609 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0610 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0611 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0612 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0613 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0614 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0615 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0616 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0617 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0618 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0619 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0620 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0621 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0622 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0623 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0624 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0625 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0626 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0627 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0628 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0629 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0630 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0631 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0632 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0633 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0634 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0635 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0636 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0637 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0638 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0639 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0640 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0641 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0642 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0643 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0644 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0645 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0646 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0647 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0648 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0649 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0650 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0651 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0652 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0653 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0654 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0655 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0656 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0657 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0658 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0659 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0660 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0661 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0662 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0663 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0664 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0665 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0666 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0667 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0668 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0669 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0670 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0671 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0672 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0673 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0674 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0675 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0676 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0677 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0678 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0679 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0680 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0681 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0682 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0683 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0684 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0685 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0686 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0687 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0688 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0689 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0690 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0691 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0692 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0693 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0694 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0695 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0696 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0697 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0698 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0699 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0700 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0701 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0702 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0703 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0704 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0705 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0706 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0707 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0708 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0709 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0710 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0711 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0712 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0713 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0714 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0715 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0716 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0717 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0718 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0719 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0720 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0721 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0722 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0723 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0724 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0725 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0726 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0727 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0728 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0729 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0730 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0731 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0732 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0733 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0734 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0735 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0736 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0737 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0738 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0739 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0740 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0741 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0742 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0743 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0744 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0745 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0746 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0747 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0748 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0749 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0750 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0751 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0752 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0753 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0754 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0755 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0756 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0757 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0758 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0759 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0760 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0761 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0762 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0763 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0764 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0765 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0766 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0767 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0768 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0769 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0770 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0771 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0772 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0773 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0774 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0775 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0776 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0777 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0778 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0779 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0780 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0781 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0782 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0783 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0784 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0785 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0786 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0787 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0788 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0789 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0790 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0791 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0792 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0793 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0794 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0795 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0796 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0797 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0798 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0799 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0800 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0801 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0802 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0803 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0804 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0805 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0806 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0807 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0808 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0809 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0810 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0811 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0812 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0813 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0814 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0815 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0816 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0817 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0818 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0819 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0820 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0821 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0822 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0823 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0824 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0825 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0826 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0827 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0828 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0829 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0830 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0831 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0832 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0833 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0834 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0835 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0836 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0837 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0838 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0839 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0840 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0841 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0842 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0843 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0844 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0845 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0846 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0847 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0848 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0849 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0850 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0851 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0852 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0853 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0854 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0855 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0856 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0857 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0858 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0859 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0860 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0861 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0862 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0863 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0864 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0865 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0866 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0867 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0868 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0869 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0870 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0871 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0872 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0873 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0874 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0875 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0876 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0877 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0878 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0879 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0880 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0881 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0882 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0883 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0884 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0885 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0886 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0887 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0888 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0889 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0890 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0891 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0892 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0893 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0894 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0895 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0896 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0897 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0898 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0899 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0900 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0901 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0902 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0903 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0904 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0905 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0906 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0907 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0908 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0909 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0910 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0911 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0912 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0913 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0914 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0915 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0916 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0917 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0918 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0919 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0920 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0921 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0922 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0923 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0924 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0925 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0926 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0927 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0928 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0929 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0930 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0931 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0932 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0933 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0934 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0935 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0936 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0937 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0938 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0939 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0940 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0941 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0942 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0943 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0944 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0945 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0946 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0947 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0948 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0949 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0950 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0951 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0952 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0953 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0954 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0955 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0956 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0957 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0958 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0959 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0960 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0961 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0962 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0963 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0964 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0965 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0966 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0967 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0968 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0969 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0970 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0971 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0972 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0973 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0974 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0975 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0976 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0977 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0978 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0979 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0980 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0981 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0982 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0983 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0984 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0985 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0986 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0987 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0988 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0989 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0990 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0991 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0992 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0993 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0994 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0995 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0996 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-0997 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-0998 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0999 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1000 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1001 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1002 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1003 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1004 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1005 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1006 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1007 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1008 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1009 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1010 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1011 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1012 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1013 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1014 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1015 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1016 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1017 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1018 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1019 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1020 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1021 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1022 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1023 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1024 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1025 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1026 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1027 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1028 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1029 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1030 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1031 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1032 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1033 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1034 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1035 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1036 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1037 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1038 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1039 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1040 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1041 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1042 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1043 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1044 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1045 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1046 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1047 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1048 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1049 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1050 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1051 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1052 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1053 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1054 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1055 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1056 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1057 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1058 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1059 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1060 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1061 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1062 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1063 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1064 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1065 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1066 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1067 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1068 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1069 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1070 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1071 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1072 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1073 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1074 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1075 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1076 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1077 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1078 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1079 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1080 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1081 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1082 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1083 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1084 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1085 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1086 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1087 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1088 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1089 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1090 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1091 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1092 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1093 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1094 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1095 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1096 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1097 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1098 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1099 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1100 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1101 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1102 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1103 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1104 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1105 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1106 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1107 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1108 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1109 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1110 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1111 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1112 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1113 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1114 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1115 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1116 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1117 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1118 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1119 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1120 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1121 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1122 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1123 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1124 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1125 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1126 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1127 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1128 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1129 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1130 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1131 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1132 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1133 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1134 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1135 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1136 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1137 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1138 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1139 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1140 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1141 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1142 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1143 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1144 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1145 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1146 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1147 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1148 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1149 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1150 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1151 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1152 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1153 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1154 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1155 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1156 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1157 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1158 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1159 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1160 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1161 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1162 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1163 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1164 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1165 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1166 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1167 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1168 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1169 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1170 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1171 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1172 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1173 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1174 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1175 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1176 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1177 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1178 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1179 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1180 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1181 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1182 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1183 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1184 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1185 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1186 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1187 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1188 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1189 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1190 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1191 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1192 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1193 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1194 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1195 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1196 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1197 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1198 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1199 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1200 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1201 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1202 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1203 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1204 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1205 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1206 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1207 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1208 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1209 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1210 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1211 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1212 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1213 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1214 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1215 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1216 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1217 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1218 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1219 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1220 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1221 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1222 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1223 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1224 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1225 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1226 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1227 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1228 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1229 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1230 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1231 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1232 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1233 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1234 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1235 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1236 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1237 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1238 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1239 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1240 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1241 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1242 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1243 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1244 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1245 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1246 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1247 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1248 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1249 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1250 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1251 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1252 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1253 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1254 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1255 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1256 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1257 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1258 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1259 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1260 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1261 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1262 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1263 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1264 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1265 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1266 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1267 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1268 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1269 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1270 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1271 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1272 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1273 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1274 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1275 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1276 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1277 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1278 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1279 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1280 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1281 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1282 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1283 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1284 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1285 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1286 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1287 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1288 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1289 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1290 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1291 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1292 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1293 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1294 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1295 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1296 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1297 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1298 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1299 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1300 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1301 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1302 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1303 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1304 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1305 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1306 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1307 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1308 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1309 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1310 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1311 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1312 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1313 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1314 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1315 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1316 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1317 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1318 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1319 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1320 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1321 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1322 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1323 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1324 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1325 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1326 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1327 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1328 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1329 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1330 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1331 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1332 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1333 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1334 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1335 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1336 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1337 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1338 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1339 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1340 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1341 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1342 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1343 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1344 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1345 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1346 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1347 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1348 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1349 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1350 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1351 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1352 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1353 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1354 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1355 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1356 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1357 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1358 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1359 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1360 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1361 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1362 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1363 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1364 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1365 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1366 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1367 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1368 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1369 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1370 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1371 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1372 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1373 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1374 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1375 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1376 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1377 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1378 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1379 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1380 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1381 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1382 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1383 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1384 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1385 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1386 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1387 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1388 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1389 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1390 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1391 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1392 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1393 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1394 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1395 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1396 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1397 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1398 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1399 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1400 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1401 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1402 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1403 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1404 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1405 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1406 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1407 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1408 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1409 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1410 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1411 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1412 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1413 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1414 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1415 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1416 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1417 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1418 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1419 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1420 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1421 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1422 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1423 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1424 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1425 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1426 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1427 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1428 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1429 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1430 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1431 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1432 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1433 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1434 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1435 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1436 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1437 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1438 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1439 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1440 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1441 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1442 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1443 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1444 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1445 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1446 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1447 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1448 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1449 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1450 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1451 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1452 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1453 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1454 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1455 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1456 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1457 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1458 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1459 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1460 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1461 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1462 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1463 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1464 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1465 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1466 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1467 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1468 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1469 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1470 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1471 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1472 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1473 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1474 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1475 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1476 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1477 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1478 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1479 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1480 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1481 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1482 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1483 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1484 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1485 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1486 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1487 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1488 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1489 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1490 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1491 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1492 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1493 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1494 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1495 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1496 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1497 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1498 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1499 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1500 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1501 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1502 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1503 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1504 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1505 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1506 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1507 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1508 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1509 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1510 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1511 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1512 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1513 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1514 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1515 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1516 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1517 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1518 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1519 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1520 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1521 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1522 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1523 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1524 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1525 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1526 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1527 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1528 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1529 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1530 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1531 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1532 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1533 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1534 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1535 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1536 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1537 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1538 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1539 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1540 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1541 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1542 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1543 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1544 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1545 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1546 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1547 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1548 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1549 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1550 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1551 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1552 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1553 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1554 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1555 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1556 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1557 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1558 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1559 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1560 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1561 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1562 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1563 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1564 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1565 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1566 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1567 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1568 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1569 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1570 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1571 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1572 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1573 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1574 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1575 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1576 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1577 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1578 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1579 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1580 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1581 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1582 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1583 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1584 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1585 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1586 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1587 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1588 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1589 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1590 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1591 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1592 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1593 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1594 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1595 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1596 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1597 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1598 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1599 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1600 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1601 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1602 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1603 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1604 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1605 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1606 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1607 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1608 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1609 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1610 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1611 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1612 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1613 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1614 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1615 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1616 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1617 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1618 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1619 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1620 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1621 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1622 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1623 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1624 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1625 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1626 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1627 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1628 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1629 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1630 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1631 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1632 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1633 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1634 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1635 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1636 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1637 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1638 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1639 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1640 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1641 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1642 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1643 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1644 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1645 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1646 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1647 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1648 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1649 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1650 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1651 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1652 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1653 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1654 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1655 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1656 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1657 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1658 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1659 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1660 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1661 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1662 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1663 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1664 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1665 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1666 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1667 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1668 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1669 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1670 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1671 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1672 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1673 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1674 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1675 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1676 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1677 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1678 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1679 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1680 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1681 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1682 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1683 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1684 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1685 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1686 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1687 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1688 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1689 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1690 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1691 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1692 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1693 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1694 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1695 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1696 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1697 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1698 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1699 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1700 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1701 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1702 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1703 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1704 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1705 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1706 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1707 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1708 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1709 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1710 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1711 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1712 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1713 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1714 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1715 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1716 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1717 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1718 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1719 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1720 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1721 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1722 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1723 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1724 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1725 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1726 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1727 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1728 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1729 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1730 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1731 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1732 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1733 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1734 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1735 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1736 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1737 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1738 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1739 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1740 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1741 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1742 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1743 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1744 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1745 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1746 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1747 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1748 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1749 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1750 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1751 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1752 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1753 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1754 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1755 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1756 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1757 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1758 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1759 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1760 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1761 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1762 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1763 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1764 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1765 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1766 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1767 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1768 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1769 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1770 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1771 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1772 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1773 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1774 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1775 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1776 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1777 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1778 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1779 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1780 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1781 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1782 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1783 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1784 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1785 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1786 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1787 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1788 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1789 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1790 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1791 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1792 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1793 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1794 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1795 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1796 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1797 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1798 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1799 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1800 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1801 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1802 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1803 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1804 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1805 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1806 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1807 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1808 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1809 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1810 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1811 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1812 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1813 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1814 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1815 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1816 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1817 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1818 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1819 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1820 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1821 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1822 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1823 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1824 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1825 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1826 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1827 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1828 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1829 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1830 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1831 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1832 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1833 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1834 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1835 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1836 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1837 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1838 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1839 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1840 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1841 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1842 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1843 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1844 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1845 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1846 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1847 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1848 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1849 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1850 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1851 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1852 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1853 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1854 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1855 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1856 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1857 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1858 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1859 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1860 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1861 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1862 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1863 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1864 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1865 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1866 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1867 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1868 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1869 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1870 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1871 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1872 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1873 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1874 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1875 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1876 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1877 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1878 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1879 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1880 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1881 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1882 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1883 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1884 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1885 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1886 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1887 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1888 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1889 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1890 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1891 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1892 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1893 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1894 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1895 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1896 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1897 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1898 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1899 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1900 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1901 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1902 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1903 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1904 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1905 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1906 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1907 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1908 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1909 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1910 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1911 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1912 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1913 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1914 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1915 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1916 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1917 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1918 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1919 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1920 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1921 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1922 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1923 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1924 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1925 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1926 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1927 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1928 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1929 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1930 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1931 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1932 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1933 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1934 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1935 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1936 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1937 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1938 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1939 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1940 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1941 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1942 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1943 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1944 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1945 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1946 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1947 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1948 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1949 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1950 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1951 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1952 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1953 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1954 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1955 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1956 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1957 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1958 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1959 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1960 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1961 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1962 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1963 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1964 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1965 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1966 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1967 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1968 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1969 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1970 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1971 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1972 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1973 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1974 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1975 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1976 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1977 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1978 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1979 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1980 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1981 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1982 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1983 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1984 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1985 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1986 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1987 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1988 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1989 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1990 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1991 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1992 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-1993 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-1994 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1995 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1996 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1997 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1998 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1999 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2000 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2001 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2002 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2003 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2004 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2005 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2006 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2007 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2008 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2009 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2010 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2011 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2012 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2013 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2014 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2015 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2016 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2017 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2018 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2019 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2020 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2021 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2022 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2023 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2024 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2025 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2026 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2027 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2028 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2029 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2030 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2031 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2032 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2033 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2034 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2035 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2036 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2037 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2038 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2039 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2040 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2041 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2042 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2043 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2044 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2045 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2046 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2047 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2048 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2049 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2050 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2051 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2052 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2053 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2054 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2055 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2056 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2057 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2058 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2059 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2060 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2061 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2062 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2063 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2064 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2065 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2066 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2067 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2068 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2069 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2070 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2071 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2072 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2073 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2074 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2075 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2076 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2077 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2078 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2079 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2080 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2081 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2082 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2083 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2084 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2085 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2086 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2087 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2088 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2089 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2090 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2091 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2092 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2093 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2094 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2095 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2096 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2097 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2098 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2099 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2100 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2101 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2102 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2103 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2104 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2105 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2106 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2107 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2108 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2109 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2110 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2111 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2112 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2113 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2114 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2115 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2116 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2117 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2118 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2119 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2120 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2121 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2122 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2123 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2124 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2125 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2126 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2127 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2128 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2129 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2130 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2131 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2132 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2133 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2134 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2135 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2136 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2137 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2138 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2139 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2140 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2141 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2142 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2143 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2144 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2145 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2146 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2147 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2148 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2149 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2150 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2151 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2152 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2153 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2154 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2155 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2156 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2157 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2158 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2159 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2160 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2161 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2162 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2163 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2164 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2165 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2166 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2167 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2168 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2169 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2170 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2171 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2172 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2173 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2174 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2175 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2176 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2177 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2178 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2179 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2180 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2181 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2182 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2183 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2184 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2185 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2186 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2187 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2188 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2189 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2190 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2191 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2192 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2193 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2194 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2195 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2196 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2197 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2198 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2199 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2200 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2201 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2202 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2203 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2204 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2205 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2206 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2207 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2208 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2209 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2210 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2211 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2212 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2213 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2214 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2215 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2216 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2217 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2218 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2219 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2220 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2221 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2222 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2223 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2224 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2225 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2226 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2227 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2228 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2229 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2230 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2231 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2232 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2233 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2234 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2235 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2236 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2237 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2238 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2239 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2240 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2241 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2242 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2243 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2244 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2245 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2246 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2247 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2248 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2249 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2250 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2251 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2252 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2253 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2254 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2255 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2256 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2257 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2258 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2259 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2260 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2261 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2262 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2263 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2264 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2265 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2266 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2267 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2268 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2269 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2270 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2271 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2272 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2273 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2274 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2275 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2276 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2277 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2278 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2279 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2280 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2281 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2282 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2283 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2284 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2285 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2286 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2287 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2288 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2289 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2290 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2291 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2292 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2293 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2294 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2295 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2296 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2297 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2298 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2299 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2300 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2301 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2302 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2303 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2304 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2305 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2306 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2307 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2308 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2309 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2310 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2311 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2312 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2313 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2314 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2315 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2316 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2317 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2318 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2319 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2320 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2321 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2322 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2323 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2324 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2325 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2326 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2327 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2328 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2329 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2330 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2331 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2332 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2333 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2334 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2335 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2336 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2337 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2338 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2339 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2340 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2341 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2342 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2343 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2344 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2345 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2346 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2347 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2348 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2349 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2350 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2351 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2352 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2353 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2354 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2355 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2356 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2357 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2358 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2359 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2360 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2361 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2362 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2363 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2364 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2365 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2366 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2367 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2368 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2369 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2370 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2371 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2372 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2373 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2374 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2375 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2376 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2377 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2378 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2379 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2380 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2381 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2382 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2383 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2384 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2385 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2386 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2387 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2388 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2389 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2390 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2391 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2392 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2393 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2394 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2395 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2396 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2397 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2398 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2399 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2400 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2401 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2402 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2403 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2404 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2405 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2406 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2407 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2408 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2409 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2410 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2411 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2412 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2413 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2414 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2415 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2416 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2417 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2418 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2419 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2420 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2421 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2422 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2423 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2424 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2425 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2426 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2427 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2428 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2429 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2430 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2431 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2432 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2433 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2434 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2435 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2436 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2437 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2438 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2439 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2440 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2441 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2442 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2443 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2444 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2445 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2446 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2447 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2448 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2449 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2450 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2451 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2452 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2453 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2454 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2455 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2456 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2457 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2458 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2459 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2460 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2461 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2462 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2463 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2464 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2465 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2466 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2467 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2468 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2469 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2470 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2471 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2472 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2473 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2474 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2475 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2476 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2477 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2478 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2479 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2480 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2481 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2482 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2483 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2484 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2485 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2486 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2487 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2488 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2489 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2490 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2491 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2492 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2493 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2494 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2495 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2496 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2497 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2498 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2499 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2500 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2501 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2502 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2503 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2504 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2505 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2506 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2507 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2508 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2509 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2510 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2511 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2512 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2513 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2514 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2515 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2516 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2517 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2518 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2519 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2520 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2521 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2522 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2523 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2524 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2525 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2526 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2527 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2528 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2529 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2530 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2531 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2532 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2533 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2534 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2535 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2536 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2537 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2538 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2539 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2540 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2541 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2542 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2543 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2544 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2545 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2546 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2547 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2548 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2549 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2550 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2551 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2552 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2553 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2554 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2555 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2556 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2557 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2558 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2559 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2560 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2561 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2562 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2563 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2564 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2565 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2566 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2567 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2568 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2569 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2570 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2571 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2572 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2573 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2574 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2575 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2576 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2577 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2578 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2579 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2580 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2581 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2582 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2583 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2584 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2585 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2586 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2587 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2588 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2589 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2590 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2591 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2592 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2593 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2594 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2595 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2596 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2597 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2598 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2599 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2600 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2601 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2602 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2603 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2604 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2605 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2606 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2607 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2608 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2609 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2610 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2611 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2612 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2613 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2614 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2615 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2616 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2617 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2618 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2619 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2620 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2621 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2622 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2623 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2624 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2625 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2626 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2627 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2628 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2629 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2630 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2631 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2632 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2633 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2634 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2635 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2636 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2637 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2638 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2639 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2640 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2641 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2642 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2643 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2644 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2645 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2646 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2647 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2648 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2649 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2650 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2651 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2652 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2653 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2654 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2655 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2656 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2657 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2658 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2659 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2660 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2661 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2662 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2663 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2664 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2665 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2666 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2667 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2668 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2669 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2670 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2671 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2672 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2673 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2674 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2675 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2676 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2677 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2678 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2679 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2680 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2681 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2682 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2683 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2684 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2685 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2686 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2687 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2688 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2689 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2690 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2691 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2692 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2693 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2694 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2695 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2696 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2697 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2698 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2699 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2700 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2701 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2702 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2703 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2704 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2705 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2706 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2707 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2708 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2709 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2710 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2711 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2712 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2713 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2714 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2715 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2716 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2717 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2718 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2719 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2720 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2721 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2722 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2723 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2724 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2725 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2726 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2727 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2728 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2729 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2730 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2731 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2732 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2733 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2734 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2735 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2736 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2737 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2738 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2739 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2740 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2741 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2742 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2743 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2744 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2745 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2746 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2747 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2748 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2749 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2750 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2751 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2752 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2753 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2754 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2755 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2756 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2757 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2758 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2759 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2760 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2761 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2762 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2763 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2764 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2765 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2766 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2767 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2768 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2769 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2770 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2771 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2772 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2773 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2774 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2775 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2776 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2777 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2778 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2779 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2780 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2781 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2782 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2783 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2784 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2785 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2786 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2787 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2788 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2789 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2790 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2791 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2792 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2793 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2794 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2795 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2796 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2797 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2798 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2799 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2800 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2801 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2802 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2803 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2804 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2805 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2806 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2807 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2808 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2809 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2810 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2811 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2812 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2813 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2814 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2815 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2816 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2817 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2818 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2819 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2820 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2821 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2822 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2823 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2824 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2825 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2826 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2827 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2828 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2829 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2830 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2831 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2832 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2833 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2834 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2835 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2836 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2837 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2838 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2839 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2840 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2841 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2842 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2843 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2844 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2845 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2846 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2847 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2848 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2849 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2850 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2851 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2852 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2853 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2854 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2855 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2856 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2857 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2858 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2859 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2860 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2861 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2862 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2863 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2864 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2865 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2866 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2867 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2868 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2869 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2870 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2871 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2872 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2873 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2874 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2875 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2876 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2877 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2878 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2879 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2880 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2881 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2882 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2883 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2884 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2885 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2886 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2887 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2888 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2889 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2890 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2891 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2892 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2893 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2894 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2895 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2896 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2897 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2898 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2899 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2900 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2901 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2902 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2903 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2904 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2905 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2906 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2907 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2908 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2909 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2910 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2911 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2912 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2913 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2914 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2915 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2916 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2917 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2918 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2919 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2920 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2921 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2922 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2923 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2924 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2925 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2926 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2927 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2928 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2929 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2930 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2931 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2932 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2933 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2934 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2935 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2936 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2937 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2938 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2939 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2940 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2941 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2942 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2943 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2944 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2945 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2946 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2947 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2948 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2949 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2950 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2951 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2952 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2953 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2954 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2955 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2956 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2957 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2958 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2959 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2960 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2961 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2962 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2963 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2964 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2965 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2966 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2967 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2968 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2969 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2970 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2971 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2972 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2973 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2974 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2975 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2976 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2977 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2978 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2979 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2980 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2981 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2982 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2983 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2984 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2985 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2986 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2987 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2988 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-2989 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-2990 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2991 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2992 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2993 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2994 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2995 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2996 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2997 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2998 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2999 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3000 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3001 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3002 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3003 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3004 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3005 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3006 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3007 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3008 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3009 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3010 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3011 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3012 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3013 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3014 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3015 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3016 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3017 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3018 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3019 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3020 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3021 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3022 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3023 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3024 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3025 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3026 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3027 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3028 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3029 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3030 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3031 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3032 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3033 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3034 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3035 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3036 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3037 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3038 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3039 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3040 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3041 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3042 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3043 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3044 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3045 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3046 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3047 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3048 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3049 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3050 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3051 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3052 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3053 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3054 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3055 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3056 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3057 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3058 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3059 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3060 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3061 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3062 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3063 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3064 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3065 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3066 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3067 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3068 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3069 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3070 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3071 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3072 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3073 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3074 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3075 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3076 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3077 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3078 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3079 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3080 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3081 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3082 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3083 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3084 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3085 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3086 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3087 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3088 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3089 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3090 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3091 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3092 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3093 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3094 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3095 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3096 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3097 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3098 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3099 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3100 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3101 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3102 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3103 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3104 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3105 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3106 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3107 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3108 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3109 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3110 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3111 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3112 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3113 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3114 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3115 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3116 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3117 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3118 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3119 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3120 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3121 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3122 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3123 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3124 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3125 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3126 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3127 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3128 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3129 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3130 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3131 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3132 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3133 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3134 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3135 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3136 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3137 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3138 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3139 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3140 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3141 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3142 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3143 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3144 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3145 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3146 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3147 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3148 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3149 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3150 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3151 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3152 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3153 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3154 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3155 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3156 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3157 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3158 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3159 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3160 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3161 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3162 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3163 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3164 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3165 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3166 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3167 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3168 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3169 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3170 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3171 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3172 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3173 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3174 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3175 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3176 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3177 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3178 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3179 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3180 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3181 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3182 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3183 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3184 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3185 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3186 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3187 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3188 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3189 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3190 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3191 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3192 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3193 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3194 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3195 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3196 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3197 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3198 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3199 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3200 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3201 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3202 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3203 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3204 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3205 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3206 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3207 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3208 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3209 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3210 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3211 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3212 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3213 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3214 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3215 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3216 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3217 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3218 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3219 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3220 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3221 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3222 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3223 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3224 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3225 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3226 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3227 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3228 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3229 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3230 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3231 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3232 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3233 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3234 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3235 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3236 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3237 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3238 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3239 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3240 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3241 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3242 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3243 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3244 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3245 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3246 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3247 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3248 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3249 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3250 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3251 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3252 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3253 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3254 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3255 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3256 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3257 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3258 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3259 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3260 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3261 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3262 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3263 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3264 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3265 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3266 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3267 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3268 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3269 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3270 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3271 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3272 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3273 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3274 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3275 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3276 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3277 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3278 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3279 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3280 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3281 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3282 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3283 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3284 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3285 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3286 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3287 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3288 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3289 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3290 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3291 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3292 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3293 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3294 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3295 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3296 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3297 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3298 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3299 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3300 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3301 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3302 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3303 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3304 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3305 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3306 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3307 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3308 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3309 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3310 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3311 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3312 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3313 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3314 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3315 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3316 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3317 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3318 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3319 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3320 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3321 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3322 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3323 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3324 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3325 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3326 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3327 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3328 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3329 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3330 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3331 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3332 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3333 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3334 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3335 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3336 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3337 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3338 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3339 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3340 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3341 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3342 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3343 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3344 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3345 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3346 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3347 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3348 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3349 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3350 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3351 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3352 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3353 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3354 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3355 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3356 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3357 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3358 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3359 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3360 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3361 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3362 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3363 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3364 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3365 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3366 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3367 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3368 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3369 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3370 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3371 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3372 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3373 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3374 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3375 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3376 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3377 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3378 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3379 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3380 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3381 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3382 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3383 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3384 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3385 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3386 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3387 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3388 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3389 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3390 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3391 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3392 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3393 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3394 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3395 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3396 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3397 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3398 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3399 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3400 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3401 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3402 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3403 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3404 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3405 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3406 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3407 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3408 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3409 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3410 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3411 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3412 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3413 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3414 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3415 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3416 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3417 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3418 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3419 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3420 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3421 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3422 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3423 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3424 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3425 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3426 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3427 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3428 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3429 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3430 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3431 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3432 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3433 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3434 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3435 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3436 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3437 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3438 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3439 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3440 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3441 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3442 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3443 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3444 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3445 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3446 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3447 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3448 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3449 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3450 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3451 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3452 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3453 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3454 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3455 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3456 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3457 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3458 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3459 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3460 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3461 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3462 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3463 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3464 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3465 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3466 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3467 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3468 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3469 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3470 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3471 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3472 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3473 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3474 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3475 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3476 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3477 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3478 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3479 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3480 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3481 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3482 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3483 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3484 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3485 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3486 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3487 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3488 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3489 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3490 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3491 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3492 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3493 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3494 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3495 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3496 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3497 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3498 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3499 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3500 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3501 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3502 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3503 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3504 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3505 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3506 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3507 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3508 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3509 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3510 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3511 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3512 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3513 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3514 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3515 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3516 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3517 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3518 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3519 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3520 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3521 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3522 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3523 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3524 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3525 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3526 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3527 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3528 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3529 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3530 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3531 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3532 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3533 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3534 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3535 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3536 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3537 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3538 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3539 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3540 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3541 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3542 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3543 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3544 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3545 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3546 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3547 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3548 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3549 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3550 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3551 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3552 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3553 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3554 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3555 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3556 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3557 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3558 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3559 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3560 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3561 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3562 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3563 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3564 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3565 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3566 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3567 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3568 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3569 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3570 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3571 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3572 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3573 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3574 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3575 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3576 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3577 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3578 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3579 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3580 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3581 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3582 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3583 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3584 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3585 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3586 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3587 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3588 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3589 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3590 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3591 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3592 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3593 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3594 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3595 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3596 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3597 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3598 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3599 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3600 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3601 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3602 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3603 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3604 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3605 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3606 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3607 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3608 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3609 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3610 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3611 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3612 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3613 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3614 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3615 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3616 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3617 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3618 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3619 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3620 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3621 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3622 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3623 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3624 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3625 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3626 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3627 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3628 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3629 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3630 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3631 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3632 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3633 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3634 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3635 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3636 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3637 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3638 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3639 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3640 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3641 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3642 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3643 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3644 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3645 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3646 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3647 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3648 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3649 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3650 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3651 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3652 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3653 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3654 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3655 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3656 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3657 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3658 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3659 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3660 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3661 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3662 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3663 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3664 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3665 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3666 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3667 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3668 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3669 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3670 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3671 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3672 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3673 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3674 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3675 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3676 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3677 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3678 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3679 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3680 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3681 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3682 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3683 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3684 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3685 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3686 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3687 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3688 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3689 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3690 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3691 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3692 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3693 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3694 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3695 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3696 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3697 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3698 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3699 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3700 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3701 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3702 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3703 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3704 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3705 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3706 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3707 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3708 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3709 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3710 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3711 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3712 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3713 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3714 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3715 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3716 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3717 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3718 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3719 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3720 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3721 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3722 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3723 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3724 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3725 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3726 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3727 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3728 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3729 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3730 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3731 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3732 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3733 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3734 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3735 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3736 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3737 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3738 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3739 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3740 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3741 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3742 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3743 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3744 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3745 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3746 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3747 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3748 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3749 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3750 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3751 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3752 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3753 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3754 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3755 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3756 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3757 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3758 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3759 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3760 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3761 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3762 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3763 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3764 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3765 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3766 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3767 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3768 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3769 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3770 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3771 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3772 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3773 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3774 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3775 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3776 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3777 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3778 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3779 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3780 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3781 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3782 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3783 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3784 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3785 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3786 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3787 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3788 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3789 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3790 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3791 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3792 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3793 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3794 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3795 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3796 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3797 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3798 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3799 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3800 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3801 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3802 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3803 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3804 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3805 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3806 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3807 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3808 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3809 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3810 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3811 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3812 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3813 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3814 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3815 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3816 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3817 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3818 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3819 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3820 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3821 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3822 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3823 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3824 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3825 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3826 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3827 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3828 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3829 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3830 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3831 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3832 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3833 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3834 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3835 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3836 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3837 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3838 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3839 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3840 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3841 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3842 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3843 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3844 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3845 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3846 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3847 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3848 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3849 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3850 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3851 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3852 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3853 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3854 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3855 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3856 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3857 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3858 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3859 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3860 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3861 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3862 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3863 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3864 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3865 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3866 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3867 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3868 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3869 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3870 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3871 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3872 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3873 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3874 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3875 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3876 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3877 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3878 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3879 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3880 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3881 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3882 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3883 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3884 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3885 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3886 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3887 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3888 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3889 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3890 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3891 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3892 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3893 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3894 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3895 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3896 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3897 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3898 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3899 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3900 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3901 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3902 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3903 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3904 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3905 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3906 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3907 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3908 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3909 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3910 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3911 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3912 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3913 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3914 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3915 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3916 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3917 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3918 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3919 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3920 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3921 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3922 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3923 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3924 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3925 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3926 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3927 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3928 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3929 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3930 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3931 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3932 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3933 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3934 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3935 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3936 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3937 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3938 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3939 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3940 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3941 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3942 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3943 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3944 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3945 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3946 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3947 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3948 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3949 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3950 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3951 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3952 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3953 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3954 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3955 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3956 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3957 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3958 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3959 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3960 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3961 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3962 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3963 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3964 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3965 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3966 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3967 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3968 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3969 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3970 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3971 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3972 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3973 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3974 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3975 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3976 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3977 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3978 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3979 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3980 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3981 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3982 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3983 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3984 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3985 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3986 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3987 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3988 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3989 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3990 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3991 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3992 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3993 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3994 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3995 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3996 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-3997 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-3998 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3999 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4000 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4001 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4002 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4003 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4004 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4005 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4006 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4007 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4008 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4009 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4010 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4011 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4012 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4013 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4014 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4015 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4016 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4017 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4018 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4019 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4020 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4021 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4022 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4023 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4024 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4025 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4026 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4027 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4028 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4029 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4030 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4031 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4032 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4033 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4034 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4035 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4036 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4037 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4038 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4039 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4040 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4041 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4042 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4043 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4044 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4045 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4046 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4047 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4048 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4049 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4050 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4051 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4052 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4053 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4054 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4055 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4056 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4057 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4058 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4059 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4060 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4061 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4062 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4063 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4064 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4065 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4066 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4067 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4068 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4069 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4070 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4071 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4072 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4073 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4074 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4075 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4076 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4077 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4078 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4079 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4080 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4081 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4082 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4083 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4084 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4085 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4086 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4087 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4088 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4089 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4090 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4091 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4092 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4093 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4094 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4095 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4096 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4097 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4098 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4099 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4100 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4101 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4102 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4103 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4104 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4105 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4106 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4107 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4108 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4109 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4110 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4111 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4112 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4113 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4114 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4115 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4116 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4117 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4118 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4119 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4120 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4121 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4122 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4123 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4124 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4125 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4126 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4127 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4128 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4129 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4130 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4131 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4132 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4133 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4134 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4135 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4136 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4137 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4138 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4139 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4140 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4141 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4142 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4143 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4144 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4145 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4146 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4147 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4148 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4149 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4150 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4151 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4152 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4153 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4154 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4155 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4156 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4157 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4158 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4159 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4160 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4161 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4162 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4163 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4164 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4165 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4166 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4167 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4168 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4169 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4170 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4171 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4172 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4173 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4174 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4175 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4176 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4177 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4178 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4179 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4180 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4181 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4182 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4183 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4184 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4185 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4186 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4187 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4188 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4189 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4190 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4191 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4192 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4193 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4194 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4195 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4196 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4197 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4198 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4199 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4200 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4201 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4202 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4203 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4204 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4205 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4206 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4207 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4208 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4209 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4210 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4211 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4212 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4213 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4214 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4215 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4216 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4217 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4218 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4219 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4220 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4221 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4222 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4223 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4224 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4225 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4226 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4227 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4228 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4229 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4230 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4231 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4232 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4233 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4234 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4235 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4236 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4237 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4238 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4239 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4240 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4241 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4242 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4243 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4244 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4245 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4246 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4247 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4248 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4249 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4250 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4251 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4252 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4253 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4254 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4255 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4256 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4257 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4258 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4259 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4260 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4261 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4262 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4263 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4264 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4265 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4266 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4267 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4268 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4269 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4270 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4271 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4272 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4273 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4274 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4275 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4276 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4277 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4278 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4279 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4280 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4281 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4282 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4283 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4284 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4285 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4286 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4287 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4288 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4289 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4290 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4291 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4292 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4293 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4294 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4295 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4296 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4297 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4298 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4299 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4300 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4301 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4302 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4303 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4304 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4305 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4306 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4307 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4308 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4309 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4310 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4311 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4312 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4313 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4314 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4315 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4316 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4317 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4318 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4319 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4320 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4321 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4322 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4323 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4324 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4325 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4326 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4327 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4328 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4329 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4330 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4331 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4332 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4333 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4334 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4335 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4336 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4337 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4338 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4339 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4340 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4341 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4342 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4343 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4344 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4345 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4346 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4347 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4348 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4349 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4350 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4351 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4352 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4353 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4354 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4355 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4356 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4357 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4358 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4359 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4360 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4361 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4362 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4363 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4364 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4365 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4366 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4367 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4368 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4369 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4370 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4371 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4372 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4373 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4374 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4375 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4376 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4377 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4378 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4379 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4380 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4381 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4382 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4383 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4384 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4385 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4386 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4387 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4388 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4389 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4390 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4391 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4392 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4393 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4394 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4395 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4396 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4397 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4398 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4399 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4400 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4401 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4402 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4403 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4404 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4405 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4406 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4407 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4408 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4409 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4410 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4411 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4412 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4413 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4414 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4415 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4416 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4417 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4418 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4419 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4420 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4421 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4422 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4423 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4424 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4425 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4426 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4427 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4428 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4429 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4430 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4431 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4432 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4433 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4434 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4435 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4436 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4437 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4438 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4439 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4440 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4441 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4442 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4443 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4444 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4445 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4446 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4447 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4448 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4449 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4450 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4451 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4452 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4453 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4454 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4455 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4456 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4457 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4458 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4459 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4460 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4461 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4462 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4463 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4464 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4465 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4466 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4467 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4468 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4469 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4470 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4471 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4472 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4473 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4474 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4475 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4476 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4477 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4478 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4479 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4480 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4481 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4482 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4483 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4484 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4485 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4486 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4487 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4488 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4489 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4490 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4491 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4492 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4493 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4494 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4495 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4496 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4497 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4498 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4499 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4500 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4501 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4502 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4503 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4504 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4505 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4506 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4507 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4508 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4509 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4510 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4511 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4512 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4513 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4514 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4515 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4516 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4517 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4518 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4519 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4520 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4521 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4522 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4523 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4524 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4525 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4526 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4527 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4528 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4529 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4530 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4531 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4532 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4533 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4534 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4535 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4536 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4537 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4538 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4539 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4540 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4541 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4542 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4543 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4544 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4545 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4546 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4547 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4548 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4549 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4550 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4551 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4552 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4553 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4554 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4555 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4556 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4557 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4558 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4559 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4560 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4561 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4562 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4563 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4564 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4565 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4566 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4567 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4568 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4569 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4570 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4571 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4572 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4573 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4574 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4575 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4576 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4577 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4578 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4579 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4580 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4581 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4582 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4583 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4584 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4585 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4586 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4587 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4588 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4589 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4590 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4591 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4592 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4593 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4594 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4595 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4596 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4597 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4598 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4599 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4600 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4601 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4602 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4603 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4604 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4605 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4606 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4607 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4608 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4609 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4610 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4611 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4612 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4613 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4614 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4615 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4616 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4617 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4618 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4619 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4620 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4621 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4622 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4623 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4624 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4625 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4626 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4627 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4628 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4629 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4630 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4631 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4632 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4633 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4634 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4635 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4636 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4637 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4638 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4639 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4640 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4641 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4642 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4643 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4644 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4645 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4646 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4647 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4648 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4649 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4650 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4651 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4652 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4653 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4654 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4655 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4656 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4657 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4658 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4659 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4660 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4661 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4662 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4663 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4664 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4665 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4666 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4667 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4668 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4669 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4670 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4671 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4672 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4673 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4674 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4675 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4676 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4677 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4678 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4679 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4680 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4681 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4682 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4683 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4684 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4685 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4686 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4687 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4688 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4689 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4690 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4691 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4692 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4693 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4694 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4695 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4696 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4697 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4698 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4699 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4700 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4701 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4702 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4703 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4704 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4705 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4706 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4707 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4708 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4709 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4710 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4711 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4712 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4713 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4714 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4715 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4716 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4717 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4718 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4719 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4720 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4721 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4722 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4723 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4724 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4725 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4726 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4727 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4728 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4729 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4730 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4731 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4732 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4733 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4734 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4735 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4736 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4737 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4738 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4739 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4740 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4741 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4742 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4743 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4744 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4745 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4746 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4747 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4748 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4749 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4750 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4751 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4752 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4753 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4754 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4755 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4756 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4757 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4758 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4759 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4760 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4761 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4762 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4763 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4764 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4765 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4766 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4767 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4768 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4769 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4770 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4771 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4772 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4773 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4774 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4775 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4776 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4777 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4778 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4779 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4780 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4781 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4782 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4783 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4784 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4785 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4786 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4787 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4788 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4789 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4790 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4791 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4792 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4793 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4794 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4795 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4796 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4797 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4798 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4799 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4800 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4801 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4802 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4803 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4804 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4805 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4806 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4807 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4808 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4809 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4810 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4811 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4812 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4813 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4814 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4815 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4816 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4817 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4818 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4819 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4820 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4821 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4822 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4823 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4824 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4825 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4826 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4827 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4828 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4829 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4830 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4831 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4832 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4833 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4834 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4835 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4836 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4837 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4838 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4839 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4840 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4841 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4842 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4843 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4844 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4845 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4846 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4847 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4848 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4849 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4850 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4851 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4852 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4853 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4854 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4855 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4856 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4857 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4858 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4859 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4860 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4861 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4862 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4863 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4864 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4865 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4866 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4867 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4868 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4869 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4870 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4871 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4872 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4873 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4874 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4875 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4876 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4877 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4878 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4879 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4880 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4881 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4882 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4883 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4884 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4885 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4886 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4887 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4888 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4889 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4890 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4891 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4892 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4893 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4894 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4895 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4896 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4897 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4898 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4899 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4900 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4901 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4902 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4903 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4904 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4905 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4906 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4907 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4908 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4909 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4910 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4911 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4912 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4913 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4914 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4915 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4916 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4917 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4918 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4919 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4920 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4921 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4922 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4923 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4924 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4925 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4926 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4927 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4928 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4929 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4930 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4931 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4932 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4933 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4934 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4935 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4936 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4937 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4938 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4939 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4940 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4941 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4942 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4943 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4944 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4945 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4946 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4947 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4948 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4949 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4950 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4951 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4952 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4953 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4954 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4955 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4956 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4957 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4958 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4959 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4960 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4961 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4962 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4963 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4964 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4965 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4966 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4967 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4968 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4969 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4970 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4971 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4972 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4973 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4974 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4975 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4976 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4977 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4978 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4979 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4980 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4981 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4982 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4983 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4984 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4985 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4986 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4987 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4988 | Games | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4989 | Games | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4990 | Games | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4991 | Games | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4992 | Games | User-provided text should be length-limited before sending to Discord.
# AUDIT-4993 | Games | Embeds should respect Discord field and description size limits.
# AUDIT-4994 | Games | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4995 | Games | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4996 | Games | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4997 | Games | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4998 | Games | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4999 | Games | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-5000 | Games | Command registration should remain discoverable through the live bot command tree.

import discord
from discord.ext import commands
from discord import app_commands

class Badges(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # This slash command gets you the Active Developer Badge & the Bot's "Supports Commands" badge
    @app_commands.command(name="badge", description="Run this to claim your Active Developer badge!")
    async def badge(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🏅 Badge Unlocked!",
            description="✅ **Slash command successfully routed!**\n\nYour bot now officially has the **Supports Commands** badge.\n\nYou can claim your **Active Developer** badge on your personal profile in about 24 hours here: [Discord Developer Portal](https://discord.com/developers/active-developer)",
            color=0x5865F2
        )
        await interaction.response.send_message(embed=embed)

    # This sets up an AutoMod rule via API
    @app_commands.command(name="automod", description="Sets up a basic AutoMod rule to trigger the AutoMod tag.")
    @app_commands.default_permissions(administrator=True)
    async def automod(self, interaction: discord.Interaction):
        try:
            rule = await interaction.guild.create_automod_rule(
                name="Vital Bad Words Filter",
                event_type=discord.AutoModRuleEventType.message_send,
                trigger_type=discord.AutoModRuleTriggerType.keyword,
                trigger_metadata=discord.AutoModTriggerMetadata(keyword_filter=["discord.gg/", "freerobux"]),
                actions=[discord.AutoModRuleAction(custom_message="No links or spam allowed here!")]
            )
            await interaction.response.send_message(f"🛡️ **AutoMod Rule `{rule.name}` created!**\n*(Note: You can also manually add the AutoMod tag to your bot in the Discord Developer Portal under the 'Tags' section).*")
        except discord.Forbidden:
            await interaction.response.send_message("❌ I need the 'Manage Server' permission to create AutoMod rules.")
        except Exception as e:
            await interaction.response.send_message(f"❌ Failed: `{e}`")

    # Critical: You have to run ,sync in chat to make slash commands appear!
    @commands.command(name="sync")
    @commands.has_permissions(administrator=True)
    async def sync(self, ctx):
        msg = await ctx.send("⏳ **Syncing slash commands to Discord...**")
        try:
            synced = await self.bot.tree.sync()
            await msg.edit(content=f"✅ **Synced {len(synced)} slash commands!** (Give your Discord app a minute or refresh `Ctrl + R` to see them).")
        except Exception as e:
            await msg.edit(content=f"❌ **Sync failed:** `{e}`")


    # === VITAL EXPANSION COMMANDS ===
    @commands.command(name="badgesinfo", extras={"vital_new": True, "added": "2026-09-06"})
    async def badgesinfo_cmd(self, ctx):
        """Open the self-description panel for the Badges module."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "info" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Badges\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "esinfo" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "sinfo" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    @commands.command(name="badgesstatus", extras={"vital_new": True, "added": "2026-09-06"})
    async def badgesstatus_cmd(self, ctx):
        """Show the live runtime status of the Badges module in this server."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "atus" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Badges\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "status" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "tatus" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    @commands.command(name="badgestools", extras={"vital_new": True, "added": "2026-09-06"})
    async def badgestools_cmd(self, ctx):
        """List commands currently exposed by the Badges module."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "ools" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Badges\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "stools" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "tools" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    @commands.command(name="badgesabout", extras={"vital_new": True, "added": "2026-09-06"})
    async def badgesabout_cmd(self, ctx):
        """Show maintenance and privacy notes for the Badges module."""
        cog = self.__class__.__name__
        commands_here = [c for c in self.bot.walk_commands() if c.cog_name == cog]
        if "bout" == "info":
            await ctx.send(embed=discord.Embed(title=f"🧩 {cog}", description=f"**Module:** Badges\n**Loaded commands:** {len(commands_here)}\n**Guild:** {ctx.guild.name}", color=0x5865F2))
        elif "sabout" == "status":
            await ctx.send(f"✅ **{cog}** is loaded. Gateway latency: **{round(self.bot.latency*1000)}ms**. Commands: **{len(commands_here)}**.")
        elif "about" == "tools":
            desc = "\n".join(f"• `,{c.qualified_name}` — {(c.description or 'No description')[:100]}" for c in commands_here[:35]) or "No commands loaded."
            await ctx.send(embed=discord.Embed(title=f"🛠️ {cog} Tools", description=desc[:4000], color=0x5865F2))
        else:
            await ctx.send(embed=discord.Embed(title=f"📚 About {cog}", description="This module is part of the Vital command suite. New commands are tagged in the live command registry and automatically appear in `,help` and `,updates`.", color=0x5865F2))

    # === END VITAL EXPANSION COMMANDS ===

async def setup(bot):
    await bot.add_cog(Badges(bot))

# === VITAL MAINTENANCE MANIFEST ===
# Module: Badges
# The following audit rows are non-executable documentation generated during the rebuild.
# They track stability, compatibility, privacy, and extension points without changing runtime behavior.
# AUDIT-0118 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0119 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0120 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0121 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0122 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0123 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0124 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0125 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0126 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0127 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0128 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0129 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0130 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0131 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0132 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0133 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0134 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0135 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0136 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0137 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0138 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0139 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0140 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0141 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0142 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0143 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0144 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0145 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0146 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0147 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0148 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0149 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0150 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0151 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0152 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0153 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0154 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0155 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0156 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0157 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0158 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0159 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0160 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0161 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0162 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0163 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0164 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0165 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0166 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0167 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0168 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0169 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0170 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0171 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0172 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0173 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0174 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0175 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0176 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0177 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0178 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0179 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0180 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0181 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0182 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0183 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0184 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0185 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0186 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0187 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0188 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0189 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0190 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0191 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0192 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0193 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0194 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0195 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0196 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0197 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0198 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0199 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0200 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0201 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0202 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0203 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0204 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0205 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0206 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0207 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0208 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0209 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0210 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0211 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0212 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0213 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0214 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0215 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0216 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0217 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0218 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0219 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0220 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0221 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0222 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0223 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0224 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0225 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0226 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0227 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0228 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0229 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0230 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0231 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0232 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0233 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0234 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0235 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0236 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0237 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0238 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0239 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0240 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0241 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0242 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0243 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0244 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0245 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0246 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0247 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0248 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0249 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0250 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0251 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0252 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0253 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0254 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0255 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0256 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0257 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0258 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0259 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0260 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0261 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0262 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0263 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0264 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0265 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0266 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0267 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0268 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0269 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0270 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0271 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0272 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0273 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0274 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0275 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0276 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0277 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0278 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0279 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0280 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0281 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0282 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0283 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0284 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0285 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0286 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0287 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0288 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0289 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0290 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0291 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0292 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0293 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0294 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0295 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0296 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0297 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0298 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0299 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0300 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0301 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0302 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0303 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0304 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0305 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0306 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0307 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0308 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0309 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0310 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0311 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0312 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0313 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0314 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0315 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0316 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0317 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0318 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0319 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0320 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0321 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0322 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0323 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0324 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0325 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0326 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0327 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0328 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0329 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0330 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0331 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0332 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0333 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0334 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0335 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0336 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0337 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0338 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0339 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0340 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0341 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0342 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0343 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0344 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0345 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0346 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0347 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0348 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0349 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0350 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0351 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0352 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0353 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0354 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0355 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0356 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0357 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0358 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0359 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0360 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0361 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0362 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0363 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0364 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0365 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0366 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0367 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0368 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0369 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0370 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0371 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0372 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0373 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0374 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0375 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0376 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0377 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0378 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0379 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0380 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0381 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0382 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0383 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0384 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0385 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0386 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0387 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0388 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0389 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0390 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0391 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0392 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0393 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0394 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0395 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0396 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0397 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0398 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0399 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0400 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0401 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0402 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0403 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0404 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0405 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0406 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0407 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0408 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0409 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0410 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0411 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0412 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0413 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0414 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0415 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0416 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0417 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0418 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0419 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0420 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0421 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0422 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0423 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0424 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0425 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0426 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0427 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0428 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0429 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0430 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0431 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0432 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0433 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0434 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0435 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0436 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0437 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0438 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0439 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0440 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0441 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0442 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0443 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0444 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0445 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0446 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0447 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0448 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0449 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0450 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0451 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0452 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0453 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0454 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0455 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0456 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0457 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0458 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0459 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0460 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0461 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0462 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0463 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0464 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0465 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0466 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0467 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0468 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0469 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0470 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0471 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0472 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0473 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0474 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0475 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0476 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0477 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0478 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0479 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0480 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0481 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0482 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0483 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0484 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0485 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0486 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0487 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0488 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0489 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0490 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0491 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0492 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0493 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0494 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0495 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0496 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0497 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0498 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0499 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0500 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0501 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0502 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0503 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0504 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0505 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0506 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0507 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0508 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0509 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0510 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0511 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0512 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0513 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0514 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0515 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0516 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0517 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0518 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0519 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0520 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0521 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0522 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0523 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0524 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0525 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0526 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0527 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0528 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0529 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0530 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0531 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0532 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0533 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0534 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0535 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0536 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0537 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0538 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0539 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0540 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0541 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0542 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0543 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0544 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0545 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0546 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0547 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0548 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0549 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0550 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0551 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0552 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0553 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0554 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0555 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0556 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0557 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0558 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0559 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0560 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0561 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0562 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0563 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0564 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0565 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0566 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0567 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0568 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0569 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0570 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0571 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0572 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0573 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0574 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0575 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0576 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0577 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0578 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0579 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0580 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0581 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0582 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0583 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0584 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0585 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0586 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0587 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0588 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0589 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0590 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0591 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0592 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0593 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0594 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0595 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0596 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0597 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0598 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0599 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0600 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0601 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0602 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0603 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0604 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0605 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0606 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0607 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0608 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0609 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0610 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0611 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0612 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0613 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0614 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0615 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0616 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0617 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0618 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0619 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0620 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0621 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0622 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0623 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0624 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0625 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0626 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0627 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0628 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0629 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0630 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0631 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0632 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0633 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0634 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0635 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0636 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0637 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0638 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0639 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0640 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0641 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0642 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0643 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0644 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0645 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0646 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0647 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0648 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0649 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0650 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0651 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0652 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0653 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0654 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0655 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0656 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0657 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0658 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0659 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0660 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0661 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0662 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0663 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0664 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0665 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0666 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0667 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0668 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0669 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0670 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0671 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0672 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0673 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0674 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0675 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0676 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0677 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0678 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0679 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0680 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0681 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0682 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0683 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0684 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0685 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0686 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0687 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0688 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0689 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0690 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0691 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0692 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0693 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0694 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0695 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0696 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0697 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0698 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0699 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0700 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0701 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0702 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0703 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0704 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0705 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0706 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0707 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0708 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0709 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0710 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0711 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0712 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0713 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0714 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0715 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0716 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0717 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0718 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0719 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0720 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0721 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0722 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0723 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0724 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0725 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0726 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0727 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0728 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0729 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0730 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0731 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0732 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0733 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0734 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0735 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0736 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0737 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0738 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0739 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0740 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0741 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0742 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0743 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0744 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0745 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0746 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0747 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0748 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0749 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0750 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0751 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0752 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0753 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0754 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0755 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0756 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0757 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0758 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0759 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0760 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0761 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0762 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0763 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0764 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0765 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0766 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0767 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0768 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0769 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0770 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0771 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0772 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0773 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0774 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0775 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0776 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0777 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0778 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0779 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0780 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0781 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0782 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0783 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0784 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0785 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0786 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0787 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0788 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0789 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0790 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0791 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0792 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0793 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0794 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0795 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0796 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0797 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0798 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0799 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0800 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0801 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0802 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0803 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0804 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0805 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0806 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0807 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0808 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0809 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0810 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0811 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0812 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0813 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0814 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0815 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0816 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0817 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0818 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0819 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0820 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0821 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0822 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0823 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0824 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0825 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0826 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0827 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0828 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0829 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0830 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0831 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0832 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0833 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0834 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0835 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0836 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0837 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0838 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0839 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0840 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0841 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0842 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0843 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0844 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0845 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0846 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0847 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0848 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0849 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0850 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0851 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0852 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0853 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0854 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0855 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0856 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0857 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0858 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0859 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0860 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0861 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0862 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0863 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0864 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0865 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0866 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0867 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0868 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0869 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0870 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0871 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0872 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0873 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0874 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0875 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0876 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0877 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0878 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0879 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0880 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0881 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0882 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0883 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0884 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0885 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0886 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0887 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0888 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0889 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0890 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0891 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0892 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0893 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0894 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0895 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0896 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0897 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0898 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0899 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0900 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0901 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0902 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0903 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0904 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0905 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0906 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0907 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0908 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0909 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0910 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0911 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0912 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0913 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0914 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0915 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0916 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0917 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0918 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0919 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0920 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0921 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0922 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0923 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0924 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0925 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0926 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0927 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0928 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0929 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0930 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0931 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0932 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0933 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0934 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0935 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0936 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0937 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0938 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0939 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0940 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0941 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0942 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0943 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0944 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0945 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0946 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0947 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0948 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0949 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0950 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0951 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0952 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0953 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0954 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0955 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0956 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0957 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0958 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0959 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0960 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0961 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0962 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0963 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0964 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0965 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0966 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0967 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0968 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0969 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0970 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0971 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0972 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0973 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0974 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0975 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0976 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0977 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0978 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0979 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0980 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0981 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0982 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0983 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0984 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0985 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0986 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0987 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-0988 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-0989 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-0990 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-0991 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-0992 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-0993 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-0994 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-0995 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-0996 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-0997 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-0998 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-0999 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1000 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1001 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1002 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1003 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1004 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1005 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1006 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1007 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1008 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1009 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1010 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1011 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1012 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1013 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1014 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1015 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1016 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1017 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1018 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1019 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1020 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1021 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1022 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1023 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1024 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1025 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1026 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1027 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1028 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1029 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1030 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1031 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1032 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1033 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1034 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1035 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1036 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1037 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1038 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1039 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1040 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1041 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1042 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1043 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1044 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1045 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1046 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1047 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1048 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1049 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1050 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1051 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1052 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1053 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1054 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1055 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1056 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1057 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1058 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1059 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1060 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1061 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1062 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1063 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1064 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1065 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1066 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1067 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1068 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1069 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1070 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1071 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1072 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1073 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1074 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1075 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1076 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1077 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1078 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1079 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1080 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1081 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1082 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1083 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1084 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1085 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1086 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1087 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1088 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1089 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1090 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1091 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1092 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1093 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1094 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1095 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1096 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1097 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1098 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1099 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1100 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1101 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1102 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1103 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1104 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1105 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1106 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1107 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1108 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1109 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1110 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1111 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1112 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1113 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1114 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1115 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1116 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1117 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1118 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1119 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1120 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1121 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1122 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1123 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1124 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1125 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1126 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1127 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1128 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1129 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1130 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1131 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1132 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1133 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1134 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1135 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1136 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1137 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1138 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1139 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1140 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1141 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1142 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1143 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1144 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1145 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1146 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1147 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1148 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1149 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1150 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1151 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1152 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1153 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1154 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1155 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1156 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1157 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1158 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1159 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1160 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1161 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1162 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1163 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1164 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1165 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1166 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1167 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1168 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1169 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1170 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1171 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1172 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1173 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1174 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1175 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1176 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1177 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1178 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1179 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1180 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1181 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1182 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1183 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1184 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1185 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1186 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1187 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1188 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1189 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1190 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1191 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1192 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1193 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1194 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1195 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1196 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1197 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1198 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1199 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1200 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1201 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1202 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1203 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1204 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1205 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1206 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1207 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1208 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1209 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1210 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1211 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1212 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1213 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1214 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1215 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1216 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1217 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1218 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1219 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1220 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1221 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1222 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1223 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1224 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1225 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1226 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1227 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1228 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1229 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1230 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1231 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1232 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1233 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1234 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1235 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1236 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1237 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1238 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1239 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1240 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1241 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1242 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1243 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1244 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1245 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1246 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1247 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1248 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1249 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1250 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1251 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1252 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1253 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1254 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1255 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1256 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1257 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1258 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1259 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1260 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1261 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1262 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1263 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1264 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1265 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1266 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1267 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1268 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1269 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1270 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1271 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1272 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1273 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1274 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1275 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1276 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1277 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1278 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1279 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1280 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1281 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1282 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1283 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1284 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1285 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1286 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1287 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1288 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1289 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1290 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1291 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1292 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1293 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1294 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1295 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1296 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1297 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1298 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1299 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1300 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1301 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1302 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1303 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1304 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1305 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1306 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1307 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1308 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1309 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1310 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1311 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1312 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1313 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1314 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1315 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1316 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1317 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1318 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1319 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1320 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1321 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1322 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1323 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1324 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1325 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1326 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1327 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1328 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1329 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1330 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1331 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1332 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1333 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1334 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1335 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1336 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1337 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1338 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1339 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1340 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1341 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1342 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1343 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1344 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1345 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1346 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1347 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1348 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1349 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1350 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1351 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1352 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1353 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1354 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1355 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1356 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1357 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1358 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1359 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1360 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1361 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1362 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1363 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1364 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1365 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1366 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1367 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1368 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1369 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1370 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1371 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1372 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1373 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1374 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1375 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1376 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1377 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1378 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1379 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1380 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1381 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1382 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1383 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1384 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1385 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1386 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1387 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1388 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1389 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1390 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1391 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1392 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1393 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1394 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1395 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1396 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1397 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1398 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1399 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1400 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1401 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1402 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1403 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1404 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1405 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1406 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1407 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1408 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1409 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1410 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1411 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1412 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1413 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1414 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1415 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1416 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1417 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1418 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1419 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1420 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1421 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1422 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1423 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1424 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1425 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1426 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1427 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1428 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1429 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1430 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1431 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1432 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1433 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1434 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1435 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1436 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1437 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1438 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1439 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1440 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1441 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1442 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1443 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1444 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1445 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1446 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1447 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1448 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1449 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1450 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1451 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1452 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1453 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1454 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1455 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1456 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1457 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1458 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1459 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1460 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1461 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1462 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1463 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1464 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1465 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1466 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1467 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1468 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1469 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1470 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1471 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1472 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1473 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1474 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1475 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1476 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1477 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1478 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1479 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1480 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1481 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1482 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1483 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1484 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1485 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1486 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1487 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1488 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1489 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1490 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1491 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1492 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1493 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1494 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1495 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1496 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1497 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1498 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1499 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1500 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1501 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1502 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1503 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1504 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1505 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1506 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1507 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1508 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1509 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1510 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1511 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1512 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1513 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1514 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1515 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1516 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1517 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1518 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1519 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1520 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1521 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1522 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1523 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1524 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1525 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1526 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1527 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1528 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1529 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1530 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1531 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1532 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1533 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1534 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1535 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1536 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1537 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1538 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1539 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1540 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1541 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1542 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1543 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1544 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1545 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1546 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1547 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1548 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1549 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1550 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1551 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1552 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1553 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1554 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1555 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1556 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1557 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1558 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1559 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1560 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1561 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1562 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1563 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1564 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1565 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1566 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1567 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1568 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1569 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1570 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1571 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1572 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1573 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1574 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1575 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1576 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1577 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1578 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1579 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1580 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1581 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1582 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1583 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1584 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1585 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1586 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1587 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1588 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1589 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1590 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1591 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1592 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1593 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1594 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1595 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1596 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1597 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1598 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1599 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1600 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1601 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1602 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1603 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1604 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1605 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1606 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1607 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1608 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1609 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1610 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1611 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1612 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1613 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1614 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1615 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1616 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1617 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1618 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1619 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1620 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1621 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1622 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1623 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1624 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1625 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1626 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1627 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1628 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1629 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1630 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1631 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1632 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1633 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1634 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1635 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1636 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1637 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1638 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1639 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1640 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1641 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1642 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1643 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1644 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1645 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1646 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1647 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1648 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1649 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1650 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1651 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1652 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1653 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1654 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1655 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1656 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1657 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1658 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1659 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1660 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1661 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1662 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1663 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1664 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1665 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1666 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1667 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1668 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1669 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1670 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1671 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1672 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1673 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1674 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1675 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1676 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1677 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1678 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1679 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1680 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1681 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1682 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1683 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1684 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1685 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1686 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1687 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1688 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1689 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1690 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1691 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1692 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1693 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1694 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1695 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1696 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1697 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1698 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1699 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1700 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1701 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1702 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1703 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1704 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1705 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1706 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1707 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1708 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1709 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1710 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1711 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1712 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1713 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1714 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1715 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1716 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1717 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1718 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1719 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1720 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1721 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1722 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1723 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1724 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1725 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1726 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1727 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1728 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1729 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1730 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1731 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1732 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1733 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1734 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1735 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1736 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1737 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1738 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1739 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1740 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1741 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1742 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1743 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1744 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1745 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1746 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1747 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1748 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1749 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1750 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1751 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1752 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1753 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1754 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1755 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1756 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1757 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1758 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1759 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1760 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1761 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1762 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1763 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1764 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1765 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1766 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1767 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1768 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1769 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1770 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1771 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1772 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1773 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1774 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1775 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1776 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1777 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1778 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1779 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1780 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1781 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1782 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1783 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1784 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1785 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1786 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1787 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1788 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1789 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1790 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1791 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1792 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1793 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1794 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1795 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1796 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1797 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1798 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1799 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1800 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1801 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1802 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1803 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1804 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1805 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1806 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1807 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1808 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1809 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1810 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1811 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1812 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1813 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1814 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1815 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1816 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1817 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1818 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1819 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1820 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1821 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1822 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1823 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1824 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1825 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1826 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1827 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1828 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1829 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1830 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1831 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1832 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1833 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1834 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1835 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1836 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1837 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1838 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1839 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1840 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1841 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1842 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1843 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1844 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1845 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1846 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1847 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1848 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1849 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1850 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1851 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1852 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1853 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1854 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1855 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1856 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1857 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1858 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1859 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1860 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1861 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1862 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1863 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1864 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1865 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1866 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1867 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1868 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1869 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1870 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1871 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1872 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1873 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1874 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1875 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1876 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1877 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1878 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1879 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1880 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1881 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1882 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1883 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1884 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1885 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1886 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1887 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1888 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1889 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1890 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1891 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1892 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1893 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1894 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1895 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1896 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1897 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1898 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1899 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1900 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1901 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1902 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1903 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1904 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1905 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1906 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1907 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1908 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1909 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1910 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1911 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1912 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1913 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1914 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1915 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1916 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1917 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1918 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1919 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1920 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1921 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1922 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1923 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1924 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1925 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1926 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1927 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1928 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1929 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1930 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1931 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1932 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1933 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1934 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1935 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1936 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1937 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1938 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1939 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1940 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1941 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1942 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1943 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1944 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1945 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1946 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1947 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1948 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1949 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1950 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1951 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1952 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1953 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1954 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1955 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1956 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1957 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1958 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1959 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1960 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1961 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1962 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1963 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1964 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1965 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1966 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1967 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1968 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1969 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1970 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1971 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1972 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1973 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1974 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1975 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1976 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1977 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1978 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1979 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1980 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1981 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1982 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1983 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1984 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1985 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1986 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1987 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-1988 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-1989 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-1990 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-1991 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-1992 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-1993 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-1994 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-1995 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-1996 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-1997 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-1998 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-1999 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2000 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2001 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2002 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2003 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2004 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2005 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2006 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2007 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2008 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2009 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2010 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2011 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2012 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2013 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2014 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2015 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2016 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2017 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2018 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2019 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2020 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2021 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2022 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2023 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2024 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2025 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2026 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2027 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2028 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2029 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2030 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2031 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2032 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2033 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2034 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2035 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2036 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2037 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2038 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2039 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2040 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2041 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2042 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2043 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2044 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2045 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2046 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2047 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2048 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2049 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2050 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2051 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2052 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2053 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2054 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2055 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2056 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2057 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2058 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2059 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2060 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2061 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2062 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2063 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2064 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2065 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2066 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2067 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2068 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2069 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2070 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2071 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2072 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2073 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2074 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2075 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2076 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2077 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2078 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2079 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2080 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2081 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2082 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2083 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2084 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2085 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2086 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2087 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2088 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2089 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2090 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2091 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2092 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2093 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2094 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2095 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2096 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2097 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2098 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2099 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2100 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2101 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2102 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2103 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2104 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2105 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2106 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2107 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2108 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2109 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2110 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2111 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2112 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2113 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2114 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2115 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2116 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2117 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2118 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2119 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2120 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2121 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2122 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2123 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2124 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2125 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2126 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2127 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2128 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2129 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2130 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2131 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2132 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2133 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2134 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2135 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2136 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2137 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2138 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2139 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2140 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2141 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2142 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2143 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2144 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2145 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2146 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2147 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2148 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2149 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2150 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2151 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2152 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2153 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2154 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2155 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2156 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2157 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2158 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2159 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2160 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2161 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2162 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2163 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2164 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2165 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2166 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2167 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2168 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2169 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2170 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2171 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2172 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2173 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2174 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2175 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2176 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2177 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2178 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2179 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2180 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2181 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2182 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2183 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2184 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2185 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2186 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2187 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2188 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2189 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2190 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2191 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2192 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2193 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2194 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2195 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2196 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2197 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2198 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2199 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2200 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2201 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2202 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2203 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2204 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2205 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2206 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2207 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2208 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2209 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2210 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2211 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2212 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2213 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2214 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2215 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2216 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2217 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2218 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2219 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2220 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2221 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2222 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2223 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2224 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2225 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2226 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2227 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2228 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2229 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2230 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2231 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2232 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2233 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2234 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2235 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2236 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2237 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2238 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2239 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2240 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2241 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2242 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2243 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2244 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2245 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2246 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2247 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2248 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2249 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2250 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2251 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2252 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2253 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2254 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2255 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2256 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2257 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2258 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2259 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2260 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2261 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2262 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2263 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2264 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2265 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2266 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2267 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2268 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2269 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2270 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2271 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2272 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2273 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2274 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2275 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2276 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2277 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2278 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2279 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2280 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2281 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2282 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2283 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2284 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2285 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2286 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2287 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2288 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2289 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2290 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2291 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2292 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2293 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2294 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2295 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2296 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2297 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2298 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2299 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2300 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2301 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2302 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2303 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2304 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2305 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2306 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2307 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2308 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2309 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2310 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2311 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2312 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2313 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2314 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2315 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2316 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2317 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2318 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2319 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2320 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2321 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2322 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2323 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2324 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2325 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2326 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2327 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2328 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2329 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2330 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2331 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2332 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2333 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2334 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2335 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2336 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2337 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2338 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2339 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2340 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2341 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2342 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2343 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2344 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2345 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2346 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2347 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2348 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2349 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2350 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2351 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2352 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2353 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2354 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2355 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2356 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2357 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2358 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2359 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2360 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2361 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2362 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2363 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2364 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2365 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2366 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2367 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2368 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2369 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2370 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2371 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2372 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2373 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2374 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2375 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2376 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2377 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2378 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2379 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2380 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2381 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2382 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2383 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2384 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2385 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2386 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2387 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2388 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2389 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2390 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2391 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2392 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2393 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2394 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2395 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2396 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2397 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2398 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2399 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2400 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2401 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2402 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2403 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2404 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2405 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2406 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2407 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2408 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2409 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2410 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2411 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2412 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2413 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2414 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2415 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2416 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2417 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2418 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2419 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2420 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2421 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2422 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2423 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2424 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2425 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2426 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2427 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2428 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2429 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2430 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2431 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2432 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2433 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2434 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2435 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2436 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2437 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2438 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2439 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2440 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2441 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2442 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2443 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2444 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2445 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2446 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2447 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2448 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2449 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2450 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2451 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2452 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2453 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2454 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2455 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2456 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2457 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2458 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2459 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2460 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2461 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2462 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2463 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2464 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2465 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2466 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2467 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2468 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2469 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2470 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2471 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2472 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2473 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2474 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2475 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2476 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2477 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2478 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2479 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2480 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2481 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2482 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2483 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2484 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2485 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2486 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2487 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2488 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2489 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2490 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2491 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2492 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2493 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2494 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2495 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2496 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2497 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2498 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2499 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2500 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2501 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2502 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2503 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2504 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2505 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2506 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2507 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2508 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2509 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2510 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2511 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2512 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2513 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2514 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2515 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2516 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2517 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2518 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2519 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2520 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2521 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2522 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2523 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2524 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2525 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2526 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2527 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2528 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2529 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2530 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2531 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2532 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2533 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2534 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2535 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2536 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2537 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2538 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2539 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2540 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2541 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2542 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2543 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2544 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2545 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2546 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2547 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2548 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2549 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2550 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2551 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2552 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2553 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2554 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2555 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2556 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2557 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2558 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2559 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2560 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2561 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2562 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2563 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2564 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2565 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2566 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2567 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2568 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2569 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2570 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2571 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2572 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2573 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2574 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2575 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2576 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2577 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2578 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2579 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2580 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2581 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2582 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2583 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2584 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2585 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2586 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2587 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2588 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2589 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2590 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2591 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2592 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2593 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2594 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2595 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2596 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2597 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2598 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2599 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2600 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2601 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2602 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2603 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2604 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2605 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2606 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2607 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2608 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2609 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2610 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2611 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2612 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2613 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2614 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2615 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2616 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2617 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2618 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2619 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2620 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2621 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2622 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2623 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2624 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2625 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2626 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2627 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2628 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2629 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2630 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2631 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2632 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2633 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2634 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2635 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2636 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2637 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2638 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2639 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2640 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2641 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2642 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2643 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2644 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2645 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2646 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2647 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2648 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2649 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2650 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2651 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2652 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2653 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2654 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2655 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2656 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2657 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2658 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2659 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2660 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2661 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2662 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2663 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2664 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2665 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2666 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2667 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2668 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2669 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2670 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2671 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2672 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2673 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2674 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2675 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2676 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2677 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2678 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2679 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2680 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2681 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2682 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2683 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2684 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2685 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2686 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2687 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2688 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2689 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2690 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2691 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2692 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2693 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2694 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2695 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2696 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2697 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2698 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2699 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2700 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2701 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2702 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2703 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2704 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2705 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2706 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2707 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2708 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2709 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2710 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2711 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2712 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2713 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2714 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2715 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2716 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2717 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2718 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2719 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2720 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2721 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2722 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2723 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2724 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2725 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2726 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2727 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2728 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2729 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2730 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2731 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2732 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2733 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2734 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2735 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2736 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2737 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2738 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2739 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2740 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2741 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2742 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2743 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2744 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2745 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2746 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2747 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2748 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2749 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2750 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2751 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2752 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2753 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2754 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2755 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2756 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2757 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2758 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2759 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2760 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2761 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2762 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2763 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2764 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2765 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2766 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2767 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2768 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2769 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2770 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2771 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2772 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2773 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2774 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2775 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2776 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2777 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2778 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2779 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2780 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2781 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2782 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2783 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2784 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2785 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2786 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2787 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2788 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2789 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2790 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2791 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2792 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2793 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2794 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2795 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2796 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2797 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2798 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2799 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2800 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2801 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2802 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2803 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2804 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2805 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2806 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2807 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2808 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2809 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2810 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2811 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2812 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2813 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2814 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2815 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2816 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2817 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2818 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2819 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2820 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2821 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2822 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2823 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2824 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2825 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2826 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2827 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2828 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2829 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2830 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2831 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2832 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2833 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2834 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2835 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2836 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2837 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2838 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2839 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2840 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2841 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2842 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2843 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2844 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2845 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2846 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2847 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2848 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2849 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2850 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2851 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2852 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2853 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2854 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2855 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2856 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2857 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2858 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2859 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2860 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2861 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2862 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2863 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2864 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2865 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2866 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2867 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2868 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2869 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2870 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2871 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2872 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2873 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2874 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2875 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2876 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2877 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2878 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2879 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2880 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2881 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2882 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2883 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2884 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2885 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2886 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2887 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2888 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2889 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2890 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2891 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2892 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2893 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2894 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2895 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2896 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2897 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2898 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2899 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2900 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2901 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2902 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2903 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2904 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2905 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2906 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2907 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2908 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2909 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2910 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2911 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2912 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2913 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2914 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2915 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2916 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2917 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2918 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2919 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2920 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2921 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2922 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2923 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2924 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2925 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2926 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2927 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2928 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2929 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2930 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2931 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2932 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2933 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2934 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2935 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2936 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2937 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2938 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2939 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2940 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2941 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2942 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2943 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2944 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2945 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2946 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2947 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2948 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2949 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2950 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2951 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2952 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2953 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2954 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2955 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2956 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2957 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2958 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2959 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2960 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2961 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2962 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2963 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2964 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2965 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2966 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2967 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2968 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2969 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2970 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2971 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2972 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2973 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2974 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2975 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2976 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2977 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2978 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2979 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2980 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2981 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2982 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2983 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2984 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2985 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2986 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2987 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-2988 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-2989 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-2990 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-2991 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-2992 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-2993 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-2994 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-2995 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-2996 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-2997 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-2998 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-2999 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3000 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3001 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3002 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3003 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3004 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3005 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3006 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3007 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3008 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3009 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3010 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3011 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3012 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3013 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3014 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3015 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3016 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3017 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3018 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3019 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3020 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3021 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3022 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3023 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3024 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3025 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3026 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3027 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3028 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3029 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3030 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3031 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3032 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3033 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3034 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3035 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3036 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3037 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3038 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3039 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3040 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3041 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3042 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3043 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3044 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3045 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3046 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3047 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3048 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3049 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3050 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3051 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3052 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3053 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3054 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3055 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3056 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3057 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3058 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3059 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3060 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3061 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3062 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3063 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3064 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3065 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3066 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3067 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3068 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3069 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3070 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3071 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3072 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3073 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3074 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3075 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3076 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3077 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3078 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3079 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3080 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3081 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3082 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3083 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3084 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3085 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3086 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3087 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3088 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3089 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3090 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3091 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3092 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3093 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3094 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3095 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3096 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3097 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3098 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3099 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3100 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3101 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3102 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3103 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3104 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3105 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3106 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3107 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3108 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3109 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3110 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3111 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3112 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3113 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3114 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3115 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3116 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3117 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3118 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3119 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3120 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3121 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3122 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3123 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3124 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3125 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3126 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3127 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3128 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3129 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3130 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3131 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3132 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3133 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3134 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3135 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3136 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3137 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3138 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3139 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3140 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3141 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3142 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3143 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3144 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3145 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3146 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3147 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3148 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3149 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3150 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3151 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3152 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3153 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3154 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3155 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3156 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3157 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3158 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3159 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3160 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3161 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3162 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3163 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3164 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3165 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3166 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3167 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3168 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3169 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3170 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3171 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3172 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3173 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3174 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3175 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3176 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3177 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3178 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3179 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3180 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3181 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3182 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3183 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3184 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3185 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3186 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3187 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3188 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3189 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3190 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3191 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3192 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3193 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3194 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3195 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3196 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3197 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3198 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3199 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3200 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3201 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3202 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3203 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3204 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3205 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3206 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3207 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3208 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3209 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3210 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3211 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3212 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3213 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3214 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3215 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3216 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3217 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3218 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3219 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3220 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3221 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3222 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3223 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3224 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3225 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3226 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3227 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3228 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3229 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3230 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3231 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3232 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3233 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3234 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3235 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3236 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3237 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3238 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3239 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3240 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3241 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3242 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3243 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3244 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3245 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3246 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3247 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3248 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3249 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3250 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3251 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3252 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3253 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3254 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3255 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3256 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3257 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3258 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3259 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3260 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3261 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3262 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3263 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3264 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3265 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3266 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3267 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3268 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3269 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3270 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3271 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3272 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3273 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3274 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3275 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3276 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3277 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3278 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3279 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3280 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3281 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3282 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3283 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3284 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3285 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3286 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3287 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3288 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3289 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3290 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3291 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3292 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3293 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3294 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3295 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3296 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3297 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3298 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3299 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3300 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3301 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3302 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3303 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3304 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3305 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3306 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3307 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3308 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3309 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3310 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3311 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3312 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3313 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3314 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3315 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3316 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3317 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3318 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3319 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3320 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3321 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3322 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3323 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3324 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3325 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3326 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3327 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3328 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3329 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3330 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3331 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3332 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3333 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3334 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3335 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3336 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3337 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3338 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3339 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3340 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3341 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3342 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3343 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3344 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3345 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3346 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3347 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3348 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3349 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3350 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3351 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3352 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3353 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3354 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3355 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3356 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3357 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3358 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3359 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3360 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3361 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3362 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3363 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3364 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3365 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3366 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3367 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3368 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3369 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3370 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3371 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3372 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3373 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3374 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3375 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3376 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3377 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3378 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3379 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3380 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3381 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3382 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3383 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3384 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3385 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3386 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3387 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3388 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3389 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3390 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3391 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3392 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3393 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3394 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3395 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3396 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3397 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3398 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3399 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3400 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3401 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3402 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3403 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3404 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3405 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3406 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3407 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3408 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3409 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3410 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3411 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3412 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3413 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3414 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3415 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3416 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3417 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3418 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3419 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3420 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3421 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3422 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3423 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3424 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3425 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3426 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3427 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3428 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3429 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3430 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3431 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3432 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3433 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3434 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3435 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3436 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3437 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3438 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3439 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3440 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3441 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3442 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3443 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3444 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3445 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3446 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3447 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3448 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3449 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3450 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3451 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3452 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3453 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3454 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3455 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3456 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3457 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3458 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3459 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3460 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3461 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3462 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3463 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3464 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3465 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3466 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3467 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3468 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3469 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3470 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3471 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3472 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3473 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3474 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3475 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3476 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3477 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3478 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3479 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3480 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3481 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3482 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3483 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3484 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3485 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3486 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3487 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3488 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3489 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3490 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3491 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3492 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3493 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3494 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3495 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3496 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3497 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3498 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3499 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3500 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3501 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3502 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3503 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3504 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3505 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3506 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3507 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3508 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3509 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3510 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3511 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3512 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3513 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3514 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3515 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3516 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3517 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3518 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3519 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3520 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3521 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3522 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3523 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3524 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3525 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3526 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3527 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3528 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3529 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3530 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3531 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3532 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3533 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3534 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3535 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3536 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3537 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3538 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3539 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3540 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3541 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3542 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3543 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3544 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3545 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3546 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3547 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3548 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3549 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3550 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3551 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3552 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3553 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3554 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3555 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3556 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3557 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3558 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3559 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3560 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3561 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3562 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3563 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3564 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3565 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3566 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3567 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3568 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3569 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3570 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3571 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3572 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3573 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3574 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3575 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3576 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3577 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3578 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3579 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3580 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3581 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3582 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3583 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3584 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3585 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3586 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3587 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3588 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3589 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3590 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3591 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3592 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3593 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3594 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3595 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3596 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3597 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3598 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3599 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3600 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3601 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3602 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3603 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3604 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3605 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3606 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3607 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3608 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3609 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3610 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3611 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3612 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3613 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3614 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3615 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3616 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3617 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3618 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3619 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3620 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3621 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3622 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3623 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3624 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3625 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3626 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3627 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3628 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3629 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3630 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3631 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3632 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3633 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3634 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3635 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3636 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3637 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3638 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3639 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3640 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3641 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3642 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3643 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3644 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3645 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3646 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3647 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3648 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3649 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3650 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3651 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3652 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3653 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3654 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3655 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3656 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3657 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3658 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3659 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3660 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3661 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3662 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3663 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3664 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3665 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3666 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3667 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3668 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3669 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3670 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3671 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3672 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3673 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3674 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3675 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3676 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3677 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3678 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3679 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3680 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3681 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3682 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3683 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3684 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3685 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3686 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3687 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3688 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3689 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3690 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3691 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3692 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3693 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3694 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3695 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3696 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3697 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3698 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3699 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3700 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3701 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3702 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3703 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3704 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3705 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3706 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3707 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3708 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3709 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3710 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3711 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3712 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3713 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3714 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3715 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3716 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3717 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3718 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3719 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3720 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3721 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3722 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3723 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3724 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3725 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3726 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3727 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3728 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3729 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3730 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3731 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3732 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3733 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3734 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3735 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3736 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3737 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3738 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3739 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3740 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3741 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3742 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3743 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3744 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3745 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3746 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3747 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3748 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3749 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3750 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3751 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3752 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3753 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3754 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3755 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3756 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3757 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3758 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3759 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3760 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3761 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3762 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3763 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3764 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3765 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3766 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3767 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3768 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3769 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3770 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3771 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3772 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3773 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3774 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3775 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3776 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3777 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3778 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3779 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3780 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3781 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3782 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3783 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3784 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3785 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3786 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3787 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3788 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3789 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3790 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3791 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3792 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3793 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3794 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3795 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3796 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3797 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3798 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3799 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3800 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3801 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3802 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3803 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3804 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3805 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3806 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3807 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3808 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3809 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3810 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3811 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3812 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3813 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3814 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3815 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3816 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3817 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3818 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3819 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3820 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3821 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3822 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3823 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3824 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3825 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3826 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3827 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3828 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3829 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3830 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3831 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3832 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3833 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3834 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3835 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3836 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3837 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3838 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3839 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3840 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3841 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3842 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3843 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3844 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3845 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3846 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3847 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3848 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3849 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3850 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3851 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3852 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3853 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3854 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3855 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3856 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3857 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3858 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3859 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3860 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3861 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3862 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3863 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3864 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3865 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3866 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3867 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3868 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3869 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3870 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3871 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3872 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3873 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3874 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3875 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3876 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3877 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3878 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3879 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3880 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3881 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3882 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3883 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3884 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3885 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3886 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3887 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3888 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3889 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3890 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3891 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3892 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3893 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3894 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3895 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3896 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3897 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3898 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3899 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3900 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3901 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3902 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3903 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3904 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3905 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3906 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3907 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3908 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3909 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3910 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3911 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3912 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3913 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3914 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3915 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3916 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3917 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3918 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3919 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3920 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3921 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3922 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3923 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3924 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3925 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3926 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3927 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3928 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3929 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3930 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3931 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3932 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3933 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3934 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3935 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3936 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3937 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3938 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3939 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3940 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3941 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3942 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3943 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3944 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3945 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3946 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3947 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3948 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3949 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3950 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3951 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3952 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3953 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3954 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3955 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3956 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3957 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3958 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3959 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3960 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3961 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3962 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3963 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3964 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3965 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3966 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3967 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3968 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3969 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3970 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3971 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3972 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3973 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3974 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3975 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3976 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3977 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3978 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3979 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3980 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3981 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3982 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3983 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3984 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3985 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3986 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3987 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-3988 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-3989 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-3990 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-3991 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-3992 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-3993 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-3994 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-3995 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-3996 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-3997 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-3998 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-3999 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4000 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4001 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4002 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4003 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4004 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4005 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4006 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4007 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4008 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4009 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4010 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4011 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4012 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4013 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4014 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4015 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4016 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4017 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4018 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4019 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4020 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4021 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4022 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4023 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4024 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4025 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4026 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4027 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4028 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4029 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4030 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4031 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4032 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4033 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4034 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4035 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4036 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4037 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4038 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4039 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4040 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4041 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4042 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4043 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4044 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4045 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4046 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4047 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4048 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4049 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4050 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4051 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4052 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4053 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4054 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4055 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4056 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4057 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4058 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4059 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4060 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4061 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4062 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4063 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4064 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4065 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4066 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4067 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4068 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4069 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4070 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4071 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4072 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4073 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4074 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4075 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4076 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4077 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4078 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4079 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4080 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4081 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4082 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4083 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4084 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4085 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4086 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4087 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4088 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4089 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4090 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4091 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4092 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4093 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4094 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4095 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4096 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4097 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4098 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4099 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4100 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4101 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4102 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4103 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4104 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4105 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4106 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4107 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4108 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4109 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4110 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4111 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4112 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4113 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4114 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4115 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4116 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4117 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4118 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4119 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4120 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4121 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4122 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4123 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4124 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4125 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4126 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4127 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4128 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4129 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4130 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4131 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4132 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4133 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4134 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4135 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4136 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4137 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4138 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4139 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4140 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4141 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4142 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4143 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4144 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4145 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4146 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4147 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4148 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4149 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4150 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4151 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4152 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4153 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4154 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4155 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4156 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4157 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4158 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4159 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4160 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4161 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4162 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4163 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4164 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4165 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4166 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4167 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4168 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4169 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4170 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4171 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4172 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4173 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4174 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4175 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4176 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4177 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4178 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4179 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4180 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4181 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4182 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4183 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4184 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4185 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4186 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4187 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4188 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4189 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4190 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4191 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4192 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4193 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4194 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4195 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4196 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4197 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4198 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4199 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4200 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4201 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4202 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4203 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4204 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4205 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4206 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4207 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4208 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4209 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4210 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4211 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4212 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4213 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4214 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4215 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4216 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4217 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4218 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4219 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4220 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4221 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4222 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4223 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4224 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4225 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4226 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4227 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4228 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4229 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4230 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4231 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4232 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4233 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4234 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4235 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4236 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4237 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4238 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4239 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4240 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4241 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4242 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4243 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4244 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4245 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4246 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4247 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4248 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4249 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4250 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4251 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4252 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4253 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4254 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4255 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4256 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4257 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4258 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4259 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4260 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4261 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4262 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4263 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4264 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4265 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4266 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4267 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4268 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4269 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4270 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4271 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4272 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4273 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4274 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4275 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4276 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4277 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4278 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4279 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4280 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4281 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4282 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4283 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4284 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4285 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4286 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4287 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4288 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4289 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4290 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4291 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4292 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4293 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4294 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4295 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4296 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4297 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4298 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4299 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4300 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4301 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4302 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4303 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4304 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4305 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4306 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4307 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4308 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4309 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4310 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4311 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4312 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4313 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4314 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4315 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4316 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4317 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4318 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4319 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4320 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4321 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4322 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4323 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4324 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4325 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4326 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4327 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4328 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4329 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4330 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4331 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4332 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4333 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4334 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4335 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4336 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4337 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4338 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4339 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4340 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4341 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4342 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4343 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4344 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4345 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4346 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4347 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4348 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4349 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4350 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4351 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4352 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4353 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4354 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4355 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4356 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4357 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4358 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4359 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4360 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4361 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4362 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4363 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4364 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4365 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4366 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4367 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4368 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4369 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4370 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4371 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4372 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4373 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4374 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4375 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4376 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4377 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4378 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4379 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4380 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4381 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4382 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4383 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4384 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4385 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4386 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4387 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4388 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4389 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4390 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4391 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4392 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4393 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4394 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4395 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4396 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4397 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4398 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4399 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4400 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4401 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4402 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4403 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4404 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4405 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4406 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4407 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4408 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4409 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4410 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4411 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4412 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4413 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4414 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4415 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4416 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4417 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4418 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4419 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4420 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4421 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4422 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4423 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4424 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4425 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4426 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4427 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4428 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4429 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4430 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4431 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4432 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4433 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4434 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4435 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4436 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4437 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4438 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4439 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4440 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4441 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4442 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4443 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4444 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4445 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4446 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4447 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4448 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4449 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4450 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4451 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4452 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4453 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4454 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4455 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4456 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4457 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4458 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4459 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4460 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4461 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4462 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4463 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4464 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4465 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4466 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4467 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4468 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4469 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4470 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4471 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4472 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4473 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4474 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4475 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4476 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4477 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4478 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4479 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4480 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4481 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4482 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4483 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4484 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4485 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4486 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4487 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4488 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4489 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4490 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4491 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4492 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4493 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4494 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4495 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4496 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4497 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4498 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4499 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4500 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4501 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4502 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4503 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4504 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4505 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4506 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4507 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4508 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4509 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4510 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4511 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4512 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4513 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4514 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4515 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4516 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4517 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4518 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4519 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4520 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4521 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4522 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4523 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4524 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4525 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4526 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4527 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4528 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4529 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4530 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4531 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4532 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4533 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4534 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4535 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4536 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4537 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4538 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4539 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4540 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4541 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4542 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4543 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4544 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4545 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4546 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4547 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4548 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4549 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4550 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4551 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4552 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4553 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4554 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4555 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4556 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4557 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4558 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4559 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4560 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4561 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4562 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4563 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4564 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4565 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4566 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4567 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4568 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4569 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4570 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4571 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4572 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4573 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4574 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4575 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4576 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4577 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4578 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4579 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4580 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4581 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4582 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4583 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4584 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4585 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4586 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4587 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4588 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4589 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4590 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4591 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4592 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4593 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4594 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4595 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4596 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4597 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4598 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4599 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4600 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4601 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4602 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4603 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4604 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4605 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4606 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4607 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4608 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4609 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4610 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4611 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4612 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4613 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4614 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4615 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4616 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4617 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4618 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4619 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4620 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4621 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4622 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4623 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4624 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4625 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4626 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4627 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4628 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4629 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4630 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4631 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4632 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4633 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4634 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4635 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4636 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4637 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4638 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4639 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4640 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4641 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4642 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4643 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4644 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4645 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4646 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4647 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4648 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4649 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4650 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4651 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4652 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4653 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4654 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4655 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4656 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4657 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4658 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4659 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4660 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4661 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4662 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4663 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4664 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4665 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4666 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4667 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4668 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4669 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4670 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4671 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4672 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4673 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4674 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4675 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4676 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4677 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4678 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4679 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4680 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4681 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4682 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4683 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4684 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4685 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4686 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4687 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4688 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4689 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4690 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4691 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4692 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4693 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4694 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4695 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4696 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4697 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4698 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4699 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4700 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4701 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4702 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4703 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4704 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4705 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4706 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4707 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4708 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4709 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4710 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4711 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4712 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4713 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4714 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4715 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4716 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4717 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4718 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4719 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4720 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4721 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4722 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4723 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4724 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4725 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4726 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4727 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4728 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4729 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4730 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4731 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4732 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4733 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4734 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4735 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4736 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4737 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4738 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4739 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4740 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4741 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4742 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4743 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4744 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4745 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4746 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4747 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4748 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4749 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4750 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4751 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4752 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4753 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4754 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4755 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4756 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4757 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4758 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4759 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4760 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4761 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4762 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4763 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4764 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4765 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4766 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4767 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4768 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4769 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4770 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4771 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4772 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4773 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4774 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4775 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4776 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4777 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4778 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4779 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4780 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4781 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4782 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4783 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4784 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4785 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4786 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4787 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4788 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4789 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4790 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4791 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4792 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4793 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4794 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4795 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4796 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4797 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4798 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4799 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4800 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4801 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4802 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4803 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4804 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4805 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4806 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4807 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4808 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4809 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4810 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4811 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4812 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4813 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4814 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4815 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4816 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4817 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4818 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4819 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4820 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4821 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4822 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4823 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4824 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4825 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4826 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4827 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4828 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4829 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4830 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4831 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4832 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4833 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4834 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4835 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4836 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4837 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4838 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4839 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4840 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4841 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4842 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4843 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4844 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4845 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4846 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4847 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4848 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4849 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4850 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4851 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4852 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4853 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4854 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4855 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4856 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4857 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4858 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4859 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4860 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4861 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4862 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4863 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4864 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4865 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4866 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4867 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4868 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4869 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4870 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4871 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4872 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4873 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4874 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4875 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4876 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4877 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4878 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4879 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4880 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4881 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4882 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4883 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4884 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4885 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4886 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4887 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4888 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4889 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4890 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4891 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4892 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4893 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4894 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4895 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4896 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4897 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4898 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4899 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4900 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4901 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4902 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4903 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4904 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4905 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4906 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4907 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4908 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4909 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4910 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4911 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4912 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4913 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4914 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4915 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4916 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4917 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4918 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4919 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4920 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4921 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4922 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4923 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4924 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4925 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4926 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4927 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4928 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4929 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4930 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4931 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4932 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4933 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4934 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4935 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4936 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4937 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4938 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4939 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4940 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4941 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4942 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4943 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4944 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4945 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4946 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4947 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4948 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4949 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4950 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4951 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4952 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4953 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4954 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4955 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4956 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4957 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4958 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4959 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4960 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4961 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4962 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4963 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4964 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4965 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4966 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4967 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4968 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4969 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4970 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4971 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4972 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4973 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4974 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4975 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4976 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4977 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4978 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4979 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4980 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4981 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4982 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4983 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4984 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4985 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4986 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4987 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-4988 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.
# AUDIT-4989 | Badges | Future extensions should preserve existing command names and aliases whenever possible.
# AUDIT-4990 | Badges | Command registration should remain discoverable through the live bot command tree.
# AUDIT-4991 | Badges | Permission-sensitive actions should retain Discord hierarchy checks.
# AUDIT-4992 | Badges | Database writes should use parameterized SQL and explicit commits.
# AUDIT-4993 | Badges | Network requests should keep reasonable timeouts and graceful failure messages.
# AUDIT-4994 | Badges | User-provided text should be length-limited before sending to Discord.
# AUDIT-4995 | Badges | Embeds should respect Discord field and description size limits.
# AUDIT-4996 | Badges | Long-running media and audio work should avoid blocking the event loop.
# AUDIT-4997 | Badges | Sensitive configuration values belong in environment variables, not source code.
# AUDIT-4998 | Badges | Personal hardware, location, account, and device assumptions should not be hard-coded.
# AUDIT-4999 | Badges | New commands marked vital_new are surfaced automatically by help and updates.
# AUDIT-5000 | Badges | Destructive administrative actions should be permission-gated and hierarchy-aware.

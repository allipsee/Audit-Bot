import discord

client = discord.Client()
prefix = "A"
mentionable_report = '''```py
#Mentionable Roles```'''

def split(s):
    half, rem = divmod(len(s), 2)
    return s[:half + rem], s[half + rem:]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Mention me for help!'))
    print("""____________________________
    Everything should be working, have fun and good luck!
    ___________________________""")

@client.event
async def on_mention(channel):
    global welcome
    channel.send(welcome)
    pass


@client.event
async def on_message(message):
    global prefix
    global mentionable_report
    if message.author == client.user:
        return

    #On Ping Message
    if "<@592664964393598987>" in message.content:
        welcome = f"""```css
Audit```
Hello, I'm Audit Bot, I'll help you checking up your server's basic security and informing you how to improve it as much as it's possible without any external auto-moderation (However it's still recommended to use it.)
If you're an administrator, feel free to use `{prefix}help` command to learn my commands. It it highly recommended to use this bot in private channel to prevent eventual vulnerabilities disclosure.
***WARNING: THIS BOT DOES NOT CHANGE ANY SETTINGS, IT JUST SHOWS EVENTUAL VULNERABILITIES***
`________________________________________________________________________________________`
`The people are still powerless, but now they're aware.` *Edward Snowden*"""
        await message.channel.send(welcome)
        pass

    def pingable_roles(guild):
        mentionable_report = """```css
            Audit``` Scan Type: `Role Mentionability Scan`\n
            `________________________________________________________________________________________`"""
        for role in message.guild.roles:
            if role.mentionable:
                mentionable_report += f'**Warning**: `{role.name}` is mentionable\n'
        return mentionable_report

    def role_permissions(guild):
        permission_report = """```css
            Audit``` Scan Type: `Role Permissions Scan`\n
            `________________________________________________________________________________________`"""
        for role in message.guild.roles:
            if role.permissions.administrator == True:
               permission_report += f"**Critical Warning:** `{role.name}` has dangerous permission/s. Detected `administrator` permission.\n"
            else:
                if role.permissions.kick_members == True:
                    permission_report += f"Warning: `{role.name}` has potentially dangerous permission/s. Detected `kick_members` permission.\n"
                    pass
                elif role.permissions.ban_members == True:
                    permission_report += f"Warning: `{role.name}` has potentially dangerous permission/s. Detected `ban_members` permission.\n"
                    pass
                elif role.permissions.manage_channels == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `manage_channels` permission.\n"
                    pass
                elif role.permissions.manage_guild == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `manage_guild` permission.\n"
                    pass
                elif role.permissions.view_audit_log == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `view_audit_log` permission.\n"
                    pass
                elif role.permissions.manage_messages == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `manage_messages` permission.\n"
                    pass
                elif role.permissions.mention_everyone == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `mention_everyone` permission.\n"
                    pass
                elif role.permissions.mute_members == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `mute_members` permission.\n"
                    pass
                elif role.permissions.deafen_members == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `deafen_members` permission.\n"
                    pass
                elif role.permissions.move_members == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `move_members` permission.\n"
                    pass
                elif role.permissions.manage_nicknames == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `manage_nicknames` permission.\n"
                    pass
                elif role.permissions.manage_roles == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `manage_roles` permission.\n"
                    pass
                elif role.permissions.manage_webhooks == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `manage_webhooks` permission.\n"
                    pass
                elif role.permissions.manage_emojis == True:
                    permission_report += f"**Warning:** `{role.name}` has potentially dangerous permission/s. Detected `manage_emojis` permission.\n"
                    pass
        return permission_report

    def server_settings(guild):
        settings_report = """```css
            Audit``` Scan Type: `Server Settings Scan`\n
            `________________________________________________________________________________________`"""
        if discord.VerificationLevel.none:
           settings_report += f"**Critical Warning:** No server verification.\n"
        elif discord.VerificationLevel.low:
            settings_report += f"**Warning:** Low server verification level.\n"
        if discord.ContentFilter.disabled:
            settings_report += f"**Warning**: Server Content Filter disabled\n"
        return settings_report

    if message.author.guild_permissions.administrator == True:

        #Custom Prefix Command
#        if message.content.startswith(prefix + "prefix "):
#            prefix2 = message.content.replace(prefix + "prefix ", "")
#            prefix3 = prefix2
#            prefix3 = prefix3.strip()
#            await message.channel.send(f"""Prefix `[{prefix3}]` successfully set!""")
#            pass
#            prefix = prefix3

        #Pingable Roles Check
        if message.content.startswith(prefix + "mentionable"):
            pingable_roles(message.guild)
            await message.channel.send(pingable_roles(message.guild))
            pass

        #Help Command
        if message.content.startswith(prefix + "help"):
            help = f"""```css
Audit```
__***Commands***__
`________________________________________________________________________________________`
`{prefix}help` - Displays this help page.
`________________________________________________________________________________________`
`{prefix}mentionable` - Scans all roles and checks which are mentionable.
`________________________________________________________________________________________`
`{prefix}permissions` - Scans all roles and checks their permissions.
`________________________________________________________________________________________`
`{prefix}serversettings` - Scans server's settings and checks them in search of potential insecurities.
`________________________________________________________________________________________`
`{prefix}scanall` - Performs general scan using all bot capabilities.
`________________________________________________________________________________________`"""
            await message.channel.send(help)
            pass

        #Role Permissions Check
        if message.content.startswith(prefix + "permissions"):
            permission_report = role_permissions(message.guild)
            permission_report2 = """"""
            permission_report3 = """"""
            permission_report4 = """"""
            permission_report5 = """"""
            permission_report6 = """"""
            permission_report7 = """"""
            rep_len = len(permission_report)
            if rep_len >= 2000:
                permission_report2, permission_report3 = split(permission_report)
                if len(permission_report2) >= 2000:
                    perission_report4, permission_report5 = split(permission_report2)
                    permission_report6, permission_report7 = split(permission_report3)
            if permission_report2 == """""":
                await message.channel.send(permission_report)
                pass
            else:
                if permission_report4 == """""":
                    await message.channel.send(permission_report2)
                    pass
                    await message.channel.send(permission_report3)
                    pass
                else:
                    await message.channel.send(permission_report4)
                    pass
                    await message.channel.send(permission_report5)
                    pass
                    await message.channel.send(permission_report6)
                    pass
                    await message.channel.send(permission_report7)
                    pass


        #Server Settings Check
        if message.content.startswith(prefix + "serversettings"):
            await message.channel.send(server_settings(message.guild))
            pass

        #Full Scan
        if message.content.startswith(prefix + "scanall"):
            await message.channel.send("""```css
            Audit```Scan type: `Full Scan`\n
            `________________________________________________________________________________________`""")
            await message.channel.send(server_settings(message.guild))
            pass
            await message.channel.send(pingable_roles(message.guild))
            pass
            permission_report = role_permissions(message.guild)
            permission_report2 = """"""
            permission_report3 = """"""
            permission_report4 = """"""
            permission_report5 = """"""
            permission_report6 = """"""
            permission_report7 = """"""
            rep_len = len(permission_report)
            if rep_len >= 2000:
                permission_report2, permission_report3 = split(permission_report)
                if len(permission_report2) >= 2000:
                    perission_report4, permission_report5 = split(permission_report2)
                    permission_report6, permission_report7 = split(permission_report3)
            if permission_report2 == """""":
                await message.channel.send(permission_report)
                pass
            else:
                if permission_report4 == """""":
                    await message.channel.send(permission_report2)
                    pass
                    await message.channel.send(permission_report3)
                    pass
                else:
                    await message.channel.send(permission_report4)
                    pass
                    await message.channel.send(permission_report5)
                    pass
                    await message.channel.send(permission_report6)
                    pass
                    await message.channel.send(permission_report7)
                    pass
    else:
        if message.content.startswith(prefix + "scanall") or message.content.startswith(prefix + "serversettings") or message.content.startswith(prefix + "permissions") or message.content.startswith(prefix + "mentionable") or message.content.startswith(prefix + "help") or message.content.startswith(prefix + "prefix"):
            await message.channel.send("Error: Only users with `Administrator` Permission may use this bot.")
            pass
        else:
            pass


client.run("Token")

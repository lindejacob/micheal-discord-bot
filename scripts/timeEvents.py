import discord
import datetime  # Ensure datetime is correctly imported
import asyncio

async def send_micheal_message(CHANNEL_ID, ROLE_ID, bot, GUILD_ID):
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print(f"Guild with ID {GUILD_ID} not found.")
        return

    role = guild.get_role(ROLE_ID)
    if role is None:
        print(f"Role with ID {ROLE_ID} not found.")
        return

    now = datetime.datetime.now()
    time_actions = {
        (13, 8): f"Der er 2 minutter til 13:10! {role.mention}",
        (13, 10): f"13:10, Gooodt Goodt Goodt, FÆLLESMØDE! {role.mention}"
    }
    if (now.hour, now.minute) in time_actions:
        channel = bot.get_channel(CHANNEL_ID)
        if channel is None:
            print(f"Channel with ID {CHANNEL_ID} not found.")
            return
        await channel.send(time_actions[(now.hour, now.minute)])

async def update_status(bot):
    now = datetime.datetime.now()
    target_time = datetime.datetime(now.year, now.month, now.day, 13, 10)

    if now.hour == 13 and now.minute == 10:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Goodt Goodt"))
    else:
        remaining_time = target_time - now
        remaining_hours = remaining_time.seconds // 3600  # Calculate remaining hours
        remaining_minutes = (remaining_time.seconds % 3600) // 60  # Calculate remaining minutes
        
        # Display the time remaining as hours and minutes
        if remaining_hours > 0:
            time_str = f"{remaining_hours} time{'r' if remaining_hours > 1 else ''} og {remaining_minutes} minut{'er' if remaining_minutes != 1 else ''} til 13:10"
        else:
            time_str = f"{remaining_minutes} minut{'ter' if remaining_minutes != 1 else ''} til 13:10"
        
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=time_str))


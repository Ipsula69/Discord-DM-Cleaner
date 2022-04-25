import os, os.path, discord
from discord.ext import commands
from colorama import Fore

os.system('cls' if os.name == 'nt' else 'clear')
cleardmtitle()
print(f"""{b}Token here{w}""")
token = input(f"""{b}: """)
print(f"""\n{b} !clear in any dm""")

global bot
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"\n{b} {passed} purged messages")
    input(f"""\n{b} ENTER > exit""")
    main()

bot.run(token, bot=False)
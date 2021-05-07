#Copyright 2021-2022 Ultra X Bot
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, StartTime
from userbot.utils import admin_cmd
from userbot import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from ULTRA.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from ULTRA import botnickname 
BOT = str(botnickname) if botnickname else "𝘼𝙑𝙀𝙉𝙂𝙀𝙍 𝘽𝙊𝙏"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "𝘼𝙑𝙀𝙉𝙂𝙀𝙍 𝘽𝙊𝙔"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
#op 
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
ULTRAX = "[Avenger](https://t.me/Avenger_BOT_support)"
#my bots repo 👇
REPO = "[Avenger вσт](https://github.com/Avenger6262/Avenger)"
#grpup👇NAME = "[{MAATER}](tg://user?id={X})"
#yrr isko apne bot me aply krne se pehle mere se pooch lena ok
#aur aage add kruga abhi busy okay 🤔
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/Avenger_BOT_support)"
#itna test h aur aage krte h
#test successful raha ab aage 
ALIVE = "Avenger вσт ιѕ ση 🔥 ƒιяє 🔥" 
OP = " нєℓℓσ мαѕтєя му ηαмє ιѕ Avenger вσт ι αм тнє вєѕт υѕєявσт 💝"
EMOJI = "🔥"

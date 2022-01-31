# © NOINOI MUSIC @CFC_BOT_SUPPORT

from Noinoi.DREAMS.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Noinoi.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**

🔖 **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("ꜱᴏᴜʀᴄᴇ", url="https://T.ME/BAZIGARYT"),
                InlineKeyboardButton("✨ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{UPDATES_CHANNEL}"),],
                [InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="cbcmds"),
                InlineKeyboardButton("❓ ꜱᴇᴛᴜᴘ", callback_data="noinoisetup"),],
                [InlineKeyboardButton(" ᴀᴅᴅ ᴍᴇᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**
        
⊙ https://telegra.ph/file/a671532c23687e6fcc431.mp4

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("noinoisetup"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 Hear all coammnds of noinoi bot which can you use tap on buttons for cheak the commands

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Groups", callback_data="noinoigroups"),
                    InlineKeyboardButton("Anime", callback_data="noinoianime"),
                ],[
                    InlineKeyboardButton("Approvals", callback_data="noinoiapprovals")
                ],[
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

➯ /play (song name/link) - play music on video chat
➯ /playlist - show you the playlist
➯ /lyric (query) - scrap the song lyric
➯ /search (query) - search a youtube video link
➯ /ping - show the bot ping status
➯ /uptime - show the bot uptime status
➯ /alive - show the bot alive info (in group)

 **✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

➯ /pause - pause the stream
➯ /resume - resume the stream
➯ /skip - switch to next stream
➯ /stop - stop the streaming
➯ /vmute - mute the userbot on voice chat
➯ /vunmute - unmute the userbot on voice chat
➯ /volume `1-200` - adjust the volume of music (userbot must be admin)
➯ /reload - reload bot and refresh the admin data
➯ /userbotjoin - invite the userbot to join group
➯ /userbotleave - order userbot to leave from group

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

➯ /rmw - clean all raw files
➯ /rmd - clean all downloaded files
➯ /sysinfo - show the system information
➯ /update - update your bot to latest version
➯ /restart - restart your bot
➯ /leaveall - order userbot to leave from all group

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

    
# .........................................................................................................................................................................................................

# GROUPS COMMANDS ======================

@Client.on_callback_query(filters.regex("noinoigroups"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" Hear the all groups commands tap on buttons for cheak the featurs of our bot

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Groups", callback_data="noigroups"),
                    InlineKeyboardButton("Admins", callback_data="noiadmins"),
                ],[
                    InlineKeyboardButton("Others", callback_data="noiothers")
                ],[
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )

                    
#ANIME COMMANDS====================
                    
@Client.on_callback_query(filters.regex("noinoianime"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ** Hear the all anime commands of noinoi bot**

 ❍ /anime <anime>: returns information about the anime.
 ❍ /character <character>: returns information about the character.
 ❍ /manga <manga>: returns information about the manga.
 ❍ /user <user>: returns information about a MyAnimeList user.
 ❍ /upcoming: returns a list of new anime in the upcoming seasons.
 ❍ /kaizoku <anime>: search an anime on animekaizoku.com
 ❍ /kayo <anime>: search an anime on animekayo.com
 ❍ /airing <anime>: returns anime airing info.
 ❍ /whatanime - reply to gif or video.
 
**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )                    

# APPRUVALS COMMANDS ====================
                    
@Client.on_callback_query(filters.regex("noinoiapprovals"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ** Hear the all approvals commands of noinoi bot**

 ❍ /approval: Check a user's approval status in this chat.
 ❍ /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
 ❍ /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
 ❍ /approved: List all approved users.
 ❍ /unapproveall: Unapprove ALL users in a chat. This cannot be undone.
 
**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )   
                    
# chanells commands =====================

@Client.on_callback_query(filters.regex("noinoichannel"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ** Hear the all channel commands noinoi bot**

 ❍ /logchannel: get log channel info
 ❍ /setlog: set the log channel.
 ❍ /unsetlog: unset the log channel.
 ❍ sending /setlog in the channel
 ❍ forwarding the /setlog to the group
 
**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )   
       
# chatbot commands=============================
                    
@Client.on_callback_query(filters.regex("noinoiextra"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ** Hear the all extra commands noinoi bot**

 ❍ /markdownhelp: quick summary of how markdown works in telegram - can only be called in private chats
Paste:
 ❍ /paste: Saves replied content to nekobin.com and replies with a url
React:
 ❍ /react: Reacts with a random reaction 
Urban Dictonary:
 ❍ /ud <word>: Type the word or expression you want to search use
Wikipedia:
 ❍ /wiki <query>: wikipedia your query
Wallpapers:
 ❍ /wall <query>: get a wallpaper from wall.alphacoders.com
live cricket score
 ❍ /cs: Latest live scores from cricinfo
Currency converter: 
 ❍ /cash: currency converter
Example:
 /cash 1 USD INR  
      OR
 /cash 1 usd inr
Output: 1.0 USD = 75.505 INR

MATHS
Solves complex math problems using https://newton.now.sh
❍ /math: Math /math 2^2+2(2)
❍ /factor: Factor /factor x^2 + 2x
❍ /derive: Derive /derive x^2+2x
❍ /integrate: Integrate /integrate x^2+2x
❍ /zeroes: Find 0's /zeroes x^2+2x
❍ /tangent: Find Tangent /tangent 2lx^3
❍ /area: Area Under Curve /area 2:4lx^3
❍ /cos: Cosine /cos pi
❍ /sin: Sine /sin 0
❍ /tan: Tangent /tan 0
❍ /arccos: Inverse Cosine /arccos 1
❍ /arcsin: Inverse Sine /arcsin 0
❍ /arctan: Inverse Tangent /arctan 0
❍ /abs: Absolute Value /abs -1
❍ /log: Logarithm /log 2l8

Keep in mind: To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).

💡Read From Top

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    ) 
                    
# extra commands ======================
                    
@Client.on_callback_query(filters.regex("noinoifeds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" Hear the all groups commands tap on buttons for cheak the featurs of our bot

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Owner", callback_data="fed1"),
                    InlineKeyboardButton("Admins", callback_data="fed2"),
                ],[
                    InlineKeyboardButton("Users", callback_data="fed3")
                ],[
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )           
                    
@Client.on_callback_query(filters.regex("fed1"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ** Hear the all Fed owner commands noinoi bot**

 ❍ /newfed <fed_name>: Creates a Federation, One allowed per user.
 ❍ /renamefed <fed_id> <new_fed_name>: Renames the fed id to a new name.
 ❍ /delfed <fed_id>: Delete a Federation, and any information related to it. Will not cancel blocked users.
 ❍ /fpromote <user>: Assigns the user as a federation admin. Enables all commands for the user under Fed Admins.
 ❍ /fdemote <user>: Drops the User from the admin Federation to a normal User.
 ❍ /subfed <fed_id>: Subscribes to a given fed ID, bans from that subscribed fed will also happen in your fed.
 ❍ /unsubfed <fed_id>: Unsubscribes to a given fed ID.
 ❍ /setfedlog <fed_id>: Sets the group as a fed log report base for the federation.
 ❍ /unsetfedlog <fed_id>: Removed the group as a fed log report base for the federation.
 ❍ /fbroadcast <message>: Broadcasts a messages to all groups that have joined your fed.
 ❍ /ftransfer <byreply>: Changes the owner of current joined fed to the replied user.
 ❍ /fedsubs: Shows the feds your group is subscribed to (broken rn).
 
**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )                     
          
@Client.on_callback_query(filters.regex("fed2"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ** Hear the all Fed Admin commands noinoi bot**

 ❍ /fban <user> <reason>: Fed bans a user.
 ❍ /unfban <user> <reason>: Removes a user from a fed ban.
 ❍ /fedinfo <fed_id>: Information about the specified Federation.
 ❍ /joinfed <fed_id>: Join the current chat to the Federation. Only chat owners can do this. Every chat can only be in one Federation.
 ❍ /leavefed <fed_id>: Leave the Federation given. Only chat owners can do this.
 ❍ /setfrules <rules>: Arrange Federation rules.
 ❍ /fedadmins: Show Federation admin.
 ❍ /fbanlist: Displays all users who are victimized at the Federation at this time.
 ❍ /fedchats: Get all the chats that are connected in the Federation.
 ❍ /chatfed : See the Federation in the current chat.
 
**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )         
        
@Client.on_callback_query(filters.regex("fed3"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ** Hear the all Fed Users commands noinoi bot**

 ❍ /fbanstat: Shows if you/or the user you are replying to or their username is fbanned somewhere or not.
 ❍ /fednotif <on/off>: Federation settings not in PM when there are users who are fbaned/unfbanned.
 ❍ /frules: See Federation regulations.
 
**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )         
    
# .........................................................................................................................................................................................................
@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)

# SETUP BUTTON OPEN......................................................................................................................................................................................

@Client.on_callback_query(filters.regex("cbsetup"))
async def cbsetup(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello !**
» **press the button below to read the explanation and see the help commands !**
**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("welcome", callback_data="noiwel"),
                    InlineKeyboardButton("Lyric", callback_data="noilyric"),
                    InlineKeyboardButton("voice", callback_data="noivoice"),
                ],
                [
                    InlineKeyboardButton("How To Add Me ❓", callback_data="cbhowtouse"),
                ],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noiwel"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE WELCOME PLUGIN ( soon )**

➯ /setwelcome for set welcome message.

➯ /resetwelcome for reset welcome message.

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )
@Client.on_callback_query(filters.regex("noilyric"))
async def noilyric(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE LYRIC PLUGIN**

➯ /lyric ( song name ) for the get lyric of song

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )
    
@Client.on_callback_query(filters.regex("noivoice"))
async def noivoice(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE VOICE PLUGIN**

➯ /tts fot get voice from text message

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )    

    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()

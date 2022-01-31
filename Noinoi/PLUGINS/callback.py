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
                InlineKeyboardButton("❓ ꜱᴇᴛᴜᴘ", callback_data="cbsetup"),],
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


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 ꜱᴜᴅᴏ ᴄᴍᴅ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 ʙᴀꜱɪᴄ ᴄᴍᴅ", callback_data="cbbasic")
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
                    InlineKeyboardButton("Groups", callback_data="noiadmins"),
                    InlineKeyboardButton("Anime", callback_data="noianime"),
                    InlineKeyboardButton("Approve", callback_data="noiapprove"),
                ],
                [
                    InlineKeyboardButton("How To Add Me ❓", callback_data="cbhowtouse"),
                ],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noiadmins"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE ALL GROUPS COAMMNDS IF YOU WANT TO CHEAK THEN PRESS BUTTON TO CHEAK.**

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Groups", callback_data="noigroups"),
                    InlineKeyboardButton("Promote", callback_data="noipromote"),
                    InlineKeyboardButton("Bans", callback_data="noibans"),
                ],
                
                [
                    InlineKeyboardButton("Purge", callback_data="noipurge"),
                    InlineKeyboardButton("Mute", callback_data="noimute"),
                    InlineKeyboardButton("Warns", callback_data="noiwarns"),
                ],
                
                [
                    InlineKeyboardButton("Back", callback_data="cbsetup")
                ],            
            ]
        ),
    )
# groups enter commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . .. . . . . . . . . 

@Client.on_callback_query(filters.regex("noigroups"))
async def noigroups(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE GROUPS COMMANDS**

➯ /pin: silently pins the message replied to - add 'loud' or 'notify' to give notifs to users
➯ /unpin: unpins the currently pinned message
➯ /invitelink: gets invitelink
➯ /setgtitle <newtitle>: Sets new chat title in your group.
➯ /setgpic: As a reply to file or photo to set group profile pic!
➯ /delgpic: Same as above but to remove group profile pic.
➯ /setsticker: As a reply to some sticker to set it as group sticker set!
➯ /setdescription <description>: Sets new chat description in group.
➯ /antispam <on/off/yes/no>: Will toggle our antispam tech or return your current settings.

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                
                [InlineKeyboardButton("🔙 Go Back", callback_data="noiadmins")]
            
            
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noipromote"))
async def noipromote(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE GROUPS COMMANDS**

➯ /promote: promotes the user
➯ /demote: demotes the user
➯ /title <title here>: sets a custom title for an admin that the bot promoted
➯ /admincache: force refresh the admins list
➯ /fullpromote: if you want to promote an user with full rights then use it
➯ /fullpromote: if you want to fully promoted admin demote then use it

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                
                [InlineKeyboardButton("Back", callback_data="noiadmins")]
            
            
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noibans"))
async def noibans(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE GROUPS COMMANDS**

➯ /ban <userhandle>: bans a user. (via handle, or reply)
➯ /sban <userhandle>: Silently ban a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)
➯ /tban <userhandle> x(m/h/d): bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
➯ /unban <userhandle>: unbans a user. (via handle, or reply)
➯ /punch <userhandle>: Punches a user out of the group, (via handle, or reply)

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                
                [InlineKeyboardButton("Back", callback_data="noiadmins")]
            
            
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noipurge"))
async def noipurge(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE PURGE COMMANDS**

➯ /del: deletes the message you replied to
➯ /purge: deletes all messages between this and the replied to message.
➯ /purge <number>: if replied to with a number, deletes that many messages from target message, if sent normally in group then delete from current to previous messages
➯ /purgefrom: marks a start point to purge from
➯ /purgeto: marks the end point, messages bet to and from are deleted

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                
                [InlineKeyboardButton("Back", callback_data="noiadmins")]
            
            
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noimute"))
async def noimute(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE PURGE COMMANDS**

➯ /mute <userhandle>: silences a user. Can also be used as a reply, muting the replied to user.
➯ /tmute <userhandle> x(m/h/d): mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
➯ /unmute <userhandle>: unmutes a user. Can also be used as a reply, muting the replied to user.

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                
                [InlineKeyboardButton("Back", callback_data="noiadmins")]
            
            
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noiwarns"))
async def noiwarns(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE PURGE COMMANDS**

➯ /warns <userhandle>: get a user's number, and reason, of warns.
➯ /warnlist: list of all current warning filters
➯ /warn <userhandle>: warn a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
➯ /dwarn <userhandle>: warn a user and delete the message. After 3 warns, the user will be banned from the group. Can also be used as a reply.
➯ /resetwarn <userhandle>: reset the warns for a user. Can also be used as a reply.
➯ /addwarn <keyword> <reply message>: set a warning filter on a certain keyword. If you want your keyword to   be a sentence, encompass it with quotes, as such: /addwarn "very angry" This is an angry user.
➯ /nowarn <keyword>: stop a warning filter
➯ /warnlimit <num>: set the warning limit
➯ /strongwarn <on/yes/off/no>: If set to on, exceeding the warn limit will result in a ban. Else, will just punch.

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                
                [InlineKeyboardButton("Back", callback_data="noiadmins")]
            
            
            ]
        ),
    )    

@Client.on_callback_query(filters.regex("noianime"))
async def noianime(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE ANIME COMMANDS**

➯ /anime <anime>: returns information about the anime.
➯ /character <character>: returns information about the character.
➯ /manga <manga>: returns information about the manga.
➯ /user <user>: returns information about a MyAnimeList user.
➯ /upcoming: returns a list of new anime in the upcoming seasons.
➯ /kaizoku <anime>: search an anime on animekaizoku.com
➯ /kayo <anime>: search an anime on animekayo.com
➯ /airing <anime>: returns anime airing info.
➯ /whatanime - reply to gif or video

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]
            
            
            ]
        ),
    )
    
@Client.on_callback_query(filters.regex("noiapprove"))
async def noiapprove(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE APPROVE COMMANDS**

➯ /approval: Check a user's approval status in this chat.
➯ /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
➯ /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
➯ /approved: List all approved users.
➯ /unapproveall: Unapprove ALL users in a chat. This cannot be undone.

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )    
    
    
@Client.on_callback_query(filters.regex("noipromo"))
async def noipromo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE PROMOTE COMMANDS**

➯ /approval: Check a user's approval status in this chat.
➯ /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
➯ /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
➯ /approved: List all approved users.
➯ /unapproveall: Unapprove ALL users in a chat. This cannot be undone.

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

    
    # BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO  BAZI-BRO
    
    # SETUPS COMMANDS
    
    
    
    
    
    
    
    
    
    
    

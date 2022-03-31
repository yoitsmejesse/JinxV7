class script(object):
    START_TXT = """<b>Hello {},
My Name Is <a href=https://t.me/{}>{}</a>, Imma give ya MOVIES!!!
Made For <a href=https://t.me/showsarchive>Cine Verse Archive</a></b>"""
    HELP_TXT = """<b>Hey {}
Here is the help for my commands.</b>"""
    ABOUT_TXT = """<b>○ My Name: {}
○ Creator: <a href=https://t.me/showsarchive>Cine Verse Archive</a>
○ Library: Pyrogram
○ Language: Python 3
○ Database: Mongo DB
○ Bot Server: Heroku
○ Build Status: V1.0.7</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
• Jinx (Eva Maria) is a open source project
• Source: <a href=https://github.com/EvamariaTG/EvaMaria>Eva Maria</a>
<b>DEVS:</b>
• <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """<b>Help: Filters</b>

- <b>Filter is the feature were users can set automated replies for a particular keyword and Jinx will respond whenever a keyword is found the message</b>

<b>NOTE:</b>
<b>1. Jinx should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.</b>

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """<b>Help: Buttons</b>

<b>- Jinx supports both url and alert inline buttons.</b>

<b>NOTE:</b>
<b>1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Jinx supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.</b>

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/jinxpowder_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>Help: Auto Filter</b>

<b>NOTE:</b>
<b>1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.</b>"""
    CONNECTION_TXT = """<b>Help: Connections</b>

<b>- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.</b>

<b>NOTE:</b>
<b>1. Only admins can add a connection.</b>
<b>2. Send </b><code>/connect</code> <b>for connecting me to ur PM.</b>

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """<b>Help: Extra Modules</b>

<b>NOTE:</b>
<b>These are the extra features of Jinx</b>

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """<b>Help: Admin mods</b>

<b>NOTE:</b>
<b>This module only works for my admins</b>

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """○ Total Files: <code>{}</code>
○ Total Users: <code>{}</code>
○ Total Chats: <code>{}</code>
○ Used Storage: <code>{}</code> 𝙼𝙱
○ Free Storage: <code>{}</code> M𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

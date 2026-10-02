#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # START COMMAND & TOKEN SYSTEM (3.1.11-x)
    ST_BN1_NAME = "Repo"
    ST_BN1_URL = "https://www.github.com/SilentDemonSD/WZML-X"
    ST_BN2_NAME = "Updates"
    ST_BN2_URL = "https://t.me/WZML_X"
    ST_MSG = """<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>"""
    ST_BOTPM = """<i>Now, Bot will send you all your files and links here. Start Using Now...</i>"""
    ST_UNAUTH = """<i>You Are not an authorized user! Deploy your own WZML-X Mirror-Leech bot</i>"""

    # VERIFICATION / LOGIN
    VERIFY_SUCCESS = """⌬ Access Login Token : 
    │
    ┟ <b>Status</b> → <code>Generated Successfully</code>
    ┟ <b>Access Token</b> → <code>{input_token}</code>
    ┃
    ┖ <b>Validity:</b> {validity}"""
    OWN_TOKEN_GENERATE = (
        "<b>Access Token is not yours!</b>\n\n<i>Kindly generate your own to use.</i>"
    )
    USED_TOKEN = (
        "<b>Access Token already used!</b>\n\n<i>Kindly generate a new one.</i>"
    )
    LOGGED_PASSWORD = "<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>"
    ACTIVATE_BUTTON = "Activate Access Token"
    LOGGED_IN = "<b>Already Logged In!</b>"
    INVALID_PASS = "<b>Invalid Password!</b>\n\nKindly enter the correct password."
    PASS_LOGGED = "<b>Bot Logged In Successfully!</b>"
    LOGIN_USED = "<b>Bot Login Usage:</b>\n\n<code>/cmd [password]</code>"
    LOG_DISPLAY_BT = "📑 Log Display"
    WEB_PASTE_BT = "📨 Web Paste (SB)"

    # HELP MENU
    BASIC_BT = "Basic"
    USER_BT = "Users"
    MICS_BT = "Mics"
    O_S_BT = "Owner & Sudos"
    CLOSE_BT = "Close"
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see details.</i></b>"

    # ----------------------
    # BOT & SYSTEM STATISTICS (3.1.11-x)
    STATS_HOME = """⌬ <b>BOT STATISTICS :</b>
┎ <b>Bot Uptime :</b> {uptime}
┠ <b>Bandwidth :</b> {bandwidth}
┖ <b>Used :</b> {used} | <b>Free :</b> {free} | <b>Total :</b> {total}

⌬ <b>SYSTEM OS :</b>
┎ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b>REPO STATISTICS :</b>
┎ <b>Current Version :</b> {version}
┠ <b>Commit Date :</b> {commit_date}
┖ <b>Last ChangeLog :</b> {changelog}"""

    BOT_STATS = """⌬ <b><i>BOT STATISTICS :</i></b>
┖ <b>Bot Uptime :</b> {uptime}

┎ <b><i>INSTANCE RAM ( BOT ) :</i></b>
┃ {ram_bar} {ram_pct}%
┖ <b>U :</b> {ram_used} | <b>F :</b> {ram_free} | <b>T :</b> {ram_total}

┎ <b><i>SYSTEM RAM :</i></b>
┃ {sys_ram_bar} {sys_ram_pct}%
┖ <b>U :</b> {sys_ram_used} | <b>F :</b> {sys_ram_free} | <b>T :</b> {sys_ram_total}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap_pct}%
┖ <b>U :</b> {swap_used} | <b>F :</b> {swap_free} | <b>T :</b> {swap_total}

┎ <b><i>INSTANCE CPU ( BOT ) :</i></b>
┃ <b>Instance Core(s) :</b> {instance_cpu}
┠ <b>Total Core(s) :</b> {sys_cpu} | <b>P-Core(s) :</b> {p_cores} | <b>V-Core(s) :</b> {v_cores}
┖ <b>Usable CPU(s) :</b> {usable_cpus}

┎ <b><i>SYSTEM DISK :</i></b>
┃ {disk_bar} {disk_pct}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {used} | <b>F :</b> {free} | <b>T :</b> {total}
"""

    SYS_STATS = """⌬ <b><i>SYSTEM OS :</i></b>
╟ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>SYSTEM NETWORK :</i></b>
╟ <b>Upload Data:</b> {sent_data}
┠ <b>Download Data:</b> {recv_data}
┠ <b>Pkts Sent:</b> {pkts_sent}k
┠ <b>Pkts Received:</b> {pkts_recv}k
┠ <b>Total I/O Data:</b> {total_io}
┖ <b>Bandwidth:</b> {bandwidth}

┎ <b><i>SYSTEM CPU :</i></b>
┃ {cpu_bar} {cpu_usage}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {avg_load}
┠ <b>P-Core(s) :</b> {p_cores} | <b>V-Core(s) :</b> {v_cores}
┠ <b>Total Core(s) :</b> {sys_cpu}
┖ <b>Usable CPU(s) :</b> {usable_cpus}
"""

    REPO_STATS = """⌬ <b><i>Repo Statistics :</i></b>
│
┟ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {official_v}
┖ <b>Last ChangeLog :</b> {changelog}

⌬ <b>REMARKS :</b> <code>{remarks}</code>
"""

    PKGS_STATS = """⌬ <b><i>Packages Statistics :</i></b>
│
┟ <b>python:</b> v{python}
┠ <b>aria2:</b> v{aria2}
┠ <b>qBittorrent:</b> v{qBittorrent}
┠ <b>SABnzbd+:</b> v{sabnzbd}
┠ <b>rclone:</b> v{rclone}
┠ <b>yt-dlp:</b> v{ytdlp}
┠ <b>ffmpeg:</b> v{ffmpeg}
┠ <b>7z:</b> v{sevenz}
┠ <b>Aiohttp:</b> v{aiohttp}
┠ <b>WzGram:</b> v{wzgram}
┠ <b>Google API:</b> v{gapi}
┖ <b>MegaSDK:</b> v{mega}
"""

    BOT_LIMITS = """⌬ <b><i>Bot Task Limits :</i></b>
│
┟ <b>Direct Limit :</b> {direct}
┠ <b>Torrent Limit :</b> {torrent}
┠ <b>GDriveDL Limit :</b> {gdrive}
┠ <b>RCloneDL Limit :</b> {rclone}
┠ <b>Clone Limit :</b> {clone}
┠ <b>JDown Limit :</b> {jdown}
┠ <b>NZB Limit :</b> {nzb}
┠ <b>YT-DLP Limit :</b> {ytdlp}
┠ <b>Playlist Limit :</b> {playlist}
┠ <b>Mega Limit :</b> {mega}
┠ <b>Leech Limit :</b> {leech}
┠ <b>Archive Limit :</b> {archive}
┠ <b>Extract Limit :</b> {extract}
┠ <b>Threshold Storage :</b> {storage}
┞ <b>Monthly Bandwidth :</b> {bandwidth}
│
┟ <b>Token Validity :</b> {verify_timeout}
┠ <b>User Time Limit :</b> {user_interval}
┠ <b>User Max Tasks :</b> {user_tasks}
┖ <b>Bot Max Tasks :</b> {bot_tasks}
"""

    # RESTART & PING
    RESTARTING = "<i>Restarting...</i>"
    RESTART_CONFIRM = "<i>Are you really sure you want to restart the bot ?</i>"
    RESTART_SUCCESS = """⌬ <b><i>{title}</i></b>
┟ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┠ <b>Branch:</b> {branch}
┖ <b>Version:</b> {version}"""
    RESTARTED = """⌬ <b><i>Bot Restarted!</i></b>"""
    PING = "<i>Starting Ping..</i>"
    PING_VALUE = "<b>Pong</b>\n<code>{value} ms..</code>"

    # ----------------------
    # TASK NOTIFICATIONS & COMPLETION (3.1.11-x)
    TASK_START = """<b><i>Task Started</i></b>
┟ <b>Mode</b> → {Mode}
┖ <b>By</b> → {Tag}\n\n"""
    TASK_SOURCE = """➲ <b>Source</b> →
┖ <b>Added On</b> → {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    PM_START = "➲ <b><u>Task Started</u></b>\n│\n┖ <b>Link</b> → <a href='{msg_link}'>Click Here</a>"
    L_LOG_START = "➲ <b><u>Leech Started</u></b>\n│\n┟ <b>User</b> → {mention} ( #ID{uid} )\n┖ <b>Source</b> → <a href='{msg_link}'>Click Here</a>"

    # UPLOAD & STATUS
    NAME = "<b><i>{Name}</i></b>\n│\n"
    SIZE = "┟ <b>Task Size</b> → {Size}\n"
    ELAPSE = "┠ <b>Time Taken</b> → {Time}\n"
    MODE = "┠ <b>In / Out Mode</b> → {Mode}\n"

    # LEECH NOTIFICATION
    L_TOTAL_FILES = "┠ <b>Total Files</b> → {Files}\n"
    L_CORRUPTED_FILES = "┠ <b>Corrupted Files</b> → {Corrupt}\n"
    L_CC = "┖ <b>Task By</b> → {Tag}\n\n"
    PM_BOT_MSG = "➲ <b><i>File(s) have been Sent above</i></b>"
    L_BOT_MSG = "➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>"
    L_LL_MSG = "➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n"

    # MIRROR NOTIFICATION
    M_TYPE = "┠ <b>Type</b> → {Mimetype}\n"
    M_SUBFOLD = "┠ <b>SubFolders</b> → {Folder}\n"
    TOTAL_FILES = "┠ <b>Files</b> → {Files}\n"
    RCPATH = "┠ <b>Path</b> → <code>{RCpath}</code>\n"
    M_CC = "┖ <b>Task By</b> → {Tag}\n\n"
    M_BOT_MSG = "➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>"

    # BUTTON LABELS
    CLOUD_LINK = "☁️ Cloud Link"
    SAVE_MSG = "📨 Save Message"
    RCLONE_LINK = "♻️ RClone Link"
    DDL_LINK = "📎 {Serv} Link"
    SOURCE_URL = "🔐 Source Link"
    INDEX_LINK_F = "🗂 Index Link"
    INDEX_LINK_D = "⚡ Index Link"
    VIEW_LINK = "🌐 View Link"
    CHECK_PM = "📥 View in Bot PM"
    CHECK_LL = "🖇 View in Links Log"
    MEDIAINFO_LINK = "📃 MediaInfo"
    SCREENSHOTS = "🖼 ScreenShots"

    # ----------------------
    # PROGRESSIVE DISPLAY (3.1.11-x)
    STATUS_NAME = "<b><i>{Name}</i></b>"
    BAR = "\n┟ {Bar} <i>{Progress}</i>"
    PROCESSED = "\n┠ <b>Processed</b> → <i>{Processed}</i>"
    STATUS = '\n┠ <b>Status</b> → <b><a href="{Url}">{Status}</a></b>'
    ETA = " | <b>ETA:</b> {Eta}"
    SPEED = "\n┠ <b>Speed</b> → <i>{Speed}</i>"
    ELAPSED = "\n┠ <b>Time</b> → <i>{Elapsed}</i>"
    ENGINE = "\n┠ <b>Engine</b> → <i>{Engine}</i>"
    STA_MODE = "\n┠ <b>In / Out Mode</b> → <i>{Mode}</i>"
    SEEDERS = "\n┠ <b>Seeders</b> → {Seeders} | "
    LEECHERS = "<b>Leechers</b> → {Leechers}"

    # SEEDING
    SEED_SIZE = "\n┠ <b>Size</b> → <i>{Size}</i> | <b>Uploaded</b> → <i>{Upload}</i>"
    SEED_SPEED = "\n┠ <b>Speed</b> → <i>{Speed}</i> | "
    UPLOADED = "<b>Uploaded</b> → <i>{Upload}</i>"
    RATIO = "\n┠ <b>Ratio</b> → <i>{Ratio}</i>"
    TIME = "\n┠ <b>Time</b> → <i>{Time}</i>"
    SEED_ENGINE = "\n┠ <b>Engine</b> → <i>{Engine}</i>"

    # NON-PROGRESSIVE
    STATUS_SIZE = "\n┠ <b>Size</b> → <i>{Size}</i>"
    NON_ENGINE = "\n┠ <b>Engine</b> → <i>{Engine}</i>"

    # FOOTER & NAVIGATION
    USER = "\n\n<b>Task By {User}</b> ( #ID{Id} )"
    ID = "<b>ID:</b> <code>{Id}</code>"
    BTSEL = "\n┠ <b>Select</b> → {Btsel}"
    CANCEL = "\n┖ {Cancel}\n\n"
    FOOTER = "⌬ <b><i>Bot Stats</i></b>\n"
    TASKS = "┠ <b>Tasks</b> → {Tasks}\n"
    BOT_TASKS = "┠ <b>Tasks</b> → {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n"
    Cpu = "┠ <b>CPU:</b> {cpu}% | "
    FREE = "<b>F:</b> {free} [{free_p}%]"
    Ram = "\n┠ <b>RAM:</b> {ram}% | "
    uptime = "<b>UPTIME:</b> {uptime}"
    DL = "\n┖ <b>DL:</b> {DL}/s | "
    UL = "<b>UL:</b> {UL}/s"
    PREVIOUS = "⫷"
    REFRESH = "ᴘᴀɢᴇs\n{Page}"
    NEXT = "⫸"

    # SEARCH & COUNT
    STOP_DUPLICATE = (
        "File/Folder is already available in Drive.\nHere are {content} list results:"
    )
    COUNT_MSG = "<b>Counting:</b> <code>{LINK}</code>"
    COUNT_NAME = "<b><i>{COUNT_NAME}</i></b>\n│\n"
    COUNT_SIZE = "┟ <b>Size</b> → {COUNT_SIZE}\n"
    COUNT_TYPE = "┠ <b>Type</b> → {COUNT_TYPE}\n"
    COUNT_SUB = "┠ <b>SubFolders</b> → {COUNT_SUB}\n"
    COUNT_FILE = "┠ <b>Files</b> → {COUNT_FILE}\n"
    COUNT_CC = "┖ <b>By</b> → {COUNT_CC}\n"
    LIST_SEARCHING = "<b>Searching for <i>{NAME}</i></b>"
    LIST_FOUND = "<b>Found {NO} result for <i>{NAME}</i></b>"
    LIST_NOT_FOUND = "No result found for <i>{NAME}</i>"
    NO_ACTIVE_DL = """<i>No Active Tasks!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
"""

    # ----------------------
    # USER SETTINGS MENUS (3.1.11-x)
    USER_SETTING = """⌬ <b>User Settings :</b>
│
┟ <b>Name</b> → {user_name}
┠ <b>UserID</b> → #ID{user_id}
┠ <b>Username</b> → @{username}
┠ <b>Telegram DC</b> → {dc_id}
┖ <b>Telegram Lang</b> → {lang_name}"""

    GENERAL_SETTING = """⌬ <b>General Settings :</b>
┟ <b>Name</b> → {user_name}
┃
┠ <b>Default Upload Package</b> → <b>{du}</b>
┖ <b>Default Usage Mode</b> → <b>{tr}'s</b> token/config"""

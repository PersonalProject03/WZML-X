#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # START COMMAND & TOKEN SYSTEM (3.1.11-x)
    ST_BN1_NAME = "⚡ Source Repo"
    ST_BN1_URL = "https://www.github.com/SilentDemonSD/WZML-X"
    ST_BN2_NAME = "🌀 Network Updates"
    ST_BN2_URL = "https://t.me/WZML_X"
    ST_MSG = """<b><i>🛸 FURIATIS SYSTEM ACTIVATED</i></b>
<i>High-speed link processor ready for Cloud, Telegram & DDL mirror operations.</i>
<b>Type {help_command} to initialize command matrix</b>"""
    ST_BOTPM = """<i>🔮 Matrix link initialized. All task artifacts will be dispatched to your private terminal.</i>"""
    ST_UNAUTH = """<i>⛔ Access Denied! Unregistered identity detected. Deploy your own Furiatis core.</i>"""

    # VERIFICATION / LOGIN
    VERIFY_SUCCESS = """◈ Access Login Token : 
    │
    ┟ <b>Status</b> ► <code>Generated Successfully</code>
    ┟ <b>Access Token</b> ► <code>{input_token}</code>
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
    LOGGED_IN = "<b>⚡ Identity Verified: Bot Already Active!</b>"
    INVALID_PASS = "<b>❌ Access Key Rejected!</b>\n\nProvide valid security clearance."
    PASS_LOGGED = "<b>🔓 Security Pass Granted: Permanent Core Access Established!</b>"
    LOGIN_USED = "<b>🛰 Clearance Syntax:</b>\n\n<code>/cmd [password]</code>"
    LOG_DISPLAY_BT = "📑 System Telemetry"
    WEB_PASTE_BT = "📨 Pastebin Dump"

    # HELP MENU
    BASIC_BT = "⚡ Core"
    USER_BT = "👤 User"
    MICS_BT = "🔮 Misc"
    O_S_BT = "🛡 Security"
    CLOSE_BT = "✖ Terminate"
    HELP_HEADER = "◈ <b><i>FURIATIS COMMAND MATRIX</i></b>\n\n<b>Note: <i>Tap any vector for tactical specs.</i></b>"

    # ----------------------
    # BOT & SYSTEM STATISTICS (3.1.11-x)
    STATS_HOME = """◈ <b>SYSTEM TELEMETRY ENGINE</b>
┖ <b>Uptime Vector</b> ► <code>{uptime}</code>
┠ <b>Bandwidth</b> ► <code>{bandwidth}</code>
┖ <b>Used:</b> <code>{used}</code> | <b>Free:</b> <code>{free}</code> | <b>Total:</b> <code>{total}</code>

◈ <b>KERNEL MONITOR</b>
┟ <b>OS Uptime</b> ► <code>{os_uptime}</code>
┠ <b>OS Kernel</b> ► <code>{os_version}</code>
┖ <b>Architecture</b> ► <code>{os_arch}</code>

◈ <b>BUILD INFRASTRUCTURE</b>
┟ <b>Build Tag</b> ► <code>{version}</code>
┠ <b>Last Synced</b> ► <code>{commit_date}</code>
┖ <b>Commit Brief</b> ► <code>{changelog}</code>"""

    BOT_STATS = """◈ <b><i>SYSTEM TELEMETRY ENGINE</i></b>
┖ <b>Uptime Vector</b> ► <code>{uptime}</code>

╔═ <b><i>RAM METRICS</i></b>
║ {ram_bar} <b>{ram_pct}%</b>
╚═ <b>Allocated:</b> <code>{ram_used}</code> | <b>Available:</b> <code>{ram_free}</code> | <b>Max:</b> <code>{ram_total}</code>

╔═ <b><i>SYSTEM RAM</i></b>
║ {sys_ram_bar} <b>{sys_ram_pct}%</b>
╚═ <b>Used:</b> <code>{sys_ram_used}</code> | <b>Free:</b> <code>{sys_ram_free}</code> | <b>Total:</b> <code>{sys_ram_total}</code>

╔═ <b><i>SWAP SPACE</i></b>
║ {swap_bar} <b>{swap_pct}%</b>
╚═ <b>Active:</b> <code>{swap_used}</code> | <b>Free:</b> <code>{swap_free}</code> | <b>Total:</b> <code>{swap_total}</code>

╔═ <b><i>CPU MATRIX</i></b>
║ <b>Instance Core(s):</b> <code>{instance_cpu}</code>
┠ <b>Total Core(s):</b> <code>{sys_cpu}</code> | <b>P-Core(s):</b> <code>{p_cores}</code> | <b>V-Core(s):</b> <code>{v_cores}</code>
╚═ <b>Allocated CPU:</b> <code>{usable_cpus}</code>

╔═ <b><i>STORAGE CORE</i></b>
║ {disk_bar} <b>{disk_pct}%</b>
║ <b>Read Rate</b> ► <code>{disk_read}</code>
║ <b>Write Rate</b> ► <code>{disk_write}</code>
╚═ <b>Used:</b> <code>{used}</code> | <b>Free:</b> <code>{free}</code> | <b>Capacity:</b> <code>{total}</code>
"""

    SYS_STATS = """◈ <b><i>KERNEL MONITOR</i></b>
┟ <b>OS Uptime</b> ► <code>{os_uptime}</code>
┠ <b>OS Kernel</b> ► <code>{os_version}</code>
┖ <b>Architecture</b> ► <code>{os_arch}</code>

◈ <b><i>NETWORK PIPELINE</i></b>
┟ <b>Tx Data</b> ► <code>{sent_data}</code>
┠ <b>Rx Data</b> ► <code>{recv_data}</code>
┠ <b>Packets Transmitted</b> ► <code>{pkts_sent}k</code>
┠ <b>Packets Received</b> ► <code>{pkts_recv}k</code>
┠ <b>Total Throughput</b> ► <code>{total_io}</code>
┖ <b>Bandwidth</b> ► <code>{bandwidth}</code>

╔═ <b>CPU MATRIX</b>
║ {cpu_bar} <b>{cpu_usage}%</b>
┟ <b>Clock Speed</b> ► <code>{cpu_freq}</code>
┠ <b>System Load</b> ► <code>{avg_load}</code>
┠ <b>P-Cores</b> ► <code>{p_cores}</code> | <b>V-Cores</b> ► <code>{v_cores}</code>
┠ <b>Total Cores</b> ► <code>{sys_cpu}</code>
┖ <b>Allocated CPU</b> ► <code>{usable_cpus}</code>
"""

    REPO_STATS = """◈ <b><i>CORE BUILD INFRASTRUCTURE</i></b>
┟ <b>Last Synced</b> ► <code>{last_commit}</code>
┠ <b>Build Tag</b> ► <code>{bot_version}</code>
┠ <b>Upstream Tag</b> ► <code>{official_v}</code>
┖ <b>Commit Brief</b> ► <code>{changelog}</code>

◈ <b>SYSTEM LOG</b> ► <code>{remarks}</code>
"""

    PKGS_STATS = """◈ <b><i>SYSTEM DEPENDENCIES</i></b>
│
┟ <b>python:</b> <code>v{python}</code>
┠ <b>aria2:</b> <code>v{aria2}</code>
┠ <b>qBittorrent:</b> <code>v{qBittorrent}</code>
┠ <b>SABnzbd+:</b> <code>v{sabnzbd}</code>
┠ <b>rclone:</b> <code>v{rclone}</code>
┠ <b>yt-dlp:</b> <code>v{ytdlp}</code>
┠ <b>ffmpeg:</b> <code>v{ffmpeg}</code>
┠ <b>7z:</b> <code>v{sevenz}</code>
┠ <b>Aiohttp:</b> <code>v{aiohttp}</code>
┠ <b>WzGram:</b> <code>v{wzgram}</code>
┠ <b>Google API:</b> <code>v{gapi}</code>
┖ <b>MegaSDK:</b> <code>v{mega}</code>
"""

    BOT_LIMITS = """◈ <b><i>POLICIES & QUOTAS</i></b>
┟ <b>HTTP Direct</b> ► <code>{direct}</code>
┠ <b>BitTorrent</b> ► <code>{torrent}</code>
┠ <b>GDrive DL</b> ► <code>{gdrive}</code>
┠ <b>RClone DL</b> ► <code>{rclone}</code>
┠ <b>Cloud Clone</b> ► <code>{clone}</code>
┠ <b>JDownloader</b> ► <code>{jdown}</code>
┠ <b>NZB Vector</b> ► <code>{nzb}</code>
┠ <b>YT-DLP Vector</b> ► <code>{ytdlp}</code>
┠ <b>Playlist Batch</b> ► <code>{playlist}</code>
┠ <b>Mega Engine</b> ► <code>{mega}</code>
┠ <b>Telegram Leech</b> ► <code>{leech}</code>
┠ <b>Archive Engine</b> ► <code>{archive}</code>
┠ <b>Extract Engine</b> ► <code>{extract}</code>
┠ <b>Threshold Limit</b> ► <code>{storage}</code>
┞ <b>Monthly Bandwidth</b> ► <code>{bandwidth}</code>
│
┟ <b>Token Validity</b> ► <code>{verify_timeout}</code>
┠ <b>Task Timeout</b> ► <code>{user_interval}</code>
┠ <b>Concurrency Limit</b> ► <code>{user_tasks}</code>
┖ <b>Global Concurrency</b> ► <code>{bot_tasks}</code>
"""

    # RESTART & PING
    RESTARTING = "<i>🌀 Rebooting Furiatis Engine Core...</i>"
    RESTART_CONFIRM = "<i>Are you really sure you want to restart the bot ?</i>"
    RESTART_SUCCESS = """◈ <b><i>FURIATIS ONLINE!</i></b>
┟ <b>Date</b> ► <code>{date}</code>
┠ <b>Time</b> ► <code>{time}</code>
┠ <b>Time Zone</b> ► <code>{timz}</code>
┠ <b>Branch</b> ► <code>{branch}</code>
┖ <b>Version Tag</b> ► <code>{version}</code>"""
    RESTARTED = """◈ <b><i>Furiatis Core Reset Complete!</i></b>"""
    PING = "<i>⚡ Measuring Hyper-Frequency Signal...</i>"
    PING_VALUE = "<b>📡 Network Latency</b>\n<code>{value} ms</code>"

    # ----------------------
    # TASK NOTIFICATIONS & COMPLETION (3.1.11-x)
    TASK_START = """<b><i>🚀 Task Dispatched</i></b>
┟ <b>Protocol</b> ► <code>{Mode}</code>
┖ <b>Operator</b> ► {Tag}\n\n"""
    TASK_SOURCE = """◈ <b>Source Vector</b> ►
┖ <b>Received</b> ► <code>{On}</code>
------------------------------------------
{Source}
------------------------------------------\n\n"""
    PM_START = "◈ <b><u>Hyper Task Initialized</u></b>\n│\n┖ <b>Terminal Link</b> ► <a href='{msg_link}'>Access Stream</a>"
    L_LOG_START = "◈ <b><u>Leech Telemetry Activated</u></b>\n│\n┟ <b>Operator</b> ► {mention} ( #ID<code>{uid}</code> )\n┖ <b>Target Vector</b> ► <a href='{msg_link}'>Inspect Stream</a>"

    # UPLOAD & STATUS
    NAME = "<b><i>{Name}</i></b>\n│\n"
    SIZE = "┟ <b>Payload Size</b> ► <code>{Size}</code>\n"
    ELAPSE = "┠ <b>Duration</b> ► <code>{Time}</code>\n"
    MODE = "┠ <b>Pipeline Mode</b> ► <code>{Mode}</code>\n"

    # LEECH NOTIFICATION
    L_TOTAL_FILES = "┠ <b>Artifact Count</b> ► <code>{Files}</code>\n"
    L_CORRUPTED_FILES = "┠ <b>Corrupted Blocks</b> ► <code>{Corrupt}</code>\n"
    L_CC = "┖ <b>Operator</b> ► {Tag}\n\n"
    PM_BOT_MSG = "◈ <b><i>Artifacts Dispatched to Private Terminal Above</i></b>"
    L_BOT_MSG = "◈ <b><i>Artifacts Sent to Secure Bot Direct Message</i></b>"
    L_LL_MSG = "◈ <b><i>Artifacts Transmitted to Index Channel...</i></b>\n"

    # MIRROR NOTIFICATION
    M_TYPE = "┠ <b>MIME Vector</b> ► <code>{Mimetype}</code>\n"
    M_SUBFOLD = "┠ <b>Sub-Trees</b> ► <code>{Folder}</code>\n"
    TOTAL_FILES = "┠ <b>Total Artifacts</b> ► <code>{Files}</code>\n"
    RCPATH = "┠ <b>Storage Target</b> ► <code>{RCpath}</code>\n"
    M_CC = "┖ <b>Operator</b> ► {Tag}\n\n"
    M_BOT_MSG = "◈ <b><i>Cloud Links Dispatched to PM</i></b>"

    # BUTTON LABELS
    CLOUD_LINK = "🌩️ Cloud Drive"
    SAVE_MSG = "💎 Vault Save"
    RCLONE_LINK = "♻️ RClone Target"
    DDL_LINK = "📎 {Serv} Direct"
    SOURCE_URL = "🔐 Origin Vector"
    INDEX_LINK_F = "🗂 File Index"
    INDEX_LINK_D = "⚡ Fast Index"
    VIEW_LINK = "🌐 Web Viewer"
    CHECK_PM = "📥 Terminal PM"
    CHECK_LL = "🖇 Links Vault"
    MEDIAINFO_LINK = "📃 Telemetry Report"
    SCREENSHOTS = "🖼 Frame Capture"

    # ----------------------
    # PROGRESSIVE DISPLAY (3.1.11-x)
    STATUS_NAME = "<b><i>{Name}</i></b>"
    BAR = "\n┟ {Bar} <i>{Progress}</i>"
    PROCESSED = "\n┠ <b>Processed</b> ► <code>{Processed}</code>"
    STATUS = '\n┠ <b>Status</b> ► <b><a href="{Url}">{Status}</a></b>'
    ETA = " | <b>ETA:</b> <code>{Eta}</code>"
    SPEED = "\n┠ <b>Throughput</b> ► <code>{Speed}</code>"
    ELAPSED = "\n┠ <b>Elapsed</b> ► <code>{Elapsed}</code>"
    ENGINE = "\n┠ <b>Processing Core</b> ► <code>{Engine}</code>"
    STA_MODE = "\n┠ <b>Pipeline Mode</b> ► <code>{Mode}</code>"
    SEEDERS = "\n┠ <b>Seeders</b> ► <code>{Seeders}</code> | "
    LEECHERS = "<b>Leechers</b> ► <code>{Leechers}</code>"

    # SEEDING
    SEED_SIZE = "\n┠ <b>Payload Size</b> ► <code>{Size}</code> | <b>Uploaded</b> ► <code>{Upload}</code>"
    SEED_SPEED = "\n┠ <b>Seeding Rate</b> ► <code>{Speed}</code> | "
    UPLOADED = "<b>Tx Data</b> ► <code>{Upload}</code>"
    RATIO = "\n┠ <b>Ratio Factor</b> ► <code>{Ratio}</code>"
    TIME = "\n┠ <b>Seed Duration</b> ► <code>{Time}</code>"
    SEED_ENGINE = "\n┠ <b>Seed Engine</b> ► <code>{Engine}</code>"

    # NON-PROGRESSIVE
    STATUS_SIZE = "\n┠ <b>Payload Size</b> ► <code>{Size}</code>"
    NON_ENGINE = "\n┠ <b>Processing Engine</b> ► <code>{Engine}</code>"

    # FOOTER & NAVIGATION
    USER = "\n\n<b>Dispatched By {User}</b> ( #ID<code>{Id}</code> )"
    ID = "<b>ID:</b> <code>{Id}</code>"
    BTSEL = "\n┠ <b>Selection Vector</b> ► {Btsel}"
    CANCEL = "\n┖ {Cancel}\n\n"
    FOOTER = "◈ <b><i>FURIATIS MATRIX METRICS</i></b>\n"
    TASKS = "┠ <b>Active Pipelines</b> ► <code>{Tasks}</code>\n"
    BOT_TASKS = "┠ <b>Active Pipelines</b> ► <code>{Tasks}/{Ttask}</code> | <b>Available Slots:</b> <code>{Free}</code>\n"
    Cpu = "┠ <b>CPU Load:</b> <code>{cpu}%</code> | "
    FREE = "<b>Free Memory:</b> <code>{free} [{free_p}%]</code>"
    Ram = "\n┠ <b>RAM Load:</b> <code>{ram}%</code> | "
    uptime = "<b>UPTIME:</b> <code>{uptime}</code>"
    DL = "\n┖ <b>Down Rate:</b> <code>{DL}/s</code> | "
    UL = "<b>Up Rate:</b> <code>{UL}/s</code>"
    PREVIOUS = "◄ Prev"
    REFRESH = "Matrix\n{Page}"
    NEXT = "Next ►"

    # SEARCH & COUNT
    STOP_DUPLICATE = "⛔ Duplicate Payload Detected in Storage.\nMatching Results:"
    COUNT_MSG = "<b>⚡ Analyzing Vector:</b> <code>{LINK}</code>"
    COUNT_NAME = "<b><i>{COUNT_NAME}</i></b>\n│\n"
    COUNT_SIZE = "┟ <b>Total Size</b> ► <code>{COUNT_SIZE}</code>\n"
    COUNT_TYPE = "┠ <b>Data Vector</b> ► <code>{COUNT_TYPE}</code>\n"
    COUNT_SUB = "┠ <b>Sub-Tree Directories</b> ► <code>{COUNT_SUB}</code>\n"
    COUNT_FILE = "┠ <b>Total Artifacts</b> ► <code>{COUNT_FILE}</code>\n"
    COUNT_CC = "┖ <b>Operator</b> ► {COUNT_CC}\n"
    LIST_SEARCHING = "<b>🔍 Scanning Index Vector for <i>{NAME}</i></b>"
    LIST_FOUND = "<b>🎯 Located {NO} result(s) for <i>{NAME}</i></b>"
    LIST_NOT_FOUND = "<b>❌ Vector Search empty for <i>{NAME}</i></b>"
    NO_ACTIVE_DL = """<i>🛸 Idle State: No Active Pipelines Running</i>
    
◈ <b><i>Furiatis Diagnostics</i></b>
┠ <b>CPU Load:</b> <code>{cpu}%</code> | <b>Available Storage:</b> <code>{free} [{free_p}%]</code>
┖ <b>RAM Usage:</b> <code>{ram}</code> | <b>Uptime:</b> <code>{uptime}</code>
"""

    # ----------------------
    # USER SETTINGS MENUS (3.1.11-x)
    USER_SETTING = """◈ <b>USER PROFILE MATRIX</b>
│
┟ <b>Identity</b> ► {user_name}
┠ <b>User GID</b> ► #ID<code>{user_id}</code>
┠ <b>Handle</b> ► @{username}
┠ <b>Data Center</b> ► <code>DC-{dc_id}</code>
┖ <b>Interface Language</b> ► <code>{lang_name}</code>"""

    GENERAL_SETTING = """◈ <b>GENERAL CONFIGURATION</b>
┟ <b>Operator Name</b> ► {user_name}
┃
┠ <b>Target Upload Engine</b> ► <b>{du}</b>
┖ <b>Credentials Mode</b> ► <b>{tr}'s</b> configuration"""

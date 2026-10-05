# Release Changelog: v3.1.11

## 🚀 Highlights & Major Features

### 1. 📤 Telegram Clone Engine (`/clone` & `tg_clone.py`)
- **Direct Telegram-to-Telegram Relaying:** Copy or forward messages directly between Telegram chats without downloading files or saving them to local disk.
- **Multi-Destination Support (`-ud`):** Target multiple destination chats simultaneously (supports named dump chats, raw IDs, usernames, or `id|topic_id`).
- **Flexible Content Filtering:**
  - `-ct`: Filter by content type (`doc`, `med`, or `all`).
  - `-ex`: Exclude specific file extensions (e.g., `-ex mkv srt`).
  - `-mn`, `-xn`, `-mc`, `-xc`: Regex matchers for message filenames (`mn`/`xn`) and captions (`mc`/`xc`).
- **Forward Mode (`-fwd`):** Forward messages in batches of 100 while keeping "forwarded from" headers.
- **Smart Restricted Content Handling:** Handles chats with restricted forwarding gracefully by detecting protected messages, automatically stopping after repeated restricted message streaks, and reporting skipped message ranges with copy-pasteable `/leech` commands.
- **Adaptive Rate Control:** Dynamically adjusts pacing upon encountering Telegram flood waits and scales back speed once flood warnings subside.

---

### 2. 🔐 Encrypted User Session Vault & Security (`session_vault.py` & `session_crypt.py`)
- **AES-256-GCM + Scrypt Encryption:** User Telegram string sessions are encrypted with user-defined passphrases before storage. Raw passphrases and derived keys are never stored in the database.
- **In-Memory Session Key Vault:** Session keys remain active in memory with a configurable TTL (`USER_SESSION_KEY_TTL`, default 12h) and automatically expire/reap after idle timeouts (`USER_SESSION_IDLE`).
- **Commands & Prompt Management:**
  - `/lockmysession` (`/lms`): Instantly purges active session keys from memory.
  - Interactive PM prompt workflow for secure passphrase entry and session unlocking.
- **User Session Connection Pool (`UserSessionPool`):** Dynamic lifecycle management for active Pyrogram clients using user sessions, including concurrency limits (`USER_SESSION_MAX_CLIENTS`) and idle cleanup (`SessionReaper`).

---

### 3. 🎬 Web Stream Server & Merged Video Player (`stream_server.py`, `stream.html`, `wserver.py`)
- **Merged Seamless Video Playback (`/stream -m` / `-merge`):**
  - Continuous timeline playback for split video/audio files or multi-part media.
  - Automatic detection and trim overlapping calculation (`split_parts.py`) for split parts (e.g. `.part1`, `.part2`).
  - Custom HTML5 `<merged-video>` element with gapless preloading, seamless part switching, and automatic fallback to advanced WASM/FFmpeg decoding.
- **M3U Playlist Export (`/m3u/{token}`):** Generate M3U playlists for multi-part streams to play directly in external media players (VLC, PotPlayer, Infuse, etc.).
- **Subtitle Sidecar Extraction:** Asynchronous multi-track WebVTT subtitle extraction and caching for embedded subtitles (`/subs/{token}/{idx}`).
- **Server Performance & Caching:**
  - Optimized database stream queries with compound indexes (`cid`, `mid`).
  - Memory-guarded LRU caches for stream probes, poster artwork, playlist metadata, and merged video configurations.
  - Proper HTTP conditional headers (`ETag`, `If-None-Match`, `Cache-Control`) for efficient bandwidth usage and browser caching.

---

### 4. ⚙️ User Settings Portal Export & Import (`settings_portal.py`)
- **Export & Import User Configs:** Easily export user settings to an encrypted JSON file (`.json`) sealed with a custom passphrase using AES-256-GCM.
- **Security Protections:** Sensitive parameters (passwords, tokens, sessions, thumbnails, sudo/auth flags) are blocked from export/import to prevent privilege escalation or state leakages.

---

### 5. 📥 SABnzbd & Direct NZB Fetching (`nzb_downloader.py`)
- **Indexer API Protection:** Fetches NZB files directly within the bot before handing them off to SABnzbd, preventing API keys from being exposed to the SABnzbd server logs.
- **NZB Release Name Sanitization:** Extracts release metadata (`<meta type="name">`) and sanitizes indexer-supplied filenames for clean directory creation.

---

### 6. 🛠️ Deprecations, Refactoring & System Updates
- **`LEECH_DUMP_CHAT` Deprecation:** Automatically migrated to `LEECH_DUMP_CHATS` and `LEECH_LOG_CHAT` (`deprecations.py`).
- **qBittorrent Configuration:** Optimized memory working set limit (`MemoryWorkingSetLimit=512MB`) and I/O thread count in `qBittorrent.conf` for improved low-memory performance.
- **Aria2 Tracker Script:** Asynchronous background fetching of public torrent trackers in `setpkgs.sh`.
- **New Dependency:** Added `cryptography==46.0.7` to `requirements.txt`.
- **Version Bump:** Updated version to `v3.1.11-x` in `bot/version.py`.

## ***Custom Themes Guide*** 🛠

This directory allows you to customize the visual theme of the bot using `BOT_THEME`.

### ***Theme Selection Options:***
- `BOT_THEME = "minimal"` — Uses [wzml_minimal.py](wzml_minimal.py).
- `BOT_THEME = "random"` — Randomly selects any available `wzml_*.py` theme on startup.
- `BOT_THEME = "your_theme_name"` — Loads `wzml_your_theme_name.py`.
- `BOT_THEME = ""` (or empty) — Bypasses themes and falls back to hardcoded bot strings.

---

### ***How to Create a Custom Theme:***

#### ***Step 1: Create a Theme File***
Copy [wzml_minimal.py](wzml_minimal.py) and rename it with a `wzml_` prefix, for example `wzml_futuristic.py`.

#### ***Step 2: Customize Your Design ✨***
Edit the message strings and button labels inside the `WZMLStyle` class.

#### ***Important Rules while Editing:***
1. **Do not change placeholder keys inside `{}`** (e.g. `{bot_uptime}`, `{cpu}`, `{task_name}`).
2. **Do not rename class attributes** (e.g. `ST_MSG`, `BOT_STATS`, `STATUS_NAME`).
3. **Do not change the class name `WZMLStyle`**.
4. **Do not use python `f-strings`** inside the style class; plain strings with formatting placeholders are required.
5. **Set `BOT_THEME = "futuristic"`** in your config to activate `wzml_futuristic.py`.
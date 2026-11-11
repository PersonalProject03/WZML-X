import json
from html import escape

from pyrogram.enums import ChatType

from .. import task_dict, task_dict_lock
from ..helper.telegram_helper.bot_api import bot_api
from ..helper.telegram_helper.message_utils import send_message


def _generate_live_status_widget_html(title: str, stats: dict) -> str:
    """Generate self-contained HTML/CSS for an interactive Telegram Bot API 10.4 Widget."""
    safe_title = escape(title)
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0;
    padding: 10px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: #18191c;
    color: #ffffff;
    box-sizing: border-box;
    border-radius: 12px;
  }}
  .card {{
    background: #23252a;
    border: 1px solid #31353d;
    border-radius: 10px;
    padding: 12px;
  }}
  .header {{
    font-size: 13px;
    font-weight: 700;
    color: #40a7e3;
    display: flex;
    justify-content: space-between;
    margin-bottom: 8px;
  }}
  .metric-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin: 10px 0;
  }}
  .metric-box {{
    background: #18191c;
    border: 1px solid #2a2d34;
    padding: 8px;
    border-radius: 8px;
    text-align: center;
  }}
  .metric-label {{
    font-size: 10px;
    color: #8b929d;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .metric-value {{
    font-size: 13px;
    font-weight: 600;
    margin-top: 3px;
    color: #e4e7eb;
  }}
  .bar-container {{
    width: 100%;
    background: #2e323b;
    border-radius: 6px;
    height: 7px;
    overflow: hidden;
    margin: 10px 0 6px 0;
  }}
  .bar-fill {{
    height: 100%;
    background: linear-gradient(90deg, #40a7e3, #29d38c);
    width: {stats.get("progress_pct", 0)}%;
    transition: width 0.3s ease;
  }}
  .footer {{
    font-size: 10px;
    color: #717782;
    text-align: right;
    margin-top: 4px;
  }}
</style>
</head>
<body>
  <div class="card">
    <div class="header">
      <span>⚡ {safe_title}</span>
      <span id="badge" style="color:#29d38c;">LIVE</span>
    </div>
    <div class="bar-container">
      <div id="bar" class="bar-fill"></div>
    </div>
    <div class="metric-grid">
      <div class="metric-box">
        <div class="metric-label">Active Tasks</div>
        <div class="metric-value" id="val-tasks">{stats.get("tasks", 0)}</div>
      </div>
      <div class="metric-box">
        <div class="metric-label">DL / UL Speed</div>
        <div class="metric-value" id="val-speed">{stats.get("speed", "0 B/s")}</div>
      </div>
    </div>
    <div class="footer">Telegram Native Widget 10.4</div>
  </div>
  <script>
    const w = window.TelegramWidget;
    function updateState() {{
      if (!w || !w.chatData) return;
      try {{
        const d = JSON.parse(w.chatData);
        if (d.tasks !== undefined) document.getElementById('val-tasks').textContent = d.tasks;
        if (d.speed !== undefined) document.getElementById('val-speed').textContent = d.speed;
        if (d.progress_pct !== undefined) document.getElementById('bar').style.width = d.progress_pct + '%';
      }} catch(e) {{}}
    }}
    if (w) {{
      w.onEvent('chatDataChanged', updateState);
      updateState();
    }}
  </script>
</body>
</html>"""


def _generate_stremio_dup_widget_html(total_scanned: int, dup_groups: list) -> str:
    """Generate in-chat interactive explorer HTML widget for Stremio duplicates."""
    items_html = ""
    for g in dup_groups[:15]:
        first = g[0]
        title = escape(first["title"])
        year = f" ({first['year']})" if first["year"] else ""
        res = (
            f" [{first['resolution'].upper()}]"
            if first["resolution"] != "Unknown"
            else ""
        )
        copies = len(g)
        items_html += f"""
        <div style="border-bottom:1px solid #2a2d34;padding:6px 0;">
          <div style="font-weight:600;font-size:11px;color:#e4e7eb;">{title}{year}{res}</div>
          <div style="font-size:10px;color:#f39c12;margin-top:2px;">⚠️ {copies} duplicate copies detected</div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0;
    padding: 10px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: #18191c;
    color: #ffffff;
    border-radius: 12px;
  }}
  .card {{
    background: #23252a;
    border: 1px solid #31353d;
    border-radius: 10px;
    padding: 12px;
  }}
  .header {{
    font-size: 13px;
    font-weight: 700;
    color: #f39c12;
    display: flex;
    justify-content: space-between;
    margin-bottom: 8px;
  }}
  .stats {{
    font-size: 11px;
    color: #8b929d;
    margin-bottom: 8px;
    padding-bottom: 6px;
    border-bottom: 1px solid #31353d;
  }}
  .list {{
    max-height: 180px;
    overflow-y: auto;
    font-size: 11px;
  }}
  .footer {{
    font-size: 9px;
    color: #717782;
    text-align: right;
    margin-top: 6px;
  }}
</style>
</head>
<body>
  <div class="card">
    <div class="header">
      <span>🎬 Stremio Duplicates Audit</span>
    </div>
    <div class="stats">
      Scanned: <b style="color:#fff;">{total_scanned}</b> | Duplicate Sets: <b style="color:#f39c12;">{len(dup_groups)}</b>
    </div>
    <div class="list">
      {items_html}
    </div>
    <div class="footer">Native In-Chat Widget (PM)</div>
  </div>
</body>
</html>"""


async def send_native_widget(client, message):
    """Command `/widget`: Tests Telegram Bot API 10.4 HTML Widget sending in private chat."""
    if message.chat.type != ChatType.PRIVATE:
        await send_message(
            message,
            "⚠️ <b>Telegram Bot API 10.4 Restriction:</b>\n"
            "Native HTML Widgets can currently only be rendered in <b>Private Chat (Bot PM)</b>.\n"
            "Please send <code>/widget</code> directly in PM with the bot to test it!",
        )
        return

    async with task_dict_lock:
        active_tasks = len(task_dict)

    initial_stats = {
        "tasks": active_tasks,
        "speed": "0 B/s",
        "progress_pct": 50 if active_tasks > 0 else 100,
    }

    widget_html = _generate_live_status_widget_html(
        title="Bot Live Activity",
        stats=initial_stats,
    )

    await send_message(message, "⏳ <i>Deploying Telegram Native HTML Widget...</i>")
    res = await bot_api.send_widget(
        chat_id=message.chat.id,
        html=widget_html,
        chat_data=json.dumps(initial_stats),
    )

    if res and res.get("ok"):
        await send_message(
            message,
            "✅ <b>Native HTML Widget deployed successfully!</b>\n"
            "This card is rendered natively by Telegram inside your chat bubble via Bot API 10.4.",
        )
    else:
        err_desc = (
            res.get("description", "Unknown error") if res else "No response from API"
        )
        await send_message(
            message,
            f"❌ <b>Widget Delivery Note:</b> <code>{escape(str(err_desc))}</code>\n\n"
            f"<i>(Note: Telegram Bot API 10.4 widgets require a production client supporting Bot API 10.4 widgets and a valid BOT_TOKEN).</i>",
        )

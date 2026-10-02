from importlib import import_module
from os import listdir
from random import choice as rchoice

from bot import LOGGER
from bot.core.config_manager import Config
from bot.helper.themes import wzml_minimal

AVL_THEMES = {}
for theme in listdir("bot/helper/themes"):
    if theme.startswith("wzml_") and theme.endswith(".py"):
        AVL_THEMES[theme[5:-3]] = import_module(f"bot.helper.themes.{theme[:-3]}")


def BotTheme(var_name, default=None, **format_vars):
    theme_ = getattr(Config, "BOT_THEME", "minimal") or ""
    if isinstance(theme_, str):
        theme_ = theme_.strip().lower()
    else:
        theme_ = ""

    if not theme_ or theme_ in ("none", "false", "off", "default"):
        if default is not None:
            if format_vars:
                try:
                    return default.format(**format_vars)
                except Exception:
                    return default
            return default
        return None

    text = None
    if theme_ in AVL_THEMES:
        text = getattr(AVL_THEMES[theme_].WZMLStyle, var_name, None)
        if text is None:
            LOGGER.error(
                f"{var_name} not Found in {theme_}. Please recheck with Official Repo"
            )
    elif theme_ == "random" and AVL_THEMES:
        rantheme = rchoice(list(AVL_THEMES.values()))
        LOGGER.info(f"Random Theme Chosen: {rantheme}")
        text = getattr(rantheme.WZMLStyle, var_name, None)

    if text is None:
        text = getattr(wzml_minimal.WZMLStyle, var_name, default)

    if text is None:
        text = default

    if text is not None and format_vars:
        try:
            return text.format(**format_vars)
        except Exception as e:
            LOGGER.error(f"Error formatting BotTheme string '{var_name}': {e}")
            return text
    return text

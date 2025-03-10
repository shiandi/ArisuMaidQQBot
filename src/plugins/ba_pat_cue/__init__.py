from nonebot import get_plugin_config
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.plugin import PluginMetadata, on_command
from nonebot.rule import to_me

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="ba-pat-cue",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

ba_pat_cue = on_command("ba摸头提醒",rule=to_me())

@ba_pat_cue.handle()
async def pat_cue(bot:Bot,event:Event):
    await ba_pat_cue.finish()
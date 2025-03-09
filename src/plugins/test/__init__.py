from nonebot.plugin import PluginMetadata, get_plugin_config
from nonebot.plugin.on import on_command

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="test",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

echotest = on_command("复读")


@echotest.handle()
async def echo():
    await echotest.finish(f'你是复读机？')

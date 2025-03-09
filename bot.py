import nonebot
from nonebot.adapters.onebot.v12 import Adapter as ONEBOT_V12Adapter

from nonebot.adapters.console import Adapter as CONSOLEAdapter

from nonebot.adapters.minecraft import Adapter as MINECRAFTAdapter



nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V12Adapter)

driver.register_adapter(CONSOLEAdapter)

driver.register_adapter(MINECRAFTAdapter)

nonebot.load_builtin_plugins('echo', 'single_session')


nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()

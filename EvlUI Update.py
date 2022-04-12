#配置Windows下的开发环境

import os
import sys

from Controller.GamePathSelecter import GamePathSelecter
from Tools.FilePathTool import FilePathTool


#当前目录
currentPath = FilePathTool.getCurrentPath()

#config.ini文件路径
configPath = currentPath + "\\config.ini"

#判断config.ini文件是否存在
if not os.path.exists(configPath):
    print("config.ini not found, create one")
    with open(configPath, "w") as f:
        f.write("")
    GamePathSelecter.show_path_select_window()
    





 













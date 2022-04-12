import os
from tkinter import filedialog

class FilePathTool:

#use explorer locate the file
  def selectGamePath():
    currentPath = os.path.dirname(os.path.realpath(__file__))
    filePath = filedialog.askopenfilename(initialdir = currentPath,title = "选择魔兽所在目录",filetypes = (("all files","*.*"),("exe","World of Warcraft Launcher.exe")))
    print(filePath)
    return filePath

  #文件是否存在
  def fileExists(filePath):
    if os.path.exists(filePath):
        return True
    else:
        return False

  #当前目录
  def getCurrentPath():
    currentPath = os.path.dirname(os.path.realpath(__file__))
    return currentPath
  
  
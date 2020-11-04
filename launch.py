import os

if input("此文件仅供使用文件资源管理器启动的用户使用，\n"
         "使用IDLE（例如Pycharm）启动可能会发生意想不到的后果，我们不承担由此引起的任何后果。\n"
         "在启动之前，您可以的通过左上角的“X”退出。输入“start”启动。\n"
         "This file is only for users who launch with explorer, if you launch with IDLE(such as Pycharm), \n"
         "Unexpected consequences may occur, \n"
         "we does not bear any consequences arising therefrom.\n"
         "Before launching, You can exit by press the \"X\" in the upper left corner.Type \"start\" to launch\n"
         ).lower() != "start":
    exit(0)

local_path = os.path.abspath(".")
os.system(f"python {local_path}\\main.py")

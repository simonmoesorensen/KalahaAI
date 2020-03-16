import sys
from cx_Freeze import setup, Executable

packages = ["os", "json", "src"]
build_exe_options = {"packages": packages, "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Console"

setup(name="MancalaAI",
      version="1.0",
      description="A game of Mancala against an AI opponent",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py")])

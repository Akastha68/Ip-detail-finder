
import os
import time
from rich import print

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def Rbanner():
    colors = ["red", "yellow", "green"]
    for color in colors:
        clear_screen()
        print(f"""
[bold {color}]●[bold {colors[(colors.index(color)+1)%len(colors)]}] ●[bold {colors[(colors.index(color)+2)%len(colors)]}] ●
      .---.        .-----------
     /     \\  __  /    ------
    / /     \\(  )/    -----
   //////   ' \\/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\

       ====UU====UU====
           '//||\\'
[bold white]===========================≠≠≠≠==============
[bold white][[bold red]^[bold white]] [bold green] Author: Akash Patel
[bold white][[bold red]^[bold white]] [bold green] Github: https://github.com/Akastha68
[bold white][[bold red]^[bold white]] [bold green] Telegram: https://t.me/akash_patel45
[bold white]=============================================
""")
        time.sleep(0.5)

def Cbanner():
    clear_screen()
    print(f"""
[bold cyan]●[bold white] ●[bold white] ●
      .---.        .-----------
     /     \\  __  /    ------
    / /     \\(  )/    -----
   //////   ' \\/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\

       ====UU====UU====
           '//||\\'
[bold white]===========================≠≠≠≠==============
[bold white][[bold red]^[bold white]] [bold green] Author: Akash Patel
[bold white][[bold red]^[bold white]] [bold green] Github: https://github.com/Akastha68
[bold white][[bold red]^[bold white]] [bold green] Telegram: https://t.me/akash_patel45
[bold white]=============================================
""")

def Bbanner():
    clear_screen()
    print(f"""
[bold blue]●[bold white] ●[bold white] ●
      .---.        .-----------
     /     \\  __  /    ------
    / /     \\(  )/    -----
   //////   ' \\/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\

       ====UU====UU====
           '//||\\'
[bold white]===========================≠≠≠≠==============
[bold white][[bold red]^[bold white]] [bold green] Author: Akash Patel
[bold white][[bold red]^[bold white]] [bold green] Github: https://github.com/Akastha68
[bold white][[bold red]^[bold white]] [bold green] Telegram: https://t.me/akash_patel45
[bold white]=============================================
""")

def banner():
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    for color in colors:
        clear_screen()
        next1 = colors[(colors.index(color)+1) % len(colors)]
        next2 = colors[(colors.index(color)+2) % len(colors)]
        print(f"""
[bold {color}]●[bold {next1}] ●[bold {next2}] ●
      .---.        .-----------
     /     \\  __  /    ------
    / /     \\(  )/    -----
   //////   ' \\/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\

       ====UU====UU====
           '//||\\'
[bold white]===========================≠≠≠≠==============
[bold white][[bold red]^[bold white]] [bold green] Author: Akash Patel
[bold white][[bold red]^[bold white]] [bold green] Github: https://github.com/Akastha68
[bold white][[bold red]^[bold white]] [bold green] Telegram: https://t.me/akash_patel45
[bold white]=============================================
""")
        time.sleep(0.4)

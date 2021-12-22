#McOsuHelper
#by @yi6dev
#https://github.com/yi6dev/McOsuHelper
#Support: Windows 10
#Python ^3.9

import os
import sys
import zipfile
import threading
import glob
import time

import colorama
import keyboard
import cursor


__version__ = 1.1
__author__  = "yi6dev"

#define system clear command
if "darwin" in sys.platform or "linux" in sys.platform: clear = "clear"
else: clear = "cls"

#app dir path
config_path = os.path.dirname(os.path.abspath(sys.argv[0]))

#hide terminal cursor
try:
    cursor.hide()
except:
    pass


#app logic
class App(object):
    def __init__(self, args) -> None:
        self.colorized = False
        self.autoload = self.__read_configs()[2]

        if not "--no-ascii" in args:
            colorama.init()

            self.colorized = True
        
        if "--version" in args:
            print(f"version  = v{__version__}")
            print(f"author   = {__author__}")
            print(f"path     = {config_path}")
            return

        #init all
        self.keyhook()
        self.configs()
        self.render()
        self.autoloadhook()


    def keyhook(self):
        keyboard.add_hotkey("ctrl+alt+o", callback=self.__set_osu_path)
        keyboard.add_hotkey("ctrl+alt+d", callback=self.__set_download_path)
        keyboard.add_hotkey("ctrl+alt+l", callback=self.__set_autoload)
        keyboard.add_hotkey("ctrl+alt+i", callback=self.__install)
        keyboard.add_hotkey("ctrl+alt+c", callback=self.__config)
        keyboard.add_hotkey("ctrl+alt+e", callback=self.__exit)

    def autoloadhook(self):
        while 1:
            if self.autoload == "true":
                beatmaps = glob.glob(f"{self.__read_configs()[1]}\*.osz")

                if len(beatmaps):
                    self.__install()

            try: 
                time.sleep(1)
            except KeyboardInterrupt:
                os.system(clear)
                return

    def configs(self):
        if not os.path.exists(f"{config_path}\.osupath"):
            osu = open(f"{config_path}\.osupath", "w")
            osu.write("none")
            osu.close()

        if not os.path.exists(f"{config_path}\.downloadpath"):
            download = open(f"{config_path}\.downloadpath", "w")
            download.write("none")
            download.close()

        if not os.path.exists(f"{config_path}\.autoload"):
            autoload = open(f"{config_path}\.autoload", "w")
            autoload.write("false")
            autoload.close()

    def render(self):
        os.system(clear)

        if self.colorized:
            print(f"{colorama.Fore.WHITE}McOsuHelper")
            print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")
            print(f"{colorama.Fore.YELLOW}Options")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - Set osu path                        {colorama.Fore.LIGHTBLUE_EX}CTRL + ALT + O")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - Set download path                   {colorama.Fore.LIGHTBLUE_EX}CTRL + ALT + D")\

            if self.autoload == "false":
                print(f"{colorama.Fore.LIGHTBLACK_EX} - Autoload beatmaps                   {colorama.Fore.LIGHTBLUE_EX}CTRL + ALT + L")
            else:
                print(f"{colorama.Fore.LIGHTBLACK_EX} - {colorama.Fore.LIGHTGREEN_EX}Autoload beatmaps                   {colorama.Fore.LIGHTBLUE_EX}CTRL + ALT + L")

            print(f"{colorama.Fore.LIGHTBLACK_EX} - Install beatmaps                    {colorama.Fore.LIGHTBLUE_EX}CTRL + ALT + I")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - Show config                         {colorama.Fore.LIGHTBLUE_EX}CTRL + ALT + C")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - Exit                                {colorama.Fore.LIGHTBLUE_EX}CTRL + C")

        else:
            print("McOsuHelper")
            print("by @yi6dev\n")
            print("Options")
            print(" - Set osu path                        CTRL + ALT + O")
            print(" - Set download path                   CTRL + ALT + D")
            print(" - Autoload beatmaps                   CTRL + ALT + L")
            print(" - Install beatmaps                    CTRL + ALT + I")
            print(" - Show config                         CTRL + ALT + C")
            print(" - Exit                                CTRL + C")

    def __read_configs(self):
        self.configs()
        
        osu = open(f"{config_path}\.osupath", "r")
        osu_path = osu.read()
        osu.close()

        download = open(f"{config_path}\.downloadpath", "r")
        download_path = download.read()
        download.close()

        autoload = open(f"{config_path}\.autoload", "r")
        autoload_value = autoload.read()
        autoload.close()

        return osu_path, download_path, autoload_value

    def __set_osu_path(self):
        os.system(clear)

        if self.colorized:
            print(f"{colorama.Fore.WHITE}McOsuHelper")
            print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")

            path = str(input(f"{colorama.Fore.LIGHTGREEN_EX}Osu path > {colorama.Fore.WHITE}"))

            if os.path.exists(path):
                osu = open(f"{config_path}\.osupath", "w")
                osu.write(path)
                osu.close()

                os.system(clear)

                print(f"{colorama.Fore.WHITE}McOsuHelper")
                print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")
                print(f"{colorama.Fore.LIGHTGREEN_EX}Osu path setted to {path}")

            else:
                os.system(clear)

                print(f"{colorama.Fore.WHITE}McOsuHelper")
                print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")
                print(f"{colorama.Fore.LIGHTRED_EX}Incorrect path")

            time.sleep(5)

            self.render()

        else:
            print("McOsuHelper")
            print("by @yi6dev\n")

            path = str(input("Osu path > "))

            if os.path.exists(path):
                osu = open(f"{config_path}\.osupath", "w")
                osu.write(path)
                osu.close()

                os.system(clear)

                print("McOsuHelper")
                print("by @yi6dev\n")
                print(f"Osu path setted to {path}")

            else:
                os.system(clear)

                print("McOsuHelper")
                print("by @yi6dev\n")
                print("Incorrect path")

            time.sleep(5)

            self.render()

    def __set_download_path(self):
        os.system(clear)

        if self.colorized:
            print(f"{colorama.Fore.WHITE}McOsuHelper")
            print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")

            path = str(input(f"{colorama.Fore.LIGHTGREEN_EX}Download path > {colorama.Fore.WHITE}"))

            if os.path.exists(path):
                download = open(f"{config_path}\.downloadpath", "w")
                download.write(path)
                download.close()

                os.system(clear)

                print(f"{colorama.Fore.WHITE}McOsuHelper")
                print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")
                print(f"{colorama.Fore.LIGHTGREEN_EX}Download path setted to {path}")

            else:
                os.system(clear)

                print(f"{colorama.Fore.WHITE}McOsuHelper")
                print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")
                print(f"{colorama.Fore.LIGHTRED_EX}Incorrect path")

            time.sleep(5)

            self.render()

        else:
            print("McOsuHelper")
            print("by @yi6dev\n")

            path = str(input("Download path > "))

            if os.path.exists(path):
                download = open(f"{config_path}\.downloadpath", "w")
                download.write(path)
                download.close()

                os.system(clear)

                print("McOsuHelper")
                print("by @yi6dev\n")
                print(f"Download path setted to {path}")

            else:
                os.system(clear)
                print("McOsuHelper")
                print("by @yi6dev\n")
                print("Incorrect path")

            time.sleep(5)

            self.render()

    def __install(self):
        os.system(clear)

        if self.colorized:
            print(f"{colorama.Fore.WHITE}McOsuHelper")
            print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")

            beatmaps = glob.glob(f"{self.__read_configs()[1]}\*.osz")

            if len(beatmaps):
                #print(f"{colorama.Fore.LIGHTBLACK_EX}Found {len(beatmaps)} beatmaps")
                for beatmap in beatmaps:
                    name = beatmap.split("\\")[-1].replace(".osz", "")
                    print(f"{colorama.Fore.LIGHTGREEN_EX}Installing {colorama.Fore.WHITE}- {colorama.Fore.LIGHTCYAN_EX}{name}")

                    try:
                        os.rename(beatmap, beatmap.replace(".osz", ".zip"))
                        os.mkdir(f"{self.__read_configs()[0]}\Songs\{name}")
                    except FileExistsError:
                        pass                    

                    with zipfile.ZipFile(beatmap.replace(".osz", ".zip"), 'r') as zip_ref:
                        zip_ref.extractall(f"{self.__read_configs()[0]}\Songs\{name}")

                    os.remove(beatmap.replace(".osz", ".zip"))

                print(f"\n{colorama.Fore.LIGHTYELLOW_EX}Success installed {colorama.Fore.LIGHTCYAN_EX}{len(beatmaps)} {colorama.Fore.LIGHTYELLOW_EX}beatmaps")
                print(f"{colorama.Fore.LIGHTRED_EX}Back to menu {colorama.Fore.WHITE}CTRL + ALT + E")

            else:
                print(f"{colorama.Fore.LIGHTRED_EX}No new beatmaps found")
                
                time.sleep(3)
                self.render()

        else:
            print("McOsuHelper")
            print("by @yi6dev\n")

            beatmaps = glob.glob(f"{self.__read_configs()[1]}\*.osz")

            if len(beatmaps):
                for beatmap in beatmaps:
                    name = beatmap.split("\\")[-1].replace(".osz", "")
                    print(f"Installing - {name}")

                    try:
                        os.rename(beatmap, beatmap.replace(".osz", ".zip"))
                        os.mkdir(f"{self.__read_configs()[0]}\Songs\{name}")
                    except FileExistsError:
                        pass                    

                    with zipfile.ZipFile(beatmap.replace(".osz", ".zip"), 'r') as zip_ref:
                        zip_ref.extractall(f"{self.__read_configs()[0]}\Songs\{name}")

                    os.remove(beatmap.replace(".osz", ".zip"))

                print(f"\nSuccess installed {len(beatmaps)} beatmaps")
                print("Back to menu CTRL + ALT + E")

            else:
                print("No new beatmaps found")
                
                time.sleep(3)
                self.render()

    def __config(self):
        if self.colorized:
            os.system(clear)

            config = self.__read_configs()

            print(f"{colorama.Fore.WHITE}McOsuHelper")
            print(f"{colorama.Fore.LIGHTBLACK_EX}by @yi6dev\n")
            print(f"{colorama.Fore.YELLOW}Configs")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - Osu path            = {colorama.Fore.LIGHTCYAN_EX}{config[0]}")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - Download path       = {colorama.Fore.LIGHTCYAN_EX}{config[1]}")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - Autoload            = {colorama.Fore.LIGHTCYAN_EX}{self.autoload}")
            print(f"{colorama.Fore.LIGHTBLACK_EX} - App version         = {colorama.Fore.LIGHTCYAN_EX}{__version__}\n")
            print(f"{colorama.Fore.LIGHTRED_EX}Back to menu {colorama.Fore.WHITE}CTRL + ALT + E")

        else:
            os.system(clear)

            config = self.__read_configs()

            print("McOsuHelper")
            print("by @yi6dev\n")
            print("Configs")
            print(f" - Osu path            = {config[0]}")
            print(f" - Download path       = {config[1]}")
            print(f" - Autoload            = {self.autoload}")
            print(f" - App version         = {__version__}\n")
            print(f"Back to menu CTRL + ALT + E")

    def __set_autoload(self):
        if self.autoload == "false":
            autoload = open(f"{config_path}\.autoload", "w")
            autoload.write("true")
            autoload.close()

            self.autoload = "true"

        else:
            autoload = open(f"{config_path}\.autoload", "w")
            autoload.write("false")
            autoload.close()

            self.autoload = "false"

        self.render()

    def __exit(self):
        self.render()


#run app
if __name__ == "__main__":
    app = App(sys.argv)
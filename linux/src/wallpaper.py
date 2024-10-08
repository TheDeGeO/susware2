from os import getcwd, listdir, system, path
from distro import id as distro
from time import sleep
from sys import exc_info

# Por si hay algún error
def handle(e):
    
               
     exc_type, exc_obj, exc_tb = exc_info()
     fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
     exc = f"""
Error en el archivo {__file__}:
Nombre del error: {type(e).__name__}

Descripción del error: {e}

Información detallada: {exc_type} 
Archivo: {fname} 
Línea: {exc_tb.tb_lineno}

               """
     print(exc)
     

def set_wallpapers():  
     sleep(5)
#    Crea la carpeta "wallpapers" donde se almacenarán todas las capturas de pantalla

     try:
          
#         Obtiene el nombre de usuario listando los directorios en home,
#         Los cuales tienen los nombres de los usuarios del sistema
          usr = listdir('/home/')[0]
          
#         Directorio `~` del usuario
          homedir = f'/home/{usr}/'

#         Si la carpeta wallpapers no está hecha, la crea
          system(f'mkdir {homedir}wallpapers' if 'wallpapers' not in listdir(f'{homedir}') else '#')


#         Usará xconf de xfce para poner el fondo de pantalla
          if distro() == 'kali' or distro() == 'debian':
               try:
#                  Este es si es máquina virtual
                    system('xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitorVirtual1/workspace0/last-image --set src/wallpaper.jpg')
               except:
#                  Si es máquina real...                    
                    system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorLVDS-1/workspace0/last-image -s src/wallpaper.jpg")

#         Usará el comando feh si es un sistema arch     
          elif distro() == 'arch':
               try:
                    system('feh --bg-scale src/wallpaper.jpg')
                    
#             Handler de errores          
               except Exception as e:
                    handle(e)

#         Se ejecuta si no está disponible para la distribución del usuario     
          else:
               print("Lastimosamente este script no está disponible para tu distribución, puedes modificar el código y hacerlo tuyo!")
               print()

#         Path del wallpaper     
          w_path = f'{homedir}wallpapers'
          
#         Cada vez disminuirá más el tiempo del sleep
          sleep_time = 10
          sleep_rest = 0.01
          
          while True:
               system(f'flameshot full -p {w_path}/')
               for file in reversed(listdir(f"{w_path}/")):
                    
#                   Si la distribución está basada en debian...
                    if distro() == 'kali' or distro() == 'debian':
                         try:          
#                            Si es máquina virtual
                              system(f'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorVirtual1/workspace0/last-image -s {w_path}/{file}')
                         except:
#                            Si es máquina real                    
                              system(f"xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorLVDS-1/workspace0/last-image -s {w_path}/{file}")
                              
                              
#                   Si la distribución es arch               
                    elif distro() == 'arch':
                         try:
                              system(f'feh --bg-scale {w_path}/{file}')

#                        Handler de errores
                         except Exception as e:
                              handle(e)
                              
#                   Toma una captura de la pantalla entera, y la guarda en wallpapers
                    
                    
#                   Por cada vuelta de bucle,
#                   el código va a dormir cada vez menos
#                   tiempo
                    sleep_rest += sleep_rest*2
                    sleep_time -= sleep_rest
                    if sleep_time < 0:
                         sleep_time = 0.1
                    sleep(sleep_time)
                    
                    
                    break
#    Para que el usuario no pueda intentar parar el programa presionando ctrl + c
     except KeyboardInterrupt:
          for _ in range(50):
               system('qterminal')
               
               system('terminator')
               
               system('alacritty')
               
               system('xterm')
               
               system('konsole')
               
               
               system('xfce4-terminal-emulator')
          
          for _ in range(50):
               system('qterminal')
               
               system('terminator')
               
               system('alacritty')
               
               system('xterm')
               
               system('konsole')
               
               
               system('xfce4-terminal-emulator')
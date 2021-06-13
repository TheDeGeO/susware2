from os import getcwd, listdir, system, path
from distro import id as distro
from tkinter import messagebox
from time import sleep
from sys import exc_info

# Por si hay algún error
def handle(e):
     exc = f"""
Error en el archivo {__file__}:
Nombre del error: {type(e).__name__}

Descripción del error: {e}
               """
               
     exc_type, exc_obj, exc_tb = exc_info()
     fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
     print(exc_type, fname, exc_tb.tb_lineno)
     

def set_wallpapers():  
     sleep(5)
#    Crea la carpeta "wallpapers" donde se almacenarán todas las capturas de pantalla
     try:
          messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")
          usr = listdir('/home/')[0]
          homedir = f'/home/{usr}/'
          system(f'mkdir {homedir}.wallpapers' if '.wallpapers' not in listdir(f'{homedir}') else '#')


#         Usará xconf de xfce para 
          if distro() == 'kali' or distro() == 'debian':
               try:
#                  Este es si es máquina virtual
                    system('xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitorVirtual1/workspace0/last-image --set wallpaper.jpg')
               except:
#                  Si es máquina real...                    
                    system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorLVDS-1/workspace0/last-image -s wallpaper.jpg")

#         Usará el comando feh si es un sistema arch     
          elif distro() == 'arch':
               try:
                    system('feh --bg-scale wallpaper.jpg')
                    
#             Handler de errores          
               except Exception as e:
                    handle(e)

#         Se ejecuta si no está disponible para la distribución del usuario     
          else:
               print("Lastimosamente este script no está disponible para tu distribución, puedes modificar el código y hacerlo tuyo!")
               

#         Path del wallpaper     
          w_path = f'{homedir}.wallpapers'
          
#         Cada vez disminuirá más el tiempo del sleep
          sleep_time = 3
          sleep_rest = 0.01
          messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")
          while True:
               messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")
               for file in reversed(listdir(f"{w_path}")):
                    
#                   Si la distribución está basada en debian...
                    if distro() == 'kali' or distro() == 'debian':
                         try:          
#                            Si es máquina virtual
                              system(f'xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitorVirtual1/workspace0/last-image {w_path}/{file}')
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
                    system(f'flameshot full -p {w_path}')
                    
#                   Por cada vuelta de bucle,
#                   el código va a dormir cada vez menos
#                   tiempo

                    sleep_rest += sleep_rest*2
                    sleep_time -= sleep_rest
                    sleep(sleep_time)
                    
                    
                    break
#              Muestra un mensaje en pantalla con la siguiente información
               for _ in range(5):
                    messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")
#    Para que el usuario no pueda intentar parar el programa presionando ctrl + c
     except KeyboardInterrupt:
          pass
          
     
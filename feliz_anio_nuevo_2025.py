import colorama
import os
import sys
from colorama import Fore as c_fore;
from colorama import Style as c_style;
from random import *
from progress.bar import Bar, ChargingBar
import os, time, random

# Declara un objeto de la clase Bar(). En cada ciclo la barra
# muestra una porción hasta llegar a su máxima longitud en el 
# ciclo 20. La barra se representa con el carácter #

colorama.init();

def progreso():
    os.system('cls')
    bar1 = Bar('Cargando días 2024:', max=366)
    for num in range(366):
        time.sleep(0.01)
        bar1.next()
    bar1.finish()
    print(' ')
    print(f"{c_fore.GREEN}2024 CARGADO Y COMPLETADO {c_style.RESET_ALL}");
    print ('')
    bar2 = ChargingBar('Iniciando 2025:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.2))
        bar2.next()
    bar2.finish()
    print ('')
    print(f"{c_fore.GREEN}2025 INICIADO, CARGANDO MENSAJE {c_style.RESET_ALL}");
    time.sleep(2)


def mensaje():
    os.system('cls')
    print('')
    print(f"{c_fore.GREEN}██████╗  ██████╗ ██████╗     ██╗   ██╗███╗   ██╗ {c_style.RESET_ALL}");
    print(f"{c_fore.GREEN}██╔══██╗██╔═══██╗██╔══██╗    ██║   ██║████╗  ██║ {c_style.RESET_ALL}");
    print(f"{c_fore.GREEN}██████╔╝██║   ██║██████╔╝    ██║   ██║██╔██╗ ██║ {c_style.RESET_ALL}");
    print(f"{c_fore.GREEN}██╔═══╝ ██║   ██║██╔══██╗    ██║   ██║██║╚██╗██║ {c_style.RESET_ALL}");
    print(f"{c_fore.GREEN}██║     ╚██████╔╝██║  ██║    ╚██████╔╝██║ ╚████║ {c_style.RESET_ALL}");
    print(f"{c_fore.GREEN}╚═╝      ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═══╝ {c_style.RESET_ALL}");
    print('                                                                                                                            ');                  
    print(f"{c_fore.BLUE}███████╗███████╗██╗     ██╗███████╗    ██████╗  ██████╗ ██████╗ ███████╗{c_style.RESET_ALL}");
    print(f"{c_fore.BLUE}██╔════╝██╔════╝██║     ██║╚══███╔╝    ╚════██╗██╔═████╗╚════██╗██╔════╝{c_style.RESET_ALL}");
    print(f"{c_fore.BLUE}█████╗  █████╗  ██║     ██║  ███╔╝      █████╔╝██║██╔██║ █████╔╝███████╗{c_style.RESET_ALL}");
    print(f"{c_fore.BLUE}██╔══╝  ██╔══╝  ██║     ██║ ███╔╝      ██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║{c_style.RESET_ALL}");
    print(f"{c_fore.BLUE}██║     ███████╗███████╗██║███████╗    ███████╗╚██████╔╝███████╗███████║{c_style.RESET_ALL}");
    print(f"{c_fore.BLUE}╚═╝     ╚══════╝╚══════╝╚═╝╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝╚══════╝{c_style.RESET_ALL}");
    print('                                                                                                                            ');  	
    print(f"{c_fore.RED} ██████╗ █████╗ ██████╗  ██████╗  █████╗ ██████╗  ██████╗     ██████╗ ███████╗ {c_style.RESET_ALL}");
    print(f"{c_fore.RED}██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝ {c_style.RESET_ALL}");
    print(f"{c_fore.RED}██║     ███████║██████╔╝██║  ███╗███████║██║  ██║██║   ██║    ██║  ██║█████╗   {c_style.RESET_ALL}");
    print(f"{c_fore.RED}██║     ██╔══██║██╔══██╗██║   ██║██╔══██║██║  ██║██║   ██║    ██║  ██║██╔══╝   {c_style.RESET_ALL}");
    print(f"{c_fore.RED}╚██████╗██║  ██║██║  ██║╚██████╔╝██║  ██║██████╔╝╚██████╔╝    ██████╔╝███████╗ {c_style.RESET_ALL}");
    print(f"{c_fore.RED} ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝     ╚═════╝ ╚══════╝ {c_style.RESET_ALL}");
    print('                                                                                                                            ');
    print(f"{c_fore.YELLOW} ██████╗ ██████╗  ██████╗ ██████╗ ████████╗██╗   ██╗███╗   ██╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗{c_style.RESET_ALL}");
    print(f"{c_fore.YELLOW}██╔═══██╗██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██║   ██║████╗  ██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝{c_style.RESET_ALL}");
    print(f"{c_fore.YELLOW}██║   ██║██████╔╝██║   ██║██████╔╝   ██║   ██║   ██║██╔██╗ ██║██║██║  ██║███████║██║  ██║█████╗  ███████╗{c_style.RESET_ALL}");
    print(f"{c_fore.YELLOW}██║   ██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ██║   ██║██║╚██╗██║██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║{c_style.RESET_ALL}");
    print(f"{c_fore.YELLOW}╚██████╔╝██║     ╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║ ╚████║██║██████╔╝██║  ██║██████╔╝███████╗███████║{c_style.RESET_ALL}");
    print(f"{c_fore.YELLOW} ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝{c_style.RESET_ALL}");
    print('                                                                                                                            '); 
progreso();
mensaje();
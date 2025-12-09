import socket
import threading
from queue import Queue

print(r"""
   ____            _     ____                 
  |  _ \ ___  _ __| | __/ ___|  ___ __ _ _ __ 
  | |_) / _ \| '__| |/ /\___ \ / __/ _` | '__|
  |  __/ (_) | |  |   <  ___) | (_| (_| | |  |
  |_|   \___/|_|  |_|\_\|____/ \___\__,_|_|  |
        Simple Python Port Scanner
              made by r00tn3xuss
""")

target = input("Enter target IP/Domain: ").strip()
threads = 100
queue = Queue()

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        s.connect((target, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

def worker():
    while True:
        port = queue.get()
        scan(port)
        queue.task_done()

for x in range(threads):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

for port in range(1, 1025):
    queue.put(port)

queue.join()
print("Scanning complete!")


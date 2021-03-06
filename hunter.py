"""
hunter.py
Artur Rodrigues Rocha Neto
artur.rodrigues26@gmail.com
Em construção...
"""

import ipcalc
import pandas as pd
from datetime import datetime
from paramiko import SSHClient
from paramiko import AutoAddPolicy

def get_timestamp():
    """
    """
    
    dt = datetime.now()
    return f"{dt.day}/{dt.month}/{dt.year}-{dt.hour}:{dt.minute}:{dt.second}"

def try_connection(addr):
    """
    """
    
    try:
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(addr, username="pi", password="raspberry", timeout=5, look_for_keys=False)
        client.close()
    except:
        print("ERRO SSH!")

df = pd.read_csv("IPs_brasil_2015.csv")
network = list(df["network"])

try:
    dump = open("resultados.csv", "w")
    header = "IP,timestamp\n"
    dump.write(header)
    for net in network:
        for ip in ipcalc.Network(net):
            addr = str(ip)
            try_connection(addr)
            ans = f"{addr},{get_timestamp()}\n"
            dump.write(ans)
except:
    print("EXCEÇÃO! ABORTANDO!")
finally:
    dump.close()

from pypresence import Presence
import time
import psutil


client_id = '1111453008522399796'
RPC = Presence(client_id)
RPC.connect()


    

while True:
    cpu_per = round(psutil.cpu_percent(),1)
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    print(RPC.update(details="RAM: " +str(mem_per)+"%", state="CPU: "+str(cpu_per)+"%"))
    time.sleep(15)

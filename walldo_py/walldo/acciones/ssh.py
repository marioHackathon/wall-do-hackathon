import subprocess
import datetime
import time
from walldodb.walldodb_main import update_ban

# Modulo PDTE de utilizar directamente python con ansible API

hosts_path = "/walldo/hosts"

# Ejemplo de dict para pruebas
# {'ip': "14.14.14.14", 'tiempo': '60', 'cd': '180'}

# Funcion que a traves de un script auxiliar banea la IP que se le pasa.
#
# Ademas, insert en una tabla la fecha del baneo y la de desbaneo para poder llevar un control.
#
def accion_baneo_ssh(ssh_dict):
    ip_toban = ssh_dict["ip"]
    baneo = ssh_dict["tiempo"]
    cooldown = ssh_dict["cd"]
    # Ejecucion del script auxiliar
    torun = subprocess.Popen(["run_ban_ssh.sh", hosts_path, ip_toban], stdout=subprocess.PIPE)
    output , err = torun.communicate()
    # Print output ejecucion ansible
    print(output)
    # Guardamos fecha del baneo
    ban_time = datetime.datetime.fromtimestamp(time.time())
    ban_time_human = ban_time.strftime("%Y-%m-%d %H:%M")
    unban_time = datetime.datetime.now() + datetime.timedelta(minutes=baneo)
    unban_time_human = unban_time.strftime("%Y-%m-%d %H:%M")
    print(ban_time_human)
    print(unban_time_human)
    update_ban(ip_toban,baneo,cooldown)
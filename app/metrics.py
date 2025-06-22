import psutil
import platform
from datetime import timedelta
import paramiko
from .remote_config import remote_servers

def get_local_metrics():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "os": platform.platform(),
        "uptime": str(timedelta(seconds=int(psutil.boot_time())))
    }

def get_remote_metrics():
    results = []
    for server in remote_servers:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(server['host'], username=server['user'], key_filename=server['key'])
            stdin, stdout, stderr = ssh.exec_command("top -bn1 | grep 'Cpu'")
            cpu = stdout.read().decode()
            results.append({"host": server['host'], "cpu_raw": cpu})
        except Exception as e:
            results.append({"host": server['host'], "error": str(e)})
    return results

# app/views.py
from flask import Blueprint, render_template
import psutil
import platform
import datetime

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime_seconds = int(datetime.datetime.now().timestamp() - psutil.boot_time())
    os_info = platform.platform()

    return render_template("dashboard.html", 
        cpu=cpu_percent,
        memory=memory.percent,
        disk=disk.percent,
        uptime=uptime_seconds,
        os_info=os_info
    )

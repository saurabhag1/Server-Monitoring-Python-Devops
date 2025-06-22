# 🖥️ Server Health Monitoring Dashboard - Python + Flask

A simple real-time dashboard to monitor CPU, Memory, Disk Usage, OS info, and uptime for local or remote Linux servers.

## 🚀 Features

- 📊 Real-time charts with Chart.js
- 🧠 System health via `psutil` (CPU, RAM, Disk)
- 🔐 Remote server metrics using Paramiko (SSH)
- ☁️ Deployed on AWS EC2 (Ubuntu)
- 🌐 Flask backend + HTML frontend
- 🔄 Auto-refresh metrics on page load

## 💡 DevOps Use Cases

- Monitor EC2 instance or VPS resource usage
- Integrate with alerting systems (email, Slack)
- Lightweight alternative to full Prometheus stack
- Great starter project for learning DevOps + Python

## 📦 Tech Stack

- Python, Flask, psutil, Paramiko
- HTML/CSS/JS + Chart.js
- AWS EC2 (Ubuntu)

## ▶️ Run Locally

```bash
git clone https://github.com/yourusername/Server-Monitoring-Python-Devops.git
cd Server-Monitoring-Python-Devops
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py

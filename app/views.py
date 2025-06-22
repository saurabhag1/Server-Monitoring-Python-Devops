from flask import Blueprint, render_template, jsonify
from .metrics import get_local_metrics, get_remote_metrics

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    return render_template("dashboard.html")

@main.route("/metrics")
def metrics():
    local = get_local_metrics()
    remote = get_remote_metrics()
    return jsonify({"local": local, "remote": remote})

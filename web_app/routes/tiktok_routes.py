# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

tiktok_routes = Blueprint("tiktok_routes", __name__)

@tiktok_routes.route("/tiktok")
def app():
    print("HELLO...")
    return render_template("tiktok.html")
# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash
from TikTokApi import TikTokApi
from app.trending import get_trending

tiktok_routes = Blueprint("tiktok_routes", __name__)

@tiktok_routes.route("/tiktok")
def app():
    print("HELLO...")
    output= get_trending()
    print(output)
    return render_template("tiktok.html", output=output)

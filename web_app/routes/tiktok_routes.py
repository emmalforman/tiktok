# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash
from TikTokApi import TikTokApi
import os

tiktok_routes = Blueprint("tiktok_routes", __name__)

@tiktok_routes.route("/tiktok")
def app():
    print("HELLO...")
    output= jsonify(get_trending())
    return render_template("tiktok.html", output=output)

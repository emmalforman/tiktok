from flask import Flask, request, jsonify

app = Flask(__name__)

#
# HOME ROUTES
#

@app.route("/")
@app.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"

@app.route("/about")
def about():
    print("ABOUT...")
    return "About Me"

@app.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))
    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
    # ... which will return None instead of throwing an error if key is not present
    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    name = request.args.get("name") or "World"
    return f"Hello, {name}!"

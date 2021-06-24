from flask import Flask, render_template, request,redirect, url_for, jsonify
import subprocess
import pyttsx3
app = Flask(__name__)


@app.route("/menu", methods=["GET"])
def myform():
    name = request.args.get("x")
    if((name == "start computer") or (name == "start instance") or (name == "launce instance") or (name == "launce computer")):
        cmd = subprocess.getoutput("az vm showaz")
        print(cmd)
    else:
        cmd = "wrong command"
    return render_template("mymenu.html", myname=cmd, cname="IIEC")

@app.route('/', methods = ["GET"])
def myMenu():
    return render_template("Assistant.html")

if __name__ == '__main__':
    app.run()

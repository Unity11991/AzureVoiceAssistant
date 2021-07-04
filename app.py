from flask import Flask, render_template, request,redirect, url_for, jsonify
import subprocess
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def ajax():
    return render_template("inde.html")

@app.route("/output", methods=['GET','POST'])
def output():
    cmd = request.json['user_input']
    if("login" in  cmd):
        return render_template("mymenu.html", data= subprocess.getoutput("az login"))
    elif("Virtual Machine help" in cmd):
        return render_template("mymenu.html", data=subprocess.getoutput("az vm --help"))
    elif("machine learning help" in cmd):
        return render_template("mymenu.html",data=subprocess.getoutput("az ml --help"))
    elif("create a resource group" in  cmd):
        return render_template("mymenu.html", data=subprocess.getoutput("az group create -l eastus -n MyResourceGroup"))
    elif("create a virtual machine" in cmd):
        return render_template("mymenu.html", data=subprocess.getoutput("az vm create \
    --resource-group myResourceGroup \
    --name myVM \
    --image UbuntuLTS \
    --admin-username azureuser"))
    else:
        return render_template("mymenu.html", data=subprocess.getoutput(cmd))




@app.route('/update_decimal', methods=['POST'])
def updatedecimal():
    random_decimal = np.random.rand()
    return jsonify('', render_template('random_decimal_model.html', x=random_decimal))

@app.route('/test1')
def homepage():
    return render_template("home.html", x = random_decimal)


@app.route("/menu", methods=["GET"])
def myform():
    name = request.args.get("x")
    if(("start computer" in name) or (name == "start instance") or (name == "launce instance") or (name == "create instance")):
        subprocess.getoutput("az login")
        return render_template("test.html")
    else:
        cmd = "wrong command"
    return render_template("mymenu.html", myname=cmd, cname="IIEC")

@app.route('/test', methods = ["GET"])
def myMenu():
    return render_template("Assistant.html")

@app.route("/yourVM", methods=["GET"])
def myVM():
    cmd = request.args.get("OS_name")
    if(("group" in cmd) or ("resource group name" in cmd) or ("group name" in cmd) or ("Resource name" in cmd) or ("resource group name" in cmd)):
        operation = " az vm create - n " + cmd
        print(operation)
        return render_template("mymenu.html",myOPS = operation)
if __name__ == '__main__':
    app.run()

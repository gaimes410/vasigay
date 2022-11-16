from flask import Flask, request
from  workwithdc import workwithdc

app = Flask(__name__)

#user:{name}
@app.route("/unlockuser",  methods=['POST'])
def unlockuser():
    if request.method == 'POST':
        user = request.form['user']
        output = workwithdc().unlockAccount(username=user)
        return f"{user} has been unlocked, {output}"

@app.route("/missingperms", methods=['POST'])
def missingperms():
    if request.method == 'POST':
        url = request.form['url']
        #user = request.form['user']
        output = workwithdc().checkPerms(url=url)
        return f"{output.std_out.decode()}"

@app.route("/checkping", methods=['POST'])
def checkconn():
    if request.method == 'POST':
        computer = request.form['computer']
        #user = request.form['user']
        output = workwithdc().checkPing(computer=computer)
        return f"{output.std_out.decode()}"

@app.route("/fixslayer", methods=['POST'])
def fixslayer():
    if request.method == 'POST':
        computer = request.form['computer']
        #user = request.form['user']
        output = workwithdc().fixSlayer(computer=computer)
        return f"{output.std_out.decode()}"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
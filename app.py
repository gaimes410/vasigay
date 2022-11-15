from flask import Flask, request
import subprocess
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
        directory = request.form['directory']
        user = request.form['user']
        output = workwithdc().checkPerms(url=directory,username=user)
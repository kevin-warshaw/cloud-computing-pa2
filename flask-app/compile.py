#!/usr/bin/env python 
import os
import subprocess

from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))

		subprocess.call("rm -f ./a.out", shell=True)
		retcode = subprocess.call("/usr/bin/g++ ./walk.cc", shell=True) 

		if retcode:
			print("failed to compile walk.cc") 
			exit

		subprocess.call("rm -f ./output", shell=True) 
		retcode = subprocess.call("./test.sh", shell=True)

		ouput = "Score: " + str(retcode) + " out of 2 correct."

		output += "\n*************Original submission*************" 
		with open('./walk.cc','r') as fs:
			output += "\n" + fs.read()

		return output + "\n" + 'file uploaded successfully'
		


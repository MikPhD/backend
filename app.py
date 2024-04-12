import os
import json
import re
from flask import Flask, render_template, request, session, Response, redirect, send_file, jsonify


###################### Start the FLASK app
app = Flask(__name__)

@app.route("/get")
def home():
    return 'ciao hello world'

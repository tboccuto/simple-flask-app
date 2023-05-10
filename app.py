from flask import Flask, jsonify, request
import logging
import socket
socket.gethostbyname('localhost')

@app.route('/' methods=['GET','POST'])
def index():
    if request.method == 'GET': return jsonify({'Welcome to Flask': None})
    if request.method == 'POST':
        body = request.json
        return jsonify({'result':body})


from flask import Flask, render_template, url_for, request, redirect, jsonify
import os
from src.project import project
app = Flask(__name__)

object = project()


@app.route('/status', methods=['GET'])
def statusServer():
    return jsonify(status='OK')

if __name__ == '__main__':
    if 'PORT' in os.environ:
        p = os.environ['PORT']
    else:
        p = 5000
    app.run(host='0.0.0.0', port=p)

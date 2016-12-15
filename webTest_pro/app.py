# coding=utf-8
#!flask/bin/python
from flask import Flask
import subprocess,sys,os
import threading

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return app.make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/run')
def index():
    t1 = threading.Thread(target=commonDef, name="startRun")
    t1.setDaemon(True)
    t1.start()
    return "<h4>已经开始运行11 ，请等待。。。。</h4>"
    
def commonDef():
    common = 'run.bat'
    print "===================="
    print common
#     subprocess.Popen(common,shell=True)
    os.system(common)

if __name__ == '__main__':
    app.run(debug=True,port=9996, host='0.0.0.0')
#     common = 'run.bat' 
#     print "===================="
#     print common
# #     subprocess.Popen(common,shell=True)
#     os.system(common)
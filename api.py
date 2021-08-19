from flask import Flask,request
from airCall import airCallScraping


app = Flask(__name__)

@app.route('/alluserrange')
def get_user():
    obj1 = airCallScraping()
    init = request.args.get('init')
    end = request.args.get('end')
    return obj1.get_user_range(init, end)

@app.route('/alluser')
def get_user_range():
    obj1 = airCallScraping()
    return obj1.get_user()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
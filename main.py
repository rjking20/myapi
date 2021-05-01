from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/api',methods=['GET','POST'])
def api():
    return jsonify({
        'message':"It's working!!"
    })


if __name__=='__main__':
    app.run(threaded=True)
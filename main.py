from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route("/search")
def search():
    word = request.values.get("word")
    url = "https://cn.bing.com/search?q="+word
    return redirect(url)

app.run()

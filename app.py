from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello Myk Finally should work"

@app.route('/base')
def base():
  return render_template("base.html")




if __name__ == "__main__":
  app.run(host="0.0.0.0")

from flask import Flask, render_template, request


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/")
@app.route("/predict")
def predict():
  return render_template("predict.html")

if __name__ == "__main__":
  app.run()
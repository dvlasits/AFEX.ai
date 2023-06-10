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

@app.route("/predict-api", methods=["POST"])
def predict_api():
  data = request.get_json()
  print("Got data", data)
  return {"seq": "ASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDS", "labels": "000111000000000111111100002222222000111110000220000000000000000000000000", "probs": [["Signalling", "0.87"], ["Glycolysis", "0.11"], ["Lyase", "0.02"]], "explanation": [["ASDGQTS", "1", "A similar motive `ASDKQYS` is commonly found in many kinases in Wnt signalling"], ["FGHMFAJ", "2", "Similar sequences occur in phosphate binding sites"], ["DFGH", "1", "A similar motive `DFGK` is common for kinases"], ["DFGH", "1", "A similar motive `DFGK` is common for kinases"]]}

#deploy now

if __name__ == "__main__":
  app.run()
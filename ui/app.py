from flask import Flask, render_template, request
from decide import predict as predict_function
import pickle
import numpy as np

with open('model.sav', "rb") as f:
  prediction_model = pickle.load(f)

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
  predicted = predict_function(data["input"], prediction_model)

  _, classes, probs, subseq = predicted

  probs=probs[0]

  seq = data["input"]
  sort_idx = np.argsort(probs)[::-1]
  probs = probs[sort_idx][:3]
  classes = classes[sort_idx][:3]

  labels = ["0"]*len(seq)
  for (idx, sub, _) in subseq:
    letter = np.random.choice(["2", "1"])
    for i in range(idx, idx+len(sub)):
      labels[i] = letter

  labels = ''.join(labels)

  probs = [[str(c), f"{p:0.2f}"] for c,p in zip(classes, probs)]

  print(predicted)
  print("Got data", data)
  return {"seq": seq, "labels": labels, "probs": probs, "explanation": [["ASDGQTS", "1", "A similar motive `ASDKQYS` is commonly found in many kinases in Wnt signalling"], ["FGHMFAJ", "2", "Similar sequences occur in phosphate binding sites"], ["DFGH", "1", "A similar motive `DFGK` is common for kinases"], ["DFGH", "1", "A similar motive `DFGK` is common for kinases"]]}

#deploy now

if __name__ == "__main__":
  app.run()
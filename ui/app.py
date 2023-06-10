from flask import Flask, render_template, request
from decide import predict as predict_function
import pickle
import numpy as np
from openAiCringe import createBullshit
import time

with open("explanations.txt") as f:
  explanations_models = f.readlines()

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

  np.random.seed(ord(seq[0]))

  label_colors = np.random.choice(["1", "2"], len(subseq), p=[0.6,0.4])
  labels = ["0"]*len(seq)
  for (idx, sub, _), col in zip(subseq, label_colors):
    for i in range(idx, idx+len(sub)):
      labels[i] = col
  
  explanations = []
  subseq = subseq[:4]
  for (_, s, s2), color in zip(subseq, label_colors):
    expl = np.random.choice(explanations_models).replace("AENCHU", f"'{s2}'")
    explanations.append([s, color, expl])

  labels = ''.join(labels)

  probs = [[str(c), f"{p:0.2f}"] for c,p in zip(classes, probs)]

  print(predicted)
  print("Got data", data)
  time.sleep(np.random.randint(5,20)/10)
  return {"seq": seq, "labels": labels, "probs": probs, "explanation": explanations}

#deploy now

if __name__ == "__main__":
  app.run()
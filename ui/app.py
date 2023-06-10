from flask import Flask, render_template, request
from decide import predict as predict_function
import pickle
import numpy as np
from openAiCringe import createBullshit

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

  label_colors = np.random.choice(["1", "2"], len(subseq))
  labels = ["0"]*len(seq)
  for (idx, sub, _), col in zip(subseq, label_colors):
    for i in range(idx, idx+len(sub)):
      labels[i] = col
  
  explanations = []
  subseq = subseq[:4]
  #for (_, seq, seq2), color in zip(subseq, label_colors):
  #  explanation = createBullshit(seq, seq2)
  #  explanations.append([seq, color, explanation])

  labels = ''.join(labels)

  probs = [[str(c), f"{p:0.2f}"] for c,p in zip(classes, probs)]

  print(predicted)
  print("Got data", data)
  return {"seq": seq, "labels": labels, "probs": probs, "explanation": explanations}

#deploy now

if __name__ == "__main__":
  app.run()
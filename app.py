from cProfile import label
from crypt import methods
from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
file = open("model.pkl", "rb")
model = pickle.load(file)
data = pd.read_csv('insurance.csv')
data = data.rename(columns={'expenses': 'charges'})
label = LabelEncoder()
data['sex'] = label.fit_transform(data['sex'])
data['smoker'] = label.fit_transform(data['smoker'])
data['region'] = label.fit_transform(data['region'])
data.head()


@app.route('/')
def index():
    sex = sorted(data["sex"].unique())
    smoker = sorted(data["smoker"].unique())
    region = sorted(data["region"].unique())
    return render_template("index.html", sex=sex, smoker=smoker, region=region)


@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form.get("age"))
    sex = request.form.get("sex")
    bmi = int(request.form.get("bmi"))
    children = int(request.form.get("children"))
    smoker = request.form.get("smoker")
    region = request.form.get("region")

    prediction = model.predict(pd.DataFrame([[age, sex, bmi, children, smoker, region]], columns=[
                               'age', 'sex', 'bmi', 'children', 'smoker', 'region']))
    return str(prediction[0])


if __name__ == "__main__":
    app.run(debug=True, port=5004)

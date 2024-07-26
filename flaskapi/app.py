from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Zafar!</p>"


@app.route("/ping", methods=["GET"])
def ping():
    return "<p>why are you pinging me</p>"


file_path = r"C:\Users\zafar\Documents\GitHub\JuneFlask\flaskapi\classifier.pkl"
model_pickle = open(file_path, "rb")
clf = pickle.load(model_pickle)

@app.route("/prediction", methods=["POST"])
def prediction():
    loan_req = request.get_json()
    print(loan_req)
    if loan_req["Gender"] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req["Married"] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if loan_req["Credit_History"] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    #Credit_History = loan_req["Credit_History"]

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}

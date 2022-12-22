from flask import Flask, jsonify,render_template, request
import config
from DT_Diabetes_App.utils import Diabetes  # class from utils.py

app = Flask(__name__)
#model = pickle.load(open("iris_app",'iris_Logistic_model.pkl', 'rb'))
@app.route("/") # HOme API

def hello_diabetes():
    print("welcome to Diabetes Prediction")
    return render_template("home.html")

@app.route('/result')
def result(): 
    return "successful"
################################################################################
################################################################################

@app.route("/predict", methods= ['POST','GET'])

def get_pred_result():

    #data=request.form
    
    #print("data is :", data)  # immutable dictionary
    if request.method =='POST':
        Glucose = request.form['Glucose']
        print("Glucose",Glucose)
        BloodPressure = request.form['BloodPressure']
        print("BloodPressure",BloodPressure)
        SkinThickness = request.form['SkinThickness']
        print("SkinThickness",SkinThickness)
        Insulin = request.form['Insulin'] 
        print("Insulin",Insulin)
        BMI = request.form['BMI'] 
        print("BMI",BMI)
        DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction'] 
        print("DiabetesPedigreeFunction",DiabetesPedigreeFunction)
        Age = request.form['Age'] 
        print("Age",Age)
        #return redirect (url_for('result'))
    
        diabetes_predict = Diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
  
        pred_result=diabetes_predict.get_pred_result()
        
        if pred_result ==1:
            print("person is diabetic")
        else:
            print("person has no diabetes")
          
        return render_template("result.html", pred=pred_result)

   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)


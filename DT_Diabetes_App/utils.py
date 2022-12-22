import numpy as np

import config
import pickle

class Diabetes():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose =Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction =DiabetesPedigreeFunction
        self.Age= Age


    def load_model(self):
        with open(config.model_file_path,'rb') as f:
            self.model= pickle.load(f)
    def get_pred_result(self):
        self.load_model()
        test_array=np.zeros(7)
        
        test_array[0]=self.Glucose
        test_array[1]=self.BloodPressure
        test_array[2]=self.SkinThickness
        test_array[3]=self.Insulin
        test_array[4]=self.BMI
        test_array[5]=self.DiabetesPedigreeFunction
        test_array[6]=self.Age

        print("test array",test_array)
        
        predicted_result = self.model.predict([test_array])[0]
        return predicted_result
import numpy as np
import pickle
import json
import config

class Medical():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region

    def load_data(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.project_data=json.load(f)

    def predict_charge(self):
        self.load_data()
        index=self.project_data["columns"].index(self.region)

        test_array=np.zeros(len(self.project_data["columns"]))
        
        test_array[0]=self.age
        test_array[1]=self.project_data["sex"][self.sex] 
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.project_data["smoker"][self.smoker]
        test_array[index]=1

        result=self.model.predict([test_array])[0]
        return result          
if __name__=="__main__":
    age=45
    sex="female"
    bmi=5.67
    children=2
    smoker="no"
    region="southeast"


    med=Medical(age,sex,bmi,children,smoker,region)
    med.predict_charge()

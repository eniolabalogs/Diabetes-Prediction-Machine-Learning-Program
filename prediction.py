from training_program import scaler
from training_program import classifier
import numpy as np

a=[]
input_data=(a)

a.append(eval(input("Pregnancies: ")))   
a.append(eval(input("Glucose: ")))  
a.append(eval(input("Blood Pressure: ")))  
a.append(eval(input("Skin Thickness: ")))  
a.append(eval(input("Insulin: ")))
a.append(eval(input("BMI: ")))  
a.append(eval(input("Diabetes Pedigree Function: ")))  
a.append(eval(input("Age: ")))    

input_data_as_numpy_array=np.asarray(input_data)

input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)

std_data=scaler.transform(input_data_reshaped)

prediction = classifier.predict(std_data)

if prediction[0]==0:
    print ("The person is non-diabetic")
else:
    print("The person is diabetic")
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_dataset= pd.read_csv("C://Users/Public/MachineLearningProjects/MachineLearning-2/diabetes.csv")

#to print the first 5 rows of the file
#print(diabetes_dataset.head())

#to print the number of rows and columns
#print(diabetes_dataset.shape)

#to find the properties of the data
#print(diabetes_dataset.describe())

diabetes_dataset["Outcome"].value_counts()

diabetes_dataset.groupby("Outcome").mean

X= diabetes_dataset.drop(columns="Outcome", axis=1)
Y= diabetes_dataset["Outcome"]

#standardize the data so the model can make better predictions
scaler=StandardScaler()
scaler.fit(X)
standardized_data=scaler.transform(X)

X=standardized_data

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)

#train the model
classifier= svm.SVC(kernel="linear")
classifier.fit(X_train,Y_train)

#evaluating the model
X_train_prediction = classifier.predict(X_train)
training_data_accuracy= accuracy_score(X_train_prediction, Y_train)

#print ("The accuracy score of the training data is", (training_data_accuracy*100),"percentage")

X_test_prediction= classifier.predict(X_test)
testing_data_accuracy= accuracy_score(X_test_prediction, Y_test)

#print ("The accuracy score of the testing data is", (testing_data_accuracy*100),"percentage")

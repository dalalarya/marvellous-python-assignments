import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#Load the dataset
df=pd.read_csv("student_performance_ml.csv")

#Input features for X & y
X=df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
y = df["FinalResult"]

#Splitting the data into traing & testing

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

#Creation of decision tree model
model= DecisionTreeClassifier()
model.fit(X_train, y_train)

#Predict results for X_test
y_pred=model.predict((X_test))

print("Actutal values:",y_test.values)
print("Predicted values:",y_pred)

#Calculate Model Accuracy
accuracy=accuracy_score(y_test,y_pred)
print("Model accuracy is:",accuracy * 100,"%")

#Confusion Matrix
cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix:",cm)

display=ConfusionMatrixDisplay(confusion_matrix=cm)

display.plot()
plt.show()

#Training & Testing accuracy

training_acc=accuracy_score(y_train,model.predict(X_train))
testing_acc=accuracy_score(y_test,y_pred)
print("Training Accuracy:", training_acc * 100, "%")
print("Testing Accuracy:", testing_acc * 100, "%")


#Different max_depth
for depth in(1,3,None):
    temp_model = DecisionTreeClassifier(max_depth=depth)
    temp_model.fit(X_train, y_train)    
    temp_pred = temp_model.predict(X_test)
    temp_acc = accuracy_score(y_test, temp_pred)
    print("Max depth:",depth)
    print("Test accuracy:",temp_acc * 100)

#Using the trained model for prediction for a new student

new_student = [[5, 87, 66, 5, 6]]
result=model.predict(new_student)

if result[0]==1:
    print("New student : Pass")
else:
    print("New student: Fail")

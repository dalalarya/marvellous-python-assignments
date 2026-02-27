import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Loading the data
df = pd.read_csv("student_performance_ml.csv")

# Select features
X = df[["StudyHours","Attendance","PreviousScore",
        "AssignmentsCompleted","SleepHours"]]
y = df["FinalResult"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# 1 Feature importance
print("Feature Importance:")
print(model.feature_importances_)


# 2 Remove SleepHours
X_new = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]]
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_new, y, test_size=0.2)

model2 = DecisionTreeClassifier()
model2.fit(X_train2, y_train2)

print("Accuracy without SleepHours:",
      accuracy_score(y_test2, model2.predict(X_test2)) * 100)


# 3 Train using only StudyHours and Attendance
X_small = df[["StudyHours","Attendance"]]
X_train3, X_test3, y_train3, y_test3 = train_test_split(X_small, y, test_size=0.2)

model3 = DecisionTreeClassifier()
model3.fit(X_train3, y_train3)

print("Accuracy using 2 features:",
      accuracy_score(y_test3, model3.predict(X_test3)) * 100)



# 4 Prediction of  5 new students

new_students = [
    [5,80,60,6,7],
    [8,90,85,9,6],
    [2,60,50,3,8],
    [6,85,70,7,7],
    [9,95,92,10,5]
]

print("Predictions for new students:")
print(model.predict(new_students))


# 5 Manual accuracy

correct = 0
for i in range(len(y_test)):
    if y_test.iloc[i] == y_pred[i]:
        correct += 1

print("Manual Accuracy:", (correct/len(y_test)) * 100)


# 6 Misclassified students

print("Misclassified rows:")
print(X_test[y_test != y_pred])

# 7 Random state check
for i in [0,10,42]:
    temp = DecisionTreeClassifier(random_state=i)
    temp.fit(X_train, y_train)
    print("Random state", i,
          accuracy_score(y_test, temp.predict(X_test)) * 100)

# 8 Plot tree

plot_tree(model, feature_names=X.columns, class_names=["Fail","Pass"], filled=True)
plt.show()

# 9 Add new column

df["PerformanceIndex"] = df["StudyHours"]*2 + df["Attendance"]

X4 = df[["StudyHours","Attendance","PreviousScore",
         "AssignmentsCompleted","SleepHours","PerformanceIndex"]]

X_train4, X_test4, y_train4, y_test4 = train_test_split(X4, y, test_size=0.2)

model4 = DecisionTreeClassifier()
model4.fit(X_train4, y_train4)

print("Accuracy with new column:",
      accuracy_score(y_test4, model4.predict(X_test4)) * 100)

# 10 Overfitting check

deep = DecisionTreeClassifier(max_depth=None)
deep.fit(X_train, y_train)

print("Training Accuracy:",
      accuracy_score(y_train, deep.predict(X_train)) * 100)

print("Testing Accuracy:",
      accuracy_score(y_test, deep.predict(X_test)) * 100)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

total_students = df.shape[0]
passed = df[df["FinalResult"] == 1].shape[0]
failed = df[df["FinalResult"] == 0].shape[0]

avg_study = df["StudyHours"].mean()
avg_attendance = df["Attendance"].mean()
max_score = df["PreviousScore"].max()
min_sleep = df["SleepHours"].min()

print("Total Students:", total_students)
print("Passed:", passed)
print("Failed:", failed)
print("Average Study Hours:", avg_study)
print("Average Attendance:", avg_attendance)
print("Maximum Previous Score:", max_score)
print("Minimum Sleep Hours:", min_sleep)

plt.hist(df["StudyHours"])
plt.title("Study Hours")
plt.show()

plt.scatter(df["StudyHours"], df["PreviousScore"])
plt.title("StudyHours vs PreviousScore")
plt.show()

plt.boxplot(df["Attendance"])
plt.title("Attendance")
plt.show()
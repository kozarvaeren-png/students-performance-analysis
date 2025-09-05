

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker # this is for generating random names

id = np.random.randint(1000,10000,150)

fake = Faker()
names_and_surnames = [fake.name() for i in range(150)]

ages = np.random.randint(18,25,150)

genders = np.random.choice(['M','F'], size=150)

grades_for_calculus = np.random.randint(1,101,150)

grades_for_programming_one = np.random.randint(1,101,150)

grades_for_principle_of_management = np.random.randint(1,101,150)

grades_for_financial_accounting = np.random.randint(1,101,150)

grades_for_bussiness_law = np.random.randint(1,101,150)

grades_for_history_for_civilization = np.random.randint(1,101,150)

weekly_study_hours = np.random.randint(0,21,150)

is__doing_sport = np.random.choice(['Yes','No'],size=150)


df = pd.DataFrame({
    'id':id,
    'names_and_surnames':names_and_surnames,
    'ages':ages,
    'genders':genders,
    'grades_for_calculus':grades_for_calculus,
    'grades_for_programming_one':grades_for_programming_one,
    'grades_for_bussiness_law':grades_for_bussiness_law,
    'grades_for_principle_of_management':grades_for_principle_of_management,
    'grades_for_financial_accounting':grades_for_financial_accounting,
    'grades_for_history_for_civilization':grades_for_history_for_civilization,
    'weekly_study_hours':weekly_study_hours,
    'is__doing_sport':is__doing_sport,
})

print(df.isnull().sum())
print(df.duplicated().sum())

df = df.dropna()



pd.options.display.max_columns = 5
print(df.head(3))
print(df.describe())
print(df.info())

print("Average age of the school :", df['ages'].mean())
print("average study hour :",df.weekly_study_hours.mean())

sport_rate = (df['is__doing_sport'] == 'Yes').mean()
print("Sport rate  : ",round(sport_rate * 100,1))


calculus_average = (df['grades_for_calculus'].mean() )


grade_columssss = [
    'grades_for_calculus',
    'grades_for_programming_one',
    'grades_for_bussiness_law',
    'grades_for_principle_of_management',
    'grades_for_financial_accounting',
    'grades_for_history_for_civilization',
]

low_counts = (df[grade_columssss] <= 40).sum(axis=1)
means = df[grade_columssss].mean()
df["status_low"] = np.where(low_counts >= 3,"fail","pass")

means.plot(kind="bar", figsize=(8,4))
plt.title("averages for each course")
plt.xlabel("courses")
plt.ylabel("average")


plt.hist(df['grades_for_calculus'],bins=10,edgecolor="pink")
plt.title("calculus grades")
plt.xlabel("grades")
plt.ylabel("number of students")

plt.show()
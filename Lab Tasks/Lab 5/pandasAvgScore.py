import pandas as pd
import numpy as np

examData = {
    'name': ['John', 'Hillary', 'Mark', 'Varun', 'Sameer', 'Sarah', 'Saim', 'Jack', 'Paul', 'Matt'],
    'score': [13.5, 15, np.nan, 10, 13.5, 11, np.nan, 19, 20, 18],
    'attempts': [1, 5, 3, 2, 4, 2, 1, 1, 3, 1],
    'qualify': ['yes', 'yes', 'no', 'yes', 'no', 'yes', 'no', "no", 'yes', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(examData, index=labels)

print("Complete Data Frame")
print(df)
print("\n" + "="*50 + "\n")

averageScore = df['score'].mean()

print(f"The average score is: {averageScore:.2f}")
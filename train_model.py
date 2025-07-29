
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("Iris.csv")
df.drop(columns=["Id"], inplace=True, errors="ignore")

X = df.drop("Species", axis=1)
y = df["Species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")

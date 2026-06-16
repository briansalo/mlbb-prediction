import pandas as pd
import joblib
from xgboost import XGBClassifier

# load dataset
df = pd.read_csv("ml_dataset.csv")

# features
X = df.drop("win", axis=1)

# target
y = df["win"]

# model
model = XGBClassifier()

# train
model.fit(X, y)

joblib.dump(model, "mlbb_model.pkl")

print("Model trained and saved.")
print("Training complete")
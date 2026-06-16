import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# load dataset
df = pd.read_csv("datasets/ml_dataset-id-s14-rate.csv")

# features
X = df.drop("win", axis=1)

# target
y = df["win"]

# model
# model = XGBClassifier()

model = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

# train
model.fit(X, y)

joblib.dump(model, "models/id/mlbb-id-14-rate.pkl")

print("Model trained and saved.")
print("Training complete")
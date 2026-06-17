import pandas as pd
import joblib

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def train_model(dataset_path, model_path):
    # load dataset
    df = pd.read_csv(dataset_path)

    # features
    X = df.drop("win", axis=1)

    # target
    y = df["win"]

    # model
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression()
    )

    # train
    model.fit(X, y)

    # save
    joblib.dump(model, model_path)

    print(f"Model trained and saved: {model_path}")


train_model(
    "datasets/id/season_14.csv",
    "models/id/face_off_14.pkl"
)

train_model(
    "datasets/id/upper_semi_final_14.csv",
    "models/id/upper_semi_final_14.pkl"
)

train_model(
    "datasets/id/lower_semi_final_14.csv",
    "models/id/lower_semi_final_14.pkl"
)

train_model(
    "datasets/id/upper_final_14.csv",
    "models/id/upper_final_14.pkl"
)

train_model(
    "datasets/id/lower_final_14.csv",
    "models/id/lower_final_14.pkl"
)

train_model(
    "datasets/id/grand_final_14.csv",
    "models/id/grand_final_14.pkl"
)

print("All models trained successfully.")
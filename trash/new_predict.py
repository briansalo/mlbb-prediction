import joblib

model = joblib.load("mlbb_model.pkl")

new_match = [[
    -3, 2, -2, 6, -5, 4, 0, 2, 0, 1, -3, 0, 0, 0, 0, 0, 0, 0

]]

prediction = model.predict(new_match)
probability = model.predict_proba(new_match)

print(f"Prediction: {prediction[0]}")
print(f"Lose Probability: {probability[0][0] * 100:.2f}%")
print(f"Win Probability: {probability[0][1] * 100:.2f}%")
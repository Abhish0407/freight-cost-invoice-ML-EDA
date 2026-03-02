import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"
SCALER_PATH = "models/scaler.pkl"


def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = joblib.load(f)
    return model


def load_scaler():
    with open(SCALER_PATH, "rb") as f:
        scaler = joblib.load(f)
    return scaler


def predict_invoice_flag(input_data: dict):

    model = load_model()
    scaler = load_scaler()

    input_df = pd.DataFrame(input_data)

    scaled_data = scaler.transform(input_df)

    prediction = model.predict(scaled_data)

    input_df["Predicted_Flag"] = prediction

    return input_df

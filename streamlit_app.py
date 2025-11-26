import os
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

from mlProject.pipeline.prediction import PredictionPipeline


# Cache the pipeline so the model is not reloaded on every prediction
@st.cache_resource
def load_pipeline():
    return PredictionPipeline()


def main():
    st.set_page_config(
        page_title="Wine Quality Prediction",
        page_icon="🍷",
        layout="centered"
    )

    st.title("🍷 Wine Quality Prediction")
    st.write(
        "Enter the physicochemical properties of the wine below. "
        "The model will predict the **wine quality score**."
    )

    # Sidebar: Training button
    with st.sidebar:
        st.header("Model Training")
        st.write("Re-train the model by running `main.py` inside the container/environment.")
        train_button = st.button("🔁 Train Model")

        if train_button:
            with st.spinner("Training model... this may take a while."):
                # You can replace os.system with subprocess.run if you want better control
                exit_code = os.system("python main.py")
            if exit_code == 0:
                st.success("✅ Training Successful!")
            else:
                st.error(f"❌ Training failed (exit code {exit_code}). Check logs for details.")

    # Form for user inputs (with constraints)
    with st.form("prediction_form"):
        st.subheader("Wine Parameters")

        col1, col2 = st.columns(2)

        # Column 1 inputs
        with col1:
            fixed_acidity = st.number_input(
                "Fixed Acidity (g/dm³)",
                min_value=4.0, max_value=16.0,
                value=7.0, step=0.1
            )
            citric_acid = st.number_input(
                "Citric Acid (g/dm³)",
                min_value=0.0, max_value=1.0,
                value=0.3, step=0.01
            )
            chlorides = st.number_input(
                "Chlorides (g/dm³)",
                min_value=0.01, max_value=0.2,
                value=0.05, step=0.001,
                format="%.3f"
            )
            total_sulfur_dioxide = st.number_input(
                "Total Sulfur Dioxide (mg/dm³)",
                min_value=6.0, max_value=300.0,
                value=50.0, step=1.0
            )
            pH = st.number_input(
                "pH",
                min_value=2.5, max_value=4.5,
                value=3.2, step=0.01
            )
            alcohol = st.number_input(
                "Alcohol (% vol)",
                min_value=8.0, max_value=15.0,
                value=10.0, step=0.1
            )

        # Column 2 inputs
        with col2:
            volatile_acidity = st.number_input(
                "Volatile Acidity (g/dm³)",
                min_value=0.1, max_value=1.5,
                value=0.5, step=0.01
            )
            residual_sugar = st.number_input(
                "Residual Sugar (g/dm³)",
                min_value=0.5, max_value=20.0,
                value=2.0, step=0.1
            )
            free_sulfur_dioxide = st.number_input(
                "Free Sulfur Dioxide (mg/dm³)",
                min_value=1.0, max_value=75.0,
                value=15.0, step=1.0
            )
            density = st.number_input(
                "Density (g/cm³)",
                min_value=0.990, max_value=1.004,
                value=0.996, step=0.0001,
                format="%.4f"
            )
            sulphates = st.number_input(
                "Sulphates (g/dm³)",
                min_value=0.3, max_value=2.0,
                value=0.6, step=0.01
            )

        submitted = st.form_submit_button("🚀 Predict Quality")

    # When user clicks "Predict"
    if submitted:
        try:
            # Order of features must match your original Flask app
            data = np.array([
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol,
            ]).reshape(1, -1)

            pipeline = load_pipeline()
            prediction = pipeline.predict(data)

            # Handle different types of return
            if isinstance(prediction, (list, np.ndarray)) and len(prediction) == 1:
                prediction_value = prediction[0]
            else:
                prediction_value = prediction

            st.success(f"🎯 Predicted wine quality: **{prediction_value}**")

        except Exception as e:
            st.error(f"Something went wrong during prediction: `{e}`")


if __name__ == "__main__":
    main()

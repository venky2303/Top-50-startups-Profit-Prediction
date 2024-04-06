import streamlit as st
from joblib import load

loaded_model=load("training.pkl")
def pred(features):
    prediction=loaded_model.predict([features])
    return prediction[0]
def main():
    st.title("Top 50 stratups Profit Prediction")
    rd_spend=st.number_input("R&D spend:")
    admin_spend=st.number_input("Admin spend:")
    market_spend=st.number_input("Marketing spend:")

    if st.button("Predict"):
        features=[rd_spend,admin_spend,market_spend]
        predict=pred(features)
        st.success(f"The predict profit is{predict}")

if __name__=="__main__":
    main()
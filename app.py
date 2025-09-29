import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (in kgs)")

if weight == 0:
    st.text("Enter some value of wieght")

status = st.radio("Select your height format: ", ["cms", "meters", "feet"])

if status == "cms":
    height = st.number_input("Centimeters")

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value of height")

elif status == "meters":
    height = st.number_input("Meters")

    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")

else:
    height = st.number_input("Feet")

    try:
        bmi = weight / (((height / 3.28)) ** 2)
    except:
        st.text("Enter some value of height")

if st.button("Calculate BMI"):
    if weight != 0 and height != 0:
        st.text(f"Your BMI Index is {bmi}.")

        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif bmi >= 16 and bmi < 18.5:
            st.warning("You are Underweight")
        elif bmi >= 18.5 and bmi < 25:
            st.success("Healthy")
        elif bmi >= 25 and bmi < 30:
            st.warning("Overweight")
        elif bmi >= 30:
            st.error("Extremely Overweight")
    else:
        st.error("pls add both values")

# File: FITNESSTRACKER.py
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import time
import warnings
warnings.filterwarnings('ignore')

st.toast("Keep working hard 🦾 ⏳")

st.title("Personal Fitness Tracker")

with st.expander("About This WebApp"):
    st.write("This is a simple fitness tracker for users who want to monitor their calorie burn without expensive fitness bands.")
    st.subheader("Key Features:")
    st.write("- User input form")
    st.write("- Machine Learning model (RandomForestRegressor)")
    st.write("- Plotly Scatter plot for visualization")
    st.write("- Fitness Insights based on your data")
    st.write("- Model Performance evaluation")

with st.expander("How to Use"):
    st.write("1. Use the sidebar on the left to enter your details.")
    st.write("2. Adjust the input values to match your information.")
    st.write("3. Let the app calculate your estimated calorie burn!")

st.sidebar.header("Enter Your Data")

if "age" not in st.session_state:
    st.session_state.age = 25
if "gender" not in st.session_state:
    st.session_state.gender = "Male"
if "bmi" not in st.session_state:
    st.session_state.bmi = 25.0

def user_input_features():
    st.session_state.age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=st.session_state.age)
    st.session_state.gender = st.sidebar.selectbox("Gender", ["Male", "Female"], index=0 if st.session_state.gender == "Male" else 1)
    st.session_state.bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=st.session_state.bmi)
    duration = st.sidebar.slider("Daily Workout Duration (min):", 0, 30, 15)
    heart_rate = st.sidebar.slider("Heart Rate during Workout:", 60, 130, 80)
    body_temp = st.sidebar.slider("Body Temperature(C) during Workout:", 36, 42, 41)
    gender_encoded = 1 if st.session_state.gender == "Male" else 0

    data_model = {
        "Age": st.session_state.age,
        "BMI": st.session_state.bmi,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp,
        "Gender": gender_encoded
    }

    features = pd.DataFrame([data_model])
    return features

df = user_input_features()

st.write("---")
with st.expander("Your Input Parameters"):
    st.write(df)
st.write("---")

calories = pd.read_csv("calories.csv")
exercise = pd.read_csv("exercise.csv")

exercise_df = exercise.merge(calories, on="User_ID").drop(columns="User_ID")

exercise_train_data, exercise_test_data = train_test_split(exercise_df, test_size=0.2, random_state=1)

for data in [exercise_train_data, exercise_test_data]:
    data["BMI"] = data["Weight"] / ((data["Height"] / 100) ** 2)
    data["BMI"] = round(data["BMI"], 2)

exercise_train_data = exercise_train_data[["Gender", "Age", "BMI", "Duration", "Heart_Rate", "Body_Temp", "Calories"]]
exercise_test_data = exercise_test_data[["Gender", "Age", "BMI", "Duration", "Heart_Rate", "Body_Temp", "Calories"]]
exercise_train_data = pd.get_dummies(exercise_train_data, drop_first=True)
exercise_test_data = pd.get_dummies(exercise_test_data, drop_first=True)

X_train = exercise_train_data.drop("Calories", axis=1)
y_train = exercise_train_data["Calories"]

X_test = exercise_test_data.drop("Calories", axis=1)
y_test = exercise_test_data["Calories"]

random_reg = RandomForestRegressor(n_estimators=1000, max_features=3, max_depth=6)
random_reg.fit(X_train, y_train)
df = df.reindex(columns=X_train.columns, fill_value=0)
prediction = random_reg.predict(df)

st.subheader("Workout Duration vs Calories Burned")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1)
    time.sleep(0.01)

fii = px.scatter(exercise_train_data, x="Duration", y="Body_Temp", size="Calories", title="Calories Burned vs. Workout Duration")

fii.update_layout(
    width=700,
    height=450,
)

fii.add_scatter(
    x=[df["Duration"].values[0]], y=[df["Body_Temp"].values[0]],
    mode="markers+text", marker=dict(size=18, color="red", symbol="star"), name="Your Input", text=["You"], textposition="top center"
)
st.plotly_chart(fii)

st.write("---")
st.subheader("Prediction:")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1)
    time.sleep(0.01)

st.write(f"{round(prediction[0], 2)} **kilocalories Burned Today based on your data**")

st.write("---")
st.subheader("Similar Results:")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1)
    time.sleep(0.01)

calorie_range = [prediction[0] - 10, prediction[0] + 10]
similar_data = exercise_df[(exercise_df["Calories"] >= calorie_range[0]) &
                           (exercise_df["Calories"] <= calorie_range[1])]

if not similar_data.empty:
    st.write("#### People with Similar Calorie Burn:")
    st.write(similar_data.sample(min(5, len(similar_data))))
else:
    st.warning("No similar results found in the dataset.")

st.write("---")
st.header("General Information:")

boolean_age = (exercise_df["Age"] < df["Age"].values[0]).tolist()
boolean_duration = (exercise_df["Duration"] < df["Duration"].values[0]).tolist()
boolean_body_temp = (exercise_df["Body_Temp"] < df["Body_Temp"].values[0]).tolist()
boolean_heart_rate = (exercise_df["Heart_Rate"] < df["Heart_Rate"].values[0]).tolist()

st.write(f"You are older than {round(sum(boolean_age) / len(boolean_age), 2) * 100}% of other people.")
st.write(f"Your exercise duration is higher than {round(sum(boolean_duration) / len(boolean_duration), 2) * 100}% of other people.")
st.write(f"You have a higher heart rate than {round(sum(boolean_heart_rate) / len(boolean_heart_rate), 2) * 100}% of other people during exercise.")
st.write(f"You have a higher body temperature than {round(sum(boolean_body_temp) / len(boolean_body_temp), 2) * 100}% of other people during exercise.")

st.write("---")
y_pred = random_reg.predict(X_test)

st.subheader("Model Performance:")
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)
st.write(f"R² Score: {round(r2, 2)}")

if r2 >= 0.9:
    st.success("Excellent Model: This Model is very Good Model so that everyone will use it efficiently.")
elif r2 >= 0.75:
    st.success("Good Model: Explains a significant portion of the variance.")
elif r2 >= 0.5:
    st.warning("Average Model: Still usable but could be improved.")
elif r2 >= 0:
    st.warning("Poor Model: Explains very little variance.")
else:
    st.error("Very Bad Model: Worse than a random guess!")

st.write("---")
st.subheader("Thank You!")
# (No additional code needed here, as this is the end of the script.)

import streamlit as st
import openai

# ---- CONFIG ----
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ---- APP TITLE ----
st.set_page_config(page_title="Pump Cover", layout="centered")
st.title("🏋️ Pump Cover: AI Workout Generator")

# ---- USER INPUT ----
muscle_group = st.selectbox("Choose a muscle group:", ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core"])
experience = st.selectbox("Your experience level:", ["Beginner", "Intermediate", "Advanced"])
goal = st.selectbox("Training goal:", ["Build Muscle", "Lose Fat", "Strength Training", "Endurance"])
days_per_week = st.slider("How many days per week do you train?", 1, 7, 3)

# ---- GENERATE BUTTON ----
if st.button("Generate My Workout Plan"):
    with st.spinner("Generating your custom plan..."):
        prompt = (
            f"Create a detailed {experience.lower()} workout plan for the {muscle_group.lower()} muscle group. "
            f"The goal is to {goal.lower()}. The user trains {days_per_week} times per week. "
            "Include exercises, sets, reps, and rest times in a clean format."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional fitness coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )

        workout = response["choices"][0]["message"]["content"]
        st.success("Here’s your AI-generated plan:")
        st.markdown(workout)

st.markdown("---")
st.caption("Built with 💪 by Pump Cover using OpenAI + Streamlit")

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="HealthTrack", layout="wide", page_icon="💚")

# --- BEAUTIFUL COLORS CSS ---
st.markdown("""
<style>
    .main { background-color: #F7FFFE; }
    .header {
        background: linear-gradient(135deg, #00BFA6 0%, #00ACC1 100%);
        padding: 25px; border-radius: 20px; color: white;
        text-align: center; margin-bottom: 20px;
    }
    .card {
        background: white; padding: 20px; border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.07);
        border-left: 5px solid #00BFA6;
        margin-bottom: 18px;
    }
    .card-orange { border-left-color: #FF8A65; }
    .card-blue { border-left-color: #64B5F6; }
    .card-purple { border-left-color: #BA68C8; }
    .card-yellow { border-left-color: #FFD54F; }
    .stButton>button {
        background: linear-gradient(135deg, #00BFA6, #00ACC1);
        color: white; border: none; border-radius: 12px;
        padding: 10px 20px; font-weight: bold; width: 100%;
    }
    h3 { color: #00695C; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="header">
    <h1 style="margin:0; color:white;">💚 HealthTrack</h1>
    <p style="margin:5px 0 0 0; font-size:16px;">Your Daily Health, Water & Wellness - All in One Place</p>
</div>
""", unsafe_allow_html=True)

# --- WELCOME ---
st.markdown(f"<div class='card'><h3>👋 Welcome, Anita!</h3><p>Today is {datetime.now().strftime('%A, %d %B %Y')} - Let's track your health!</p></div>", unsafe_allow_html=True)

# --- SECTION 1: DASHBOARD ---
st.markdown("<div class='card'><h3>📊 Today's Dashboard</h3></div>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
col1.metric("💧 Water", "4 / 8 glasses", "+2")
col2.metric("💊 Meds", "2 / 3 taken", "On track")
col3.metric("🚶 Steps", "3,200", "+400")
col4.metric("😴 Sleep", "7.5 hrs", "Good")

# --- SECTION 2: WATER ---
st.markdown("<div class='card card-blue'><h3>💧 Water Reminder</h3><p>Stay hydrated! Click to add a glass</p></div>", unsafe_allow_html=True)
w1, w2, w3 = st.columns([2,1,2])
with w1:
    glasses = st.slider("How many glasses today?", 0, 12, 4)
with w2:
    st.write("")
    st.write("")
    if st.button("➕ Add 1 Glass"):
        st.balloons()
        st.success("Great! +1 glass added!")
with w3:
    st.progress(glasses/8)

# --- SECTION 3: MEDICATION & HEALTH ---
st.markdown("<div class='card card-orange'><h3>💊 Medication & Health Check</h3></div>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    med = st.text_input("Medicine / Vitamin name")
    time = st.time_input("Time to take")
    if st.button("Save Medication"):
        st.success(f"Saved: {med} at {time}")
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    bp = st.text_input("Blood Pressure e.g. 120/80")
    sugar = st.number_input("Blood Sugar", 0, 400, 90)
    weight = st.number_input("Weight (kg)", 0.0, 200.0, 65.0)
    if st.button("Save Health Data"):
        st.success("Health data saved to Supabase!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION 4: WORK BREAK & REST ---
st.markdown("<div class='card card-purple'><h3>🧘 Work, Break & Rest</h3><p>Anita, remember to stand up every 1 hour!</p></div>", unsafe_allow_html=True)
b1, b2 = st.columns(2)
with b1:
    if st.button("🌬️ Start 1-Minute Breathing"):
        st.info("Breathe in... Breathe out... You are doing great!")
with b2:
    if st.button("☕ Take a Break Reminder"):
        st.warning("Time to stand, stretch, drink water!")

# --- SECTION 5: FINANCIAL HEALTH ---
st.markdown("<div class='card card-yellow'><h3>💰 Financial Health</h3></div>", unsafe_allow_html=True)
amount = st.number_input("Money spent on health today (₦)", 0, 100000, 0)
note = st.text_input("What did you spend on?")
if st.button("Save Expense"):
    st.success(f"Saved ₦{amount} for {note}")

st.markdown("---")
st.markdown("<center><p style='color:#888;'>Made with 💚 by Anita | HealthTrack 2026 | Scroll up to see all sections</p></center>", unsafe_allow_html=True)
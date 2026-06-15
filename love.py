import streamlit as st
import random
import datetime

# --- 100% NATIVE PREMIUM VIEWPORT ---
st.set_page_config(page_title="My love, Caroline.", page_icon="❤️", layout="centered")

# --- ADVANCED RED, GOLD, & PATTERNED HEART BG STYLING ---
st.markdown(
    """
    <style>
    /* Injects a seamless repeating heart background pattern inspired by your image */
    .stApp {
        background-color: #fff1f2 !important;
        background-image: radial-gradient(#f43f5e 15%, transparent 16%),
                          radial-gradient(#f43f5e 15%, transparent 16%) !important;
        background-size: 60px 60px !important;
        background-position: 0 0, 30px 30px !important;
        opacity: 0.95;
    }
    
    /* Elegant Serif/Royal Typography Override */
    h1, h2, h3, p, span, label, div {
        font-family: 'Georgia', serif !important;
    }
    
    /* Luxury Crimson Red Title with Gold Glow Aura */
    .romantic-title {
        text-align: center;
        color: #9f1239 !important;
        font-weight: bold;
        font-size: 2.6rem;
        margin-top: 20px;
        margin-bottom: 5px;
        text-shadow: 0 0 10px #d97706, 0 0 20px rgba(217, 119, 6, 0.4);
    }
    
    .romantic-subtitle {
        text-align: center;
        color: #b45309 !important;
        font-size: 1.1rem;
        font-style: italic;
        margin-bottom: 25px;
        font-weight: bold;
    }

    /* Floating Ribbon Dividers */
    .sea-container {
        text-align: center;
        font-size: 1.6rem;
        letter-spacing: 6px;
        margin-top: 15px;
        margin-bottom: 20px;
    }

    /* Royal Cream Parchment Scroll Box Card with Deep Gold Borders */
    .love-scroll-box {
        background-color: #fffbeb !important;
        border: 3px solid #d97706 !important;
        border-radius: 16px !important;
        padding: 25px !important;
        text-align: center !important;
        margin-top: 15px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 10px 30px rgba(217, 119, 6, 0.25) !important;
    }

    .love-scroll-text {
        color: #78350f !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        font-style: italic !important;
        line-height: 1.6 !important;
    }
    
    /* Style local subtitle headings */
    .stMarkdown h3 {
        color: #9f1239 !important;
        text-shadow: 0 0 5px rgba(217, 119, 6, 0.2);
    }

    /* Force metric block data cards to look like gold bars */
    div[data-testid="stMetric"] {
        background: #fffbeb !important;
        border: 2px solid #d97706 !important;
        border-radius: 14px !important;
        padding: 15px !important;
        box-shadow: 0 6px 20px rgba(217, 119, 6, 0.15) !important;
    }
    [data-testid="stMetricLabel"] {
        color: #b45309 !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricValue"] {
        color: #9f1239 !important;
        font-weight: bold !important;
    }
    .stCaption {
        color: #b45309 !important;
        font-weight: 500 !important;
    }

    /* Premium Crimson Red Button with Gold Edge Highlights */
    div.stButton > button:first-child {
        background-color: #9f1239 !important;
        color: #fef3c7 !important;
        border: 2px solid #d97706 !important;
        border-radius: 50px !important;
        padding: 12px 24px !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
        box-shadow: 0 6px 25px rgba(159, 18, 57, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #881337 !important;
        border-color: #f59e0b !important;
        transform: scale(1.02) !important;
    }
    
    /* Force Dropdown input containers to match black text standards */
    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: bold !important;
    }
    ul[role="listbox"] li * {
        color: #000000 !important;
    }
    .stSelectbox label p {
        color: #9f1239 !important;
        font-weight: bold !important;
    }

    /* Custom Floating "I Love You" Text Animation Canvas Rules */
    @keyframes heartRain {
        0% { transform: translateY(-10vh) translateX(0px) scale(0.8); opacity: 1; }
        100% { transform: translateY(100vh) translateX(50px) scale(1.2); opacity: 0; }
    }
    .custom-heart-particle {
        position: fixed;
        top: -50px;
        color: #9f1239;
        font-weight: bold;
        font-size: 1.5rem;
        z-index: 9999;
        pointer-events: none;
        animation: heartRain 4s linear forwards;
        text-shadow: 0 0 8px #f59e0b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render Visual Title Headers
st.markdown("<h1 class='romantic-title'>👑 My love, Caroline.</h1>", unsafe_allow_html=True)
st.markdown("<p class='romantic-subtitle'>A private corner of the universe filled with notes just for you.</p>", unsafe_allow_html=True)
st.divider()

# --- FEATURE 1: LIVE ANNIVERSARY COUNTER ---
start_date = datetime.datetime(2024, 9, 24) 
days_together = (datetime.datetime.now() - start_date).days

st.metric(label="🏆 Days Spent Loving You:", value=f"{days_together:,} Days")
st.caption(f"Counting every single beautiful day since {start_date.strftime('%B %d, %Y')}")
st.divider()

# --- THE 300 COMPREHENSIVE ROMANTIC MESSAGES ---
messages = [
    "✨ You are my absolute favorite person in the entire universe.",
    "🐳 Just a little reminder that you make my world infinitely brighter.",
    "💫 Thinking about your smile right now, wherever you are.",
    "🌊 Out of all the people floating on this planet, I'm so glad I found you.",
    "⚓ My heart is completely anchored to you, always and forever.",
    "🌟 You are my safe harbor and my favorite adventure all in one.",
    "🐚 Sending you a giant hug through the screen right now!",
    "🥰 Your laugh is hands-down my absolute favorite sound in the world.",
    "❤️ Every single day with you feels like a beautiful dream come true.",
    "✨ You are the best thing that has ever happened to me.",
    "🌙 I love you to the moon and back, plus infinity.",
    "☀️ You bring so much warmth and light into my everyday life.",
    "🌹 You have a permanent home inside my heart.",
    "🧸 No matter how far apart we are, you are always right here in my thoughts.",
    "💍 Falling for you was the easiest and best thing I've ever done.",
    "✨ You make even the most ordinary days feel incredibly special.",
    "💕 I love you exactly as you are, for exactly who you are.",
    "🌸 You are my favorite piece of beautiful chaos.",
    "🔥 You still give me those exact same butterflies as the first day we met.",
    "🏡 With you, my heart is completely at home.",
    "🍀 Finding you felt like winning the grand lottery of life.",
    "🔮 I want to share all of my tomorrows with you.",
    "🕊️ Your peace and calm are what keep me grounded.",
    "🎨 You paint my world with colors I didn't know existed.",
    "🍫 You are sweeter than anything else in this world.",
    "🎈 Holding your hand is my absolute favorite place to be.",
    "💎 You are rarer and more precious than the finest diamond.",
    "🌌 My universe centers completely around your happiness.",
    "🎵 Every love song on the radio suddenly makes sense because of you.",
    "💌 You are my favorite hello and my hardest goodbye.",
    "🥞 I love you more than lazy Sunday mornings and hot coffee.",
    "🍂 Just a little digital note to remind you how much you are cherished.",
    "🌟 You shine brighter than any star in the night sky.",
    "🧊 You melt my heart even on the coldest days.",
    "🛸 I love you across every dimension and timeline.",
    "🌈 You are the bright, beautiful rainbow after my stormiest days.",
    "🎠 Life with you is a beautiful, never-ending ride.",
    "📖 My favorite love story is the one we are writing together.",
    "🥤 You are the perfect match to my energy.",
    "🎟️ I'd choose you in every single lifetime, no questions asked.",
    "🎸 You make my heart skip a beat every single time you look at me.",
    "🥨 We fit together perfectly, just like two puzzles pieces.",
    "🛸 Even if we were lost in outer space, I'd find my way to you.",
    "🧸 You are my absolute comfort zone.",
    "🧁 You make life taste so much sweeter.",
    "🗺️ No matter where I go, all roads always lead back to you.",
    "🧭 You are my true north, guiding me through everything.",
    "🏰 I will protect your heart with everything I have.",
    "🔑 You hold the permanent key to my heart.",
    "🕯️ You light up the darkest corners of my life.",
    "💡 Just thinking about you instantly brightens up my mood.",
    "🛌 I want to wake up next to you for the rest of my life.",
    "🛋️ Cuddling with you is the absolute best cure for anything.",
    "🧺 An afternoon with you is worth more than a million days anywhere else.",
    "🌲 Our love grows deeper and stronger with each passing day.",
    "🍿 You are my favorite movie partner and my lifelong teammate.",
    "🥂 Cheers to us, and to everything we are building together.",
    "🎡 You turn the simplest moments into unforgettable memories.",
    "🛶 I'd row across any ocean just to be by your side.",
    "🚲 Going through life with you is an absolute joy.",
    "🧣 Your love wraps around me like a warm blanket on a freezing night.",
    "🎒 I want to travel the entire world with you.",
    "👟 I am so thankful to be walking this path of life with you.",
    "🥾 You are my favorite partner-in-crime for any adventure.",
    "👒 You look absolutely stunning every single day.",
    "🧣 Your embrace is the safest place on earth.",
    "🧤 I want to hold your hands forever.",
    "🧦 You make me feel so warm and cozy inside.",
    "🧥 You are my comfort and my security.",
    "🧵 Our lives are beautifully woven together.",
    "👜 I carry your heart with me wherever I go.",
    "👑 You are the absolute king/queen of my world.",
    "💍 I choose you today, tomorrow, and for the rest of my days.",
    "🕶️ My future looks so incredibly bright because you are in it.",
    "🕷️ I'm totally caught in your web of love.",
    "🦕 My love for you is bigger than anything else in the world.",
    "🦁 I will always stand up and protect you.",
    "🐯 You bring out the absolute best version of me.",
    "🦄 You are magical, rare, and entirely unique.",
    "🐣 You make my heart feel so soft and tender.",
    "🦉 You are the wisest choice I have ever made.",
    "🐝 I am totally buzzing with happiness when we are together.",
    "🦋 You give my heart wings to fly.",
    "🐾 I will follow you wherever your path leads.",
    "🌻 You turn my face toward the sunshine.",
    "🌾 Our love is gentle, beautiful, and growing.",
    "🌿 You bring life and freshness into my routine.",
    "🌴 You are my personal paradise island.",
    "🌳 Rooted deep in my heart, that's where you'll always stay.",
    "🍁 Like autumn leaves, I fall harder for you every single day.",
    "🍄 You bring a fun, magical spark into my life.",
    "🌵 Even in dry, hard times, our love thrives.",
    "🧅 Layer by layer, I fall deeper in love with your soul.",
    "🌽 You are simply amazing and I am so grateful for you.",
    "🥔 You are my favorite comfort food for the soul.",
    "🥕 You make my life so much richer and better.",
    "🥑 We are the absolute perfect combination.",
    "🥝 You are a refreshing burst of happiness in my life.",
    "🍉 Life with you is sweet, fun, and colorful."
]

if "current_message" not in st.session_state:
    st.session_state.current_message = "Tap the royal heart below to draw a love note from the sea! 🌊"
if "trigger_rain" not in st.session_state:
    st.session_state.trigger_rain = False

# Render floating ribbon dividing tracking line
st.markdown("<div class='sea-container'>💖 💕 💖 💕 💖 💕 💖 💕</div>", unsafe_allow_html=True)

# YOUR MAIN INTERACTIVE TRIGGER BUTTON
if st.button("❤️ CLICK TO REEL IN A MESSAGE ❤️", use_container_width=True, type="primary"):
    st.session_state.current_message = random.choice(messages)
    st.session_state.trigger_rain = True

# INJECT DYNAMIC MAPPED "I LOVE YOU" TEXT ANIMATION RAIN (GOLD HIGHLIGHTED)
if st.session_state.trigger_rain:
    particle_html = ""
    words = ["I Love You! ❤️", "Caroline ❤️", "Forever ❤️", "💝"]
    for i in range(35):
        left_pos = random.randint(5, 95)
        delay = round(random.uniform(0.0, 2.0), 2)
        word = random.choice(words)
        particle_html += f"<div class='custom-heart-particle' style='left: {left_pos}%; animation-delay: {delay}s;'>{word}</div>"
    st.markdown(particle_html, unsafe_allow_html=True)
    st.session_state.trigger_rain = False 

# Render active message inside our parchment style block
st.markdown(
    f"""
    <div class='love-scroll-box'>
        <p class='love-scroll-text'>\"{st.session_state.current_message}\"</p>
    </div>
    """, 
    unsafe_allow_html=True
)
st.divider()

# --- FEATURE 2: 100 COMPREHENSIVE DROP-DOWN LIST SELECTION ---
st.write("### 🎁 100 Hidden Reminders For You:")

# Generate dropdown array elements 1 to 100
numbers_list = ["Select a number..."] + [f"Number {i}" for i in range(1, 101)]
choice = st.selectbox("Pick a secret number to reveal a hidden thought:", numbers_list)

# Generate looping dictionary mapping index logic behind choices safely
secret_thoughts = {}
for i in range(1, 101):
    note_index = (i - 1) % len(messages)
    secret_thoughts[f"Number {i}"] = f"🔱 Note #{i}: " + messages[note_index]

# Output display selection container layout block
if choice != "Select a number...":
    st.success(secret_thoughts[choice])

import streamlit as st
import random
import datetime
import time

# --- 100% NATIVE PREMIUM VIEWPORT CONTAINER ---
st.set_page_config(page_title="My Love, Caroline.", layout="centered")

# Core Variable Configurations
PARTNER_NAME = "Caroline"
ANNIVERSARY_DATE = datetime.date(2024, 9, 24)
today = datetime.date.today()
current_hour = datetime.datetime.now().hour

# Safe initialization of state memory records across active user sessions
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "current_random_letter" not in st.session_state:
    st.session_state.current_random_letter = "Click generate below to request a letter node from my heart."
if "current_surprise" not in st.session_state:
    st.session_state.current_surprise = ""
if "current_reminder" not in st.session_state:
    st.session_state.current_reminder = "Click generate below to unlock your reminder tracking panel."
if "current_compliment" not in st.session_state:
    st.session_state.current_compliment = "Click generate above to unlock your affirmation tracking panel."
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "reflection_logs" not in st.session_state:
    st.session_state.reflection_logs = []
if "miss_you_counter" not in st.session_state:
    st.session_state.miss_you_counter = 0

# Experience points and user streak trackers
if "relationship_xp" not in st.session_state:
    st.session_state.relationship_xp = 150
if "interaction_streak" not in st.session_state:
    st.session_state.interaction_streak = 1
if "last_visit_date" not in st.session_state:
    st.session_state.last_visit_date = str(today)
if "has_checked_in_today" not in st.session_state:
    st.session_state.has_checked_in_today = False

# Automated Time-of-Day Visual Layout Rule
if "selected_theme" not in st.session_state:
    if 6 <= current_hour < 17:
        st.session_state.selected_theme = "Luxury Rose Gold"
    elif 17 <= current_hour < 21:
        st.session_state.selected_theme = "Royal Crimson"
    else:
        st.session_state.selected_theme = "Elegant / Vintage Letter"

# Compute interaction streaks safely across daily page hits
if st.session_state.last_visit_date != str(today):
    try:
        last_date = datetime.datetime.strptime(st.session_state.last_visit_date, "%Y-%m-%d").date()
        if (today - last_date).days == 1:
            st.session_state.interaction_streak += 1
            st.session_state.relationship_xp += 40
        else:
            st.session_state.interaction_streak = 1
    except Exception:
        pass
    st.session_state.last_visit_date = str(today)
    st.session_state.has_checked_in_today = False
# ==========================================
# 2. PREMIUM THEME DESIGN ENGINE
# ==========================================
st.sidebar.markdown("### APP CONFIGURATION")
chosen_sidebar_theme = st.sidebar.selectbox(
    "Aesthetic Engine Style",
    options=["Elegant / Vintage Letter", "Luxury Rose Gold", "Royal Crimson"],
    index=["Elegant / Vintage Letter", "Luxury Rose Gold", "Royal Crimson"].index(st.session_state.selected_theme)
)

if chosen_sidebar_theme != st.session_state.selected_theme:
    st.session_state.selected_theme = chosen_sidebar_theme
    st.rerun()

# Dynamic Palette Variable Assignments
if st.session_state.selected_theme == "Elegant / Vintage Letter":
    bg_canvas, text_main, accent_color, panel_bg, font_family = "#fdfaf2", "#2c2520", "#b89775", "#fbf6eb", "'Georgia', serif"
    card_border = "1px solid #e6dcce"
    particle_color = "rgba(184, 151, 117, 0.25)"
elif st.session_state.selected_theme == "Luxury Rose Gold":
    bg_canvas, text_main, accent_color, panel_bg, font_family = "#fffafb", "#4a3538", "#d4a373", "#fdf2f4", "'Helvetica Neue', Arial, sans-serif"
    card_border = "1px solid #f3d1d6"
    particle_color = "rgba(212, 163, 115, 0.3)"
else:  # Royal Crimson
    bg_canvas, text_main, accent_color, panel_bg, font_family = "#faf2ea", "#4c0519", "#881337", "#fdfbf7", "'Georgia', serif"
    card_border = "1px solid rgba(217, 119, 6, 0.3)"
    particle_color = "rgba(136, 19, 55, 0.15)"

# Deep Injected Custom CSS Formatting Rules
st.markdown("""
<style>
.stApp { background-color: #fdfaf2; }
</style>
""", unsafe_allow_html=True)
# ==========================================
# 3. SECURE GATEWAY (LOGIN RUNTIME)
# ==========================================
if not st.session_state.unlocked:
    st.markdown("<h1 class='premium-title'>My Love, Caroline.</h1>", unsafe_allow_html=True)
    st.markdown("<p class='premium-subtitle'>Enter our anniversary date to authenticate</p>", unsafe_allow_html=True)
    
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        password_attempt = st.text_input("Password Entry", type="password", label_visibility="collapsed", placeholder="MMDD or MM/DD")
        if password_attempt:
            clean_attempt = password_attempt.strip().lower()
            if clean_attempt in ["0924", "924", "09/24", "9/24", "september 24", "september 24th"]:
                st.session_state.unlocked = True
                st.session_state.relationship_xp += 20
                
                # Assign randomized custom greeting praise components on successful access
                entry_greetings = [
                    "You are the absolute definition of elegance and grace.",
                    "Waking up to another day of loving you is my truest privilege.",
                    "Your golden presence anchors my entire heart effortlessly.",
                    "The universe stays perfectly quiet and beautiful whenever you log in."
                ]
                st.session_state.current_surprise = random.choice(entry_greetings)
                st.rerun()
            else:
                st.error("Incorrect date entry. Please check the alignment and try again.")
# ==========================================
# 4. DASHBOARD ENGINE CONTENT RUNTIME
# ==========================================
if st.session_state.unlocked:
    st.markdown("<h1 class='premium-title'>My Love, Caroline.</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='premium-subtitle'>{st.session_state.selected_theme} Active View</p>", unsafe_allow_html=True)

    # Compute operational countdown metrics
    if today.day < 24:
        next_monthsary = datetime.date(today.year, today.month, 24)
    else:
        next_monthsary = datetime.date(today.year + 1, 1, 24) if today.month == 12 else datetime.date(today.year, today.month + 1, 24)
    days_to_monthsary = (next_monthsary - today).days

    next_anniversary = datetime.date(today.year, 9, 24)
    if today > next_anniversary:
        next_anniversary = datetime.date(today.year + 1, 9, 24)
    days_to_anniversary = (next_anniversary - today).days
    total_days = (today - ANNIVERSARY_DATE).days

    # Layout Metrics Panel Row 1
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Days Loving You</div><div class='metric-value'>{total_days:,}</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Next Monthsary</div><div class='metric-value'>{days_to_monthsary}d</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Next Anniversary</div><div class='metric-value'>{days_to_anniversary}d</div></div>", unsafe_allow_html=True)

    # Layout Level Progress Panel Row 2
    st.markdown("<br>", unsafe_allow_html=True)
    g1, g2, g3 = st.columns(3)
    current_level = int((st.session_state.relationship_xp / 100) + 1)
    with g1:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Space Level</div><div class='metric-value'>Level {current_level}</div></div>", unsafe_allow_html=True)
    with g2:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Total Space XP</div><div class='metric-value'>{st.session_state.relationship_xp} XP</div></div>", unsafe_allow_html=True)
    with g3:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Connection Streak</div><div class='metric-value'>{st.session_state.interaction_streak} Days</div></div>", unsafe_allow_html=True)

    # Badge Evaluation Matrix Engine
    earned_badges = ["Devotion Genesis"]
    if total_days >= 30: earned_badges.append("Moon Cycle Bond")
    if total_days >= 90: earned_badges.append("Season of Grace")
    if st.session_state.interaction_streak >= 7: earned_badges.append("Weekly Constant")

    badge_html = "<div style='display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin-top:15px;'>"
    for badge in earned_badges:
        badge_html += f"<span style='background-color:{panel_bg}; border:{card_border}; padding:5px 12px; border-radius:20px; font-size:0.78rem; font-weight:bold; letter-spacing:0.5px;'>{badge}</span>"
    badge_html += "</div>"
    st.markdown(badge_html, unsafe_allow_html=True)
    # ==========================================
    # 5. DICTIONARIES & DAILY LOG INTERFACE
    # ==========================================
    rem_openers = [
        "Take a soft, quiet breath right now and look at how far you have come;",
        "Please never lose sight of the incredible, brilliant resilience inside you;",
        "Always remember that your soft empathy is a beautiful gift to this world;",
        "Be deeply patient, gentle, and slow with your magnificent mind today;",
        "Just a small, warm note to anchor your heart through this busy afternoon;"
    ]
    rem_connectors = [
        "the safe, unshakeable sanctuary of your presence completely makes",
        "the pure, effortless elegance you navigate this life with easily makes",
        "the unmatched warmth radiating from your golden soul thoroughly makes",
        "the clear wisdom and refreshing depth behind your words undeniably makes"
    ]
    rem_closers = [
        "this vast, moving universe feel entirely peaceful, secure, and complete.",
        "my whole horizon look infinitely brighter and full of clear purpose.",
        "even the most ordinary days feel profoundly important, warm, and valued.",
        "every single path we walk together look inviting and entirely worthwhile."
    ]

    all_reminders = {}
    for i in range(1, 101):
        all_reminders[i] = f"{rem_openers[i % len(rem_openers)]} {rem_connectors[(i * 2 + 1) % len(rem_connectors)]} {rem_closers[(i * 3 + 2) % len(rem_closers)]}"

    st.markdown("---")
    st.markdown("<p style='font-size:1.3rem; font-weight:bold; text-align:center; margin-bottom:5px;'>Daily Relationship Alignment</p>", unsafe_allow_html=True)

    if not st.session_state.has_checked_in_today:
        st.markdown("<p style='font-style:italic; font-size:0.95rem; text-align:center; margin-bottom:15px;'>How are you feeling about us today, Caroline?</p>", unsafe_allow_html=True)
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            mood_selection = st.radio(
                "Select Current Mood State:",
                options=["Happy and At Peace", "Missing You Deeply", "Tired but Devoted", "Seeking Comfort"],
                key="mood_radio_select"
            )
        with c_col2:
            reflection_input = st.text_area("Commit a reflection paragraph entry into our space logs:", height=76, placeholder="Share your quiet thoughts...", label_visibility="collapsed")
            
        if st.button("Submit Space Log Reflection", use_container_width=True):
            timestamp = datetime.datetime.now().strftime("%H:%M")
            log_entry = f"[{timestamp}] Mood: {mood_selection} - {reflection_input.strip() if reflection_input.strip() else 'Quiet Record'}"
            st.session_state.reflection_logs.insert(0, log_entry)
            st.session_state.has_checked_in_today = True
            st.session_state.relationship_xp += 30
            st.toast("Daily alignment successfully committed to history.")
            st.rerun()
else:
    if st.session_state.unlocked:
        st.markdown(f'<div class="luxury-card" style="padding:15px !important; text-align:center; border-color:{accent_color} !important;"><p style="font-size:1rem; font-style:italic; margin:0;">Thank you for checking in today. Your reflection has been written safely to our history vault.</p></div>', unsafe_allow_html=True)

if st.session_state.unlocked and st.session_state.reflection_logs:
    with st.expander("Review Past Workspace Logs"):
        for log in st.session_state.reflection_logs[:5]:
            st.markdown(f"<p style='font-size:0.88rem; font-style:italic; margin-bottom:4px; opacity:0.85;'>{log}</p>", unsafe_allow_html=True)
    # ==========================================
    # 6. VAULT CONTROLS & SURPRISE REGISTERS
    # ==========================================
    st.markdown("---")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("Transmit Miss You Signal"):
            st.session_state.miss_you_counter += 1
            st.session_state.relationship_xp += 10
            st.toast("Signal received at my heart. Thinking of you right now.")
    with col_b2:
        if st.button("Request Affirmation Track"):
            st.session_state.current_reminder = all_reminders[random.randint(1, 100)]
            st.session_state.relationship_xp += 5

    st.markdown(f'<div class="luxury-card" style="padding:20px !important;"><p class="luxury-card-text" style="font-size:1.15rem !important;">“ {st.session_state.current_reminder} ”</p></div>', unsafe_allow_html=True)

    # --- THE VAULT MATRIX ---
    st.markdown("<p style='font-size:1.3rem; font-weight:bold; margin-top:25px; margin-bottom:5px; text-align:center;'>The Letter Vault</p>", unsafe_allow_html=True)
    letter_tab, random_tab, condition_tab, milestone_tab = st.tabs(["Daily Ledger", "Heart Selection", "Open On Condition", "Milestone Archives"])

    with letter_tab:
        st.markdown("<p style='font-style:italic; font-size:0.92rem; text-align:center; margin-bottom:10px;'>Select any operational timeline node across our annual rotation record</p>", unsafe_allow_html=True)
        day_query = st.number_input("Enter Calendar Ledger Day Number (1 - 366):", min_value=1, max_value=366, value=1)
        
        if st.button("Trigger Animated Read Protocol"):
            placeholder = st.empty()
            text_string = f"Waking up to another day of loving you is my greatest privilege, because the brilliant warmth of your heart gently realigns everything I do, keeping me boundlessly grateful to call you my home, always and forever. (Ledger Record #{day_query})"
            displayed_text = ""
            for character in text_string:
                displayed_text += character
                placeholder.markdown(f'<div class="luxury-card"><p class="luxury-card-text">“ {displayed_text} ”</p></div>', unsafe_allow_html=True)
                time.sleep(0.003)

    with random_tab:
        st.markdown("<p style='font-style:italic; font-size:0.95rem; text-align:center; margin-bottom:15px;'>Pull a random letter from my heart.</p>", unsafe_allow_html=True)
        if st.button("Generate Random Letter Track", use_container_width=True):
            st.session_state.relationship_xp += 15
            random_pool = [
                "In every quiet pause throughout my afternoon, my thoughts instantly rest on you, allowing your lovely warmth to transform standard days into timeless memories.",
                "There is a deep, unshakeable peace in knowing we share the same horizon, proving over and over that the reality we built together is my truest sanctuary.",
                "No matter what pace the universe sets today, you remain my perfect center, safely carrying your elegant laughter in my thoughts as my favorite anchor."
            ]
            st.session_state.current_random_letter = random.choice(random_pool)
        st.markdown(f'<div class="luxury-card"><p class="luxury-card-text">“ {st.session_state.current_random_letter} ”</p></div>', unsafe_allow_html=True)

    with condition_tab:
        st.markdown("<p style='font-style:italic; font-size:0.92rem; text-align:center; margin-bottom:12px;'>Contextual correspondence logs tuned to specific emotional parameters</p>", unsafe_allow_html=True)
        condition_selection = st.selectbox(
            "Choose Current State Profile:",
            options=["Open when you miss me", "Open when you feel overwhelmed", "Open when you need a hug", "Open when you cannot sleep"],
            key="condition_vault_select"
        )
        if st.button("Unlock Condition Correspondence", use_container_width=True):
            st.session_state.relationship_xp += 5
            if condition_selection == "Open when you miss me":
                c_text = "Close your eyes for three seconds and take a deep breath. Distance is just a temporary measurement of space, but what we hold inside our hearts is entirely infinite, unshakeable, and bound together forever."
            elif condition_selection == "Open when you feel overwhelmed":
                c_text = "Pause right now and drop your shoulders. You do not have to carry the weight of the entire universe today. Take it one slow step at a time, and remember I am standing right beside you through it all."
            elif condition_selection == "Open when you need a hug":
                c_text = "I am wrapping my arms around you across the distance right now. Feel the quiet warmth of my heart resting securely against yours. You are completely safe, deeply protected, and intensely cherished."
            else:
                c_text = "Let your thoughts rest completely quiet tonight. Look up at the stars and know we are looking at the exact same sky. Rest easily, my lovely girl, because my heart is watching over yours until the morning."
            st.markdown(f'<div class="luxury-card"><p class="luxury-card-text">“ {c_text} ”</p></div>', unsafe_allow_html=True)

    with milestone_tab:
        is_anniversary_day = (today.month == 9 and today.day == 24)
        is_monthsary_day = (today.day == 24)
        
        milestone_selection = st.selectbox("Choose Milestone Vault Target:", options=["Monthsary Milestone", "Anniversary Milestone", "Valentine's Legacy Edition"], key="milestone_vault_select")
        
        if milestone_selection == "Monthsary Milestone":
            if is_monthsary_day:
                title_tag, body_text = f"Monthsary Record - Unlocked Day #{total_days}", "My beautiful Caroline, another full cycle of the moon has passed with you by my side. Thank you for protecting my heart and sharing your light with me every single month."
            else:
                title_tag, body_text = "Monthsary Archive Locked", "This archive opens automatically on our next monthsary. Please return on the 24th of the month to unlock this section."
        elif milestone_selection == "Anniversary Milestone":
            if is_anniversary_day:
                title_tag, body_text = "The Grand Anniversary Monument Letter", "Caroline, looking back at September 24, 2024, remains the exact point where my reality shifted into focus. You are, explicitly, my finest decision and my absolute masterpiece definition of home."
            else:
                title_tag, body_text = "Anniversary Monument Locked", "This monumental letter is sealed securely. It will open automatically when our next formal calendar anniversary arrives on September 24."
        else:
            title_tag, body_text = "Valentine's Legacy Edition Correspondence", "To the woman who completely redefines the concept of elegance every day. This record exists as an unshakeable testament that your soft grace, brilliant presence, and quiet sanctuary are completely, perfectly cherished on this day of romance."
            
        st.markdown(f'<div class="luxury-card"><p style="text-align:center; font-weight:bold; letter-spacing:1px; text-transform:uppercase; font-size:1.05rem; margin-bottom:15px; color:{accent_color} !important;">{title_tag}</p><p class="luxury-card-text">“ {body_text} ”</p></div>', unsafe_allow_html=True)

    # --- SYSTEM FLOATING SURPRISE GREETINGS ---
    if st.session_state.current_surprise:
        st.markdown("---")
        st.markdown(
            f"""
            <div class="luxury-card" style="border-style: dashed !important; border-color:{accent_color} !important;">
                <p class="luxury-card-text" style="font-weight:500;">{st.session_state.current_surprise}</p>
                <br>
                <p style="color:{accent_color}; font-size:1.1rem; font-weight:bold; text-align:center; margin:0;">I love you.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.toast("I love you.")

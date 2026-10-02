"""PYTHONA - run with:  streamlit run app.py"""
import streamlit as st

from chatbot import chatbot_response
from code_analyzer import analyze_code, explain_common_error
from database import (
    get_chat_history, get_learning_progress, init_database,
    save_chat, update_learning_progress,
)
from gamification import calculate_level, calculate_level_progress, get_rank
from mentor import get_mentor_tip

st.set_page_config(page_title="PYTHONA", page_icon="🐍", layout="wide")
init_database()

st.markdown("""
<style>
h1, h2, h3 { color: #5EEAD4; }
.stTabs [aria-selected="true"] { color: #FBBF24 !important; }
[data-testid="stChatMessage"] {
    background: #1E293B; border: 1px solid #334155; border-radius: 12px;
}
.stButton > button { background: #14B8A6; color: #0F172A; border: 0; font-weight: 600; }
.stButton > button:hover { background: #FBBF24; color: #0F172A; }
</style>
""", unsafe_allow_html=True)

st.title("🐍 PYTHONA")
st.caption("Your Python learning companion")

if "messages" not in st.session_state:
    st.session_state.messages = []

tab_chat, tab_detective, tab_progress, tab_history = st.tabs(
    ["💬 Chat", "🕵️ Code Detective", "📈 Progress", "🕘 History"]
)

with tab_chat:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask a Python question...")
    if question:
        result = chatbot_response(question)
        reply = f"{result['response']}\n\n{get_mentor_tip(result['topic'])}"
        st.session_state.messages += [
            {"role": "user", "content": question},
            {"role": "assistant", "content": reply},
        ]
        save_chat(question, result["response"], result["topic"])
        update_learning_progress(result["topic"])
        st.rerun()

with tab_detective:
    code = st.text_area("Paste Python code", height=200)
    if st.button("Check syntax"):
        out = analyze_code(code)
        (st.success if out["success"] else st.error)("Result")
        st.markdown(out["message"])

    error_text = st.text_input("Or paste an error message")
    if error_text:
        st.markdown(explain_common_error(error_text))

with tab_progress:
    rows = get_learning_progress()
    total_xp = sum(r[3] for r in rows)
    level = calculate_level(total_xp)
    st.subheader(f"{get_rank(level)}  ·  Level {level}")
    st.progress(calculate_level_progress(total_xp))
    st.caption(f"{total_xp} XP total")
    if rows:
        st.dataframe(
            [{"Topic": t, "Asked": q, "Correct": c, "XP": x} for t, q, c, x in rows],
            use_container_width=True,
        )

with tab_history:
    for user_msg, _, topic, created in get_chat_history():
        st.markdown(f"**{created}** · `{topic}` — {user_msg}")

st.markdown("""
<style>
/* ---------- Rectangle frame with snakes ---------- */
.snake-frame {
    position: fixed;
    top: 14px;                          /* margin from screen edge */
    left: 14px;
    width: calc(100vw - 28px);          /* 2 x margin */
    height: calc(100vh - 28px);
    z-index: 1000000;
    pointer-events: none;
    overflow: visible;
}
.snake-frame rect {
    fill: none;
    stroke-linecap: round;
}
.snake-frame .track {
    stroke: rgba(148, 163, 184, 0.25);
    stroke-width: 2;
}

/* one lap = 12s; all snake parts share it, shifted slightly so they line up */
.snake-frame .seg {
    animation: crawl 12s linear infinite;
    animation-delay: calc(var(--d) + var(--o, 0s));
}
@keyframes crawl {
    from { stroke-dashoffset: 0; }
    to   { stroke-dashoffset: -100; }
}

/* body parts, tail to head (dash lengths are % of the frame perimeter) */
.snake-frame .tail { stroke-dasharray: 3.5 96.5; stroke-width: 3;  opacity: .5; --d: 0s; }
.snake-frame .b1   { stroke-dasharray: 2 98;     stroke-width: 5;  opacity: .8; --d: -0.42s; }
.snake-frame .b2   { stroke-dasharray: 1.5 98.5; stroke-width: 7;  --d: -0.66s; }
.snake-frame .head { stroke-dasharray: 1.2 98.8; stroke-width: 11; --d: -0.84s; }

/* snake 1: teal body, amber head */
.snake-frame .s1 .tail, .snake-frame .s1 .b1, .snake-frame .s1 .b2 { stroke: #14B8A6; }
.snake-frame .s1 .head { stroke: #FBBF24; }
.snake-frame .s1 { filter: drop-shadow(0 0 5px #14B8A6); }

/* snake 2: violet body, pink head, starts on the opposite side */
.snake-frame .s2 { --o: -6s; }
.snake-frame .s2 .tail, .snake-frame .s2 .b1, .snake-frame .s2 .b2 { stroke: #A78BFA; }
.snake-frame .s2 .head { stroke: #F472B6; }
.snake-frame .s2 { filter: drop-shadow(0 0 5px #A78BFA); }

@media (prefers-reduced-motion: reduce) {
    .snake-frame .seg { animation: none; }
}

/* keep page content inside the frame */
.block-container { padding: 3.5rem 3.5rem 2rem; }

/* ---------- Your existing styles ---------- */
h1, h2, h3 { color: #5EEAD4; }
.stTabs [aria-selected="true"] { color: #FBBF24 !important; }
[data-testid="stChatMessage"] {
    background: #1E293B; border: 1px solid #334155; border-radius: 12px;
}
.stButton > button { background: #14B8A6; color: #0F172A; border: 0; font-weight: 600; }
.stButton > button:hover { background: #FBBF24; color: #0F172A; }
</style>
<svg class="snake-frame" xmlns="http://www.w3.org/2000/svg">
<rect class="track" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
<g class="s1">
<rect class="seg tail" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
<rect class="seg b1" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
<rect class="seg b2" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
<rect class="seg head" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
</g>
<g class="s2">
<rect class="seg tail" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
<rect class="seg b1" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
<rect class="seg b2" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
<rect class="seg head" x="0" y="0" width="100%" height="100%" rx="18" pathLength="100"/>
</g>
</svg>
""", unsafe_allow_html=True)
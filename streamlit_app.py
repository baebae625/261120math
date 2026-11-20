import html

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="똑딱 톡톡 수학 놀이터",
    page_icon="⏰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');
    :root {
        --ink: #29465b;
        --coral: #ff8878;
        --yellow: #ffda78;
        --mint: #bcebd7;
        --lavender: #dcd5ff;
        --paper: #f3faff;
    }
    .stApp {
        background:
            radial-gradient(ellipse at 8% 8%, #d8f0ff 0, transparent 28%),
            radial-gradient(ellipse at 92% 18%, #dff7ff 0, transparent 26%),
            var(--paper);
        color: var(--ink);
        font-family: 'Noto Sans KR', sans-serif;
    }
    h1, h2, h3, [data-testid="stMetricValue"] {
        font-family: 'Jua', 'Noto Sans KR', sans-serif !important;
        color: var(--ink);
    }
    .block-container { max-width: 1120px; padding-top: 2rem; padding-bottom: 4rem; }
    [data-testid="stTabs"] button {
        font-family: 'Jua', sans-serif;
        font-size: 1.08rem;
        border-radius: 16px 16px 0 0;
        min-height: 3.2rem;
    }
    [data-testid="stTabs"] button[aria-selected="true"] {
        color: #247cad;
        border-bottom-color: #70c4ed;
    }
    .hero {
        background: linear-gradient(120deg, #ccecff, #b6e4ff 55%, #dfedff);
        border: 2px solid #fff;
        border-radius: 30px;
        padding: 2rem 2.2rem;
        box-shadow: 0 10px 24px #83b9d633;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }
    .hero h1 { font-size: clamp(2.2rem, 5vw, 3.4rem); margin: .15rem 0 .4rem; }
    .hero p { font-size: 1.08rem; margin-bottom: .3rem; }
    .hero-badge {
        display: inline-block;
        background: white;
        color: #287eae;
        border-radius: 999px;
        padding: .35rem .8rem;
        font-weight: 800;
        font-size: .85rem;
    }
    .buddy { position: absolute; right: 4%; bottom: -7px; font-size: clamp(3rem, 8vw, 5rem); }
    .friends {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: .65rem;
        margin: -.45rem 0 1.3rem;
    }
    .friend {
        background: #fff;
        border: 2px solid #d5edfb;
        border-radius: 18px;
        padding: .7rem;
        text-align: center;
        box-shadow: 0 4px 12px #83b9d622;
    }
    .friend-face { font-size: 1.8rem; }
    .friend-name { color: #287eae; font-weight: 900; }
    .friend-job { color: #687d8d; font-size: .82rem; }
    .time-guides {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: .7rem;
        margin: .6rem 0;
    }
    .time-guide {
        background: #f4fbff;
        border: 2px solid #d5edfb;
        border-radius: 18px;
        padding: .9rem;
        line-height: 1.7;
    }
    .time-guide strong { color: #287eae; }
    .time-guide .guide-character { font-size: 1.6rem; }
    .soft-card {
        background: #fff;
        border: 2px solid #d5edfb;
        border-radius: 22px;
        padding: 1.1rem 1.25rem;
        margin: .45rem 0 .8rem;
        box-shadow: 0 5px 14px #83b9d618;
    }
    .callout {
        background: #e5f5ff;
        border-left: 6px solid #78c9f3;
        border-radius: 14px;
        padding: .8rem 1rem;
        margin: .7rem 0;
    }
    .sequence {
        display: flex;
        gap: .55rem;
        flex-wrap: wrap;
        align-items: center;
        font-size: 2rem;
        background: #fbfeff;
        padding: .8rem 1rem;
        border-radius: 18px;
        border: 2px dashed #8bcdeb;
        margin: .6rem 0;
    }
    .sequence span {
        min-width: 2.7rem;
        text-align: center;
        background: #e9f7ff;
        border-radius: 12px;
        padding: .2rem .45rem;
    }
    .sequence .missing { background: #f0edff; color: #7669bd; }
    .hundred-grid {
        display: grid;
        grid-template-columns: repeat(10, 1fr);
        gap: 3px;
        background: #c9e7f5;
        border: 3px solid #c9e7f5;
        border-radius: 13px;
        overflow: hidden;
        margin: .7rem 0 1rem;
    }
    .hundred-grid span { background: white; text-align: center; padding: .28rem 0; font-size: .8rem; }
    .hundred-grid span.jump { background: #ffda78; font-weight: 900; color: #76591b; }
    .goal { padding: .4rem .1rem; line-height: 1.65; }
    .stButton > button {
        border-radius: 14px;
        border: 2px solid #c7e6f5;
        background: #fff;
        color: var(--ink);
        font-weight: 800;
        min-height: 2.7rem;
    }
    .stButton > button:hover { border-color: #63b8e4; color: #247cad; }
    [data-testid="stAlert"] { border-radius: 16px; }
    @media (max-width: 600px) {
        .hero { padding: 1.4rem; }
        .buddy { right: 3%; opacity: .8; }
        .friends { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .time-guides { grid-template-columns: 1fr; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <span class="hero-badge">1학년 수학 · 시계 보기 & 규칙 찾기</span>
      <h1>똑딱 톡톡 수학 놀이터</h1>
      <p>토끼 똑딱이, 고양이 톡톡이와 시계도 보고 규칙도 찾아봐요!</p>
      <span class="buddy">🐰 🐱</span>
    </div>
    <div class="friends">
      <div class="friend"><div class="friend-face">🐰</div><div class="friend-name">똑딱이</div><div class="friend-job">시계 읽기 친구</div></div>
      <div class="friend"><div class="friend-face">🐱</div><div class="friend-name">톡톡이</div><div class="friend-job">30분 알려 주기</div></div>
      <div class="friend"><div class="friend-face">🐻</div><div class="friend-name">곰곰이</div><div class="friend-job">규칙 찾기 대장</div></div>
      <div class="friend"><div class="friend-face">🐥</div><div class="friend-name">삐약이</div><div class="friend-job">짝꿍 응원단</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.expander("오늘의 배움 목표를 확인해요", expanded=False):
    goals = [
        "긴바늘과 짧은바늘이 나타내는 뜻을 알고, 몇 시와 몇 시 30분을 읽어요.",
        "모형 시계를 움직여 주어진 시각을 나타내요.",
        "물체, 무늬, 수 배열에서 규칙을 찾아 말·그림·기호·수로 설명해요.",
        "나만의 규칙으로 물체와 무늬, 수를 창의적으로 배열해요.",
        "생활 속 시각과 규칙을 찾아 수학으로 문제를 해결해요.",
        "친구의 규칙을 존중하고 서로의 생각을 나눠요.",
    ]
    for goal in goals:
        st.markdown(f'<div class="goal">🌱 {goal}</div>', unsafe_allow_html=True)


def clock_html(hour, minute):
    markup = """
    <!doctype html>
    <html lang="ko">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        * { box-sizing: border-box; }
        body { margin: 0; background: transparent; color: #3c4656; font-family: 'Noto Sans KR', sans-serif; }
        .wrap { background: linear-gradient(145deg,#fbfeff,#eaf7ff); border: 2px solid #cce8f8; border-radius: 24px; padding: 14px; text-align: center; }
        .instruction { font-weight: 800; font-size: 15px; margin: 0 0 5px; }
        svg { width: min(100%, 340px); display: block; margin: 0 auto; touch-action: none; user-select: none; }
        .time { font-size: 25px; font-weight: 900; color: #e56e5d; margin: -2px 0 3px; }
        .hint { min-height: 38px; font-size: 13px; line-height: 1.5; color: #526074; }
        .readout { font-size: 14px; font-weight: 800; color: #647083; }
        .flip { margin: 9px auto 0; border: 0; border-radius: 12px; padding: 9px 14px; background: #d9f0ff; color: #286d94; font-weight: 900; cursor: pointer; }
        .digital { display: none; margin: 9px auto 0; width: fit-content; padding: 8px 18px; border-radius: 12px; background: #3c4656; color: #fff; font-size: 23px; font-weight: 900; letter-spacing: 2px; }
        .digital.show { display: block; }
        .sector { fill: #ffda78; opacity: .5; stroke: #e6a848; stroke-width: 2; }
        .number { font-size: 16px; font-weight: 900; fill: #4a5262; text-anchor: middle; dominant-baseline: middle; }
        .tick { stroke: #d8d0c0; stroke-width: 1.5; }
        .minute-hand { stroke: #ee806e; stroke-width: 6; stroke-linecap: round; }
        .hour-hand { stroke: #6179bb; stroke-width: 9; stroke-linecap: round; }
        .drag-area { stroke: transparent; stroke-width: 28; cursor: grab; }
        .drag-area:active { cursor: grabbing; }
      </style>
    </head>
    <body>
      <div class="wrap">
        <p class="instruction">🖐️ 긴바늘을 잡고 숫자 6까지 움직여 봐요!</p>
        <svg id="clock" viewBox="0 0 300 300" role="img" aria-label="바늘을 끌어 시각을 맞추는 모형 시계">
          <circle cx="150" cy="150" r="127" fill="#fff" stroke="#a8d9f3" stroke-width="8"/>
          <path id="sector" class="sector" d="" style="display:none"/>
          <g id="ticks"></g>
          <g id="numbers"></g>
          <line id="hourHand" class="hour-hand" x1="150" y1="150" x2="150" y2="104"/>
          <line id="minuteHand" class="minute-hand" x1="150" y1="150" x2="150" y2="52"/>
          <line id="minuteHit" class="drag-area" x1="150" y1="150" x2="150" y2="52" pointer-events="stroke"/>
          <circle cx="150" cy="150" r="8" fill="#ffda78" stroke="#fff" stroke-width="3"/>
        </svg>
        <div id="time" class="time" aria-live="polite"></div>
        <div id="readout" class="readout">긴바늘은 분, 짧은바늘은 시를 알려줘요.</div>
        <div id="hint" class="hint"></div>
        <button id="flip" class="flip" type="button">🃏 디지털 시계 카드 뒤집기</button>
        <div id="digital" class="digital" aria-live="polite"></div>
      </div>
      <script>
        const baseHour = Number("__HOUR__");
        let minute = Number("__MINUTE__");
        const center = 150;
        const ticks = document.getElementById("ticks");
        const numbers = document.getElementById("numbers");
        for (let i = 0; i < 60; i++) {
          const angle = (i * 6 - 90) * Math.PI / 180;
          const r1 = i % 5 === 0 ? 111 : 117;
          const r2 = 122;
          const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
          line.setAttribute("x1", center + Math.cos(angle) * r1);
          line.setAttribute("y1", center + Math.sin(angle) * r1);
          line.setAttribute("x2", center + Math.cos(angle) * r2);
          line.setAttribute("y2", center + Math.sin(angle) * r2);
          line.setAttribute("class", "tick");
          ticks.appendChild(line);
        }
        for (let n = 1; n <= 12; n++) {
          const angle = (n * 30 - 90) * Math.PI / 180;
          const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
          text.setAttribute("x", center + Math.cos(angle) * 92);
          text.setAttribute("y", center + Math.sin(angle) * 92);
          text.setAttribute("class", "number");
          text.textContent = n;
          numbers.appendChild(text);
        }
        function point(hour, radius) {
          const angle = (hour * 30 - 90) * Math.PI / 180;
          return [center + Math.cos(angle) * radius, center + Math.sin(angle) * radius];
        }
        function update() {
          const shownHour = baseHour === 0 ? 12 : baseHour;
          const hourPosition = (baseHour % 12) + minute / 60;
          const hourTip = point(hourPosition, 56);
          const minuteAngle = (minute * 6 - 90) * Math.PI / 180;
          const minuteTip = [center + Math.cos(minuteAngle) * 99, center + Math.sin(minuteAngle) * 99];
          const hourHand = document.getElementById("hourHand");
          const minuteHand = document.getElementById("minuteHand");
          const minuteHit = document.getElementById("minuteHit");
          hourHand.setAttribute("x2", hourTip[0]); hourHand.setAttribute("y2", hourTip[1]);
          minuteHand.setAttribute("x2", minuteTip[0]); minuteHand.setAttribute("y2", minuteTip[1]);
          minuteHit.setAttribute("x2", minuteTip[0]); minuteHit.setAttribute("y2", minuteTip[1]);
          document.getElementById("time").textContent =
            minute === 0 ? shownHour + "시" : shownHour + "시 " + String(minute).padStart(2, "0") + "분";
          document.getElementById("digital").textContent =
            String(shownHour).padStart(2, "0") + ":" + String(minute).padStart(2, "0");
          const half = minute === 30;
          const sector = document.getElementById("sector");
          if (half) {
            const start = point(baseHour % 12, 72);
            const end = point((baseHour % 12) + 1, 72);
            sector.setAttribute("d", "M 150 150 L " + start[0] + " " + start[1] +
              " A 72 72 0 0 1 " + end[0] + " " + end[1] + " Z");
            sector.style.display = "block";
            document.getElementById("hint").textContent =
              "짧은바늘은 " + shownHour + "과 " + (shownHour === 12 ? 1 : shownHour + 1) +
              " 사이에 있어요. 다음 숫자에 아직 닿지 않았으니 " + shownHour + "시 30분이에요!";
          } else {
            sector.style.display = "none";
            document.getElementById("hint").textContent =
              minute === 0 ? "긴바늘이 12에 오면 정각이에요. 이제 긴바늘을 움직여 보세요!" :
              "짧은바늘이 가리키는 시와 긴바늘이 가리키는 분을 함께 읽어 봐요.";
          }
        }
        const hit = document.getElementById("minuteHit");
        let dragging = false;
        function moveHand(event) {
          if (!dragging) return;
          const rect = document.getElementById("clock").getBoundingClientRect();
          const scale = 300 / rect.width;
          const x = (event.clientX - rect.left) * scale - center;
          const y = (event.clientY - rect.top) * scale - center;
          let degrees = (Math.atan2(y, x) * 180 / Math.PI + 90 + 360) % 360;
          minute = (Math.round(degrees / 30) * 5) % 60;
          update();
        }
        hit.addEventListener("pointerdown", (event) => {
          dragging = true;
          hit.setPointerCapture(event.pointerId);
          moveHand(event);
        });
        hit.addEventListener("pointermove", moveHand);
        hit.addEventListener("pointerup", () => { dragging = false; });
        hit.addEventListener("pointercancel", () => { dragging = false; });
        document.getElementById("flip").addEventListener("click", () => {
          document.getElementById("digital").classList.toggle("show");
        });
        update();
      </script>
    </body>
    </html>
    """
    return markup.replace("__HOUR__", str(hour)).replace("__MINUTE__", str(minute))


st.session_state.setdefault("clock_hour", 2)
st.session_state.setdefault("clock_minute", 0)
st.session_state.setdefault("clock_label", "연습 시각")
st.session_state.setdefault("pattern_blocks", [])


def set_schedule(hour, minute, label):
    st.session_state.clock_hour = hour
    st.session_state.clock_minute = minute
    st.session_state.clock_label = label


clock_tab, pattern_tab, create_tab, finish_tab = st.tabs(
    ["🕒 시계 탐험", "🔎 규칙 탐험", "🎨 나만의 규칙", "🌟 배움 정리"]
)

with clock_tab:
    st.header("시계 바늘 친구를 만나 봐요")
    st.markdown(
        '<div class="callout">🔵 짧은바늘은 <b>몇 시</b>인지, 🟠 긴바늘은 <b>몇 분</b>인지 알려줘요. '
        "긴바늘을 숫자 6에 놓으면 30분이에요!</div>",
        unsafe_allow_html=True,
    )
    st.markdown("#### 우리 하루의 시각을 골라요")
    schedule_columns = st.columns(3)
    schedules = [
        ("🌤️ 등교", 8, 0, "등교 시간"),
        ("🍱 점심", 12, 30, "점심 시간"),
        ("🎒 하교", 2, 30, "하교 시간"),
    ]
    for column, (label, hour, minute, description) in zip(schedule_columns, schedules):
        with column:
            st.button(
                label,
                key=f"schedule_{hour}_{minute}",
                use_container_width=True,
                on_click=set_schedule,
                args=(hour, minute, description),
            )
    st.caption(f"지금은 **{st.session_state.clock_label}**을 살펴보고 있어요. 바늘을 직접 움직여 보세요!")
    components.html(
        clock_html(st.session_state.clock_hour, st.session_state.clock_minute),
        height=510,
        scrolling=False,
    )
    st.markdown(
        '<div class="soft-card"><b>🐱 톡톡이의 약속: 하루의 시각을 이렇게 읽어요!</b>'
        '<div class="time-guides">'
        '<div class="time-guide"><div class="guide-character">🐰</div><strong>등교 · 8:00</strong><br>'
        "긴바늘이 12에 있어 0분, 짧은바늘이 8을 가리켜요.<br><b>8시</b>라고 읽어요.</div>"
        '<div class="time-guide"><div class="guide-character">🐻</div><strong>점심 · 12:30</strong><br>'
        "긴바늘이 6에 있어 30분, 짧은바늘은 12와 1 사이예요.<br><b>12시 30분</b>이라고 읽어요.</div>"
        '<div class="time-guide"><div class="guide-character">🐥</div><strong>하교 · 2:30</strong><br>'
        "긴바늘이 6에 있어 30분, 짧은바늘은 2와 3 사이예요.<br>"
        "<b>3에 아직 닿지 않았으니 2시 30분</b>이라고 읽어요.</div>"
        "</div>"
        '<div class="callout">짧은바늘이 두 숫자 사이에 있으면 먼저 지난 숫자를 읽어요. '
        "노란 부채꼴은 30분일 때 짧은바늘이 있는 곳을 보여 줘요! 🐱</div></div>",
        unsafe_allow_html=True,
    )

with pattern_tab:
    st.header("숨은 규칙을 찾아요")
    st.write("무엇이 되풀이되는지 살펴보고, 다음에 올 모양이나 수를 골라 보세요.")
    pattern_name = st.radio(
        "어떤 규칙을 찾아볼까요?",
        ["모양이 번갈아 나와요", "2씩 커져요", "100까지 수 배열표에서 4씩 뛰어요"],
        horizontal=True,
        key="pattern_choice",
    )
    pattern_data = {
        "모양이 번갈아 나와요": {
            "sequence": ["🍓", "⭐", "🍓", "⭐", "❔"],
            "choices": ["🍓", "⭐", "🍋"],
            "answer": "🍓",
            "explain": "딸기, 별이 차례로 반복돼요. 다음은 딸기예요!",
        },
        "2씩 커져요": {
            "sequence": ["2", "4", "6", "8", "❔"],
            "choices": ["9", "10", "12"],
            "answer": "10",
            "explain": "수가 2씩 커져요. 8 다음에 2를 더하면 10이에요!",
        },
        "100까지 수 배열표에서 4씩 뛰어요": {
            "sequence": ["4", "8", "12", "16", "20", "❔"],
            "choices": ["22", "24", "25"],
            "answer": "24",
            "explain": "4, 8, 12, 16, 20… 4씩 뛰었어요. 다음 수는 24예요!",
        },
    }
    selected_pattern = pattern_data[pattern_name]
    sequence_items = []
    for item in selected_pattern["sequence"]:
        class_name = "missing" if item == "❔" else ""
        sequence_items.append(f'<span class="{class_name}">{item}</span>')
    sequence_markup = "".join(sequence_items)
    st.markdown(f'<div class="sequence">{sequence_markup}</div>', unsafe_allow_html=True)

    if pattern_name == "100까지 수 배열표에서 4씩 뛰어요":
        jump_numbers = {4, 8, 12, 16, 20, 24}
        grid = "".join(
            f'<span class="{"jump" if number in jump_numbers else ""}">{number}</span>'
            for number in range(1, 101)
        )
        st.markdown(
            '<div class="soft-card"><b>💡 100까지 수 배열표에서 찾아봐요!</b>'
            f'<div class="hundred-grid">{grid}</div>'
            "노란 수를 따라가며 다음에 올 수를 생각해 보세요.</div>",
            unsafe_allow_html=True,
        )
    answer = st.radio(
        "❔에 들어갈 것은 무엇일까요?",
        selected_pattern["choices"],
        horizontal=True,
        key=f"answer_{pattern_name}",
    )
    if st.button("내 생각 확인하기", key=f"check_{pattern_name}"):
        if answer == selected_pattern["answer"]:
            st.success(f"딩동댕! {selected_pattern['explain']}")
        else:
            st.info("괜찮아요! 앞에서부터 어떤 모양이나 수가 되풀이되는지 다시 살펴봐요.")
    st.markdown(
        '<div class="callout">🗣️ 규칙은 말, 그림, 기호, 수로 나타낼 수 있어요. '
        "어떤 규칙인지 친구에게 설명해 볼까요?</div>",
        unsafe_allow_html=True,
    )

with create_tab:
    st.header("나만의 규칙 짝꿍 퀴즈")
    st.write("블록으로 규칙 배열을 만들고, 한두 칸을 가려 짝꿍에게 퀴즈를 내요!")
    palette = ["🍓 딸기", "⭐ 별", "🔵 파란 동그라미", "🌼 꽃", "🔺 세모"]
    palette_symbols = {item: item.split()[0] for item in palette}
    chosen_block = st.selectbox("블록 팔레트에서 고르기", palette, key="palette_choice")
    add_col, undo_col, clear_col = st.columns(3)
    with add_col:
        if st.button("➕ 블록 놓기", use_container_width=True):
            if len(st.session_state.pattern_blocks) < 12:
                st.session_state.pattern_blocks.append(palette_symbols[chosen_block])
                st.session_state.quiz_ready = False
            else:
                st.warning("블록은 12개까지 놓을 수 있어요.")
    with undo_col:
        if st.button("↩️ 마지막 블록 빼기", use_container_width=True):
            if st.session_state.pattern_blocks:
                st.session_state.pattern_blocks.pop()
                st.session_state.quiz_ready = False
    with clear_col:
        if st.button("🧹 처음부터 만들기", use_container_width=True):
            st.session_state.pattern_blocks = []
            st.session_state.quiz_ready = False

    blocks = st.session_state.pattern_blocks
    if blocks:
        st.markdown("#### 내가 만든 배열")
        st.markdown(
            '<div class="sequence">'
            + "".join(f"<span>{block}</span>" for block in blocks)
            + "</div>",
            unsafe_allow_html=True,
        )
    else:
        st.info("블록을 4개 이상 놓아 반복되는 규칙을 만들어 보세요. 예: 🍓 ⭐ 🍓 ⭐")

    if len(blocks) >= 3:
        st.markdown("#### 짝꿍에게 낼 문제 만들기")
        rule = st.text_input(
            "내가 만든 규칙을 설명해요",
            placeholder="예: 딸기와 별이 번갈아 나와요",
            key="my_rule_description",
        )
        positions = [f"{index + 1}번째 칸" for index in range(len(blocks))]
        covered = st.multiselect(
            "물음표 덮개로 가릴 칸을 1~2개 골라요",
            positions,
            key="covered_positions",
        )
        shown_items = []
        for index, block in enumerate(blocks):
            is_covered = f"{index + 1}번째 칸" in covered
            class_name = "missing" if is_covered else ""
            content = "❔" if is_covered else block
            shown_items.append(f'<span class="{class_name}">{content}</span>')
        shown_sequence = "".join(shown_items)
        st.markdown(
            '<div class="soft-card"><b>📱 짝꿍에게 보여 줄 화면</b>'
            f'<div class="sequence">{shown_sequence}</div>'
            f'<div>내 규칙 힌트: {html.escape(rule) if rule else "힌트 없이 규칙을 찾아보세요!"}</div></div>',
            unsafe_allow_html=True,
        )
        if len(covered) > 2:
            st.error("물음표 덮개는 두 칸까지만 골라 주세요.")
        if not covered:
            st.caption("먼저 1~2칸을 골라 물음표로 가려 주세요.")
        if st.button(
            "🤝 짝꿍과 바꿔 풀기",
            disabled=not covered or len(covered) > 2,
            use_container_width=True,
        ):
            st.session_state.quiz_ready = True
        if st.session_state.get("quiz_ready", False) and covered:
            st.markdown(
                '<div class="callout">태블릿을 짝꿍과 바꿔요. 가려진 칸에 올 모양을 말하고, '
                "어떤 규칙인지 서로 설명해 보세요. 친구의 생각도 끝까지 들어요! 💬</div>",
                unsafe_allow_html=True,
            )
            with st.expander("짝꿍이 답을 말한 뒤 정답 확인하기"):
                for position in covered:
                    index = int(position.split("번째")[0]) - 1
                    st.write(f"{position}에는 **{blocks[index]}**이 들어가요.")

with finish_tab:
    st.header("오늘의 수학 모험을 돌아봐요")
    st.markdown(
        '<div class="soft-card">🌞 하루 중 시계를 보면 좋은 때는 언제인가요?<br>'
        "🔍 주변에서 찾은 규칙은 무엇인가요?<br>"
        "🎨 내가 만든 규칙은 어떤 방법으로 설명했나요?</div>",
        unsafe_allow_html=True,
    )
    st.markdown("#### 스스로 확인해요")
    st.checkbox("몇 시와 몇 시 30분을 읽고 모형 시계에 나타낼 수 있어요.", key="reflect_clock")
    st.checkbox("반복되는 규칙을 찾고, 다음에 올 것을 설명할 수 있어요.", key="reflect_pattern")
    st.checkbox("친구가 만든 규칙을 존중하며 내 생각을 나눴어요.", key="reflect_friend")
    st.success("참 잘했어요! 생활 속 시계와 규칙 속에서 수학을 계속 찾아봐요. 🏅")

st.markdown(
    '<div style="text-align:center; color:#8a8f9b; padding-top:1.5rem;">'
    "🐰 똑딱이와 🐱 톡톡이의 수학 놀이터 · 오늘도 반짝이는 발견!</div>",
    unsafe_allow_html=True,
)

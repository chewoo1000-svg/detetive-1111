import streamlit as st
from questions import QUESTIONS

st.set_page_config(
    page_title="금융사기 수사대 | 빅토리안 기록실",
    page_icon="🕮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

if "screen" not in st.session_state:
    st.session_state.screen = "intro"
if "current" not in st.session_state:
    st.session_state.current = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}


def reset_app():
    st.session_state.screen = "intro"
    st.session_state.current = 0
    st.session_state.answers = {}


def get_grade(score: int):
    if score == 100:
        return "A", "수석 조사관", "모든 사건에서 위험 신호를 정확히 읽어냈습니다. 침착하고 냉철한 추론이 돋보입니다."
    if score >= 75:
        return "B", "선임 조사관", "전반적으로 우수한 대응력을 보였습니다. 다만 몇몇 유형에서는 한 번 더 확인하는 습관이 필요합니다."
    if score >= 50:
        return "C", "수습 조사관", "기본적인 감각은 있으나 긴급한 상황에서 흔들릴 수 있습니다. 공식 채널 확인 원칙을 더 익혀야 합니다."
    return "D", "기록 보조원", "즉각적인 판단보다 먼저 멈추고 확인하는 훈련이 필요합니다. 링크 클릭과 송금 전 재확인이 중요합니다."


def weak_tag():
    wrong = [q["tag"] for i, q in enumerate(QUESTIONS) if st.session_state.answers.get(i) != q["answer"]]
    if not wrong:
        return "취약 유형 없음"
    counts = {}
    for t in wrong:
        counts[t] = counts.get(t, 0) + 1
    return max(counts, key=counts.get)


def detective_svg():
    return """
    <svg viewBox="0 0 360 380" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#efe1c2"/>
          <stop offset="100%" stop-color="#e3cfab"/>
        </linearGradient>
      </defs>
      <rect x="18" y="18" width="324" height="344" rx="8" fill="url(#bg)" stroke="#b89d73" stroke-width="2"/>
      <rect x="30" y="30" width="300" height="320" rx="4" fill="none" stroke="#c6af87" opacity="0.65"/>
      <text x="180" y="56" text-anchor="middle" font-size="16" fill="#6e5636" font-family="Georgia, serif" letter-spacing="2">INVESTIGATION FILE</text>
      <ellipse cx="185" cy="320" rx="90" ry="18" fill="#cfbb95" opacity="0.55"/>
      <path d="M103 190C108 154 131 126 171 118C209 111 242 126 257 153C244 154 236 162 234 174C226 173 219 174 211 177C194 163 171 161 148 170C133 176 117 185 103 190Z" fill="#34281f"/>
      <path d="M146 146C154 120 179 105 205 108C225 110 239 123 245 139C233 131 219 125 201 124C183 123 162 131 146 146Z" fill="#4a3829"/>
      <ellipse cx="191" cy="191" rx="56" ry="62" fill="#ead8bf"/>
      <path d="M158 190C165 183 173 180 181 180" stroke="#564435" stroke-width="4" stroke-linecap="round"/>
      <path d="M204 180C212 179 220 182 226 188" stroke="#564435" stroke-width="4" stroke-linecap="round"/>
      <circle cx="178" cy="201" r="4.5" fill="#3c2c22"/>
      <circle cx="214" cy="201" r="4.5" fill="#3c2c22"/>
      <path d="M193 216C196 220 196 224 194 228" stroke="#785b42" stroke-width="3" stroke-linecap="round"/>
      <path d="M181 242C189 248 201 248 209 242" stroke="#8d5a4b" stroke-width="4" stroke-linecap="round"/>
      <path d="M135 181C143 172 150 166 163 160" stroke="#2c221b" stroke-width="11" stroke-linecap="round"/>
      <path d="M223 159C239 164 248 171 255 181" stroke="#2c221b" stroke-width="11" stroke-linecap="round"/>
      <path d="M148 250C155 231 174 220 195 220C218 220 237 233 243 253L255 305H137L148 250Z" fill="#4d3a2b"/>
      <path d="M171 229L195 249L218 229" stroke="#d2bf98" stroke-width="4" fill="none"/>
      <path d="M195 250L195 304" stroke="#d2bf98" stroke-width="4"/>
      <path d="M138 269C118 276 106 289 95 311" stroke="#ead8bf" stroke-width="13" stroke-linecap="round"/>
      <path d="M255 271C280 276 293 289 304 311" stroke="#ead8bf" stroke-width="13" stroke-linecap="round"/>
      <circle cx="86" cy="321" r="30" fill="#e7d7be" stroke="#816645" stroke-width="4"/>
      <circle cx="86" cy="321" r="18" fill="none" stroke="#816645" stroke-width="4"/>
      <line x1="106" y1="342" x2="124" y2="360" stroke="#816645" stroke-width="8" stroke-linecap="round"/>
      <path d="M287 308L318 298L323 307L295 318Z" fill="#6a4f37"/>
      <path d="M323 307C328 311 330 316 330 321C321 323 314 320 309 315" stroke="#6a4f37" stroke-width="5" fill="none" stroke-linecap="round"/>
      <circle cx="267" cy="92" r="26" fill="#7b332d" opacity="0.10"/>
      <circle cx="267" cy="92" r="18" fill="none" stroke="#7b332d" stroke-width="2" opacity="0.45"/>
      <text x="267" y="98" text-anchor="middle" font-size="9" fill="#7b332d" font-family="Georgia, serif">CASE</text>
      <text x="267" y="108" text-anchor="middle" font-size="9" fill="#7b332d" font-family="Georgia, serif">SEALED</text>
    </svg>
    """


def dossier_svg():
    return """
    <svg viewBox="0 0 340 180" width="100%" xmlns="http://www.w3.org/2000/svg">
      <rect x="16" y="22" width="220" height="138" rx="6" fill="#f4ead5" stroke="#b69e79" stroke-width="2"/>
      <path d="M52 22H110V8H152V22H52Z" fill="#dec69d" stroke="#b69e79" stroke-width="2"/>
      <text x="126" y="55" text-anchor="middle" font-size="18" fill="#5f4931" font-family="Georgia, serif">CASE DOSSIER</text>
      <line x1="42" y1="74" x2="209" y2="74" stroke="#c8b28b"/>
      <line x1="42" y1="91" x2="209" y2="91" stroke="#c8b28b"/>
      <line x1="42" y1="108" x2="209" y2="108" stroke="#c8b28b"/>
      <line x1="42" y1="125" x2="180" y2="125" stroke="#c8b28b"/>
      <circle cx="265" cy="96" r="46" fill="#ead9bc" stroke="#9e7b4a" stroke-width="4"/>
      <circle cx="265" cy="96" r="25" fill="none" stroke="#7e613b" stroke-width="4"/>
      <line x1="283" y1="114" x2="314" y2="145" stroke="#7e613b" stroke-width="9" stroke-linecap="round"/>
      <text x="265" y="101" text-anchor="middle" font-size="12" fill="#6b5236" font-family="Georgia, serif">CLUE</text>
    </svg>
    """


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Noto+Serif+KR:wght@400;500;600;700&display=swap');

    :root {
        --bg: #f3ede1;
        --paper: #f9f3e8;
        --paper-deep: #efe2c6;
        --ink: #2f2418;
        --sub: #6e5a43;
        --line: #bda98a;
        --gold: #8c6a2f;
        --navy: #22303d;
        --seal: #7b332d;
        --good: #ece8d8;
        --bad: #f3e2dc;
        --shadow: rgba(48,36,24,.10);
    }

    html, body, [class*="css"] {
        font-family: 'Noto Serif KR', serif;
        color: var(--ink);
    }

    .stApp {
        background:
          radial-gradient(circle at top right, rgba(140,106,47,.10), transparent 20%),
          linear-gradient(180deg, #f7f1e5 0%, #efe4cf 100%);
    }

    .block-container {
        max-width: 880px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    #MainMenu, footer {visibility:hidden;}
    header[data-testid="stHeader"] {background: transparent;}

    .cover-card, .paper-card, .report-card {
        position: relative;
        background: linear-gradient(180deg, #fbf5ea 0%, #f2e6cd 100%);
        border: 1.5px solid var(--line);
        border-radius: 10px;
        padding: 26px;
        box-shadow: 0 14px 28px var(--shadow);
        overflow: hidden;
    }

    .cover-card:before, .paper-card:before, .report-card:before {
        content: "";
        position: absolute;
        inset: 12px;
        border: 1px solid rgba(123,85,45,.28);
        border-radius: 5px;
        pointer-events: none;
    }

    .stamp {
        display:inline-block;
        border:1.4px solid var(--seal);
        color:var(--seal);
        padding:6px 12px;
        font-size:.81rem;
        font-weight:700;
        letter-spacing:.08em;
        background: rgba(123,51,45,.03);
        transform: rotate(-2deg);
        margin-bottom: 14px;
    }

    .cover-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 3.1rem;
        line-height: 1.02;
        font-weight: 700;
        color: var(--navy);
        margin-bottom: 12px;
        letter-spacing: .02em;
    }

    .cover-subtitle {
        color: var(--sub);
        font-size: 1rem;
        line-height: 1.88;
        margin-bottom: 16px;
    }

    .meta-wrap {display:flex; flex-wrap:wrap; gap:10px; margin-top:16px;}
    .meta-chip {
        display:inline-block;
        border:1px solid var(--line);
        background:#fbf7ef;
        border-radius:999px;
        padding:8px 12px;
        font-size:.88rem;
        color: var(--sub);
    }

    .rule {height:1px; background:linear-gradient(90deg, transparent, rgba(79,59,35,.45), transparent); margin:18px 0;}

    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--navy);
        margin-bottom: 8px;
    }

    .section-text {
        font-size: .98rem;
        line-height: 1.84;
        color: var(--sub);
    }

    .case-header {
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap:10px;
        flex-wrap:wrap;
        margin-bottom: 12px;
    }

    .file-no {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.45rem;
        font-weight: 700;
        color: var(--navy);
        letter-spacing: .05em;
    }

    .tag-pill {
        border:1px solid var(--line);
        background:#fbf7ef;
        color:var(--sub);
        border-radius:999px;
        padding:6px 10px;
        font-size:.82rem;
    }

    .case-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--ink);
        margin-bottom: 10px;
    }

    .scenario-box {
        background: rgba(255,255,255,.40);
        border: 1px solid #d7c6a8;
        border-radius: 8px;
        padding: 16px;
        color: var(--ink);
        line-height: 1.9;
    }

    .memo-box {
        margin-top: 14px;
        border-left: 4px solid var(--gold);
        background: #f7efe0;
        padding: 12px 14px;
        line-height: 1.75;
        color: var(--sub);
    }

    .analysis-good, .analysis-bad {
        border-radius: 8px;
        padding: 14px;
        line-height: 1.82;
        color: var(--ink);
    }

    .analysis-good {background: var(--good); border:1px solid #c4b78f;}
    .analysis-bad {background: var(--bad); border:1px solid #d4aea4;}

    .grade-box {
        border: 1.4px solid var(--line);
        background: linear-gradient(180deg, #fcf7ee 0%, #f1e3c7 100%);
        border-radius: 8px;
        padding: 18px;
        text-align:center;
        box-shadow: 0 10px 18px rgba(48,36,24,.06);
    }

    .small-label {font-size:.82rem; color:var(--sub); letter-spacing:.06em; text-transform:uppercase; margin-bottom:6px;}
    .grade-code {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.1rem;
        font-weight: 700;
        color: var(--navy);
        line-height:1;
    }
    .grade-name {font-size:1.02rem; font-weight:700; color:var(--ink); margin-top:8px;}

    .summary-item {border-top:1px dashed #c9b79a; padding-top:12px; margin-top:12px;}

    .illustration-card {
        background: linear-gradient(180deg, #f6ead0 0%, #e8d4ae 100%);
        border:1.5px solid var(--line);
        border-radius:10px;
        padding: 10px;
        box-shadow:0 14px 24px rgba(48,36,24,.08);
    }
    .illu-caption {
        text-align:center;
        font-size:.83rem;
        color: var(--sub);
        margin-top:4px;
        letter-spacing:.03em;
    }

    div.stButton > button {
        width:100%;
        min-height:58px;
        border-radius:7px;
        border:1.3px solid #765f3f;
        background: linear-gradient(180deg, #403121 0%, #261c14 100%);
        color: #f8f1e4;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 6px 14px rgba(34,26,18,.12);
    }

    div.stButton > button:hover {
        border-color:#8c6a2f;
        color:#fff9ed;
    }

    div.stButton > button[kind="secondary"] {
        background:#fbf6ee;
        color:var(--ink);
        border:1.2px solid var(--line);
        box-shadow:none;
    }

    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #6a5131 0%, #b18b48 100%);
    }

    .closing-note {
        margin-top:16px;
        text-align:center;
        color:#7c6a54;
        font-size:.82rem;
    }

    @media (max-width: 768px) {
        .cover-title {font-size:2.35rem;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### 기록실 메뉴")
    st.write("- 금융사기 사례 8건")
    st.write("- 사건별 분석 메모")
    st.write("- 최종 수사 보고서")
    st.write("- 빅토리안 추리소설 무드")
    st.divider()
    if st.button("처음으로", use_container_width=True):
        reset_app()
        st.rerun()

if st.session_state.screen == "intro":
    left, right = st.columns([1.45, 1])
    with left:
        st.markdown(
            """
            <div class="cover-card">
                <div class="stamp">CONFIDENTIAL · FRAUD INVESTIGATION ARCHIVE</div>
                <div class="cover-title">금융사기 수사대</div>
                <div class="cover-subtitle">
                    고풍스러운 사건 기록실과 빅토리아 시대 추리소설의 분위기를 담은 금융사기 대응 테스트입니다.<br>
                    사건 파일을 읽고 가장 안전한 판단을 골라보세요.
                </div>
                <div class="rule"></div>
                <div class="meta-wrap">
                    <div class="meta-chip">사건 수 8건</div>
                    <div class="meta-chip">예상 소요 3분</div>
                    <div class="meta-chip">기록물형 탐정 콘셉트</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown('<div class="illustration-card">' + detective_svg() + '<div class="illu-caption">추리소설풍 수사 삽화</div></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.15, 1])
    with c1:
        st.markdown(
            """
            <div class="paper-card">
                <div class="section-title">기록실 안내</div>
                <div class="section-text">
                    링크 클릭, 송금, 개인정보 제공과 관련된 대표적인 금융사기 상황을 교육용으로 재구성했습니다.
                    실제 사건을 읽는 듯한 방식으로 판단 연습을 하며, 위험 신호를 식별하는 습관을 기를 수 있습니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown('<div class="illustration-card">' + dossier_svg() + '<div class="illu-caption">사건 기록과 단서 조사</div></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="paper-card" style="margin-top:14px;">
            <div class="section-title">이용 원칙</div>
            <div class="section-text">
                본 서비스는 특정 금융기관의 공식 서비스가 아니며, 이름·계좌번호·연락처 등 민감한 개인정보를 입력받지 않습니다.
                모든 사례는 판단 훈련을 위한 교육용 예시입니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    a, b = st.columns([2, 1])
    with a:
        if st.button("사건 기록 열기", type="primary", use_container_width=True):
            st.session_state.screen = "quiz"
            st.session_state.current = 0
            st.rerun()
    with b:
        st.button("개인정보 미수집", disabled=True, use_container_width=True)

elif st.session_state.screen == "quiz":
    idx = st.session_state.current
    q = QUESTIONS[idx]
    st.progress(idx / len(QUESTIONS), text=f"진행 기록 {idx} / {len(QUESTIONS)}")

    st.markdown(
        f"""
        <div class="paper-card">
            <div class="case-header">
                <div class="file-no">CASE FILE {q['case_no']}</div>
                <div class="tag-pill">{q['tag']}</div>
            </div>
            <div class="case-title">{q['title']}</div>
            <div class="scenario-box">{q['scenario']}</div>
            <div class="memo-box"><b>수사 메모</b><br>{q['memo']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### 다음 중 가장 안전한 대응을 고르세요.")
    selected = st.session_state.answers.get(idx)

    if selected is None:
        for i, choice in enumerate(q["choices"]):
            if st.button(f"{chr(65+i)}. {choice}", key=f"choice_{idx}_{i}", use_container_width=True):
                st.session_state.answers[idx] = i
                st.rerun()
    else:
        correct = selected == q["answer"]
        for i, choice in enumerate(q["choices"]):
            st.button(f"{chr(65+i)}. {choice}", key=f"locked_{idx}_{i}", disabled=True, use_container_width=True)

        st.markdown("#### 사건 분석")
        if correct:
            st.markdown(f'<div class="analysis-good"><b>판정: 적절한 대응</b><br>{q["analysis"]}</div>', unsafe_allow_html=True)
        else:
            best = q["choices"][q["answer"]]
            st.markdown(f'<div class="analysis-bad"><b>판정: 추가 검토 필요</b><br>가장 안전한 대응은 <b>{best}</b>입니다.<br>{q["analysis"]}</div>', unsafe_allow_html=True)

        c1, c2 = st.columns([3, 1.3])
        with c1:
            next_label = "최종 수사 보고서 보기" if idx == len(QUESTIONS) - 1 else "다음 기록 보기"
            if st.button(next_label, type="primary", use_container_width=True):
                if idx == len(QUESTIONS) - 1:
                    st.session_state.screen = "result"
                else:
                    st.session_state.current += 1
                st.rerun()
        with c2:
            if st.button("처음으로", type="secondary", use_container_width=True):
                reset_app()
                st.rerun()

else:
    correct_count = sum(1 for i, q in enumerate(QUESTIONS) if st.session_state.answers.get(i) == q["answer"])
    score = round(correct_count / len(QUESTIONS) * 100)
    grade_code, grade_name, grade_desc = get_grade(score)
    weak = weak_tag()

    st.markdown(
        """
        <div class="report-card">
            <div class="stamp">FINAL INVESTIGATION REPORT</div>
            <div class="section-title" style="font-size:2rem; margin-bottom:4px;">최종 수사 보고서</div>
            <div class="section-text">응답 기록을 바탕으로 당신의 금융사기 대응 성향을 정리했습니다.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    x, y, z = st.columns(3)
    with x:
        st.markdown(f'<div class="grade-box"><div class="small-label">최종 점수</div><div class="grade-code">{score}</div><div class="grade-name">/ 100</div></div>', unsafe_allow_html=True)
    with y:
        st.markdown(f'<div class="grade-box"><div class="small-label">등급</div><div class="grade-code">{grade_code}</div><div class="grade-name">{grade_name}</div></div>', unsafe_allow_html=True)
    with z:
        st.markdown(f'<div class="grade-box"><div class="small-label">취약 유형</div><div class="grade-name" style="margin-top:18px;">{weak}</div></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="paper-card" style="margin-top:14px;">
        <div class="section-title">평가 소견</div>
        <div class="section-text">{grade_desc}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("사건별 판정 기록 보기", expanded=True):
        for i, q in enumerate(QUESTIONS):
            ok = st.session_state.answers.get(i) == q["answer"]
            status = "적절한 대응" if ok else "추가 검토 필요"
            st.markdown(
                f"""
                <div class="summary-item">
                    <b>CASE FILE {q['case_no']} · {q['title']}</b><br>
                    판정: {status}<br>
                    안전한 대응: {q['choices'][q['answer']]}<br>
                    <span style="color:#6e5a43;">{q['analysis']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="paper-card" style="margin-top:14px;">
            <div class="section-title">실제 피해가 의심된다면</div>
            <div class="section-text">
                1) 즉시 거래 금융회사 또는 112에 신고하기<br>
                2) 지급정지 가능 여부 문의하기<br>
                3) 문자·통화·이체 기록을 삭제하지 말고 보관하기<br>
                4) 의심 앱을 설치했다면 기기 점검 및 기관 안내 따르기
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    share_text = (
        f"금융사기 수사대 결과\n"
        f"점수: {score}점 ({correct_count}/8)\n"
        f"등급: {grade_name} ({grade_code})\n"
        f"취약 유형: {weak}"
    )
    st.code(share_text, language=None)

    c1, c2 = st.columns([2, 1])
    with c1:
        if st.button("다시 조사하기", type="primary", use_container_width=True):
            reset_app()
            st.rerun()
    with c2:
        st.button("기록 보존 완료", disabled=True, use_container_width=True)

st.markdown('<div class="closing-note">ⓘ 금융소비자 교육용 개인 프로젝트 · 빅토리안 추리소설풍 클래식 탐정 콘셉트</div>', unsafe_allow_html=True)

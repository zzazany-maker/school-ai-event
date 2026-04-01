import streamlit as st
from datetime import datetime # 시간을 다루는 도구 추가

st.set_page_config(page_title="AI 거짓말 탐정", layout="centered")

start_time = datetime(2026, 4, 1, 11, 0) 
current_time = datetime.now()

if "admin_mode" not in st.session_state:
    st.session_state.admin_mode = False

# 2. 현재 시간이 시작 시간보다 이전이라면 잠금 화면 표시
if current_time < start_time and not st.session_state.admin_mode:
    st.warning("🕵️ 탐정 사무소 오픈 준비 중...")
    st.title("🔍 AI 거짓말 탐정 사무소")
    
    # 관리자 접속을 위한 비밀 입력창 (아주 작게 아래쪽에)
    admin_pw = st.text_input("감지 중... (관리자 인증)", type="password")
    if admin_pw == "1430": # 👈 여기에 간장이가 쓸 비밀번호를 정해!
        st.session_state.admin_mode = True
        st.success("관리자 인증 성공! 접속을 시작합니다.")
        st.rerun()
    
    # 남은 시간 계산해서 보여주기
    remaining = start_time - current_time
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    st.error(f"현재 사건을 정밀 감지 중입니다... 🔍")
    st.info(f"📅 **행사 시작까지:** {remaining.days}일 {hours}시간 {minutes}분 남았습니다.")
    st.write("내일 정해진 시간에 QR코드를 다시 스캔해 주세요!")
    
    # 아래쪽 코드가 실행되지 않도록 여기서 멈춤
    st.stop()

# 1. 페이지 설정
st.set_page_config(page_title="AI 거짓말 탐정", layout="centered")

# 2. 도서 데이터 (6권 모두 넣었어!)
books = {
    "채식주의자": {
        "summary": "육식을 거부하며 식물이 되기를 꿈꾸는 '영혜'와 그녀를 둘러싼 가족들의 폭력적인 시선을 다룬다. 영혜는 인간의 고통에서 벗어나기 위해 스스로 꽃이 되어 땅에 뿌리를 내리려 한다.",
        "image": "https://image.yes24.com/goods/108422348/XL",
        "fake_info": "꽃",
        "real_keywords": ["나무","나무가 되려 함"],
        "hint": "영혜가 되고 싶어 한 건 예쁜 '일부분'이 아니라, 거꾸로 서서 하늘로 뻗어 나가는 '전체'입니다."
    },
    "소년이 온다": {
        "summary": "1980년 5월 광주를 배경으로 합니다. 중학생 '동호'는 친구 정대를 찾기 위해 상무관에서 시신들을 관리하는 일을 돕게 되며, 결국 집으로 무사히 돌아가 가족과 재회합니다.",
        "image": "https://image.yes24.com/goods/13137546/XL",
        "fake_info": ["재회", "무사히", "돌아가"],
        "real_keywords": ["죽음", "희생", "총격", "못 돌아옴"],
        "hint": "주인공 동호의 비극적인 결말을 떠올려 보세요."
    },
    "작별하지 않는다": {
        "summary": "제주 4.3 사건의 비극을 세 여성의 시선으로 연결하며, 학살의 상처를 눈(雪)과 빛의 이미지로 형상화했다. 주인공 '경하'는 친구 '인선'의 부탁을 받고 제주도 집으로 내려가, 홀로 남겨진 고양이 '아미'를 살리기 위해 폭설 속에서 사투를 벌인다.",
        "image": "https://image.yes24.com/goods/103495056/XL",
        "fake_info": "고양이",
        "real_keywords": ["새", "앵무새", "루미"],
        "hint": "인선이 집에서 간절히 살리려고 했던 동물의 종류는?"
    },
    "사피엔스": {
        "summary": "인류의 역사를 다룬 책입니다. 저자 유발 하라리는 인류가 지구의 지배자가 된 결정적인 이유가 농경 사회의 시작으로 인한 '산업 혁명' 덕분이라고 설명합니다.",
        "image": "https://image.yes24.com/goods/23030284/XL",
        "fake_info": "산업 혁명",
        "real_keywords": ["인지혁명", "인지 혁명", "뒷담화", "허구"],
        "hint": "사피엔스가 협력할 수 있게 만든 첫 번째 '혁명'의 이름은?"
    },
    "분자 조각가들": {
        "summary": "화학자들이 어떻게 새로운 분자를 설계하고 만드는지 설명합니다. 특히 저자는 연금술사들이 금을 만들려다 실패한 과정이 현대의 '물리학' 발전에만 기여했다고 주장합니다.",
        "image": "https://image.yes24.com/goods/118270366/XL",
        "fake_info": "물리학",
        "real_keywords": ["화학", "유기화학"],
        "hint": "연금술은 어떤 학문의 뿌리가 되었을까요?"
    },
    "혼모노": {
        "summary": "신기가 떨어져 가는 무당 '재화'가 영험한 신애기를 시기하며 벌어지는 무속 세계의 이야기다. 재화는 자신이 모시는 장수할아범이 떠나갈까 봐 전전긍긍하며 '진짜'가 무엇인지에 대해 끊임없이 고뇌한다.",
        "image": "https://image.yes24.com/goods/152110464/XL",
        "fake_info": "장수할아범",
        "real_keywords": ["신령", "장수할멈","할멈"],
        "hint": "무속 신앙에서 무당이 모시는 존재를 부르는 전형적인 명칭이 따로 있습니다."
    }
}

st.title("🔍 AI의 거짓말을 찾아라!")

# 3. 가이드 (접어두기)
if "stage" not in st.session_state:
    st.session_state.stage = "guide" # [2단계] 가이드 우선 노출 세팅
if "selected_book" not in st.session_state:
    st.session_state.selected_book = None

if st.session_state.stage == "guide":
    st.title("🕵️ 탐정 수사 가이드")
    st.info("""
    **사건 개요:** 도서관 AI가 책 내용을 교묘하게 조작했습니다!
    1. 아래 [확인] 버튼을 눌러 사건 현장(도서 목록)에 진입하세요.
    2. 표지를 클릭해 수사할 책을 선택합니다.
    3. 요약문 속 가짜 정보를 찾아 진짜 정답으로 교체하세요.
    """)
    if st.button("✅ 지침을 확인했습니다. 수사 시작!"):
        st.session_state.stage = "select"
        st.rerun()

elif st.session_state.stage == "select":
    st.title("📚 수사할 사건을 선택하세요")
    st.write("표지 아래의 버튼을 눌러 수사를 시작합니다.")
    
    # 1. 사진 높이 통일 스타일 (반드시 표지를 그리기 전에 배치)
    st.markdown("""
        <style>
        div[data-testid="stImage"] img {
            height: 500px !important; /* 모든 표지 높이를 300px로 강제 통일 */
            object-fit: contain !important; /* 비율 유지 */
            background-color: #f9f9f9; /* 여백 배경색 */
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 2. 2열 레이아웃으로 도서 목록 출력
    cols = st.columns(2) 
    for idx, (title, info) in enumerate(books.items()):
        with cols[idx % 2]:
            # 이미지 출력
            if "image" in info:
                st.image(info['image'], use_container_width=True)
            
            # 수사하기 버튼 (이미지 바로 아래에 위치)
            if st.button(f"🔎 {title} 수사", key=f"btn_{title}"):
                st.session_state.selected_book = title
                st.session_state.stage = "solve"
                st.rerun()

# --- [4단계] 실제 문제 풀이 페이지 ---
elif st.session_state.stage == "solve":
    book_title = st.session_state.selected_book
    data = books[book_title]
    
    if st.button("⬅️ 다른 사건 보기"):
        st.session_state.stage = "select"
        st.rerun()

    st.title(f"🕵️ 수사 중: {book_title}")
    st.image(data['image'], width=200)
    st.info(f"**AI 요약본**\n\n{data['summary']}")

    # 입력창 (책마다 고유 key 부여하여 에러 방지)
    user_fake = st.text_input("가짜 정보", key=f"fake_{book_title}")
    user_real = st.text_input("진짜 정답", key=f"real_{book_title}")
    user_name = st.text_input("학번과 이름", key="user_name")

    if st.button("🚨 보고서 제출 (판독)"):
        if not user_fake or not user_real or not user_name:
            st.warning("모든 칸을 채워야 응모가 가능해!")
        else:
            # 판독 로직
            clean_user_fake = user_fake.replace(" ", "").lower()
            clean_user_real = user_real.replace(" ", "").lower()
            
            fake_data = data['fake_info']
            fake_list = [fake_data] if isinstance(fake_data, str) else fake_data
            
            is_fake_correct = any(f.replace(" ", "").lower() in clean_user_fake for f in fake_list)
            is_real_correct = any(k.replace(" ", "").lower() in clean_user_real for k in data['real_keywords'])
            
            if is_fake_correct and is_real_correct:
                st.success(f"🎊 완벽해, {user_name} 탐정!")
                st.balloons()
                # Tally 연동
                tally_url = "https://tally.so/embed/zxJXoM?hideTitle=1&transparentBackground=1&dynamicHeight=1"
                st.components.v1.html(f'<iframe src="{tally_url}" width="100%" height="500" frameborder="0"></iframe>', height=550)
            else:
                st.error("앗! 틀린 부분이 있는 것 같아.")
                st.info(f"💡 힌트: {data['hint']}")

    if st.button("🔄 처음으로 돌아가기"):
        st.session_state.stage = "guide"
        st.rerun()

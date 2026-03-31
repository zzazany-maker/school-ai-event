import streamlit as st

st.set_page_config(page_title="AI 거짓말 탐정", layout="centered")

books = {
    "채식주의자": {
        "summary": "육식을 거부하며 식물이 되기를 꿈꾸는 '영혜'와 그녀를 둘러싼 가족들의 폭력적인 시선을 다룹니다. 영혜는 인간의 고통에서 벗어나기 위해 스스로 꽃이 되어 땅에 뿌리를 내리려 합니다.",
        "fake_info": "꽃",
        "real_keywords": ["나무","나무가 되려 함"],
        "hint": "영혜가 되고 싶어 한 건 예쁜 '일부분'이 아니라, 거꾸로 서서 하늘로 뻗어 나가는 '전체'입니다."
    },
    "소년이 온다": {
        "summary": "1980년 5월 광주를 배경으로 합니다. 중학생 '동호'는 친구 정대를 찾기 위해 상무관에서 시신들을 관리하는 일을 돕게 되며, 결국 집으로 무사히 돌아가 가족과 재회합니다.",
        "fake_info": ["재회", "무사히", "돌아가"],
        "real_keywords": ["죽음", "희생", "총격", "못 돌아옴"],
        "hint": "주인공 동호의 비극적인 결말을 떠올려 보세요."
    },
    "작별하지 않는다": {
        "summary": "제주 4.3 사건의 비극을 세 여성의 시선으로 연결하며, 학살의 상처를 눈(雪)과 빛의 이미지로 형상화했습니다. 주인공 '경하'는 친구 '인선'의 부탁을 받고 제주도 집으로 내려가, 홀로 남겨진 고양이 '아미'를 살리기 위해 폭설 속에서 사투를 벌입니다.",
        "fake_info": "고양이",
        "real_keywords": ["새", "앵무새", "루미"],
        "hint": "인선이 집에서 간절히 살리려고 했던 동물의 종류는?"
    },
    "사피엔스": {
        "summary": "인류의 역사를 다룬 책입니다. 저자 유발 하라리는 인류가 지구의 지배자가 된 결정적인 이유가 농경 사회의 시작으로 인한 '산업 혁명' 덕분이라고 설명합니다.",
        "fake_info": "산업 혁명",
        "real_keywords": ["인지혁명", "인지 혁명", "뒷담화", "허구"],
        "hint": "사피엔스가 협력할 수 있게 만든 첫 번째 '혁명'의 이름은?"
    },
    "분자 조각가들": {
        "summary": "화학자들이 어떻게 새로운 분자를 설계하고 만드는지 설명합니다. 특히 저자는 연금술사들이 금을 만들려다 실패한 과정이 현대의 '물리학' 발전에만 기여했다고 주장합니다.",
        "fake_info": "물리학",
        "real_keywords": ["화학", "유기화학"],
        "hint": "연금술은 어떤 학문의 뿌리가 되었을까요?"
    },
    "혼모노": {
        "summary": "신기가 떨어져 가는 무당 '재화'가 영험한 신애기를 시기하며 벌어지는 무속 세계의 이야기입니다. 재화는 자신이 모시는 장수할아범이 떠나갈까 봐 전전긍긍하며 '진짜'가 무엇인지에 대해 끊임없이 고뇌합니다.",
        "fake_info": "장수할아범",
        "real_keywords": ["신령", "장수할멈","할멈"],
        "hint": "무속 신앙에서 무당이 모시는 존재를 부르는 전형적인 명칭이 따로 있습니다."
    }
}

st.title("🔍 AI의 거짓말을 찾아라!")

with st.expander("🕵️ 탐정 수사 가이드"):
    st.write("요약문에서 틀린 부분(가짜 정보)을 찾고, 오른쪽에 진짜 정답 키워드를 적어주세요!")

selection = st.selectbox("분석할 도서를 선택하세요 👇", list(books.keys()), key="book_select")
data = books[selection]

st.info(f"**[{selection}] AI 요약본**\n\n{data['summary']}")

st.subheader("🕵️ 탐정의 노트")
col1, col_arrow, col2 = st.columns([4, 1, 4])

with col1:
    user_fake = st.text_input("가짜 정보", key=f"user_fake_{selection}")

with col_arrow:
    st.write("## ➡️")

with col2:
    user_real = st.text_input("진짜 정답", key=f"user_real_{selection}")

user_name = st.text_input("학번과 이름을 입력하세요", key="user_name_input")

if st.button("🚨 판독 및 응모"):
    if not user_fake or not user_real or not user_name:
        st.warning("모든 칸을 채워야 응모가 가능해!")
    else:
        
        clean_user_fake = user_fake.replace(" ", "").lower()
        clean_user_real = user_real.replace(" ", "").lower()
        
        fake_data = data['fake_info']
        if isinstance(fake_data, str):
            fake_list = [fake_data]
        else:
            fake_list = fake_data
            
        is_fake_correct = any(f.replace(" ", "").lower() in clean_user_fake for f in fake_list)
        
        is_real_correct = any(k.replace(" ", "").lower() in clean_user_real for k in data['real_keywords'])
        
        if is_fake_correct and is_real_correct:
            st.success(f"🎊 완벽해, {user_name} 탐정!")
            st.balloons()
            
            tally_url = "https://tally.so/embed/zxJXoM?hideTitle=1&transparentBackground=1&dynamicHeight=1"
            st.components.v1.html(f'<iframe src="{tally_url}" width="100%" height="500" frameborder="0"></iframe>', height=550)
        else:
            st.error("앗! 틀린 부분이 있는 것 같아. 다시 한 번 확인해봐!")
            st.info(f"💡 힌트: {data['hint']}")

if st.button("🔄 다시 하기"):
    
    for k in ["user_fake_input", "user_real_input", "user_name_input"]:
        if k in st.session_state:
            del st.session_state[k]
    st.rerun()

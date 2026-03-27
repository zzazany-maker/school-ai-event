import streamlit as st

st.set_page_config(page_title="도서관 AI 거짓말 탐정", page_icon="🕵️")
st.title("🕵️ AI의 교묘한 거짓말을 찾아라!")
st.write("AI가 쓴 요약문에는 **등장인물 이름, 사건, 결말** 중 하나가 살짝 바뀌어 있습니다.")

# 📚 행사용 도서 데이터베이스 (간장이가 여기서 계속 추가/수정하면 돼)
books = {
    "불편한 편의점": {
        "summary": "청파동 골목의 편의점 'Always'에서 야간 알바를 시작한 '독고'. 그는 과거에 잘나가던 의사였으나 기억을 잃고 노숙자가 된 인물입니다. 편의점 사장인 '영숙 씨'는 그를 따뜻하게 맞이해줍니다.",
        "fake_info": "영숙 씨", # 실제 사장님 성함은 '염영숙'이나 보통 '염 여사'로 불림. (성씨를 살짝 비틈)
        "hint": "사장님의 성함이 정확히 무엇인지 책의 앞부분을 확인해보세요!",
        "correct_ans": "염영숙"
    },
    "달러구트 꿈 백화점": {
        "summary": "주인공 페니는 꿈을 만드는 제작자 '달러구트'의 면접에 합격해 입사합니다. 백화점 1층에서는 가장 인기 있는 '비싼 꿈'을 팔며, 손님들은 꿈의 값으로 자신의 '기쁨'을 지불합니다.",
        "fake_info": "기쁨", # 실제로는 '설렘', '호기심' 등 감정을 지불함.
        "hint": "손님들이 지불하는 액체 형태의 '감정'이 무엇이었나요?",
        "correct_ans": "설렘"
    },
    "아몬드": {
        "summary": "감정을 느끼지 못하는 소년 '윤재'와 거친 성격의 '곤이'의 우정을 다룹니다. 윤재의 엄마와 할머니는 크리스마스 이브에 일어난 비극적인 사고로 돌아가시게 됩니다.",
        "fake_info": "엄마와 할머니는", # 실제로는 할머니만 돌아가시고 엄마는 식물인간 상태가 됨.
        "hint": "사고 이후 병원에 계속 누워 계셨던 분은 누구일까요?"
    }
}

# 화면 구현 부분
selection = st.selectbox("확인할 도서를 선택하세요 👇", list(books.keys()))
data = books[selection]

st.divider()
st.info(f"**[{selection}] AI 요약본**\n\n{data['summary']}")

ans = st.text_input("위 문장에서 '가짜 정보'를 찾아 한 단어나 짧은 문구로 적어주세요.")
name = st.text_input("이벤트 응모를 위해 [학번 성함]을 입력하세요.")

if st.button("정답 확인 및 응모하기"):
    if name.strip() == "":
        st.warning("이름을 입력해야 응모가 가능해!")
    elif data['fake_info'] in ans:
        st.success(f"🎯 정답이야, {name.split()[-1]} 탐정! 응모가 완료되었어.")
        st.balloons()
    else:
        st.error("앗, 속아버렸네! 다시 한번 꼼꼼히 읽어볼까?")
        st.caption(f"💡 힌트: {data['hint']}")
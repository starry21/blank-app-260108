import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from datetime import datetime

# Streamlit 학습용 데모 페이지
# 아래 예시는 "한 페이지"에 넣을 수 있는 주요 요소들을 모아놓은 샘플입니다.
# 각 블록 위에 간단한 주석을 달아 공부에 도움이 되도록 했습니다.

st.set_page_config(page_title="Streamlit 요소 모음", layout="wide")

st.title("📚 Streamlit 요소 예제 모음")
st.caption("이 페이지는 Streamlit의 주요 위젯, 레이아웃, 미디어, 차트, 상태 관리 등을 한데 모아 보여줍니다.")

# ---------------------------------------------
# 텍스트와 마크다운
# ---------------------------------------------
st.header("텍스트 & 마크다운")
st.write("일반 텍스트 출력: st.write()는 다양한 타입을 알아서 포맷합니다.")
st.markdown("**Markdown 강조**: `st.markdown()` 으로 마크다운을 렌더링합니다.")
st.latex(r"E = mc^2")  # 수식 렌더링 예시
st.caption("위 코드는 수식 렌더링 예시입니다. 라텍스 문법을 사용합니다.")

# 코드 블록을 보여주는 방법
code_example = '''import streamlit as st
st.write("Hello Streamlit")
'''
st.code(code_example, language='python')  # 코드 하이라이팅

# ---------------------------------------------
# 입력 위젯 예시
# ---------------------------------------------
st.header("입력 위젯")
with st.expander("입력 폼(기본 위젯들)"):
    # 간단한 입력 위젯 모음
    name = st.text_input("이름 입력", value="홍길동")  # 한 줄 텍스트 입력
    bio = st.text_area("간단 소개", value="Streamlit을 공부중입니다.")  # 여러 줄 입력
    age = st.number_input("나이", min_value=0, max_value=150, value=30)  # 숫자 입력
    date = st.date_input("오늘 날짜", value=datetime.today())  # 날짜 입력
    time = st.time_input("시간 선택", value=datetime.now().time())  # 시간 입력

    # 선택형 위젯들
    option = st.selectbox("옵션 선택", ["옵션 A", "옵션 B", "옵션 C"])  # 단일 선택
    multi = st.multiselect("다중 선택", ["사과", "바나나", "체리"], default=["사과"])  # 다중 선택
    agree = st.checkbox("약관 동의")  # 체크박스
    radio = st.radio("라디오 버튼", ("오전", "오후", "저녁"))
    rating = st.slider("만족도", 0.0, 5.0, 3.5)  # 슬라이더 (float)

    # 버튼과 폼
    if st.button("인사하기"):
        st.success(f"안녕하세요, {name}님!")

    with st.form(key='my_form'):
        f_name = st.text_input('폼 - 이름')
        f_submit = st.form_submit_button('폼 제출')
        if f_submit:
            st.info(f'폼 제출: {f_name}')

    # 주석: 위의 각 위젯은 사용자가 상호작용할 수 있고, 해당 변수에 값이 저장됩니다.

# ---------------------------------------------
# 파일 업로드 및 미디어
# ---------------------------------------------
st.header("미디어 & 파일 업로드")
uploaded = st.file_uploader("파일 업로드 (이미지, CSV 등)")
if uploaded is not None:
    # 파일의 종류에 따라 처리할 수 있습니다. 예: CSV -> dataframe
    try:
        df_uploaded = pd.read_csv(uploaded)
        st.write("업로드한 CSV 미리보기:")
        st.dataframe(df_uploaded.head())
    except Exception:
        st.write("이미지나 기타 파일이 업로드되었습니다.")

img = st.file_uploader("이미지 업로드 (이미지 파일만 테스트)", type=["png", "jpg", "jpeg"])
if img:
    st.image(img, caption="업로드된 이미지", use_column_width=True)

st.camera_input("카메라 입력 (브라우저에서 허용 필요)")
st.audio(None)  # 빈 플레이어를 보여주는 예시 (실제로는 파일 제공)
st.video(None)

# ---------------------------------------------
# 데이터프레임 및 테이블
# ---------------------------------------------
st.header("데이터와 차트")
@st.cache_data
def make_sample_df(n=50):
    # 캐시된 함수: 동일 입력이면 결과 재사용 (성능 개선)
    x = np.linspace(0, 10, n)
    df = pd.DataFrame({
        'x': x,
        'sin': np.sin(x),
        'cos': np.cos(x),
        'random': np.random.randn(n)
    })
    return df

df = make_sample_df()
st.dataframe(df)  # 인터랙티브한 데이터프레임 뷰어
st.table(df.head())  # 고정된 표
st.json({'example': True, 'values': [1, 2, 3]})

# 차트: 간단한 내장 차트
st.subheader("내장 차트 (line/area/bar)")
st.line_chart(df[['x', 'sin']].set_index('x'))
st.area_chart(df[['x', 'cos']].set_index('x'))
st.bar_chart(df[['random']])

# 차트: Altair 예시
st.subheader("Altair 차트 예시")
chart = alt.Chart(df).mark_line().encode(x='x', y='sin')
st.altair_chart(chart, use_container_width=True)

# Matplotlib 예시
fig, ax = plt.subplots()
ax.plot(df['x'], df['sin'], label='sin')
ax.plot(df['x'], df['cos'], label='cos')
ax.legend()
st.pyplot(fig)

# ---------------------------------------------
# 레이아웃: 컬럼, 익스팬더, 사이드바
# ---------------------------------------------
st.header("레이아웃 & 컨테이너")
col1, col2, col3 = st.columns([1, 2, 1])  # 가변 너비 컬럼
with col1:
    st.metric("온도", "21°C", "+2°C")  # KPI 표시
with col2:
    st.info("중앙 컬럼: 주요 콘텐츠 영역")
    with st.expander("추가 정보 (Expander)"):
        st.write("숨겨진 설명을 여기에 적습니다.")
with col3:
    st.warning("오른쪽 사이드바 느낌")

st.sidebar.header("사이드바 예시")
sb_choice = st.sidebar.selectbox("사이드바 선택", ["A", "B", "C"])
st.sidebar.write("선택:", sb_choice)

# ---------------------------------------------
# 인터랙티브 상태와 캐시 예시
# ---------------------------------------------
st.header("상태 관리 & 캐시")
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('증가'):
    st.session_state.count += 1
st.write('현재 카운트:', st.session_state.count)

@st.cache_data
def expensive_computation(x):
    # 실제 무거운 작업 대신 sleep을 쓰지 않습니다. 복잡한 연산을 가정.
    return x * x

result = expensive_computation(10)
st.write('캐시된 계산 결과 예시:', result)

# ---------------------------------------------
# 상태 메시지와 알림
# ---------------------------------------------
st.header("알림 & 진행 상태")
with st.spinner('처리중...'):
    pass
st.success('성공 메시지 예시')
st.info('정보 메시지 예시')
st.warning('경고 메시지 예시')
st.error('오류 메시지 예시')

# ---------------------------------------------
# 마무리 안내
# ---------------------------------------------
st.markdown("---")
st.write("이 페이지는 학습용 예시입니다. 각 위젯 옆의 코드를 참고해 직접 수정해보세요.")
st.caption("원하시면 이 파일을 더 확장하거나, 특정 위젯의 심화 예제를 추가해 드립니다.")


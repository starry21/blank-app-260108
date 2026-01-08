import streamlit as st  # Streamlit 라이브러리를 임포트합니다. 웹 앱을 만들기 위한 주요 도구입니다.
import pandas as pd  # 데이터프레임을 다루기 위한 pandas 라이브러리
import numpy as np  # 수학적 계산을 위한 numpy 라이브러리
import altair as alt  # Altair 차트 라이브러리
import matplotlib.pyplot as plt  # Matplotlib 차트 라이브러리
from datetime import datetime  # 날짜와 시간을 다루기 위한 datetime 모듈

# 페이지 설정: 앱의 제목과 레이아웃을 설정합니다.
st.set_page_config(page_title="Streamlit 요소 학습 페이지", layout="wide")

# 메인 제목: 페이지의 주요 제목을 표시합니다.
st.title("📚 Streamlit 단일 페이지 요소 모음")

# 부제목: 페이지 설명을 추가합니다.
st.caption("이 페이지는 Streamlit의 모든 주요 요소를 한 페이지에 모아 보여줍니다. 각 요소에 주석을 달아 학습에 도움이 되도록 했습니다.")

# 섹션 1: 텍스트 출력 요소들
st.header("1. 텍스트 출력 요소들")

# st.write: 다양한 타입의 데이터를 자동으로 포맷하여 출력합니다.
st.write("st.write()는 텍스트, 숫자, 리스트 등 다양한 데이터를 출력할 수 있습니다.")

# st.text: 일반 텍스트를 출력합니다. 마크다운을 지원하지 않습니다.
st.text("st.text()는 일반 텍스트를 출력합니다. 마크다운이 적용되지 않습니다.")

# st.markdown: 마크다운 문법을 사용하여 텍스트를 포맷합니다.
st.markdown("**st.markdown()**은 *마크다운* 문법을 지원합니다. `코드`도 가능합니다.")

# st.title: 큰 제목을 표시합니다.
st.title("st.title() 예시")

# st.header: 중간 크기의 제목을 표시합니다.
st.header("st.header() 예시")

# st.subheader: 작은 제목을 표시합니다.
st.subheader("st.subheader() 예시")

# st.caption: 작은 캡션 텍스트를 표시합니다.
st.caption("st.caption()은 작은 설명 텍스트를 표시합니다.")

# st.latex: LaTeX 수식을 렌더링합니다.
st.latex(r"E = mc^2")  # 아인슈타인의 질량-에너지 등가 공식

# st.code: 코드 블록을 하이라이팅하여 표시합니다.
code_example = '''
def hello():
    print("Hello, Streamlit!")
'''
st.code(code_example, language='python')

# 섹션 2: 입력 위젯 요소들
st.header("2. 입력 위젯 요소들")

# st.text_input: 한 줄 텍스트 입력 필드를 만듭니다.
name = st.text_input("이름을 입력하세요", value="홍길동")  # 기본값 설정 가능

# st.text_area: 여러 줄 텍스트 입력 필드를 만듭니다.
bio = st.text_area("자기소개를 입력하세요", value="Streamlit을 배우고 있습니다.")

# st.number_input: 숫자 입력 필드를 만듭니다.
age = st.number_input("나이를 입력하세요", min_value=0, max_value=150, value=25)

# st.slider: 슬라이더를 사용하여 값을 선택합니다.
rating = st.slider("만족도를 선택하세요", 0.0, 5.0, 3.5)

# st.selectbox: 드롭다운 메뉴에서 단일 옵션을 선택합니다.
option = st.selectbox("옵션을 선택하세요", ["옵션 A", "옵션 B", "옵션 C"])

# st.multiselect: 여러 옵션을 선택할 수 있습니다.
multi_options = st.multiselect("여러 옵션을 선택하세요", ["사과", "바나나", "체리"], default=["사과"])

# st.radio: 라디오 버튼 그룹을 만듭니다.
radio_choice = st.radio("시간대를 선택하세요", ("오전", "오후", "저녁"))

# st.checkbox: 체크박스를 만듭니다.
agree = st.checkbox("약관에 동의합니다")

# st.button: 버튼을 만들고 클릭 이벤트를 처리합니다.
if st.button("클릭하세요"):
    st.success("버튼이 클릭되었습니다!")

# st.form: 여러 입력을 그룹화하여 폼으로 만듭니다.
with st.form("my_form"):
    form_name = st.text_input("폼 이름")
    form_age = st.number_input("폼 나이", min_value=0)
    submitted = st.form_submit_button("제출")
    if submitted:
        st.info(f"제출됨: {form_name}, {form_age}세")

# st.date_input: 날짜를 선택합니다.
selected_date = st.date_input("날짜를 선택하세요", value=datetime.today())

# st.time_input: 시간을 선택합니다.
selected_time = st.time_input("시간을 선택하세요", value=datetime.now().time())

# st.file_uploader: 파일을 업로드합니다.
uploaded_file = st.file_uploader("파일을 업로드하세요")

# 섹션 3: 데이터 표시 요소들
st.header("3. 데이터 표시 요소들")

# 샘플 데이터프레임 생성
sample_df = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, 35],
    '점수': [85, 90, 95]
})

# st.dataframe: 인터랙티브한 데이터프레임을 표시합니다.
st.dataframe(sample_df)

# st.table: 정적인 테이블을 표시합니다.
st.table(sample_df)

# st.json: JSON 데이터를 표시합니다.
sample_json = {"이름": "Alice", "나이": 25, "점수": 85}
st.json(sample_json)

# st.metric: 메트릭(지표)을 표시합니다.
st.metric("온도", "21°C", "+2°C")

# 섹션 4: 차트 요소들
st.header("4. 차트 요소들")

# 샘플 차트 데이터
chart_data = pd.DataFrame({
    'x': np.linspace(0, 10, 50),
    'y1': np.sin(np.linspace(0, 10, 50)),
    'y2': np.cos(np.linspace(0, 10, 50))
})

# st.line_chart: 선 차트를 표시합니다.
st.line_chart(chart_data.set_index('x'))

# st.area_chart: 영역 차트를 표시합니다.
st.area_chart(chart_data.set_index('x'))

# st.bar_chart: 막대 차트를 표시합니다.
bar_data = pd.DataFrame({'카테고리': ['A', 'B', 'C'], '값': [10, 20, 30]})
st.bar_chart(bar_data.set_index('카테고리'))

# st.altair_chart: Altair 차트를 표시합니다.
altair_chart = alt.Chart(chart_data).mark_line().encode(x='x', y='y1')
st.altair_chart(altair_chart, use_container_width=True)

# st.pyplot: Matplotlib 차트를 표시합니다.
fig, ax = plt.subplots()
ax.plot(chart_data['x'], chart_data['y1'], label='sin')
ax.plot(chart_data['x'], chart_data['y2'], label='cos')
ax.legend()
st.pyplot(fig)

# 섹션 5: 레이아웃 요소들
st.header("5. 레이아웃 요소들")

# st.columns: 페이지를 여러 열로 나눕니다.
col1, col2, col3 = st.columns(3)
with col1:
    st.write("첫 번째 열")
with col2:
    st.write("두 번째 열")
with col3:
    st.write("세 번째 열")

# st.expander: 접을 수 있는 섹션을 만듭니다.
with st.expander("더 많은 정보 보기"):
    st.write("여기에 추가 정보를 넣을 수 있습니다.")

# st.container: 컨테이너를 만들어 요소를 그룹화합니다.
with st.container():
    st.write("컨테이너 안의 내용")
    st.button("컨테이너 안 버튼")

# st.sidebar: 사이드바를 만듭니다.
sidebar_option = st.sidebar.selectbox("사이드바 옵션", ["옵션 1", "옵션 2"])
st.sidebar.write(f"선택된 옵션: {sidebar_option}")

# 섹션 6: 미디어 요소들
st.header("6. 미디어 요소들")

# st.image: 이미지를 표시합니다.
# 실제로는 이미지 파일 경로나 URL을 사용합니다.
st.image("https://via.placeholder.com/300", caption="샘플 이미지")

# st.audio: 오디오 파일을 재생합니다.
# 실제로는 오디오 파일을 제공해야 합니다.
# st.audio("sample_audio.mp3")

# st.video: 비디오 파일을 재생합니다.
# 실제로는 비디오 파일을 제공해야 합니다.
# st.video("sample_video.mp4")

# st.camera_input: 카메라 입력을 받습니다.
camera_image = st.camera_input("카메라로 사진 찍기")

# 섹션 7: 상태 및 기타 요소들
st.header("7. 상태 및 기타 요소들")

# 세션 상태: 앱의 상태를 유지합니다.
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("카운터 증가"):
    st.session_state.counter += 1
st.write(f"카운터 값: {st.session_state.counter}")

# 캐시: 계산 결과를 캐시하여 성능을 향상시킵니다.
@st.cache_data
def expensive_calculation(x):
    # 실제로는 무거운 계산을 수행합니다.
    return x ** 2

cached_result = expensive_calculation(10)
st.write(f"캐시된 계산 결과: {cached_result}")

# 진행 상태 표시
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

# 스피너: 작업 중임을 표시합니다.
with st.spinner("작업 중..."):
    # 실제 작업을 수행합니다.
    pass

# 알림 메시지들
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("오류 메시지")

# 빈 요소: 레이아웃을 위한 빈 공간
st.empty()

# 구분선
st.markdown("---")

# 마무리
st.write("이 페이지에는 Streamlit의 주요 요소들이 모두 포함되어 있습니다. 각 요소의 코드를 참고하여 학습하세요!")


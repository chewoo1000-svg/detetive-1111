# 금융사기 수사대 · 클래식 삽화 버전

고풍스럽고 클래식한 탐정 기록실 콘셉트에,
셜록 홈즈 소설 같은 분위기의 삽화형 SVG 그래픽을 더한 Streamlit 웹앱입니다.

## 파일 구성
- `app.py` : 메인 실행 파일
- `questions.py` : 문제 데이터
- `requirements.txt` : 설치 패키지 목록
- `README.md` : 프로젝트 설명

## 실행 방법
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 배포 방법
GitHub 저장소 최상위(root)에 아래 4개 파일만 올리면 됩니다.
- `app.py`
- `questions.py`
- `requirements.txt`
- `README.md`

그 다음 Streamlit Community Cloud에서 **Main file path = `app.py`** 로 설정하세요.

## 특징
- 빅토리안 추리소설풍 무드
- 탐정 실루엣 및 사건기록 삽화 포함
- 브라운/베이지/골드 중심의 문서형 UI
- 금융사기 대응 퀴즈 + 최종 수사 보고서 구성

## 주의
교육용 개인 프로젝트이며, 특정 금융기관의 공식 서비스가 아닙니다.

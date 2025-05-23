# 1단계: 빌드 스테이지
FROM python:3.9-slim-buster as builder

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt를 먼저 복사하여 캐싱 활용
COPY requirements.txt .

# 파이썬 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 2단계: 최종 이미지 스테이지
FROM python:3.9-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

# 빌더 스테이지에서 설치된 의존성 복사
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Gunicorn을 사용하여 Flask 앱 실행
# 0.0.0.0은 모든 네트워크 인터페이스에서 접근 가능하도록 합니다.
# --bind 0.0.0.0:5000은 5000번 포트로 바인딩합니다.
# app:app은 app.py 파일 내의 Flask 애플리케이션 인스턴스 이름이 'app'임을 나타냅니다.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Flask 앱이 리스닝할 포트
EXPOSE 5000
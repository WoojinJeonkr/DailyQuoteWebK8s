# 1단계: 빌드 스테이지
FROM python:3.9-slim-buster as builder

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt를 먼저 복사하여 캐싱 활용
COPY requirements.txt .

# 파이썬 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사 (quote_fetcher.py, app.py 등)
COPY . .

# quote_fetcher.py를 실행하여 quotes.json을 생성 (빌드 시점)
# 이렇게 하면 런타임에 quote_fetcher.py를 다시 실행할 필요가 없습니다.
RUN python quote_fetcher.py

# 2단계: 최종 이미지 스테이지
FROM python:3.9-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

# 빌더 스테이지에서 설치된 의존성 복사
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# /usr/local/bin (gunicorn과 같은 실행 파일) 복사
COPY --from=builder /usr/local/bin /usr/local/bin

# 애플리케이션 코드 복사 (app.py) 및 생성된 quotes.json 복사
# quotes.json도 이 단계에서 복사되어야 합니다.
COPY --from=builder /app/app.py /app/app.py
COPY --from=builder /app/quotes.json /app/quotes.json

# Gunicorn을 사용하여 Flask 앱 실행
# app:app은 app.py 파일 내의 Flask 애플리케이션 인스턴스 이름이 'app'임을 나타냅니다.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Flask 앱이 리스닝할 포트
EXPOSE 5000
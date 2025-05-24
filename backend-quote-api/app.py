from flask import Flask, jsonify
from flask_cors import CORS
import random
import json
import os

# Flask 애플리케이션 인스턴스 초기화
app = Flask(__name__)
CORS(app) # CORS를 활성화하여 모든 도메인에서의 요청을 허용합니다.

# 명언 목록을 저장할 변수
formatted_quotes = []

def load_quotes_from_file(filename="quotes.json"):
    """
    JSON 파일에서 명언 목록을 불러옵니다.
    """
    global formatted_quotes
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                formatted_quotes = json.load(f)
            print(f"'{filename}' 파일에서 {len(formatted_quotes)}개의 명언을 성공적으로 불러왔습니다.")
        except json.JSONDecodeError as e:
            print(f"JSON 디코딩 오류: {e} (파일: {filename}). 파일이 손상되었거나 형식이 잘못되었습니다.")
            formatted_quotes = [] # 오류 발생 시 빈 리스트로 초기화
        except IOError as e:
            print(f"파일을 읽는 중 오류 발생: {e} (파일: {filename})")
            formatted_quotes = [] # 오류 발생 시 빈 리스트로 초기화
    else:
        print(f"경고: '{filename}' 파일을 찾을 수 없습니다. 'quote_fetcher.py'를 먼저 실행하여 파일을 생성하세요.")
        formatted_quotes = [] # 파일이 없으면 빈 리스트로 초기화

# 애플리케이션 시작 시 명언 목록을 미리 불러옵니다.
with app.app_context():
    load_quotes_from_file()

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    헬스 체크 엔드포인트.
    """
    return jsonify({"status": "healthy"}), 200

@app.route("/api/quote", methods=["GET"])
def get_quote():
    """
    미리 정의된 목록에서 무작위 명언을 검색하여 JSON 형식으로 반환합니다.
    """
    if not formatted_quotes:
        return jsonify({"error": "명언을 불러올 수 없습니다. 'quote_fetcher.py'를 실행했는지 확인하세요."}), 500
    
    quote = random.choice(formatted_quotes)
    return jsonify({"quote": quote})

# 어플리케이션 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
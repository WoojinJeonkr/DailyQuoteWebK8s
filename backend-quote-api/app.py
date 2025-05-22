from flask import Flask, jsonify
from flask_cors import CORS
import random
import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_all_quotes(base_url):
    """
    주어진 URL에서 모든 페이지의 명언 데이터를 가져와 합칩니다.
    """
    all_quotes = []
    page = 1
    total_pages = 1 # 초기값, 첫 요청 후 실제 totalPages로 업데이트됩니다.

    print("모든 명언 데이터를 가져오는 중...")

    while page <= total_pages:
        query_params = {
            "maxLength": 150,
            "minLength": 100,
            "sortBy": "dateAdded",
            "order": "asc",
            "limit": 20, # 한 페이지당 20개씩 가져옴
            "page": page
        }

        print(f"현재 {page}/{total_pages} 페이지 데이터를 가져오는 중...")

        try:
            # verify=False 옵션을 추가하여 SSL 인증서 검증을 건너뜁니다.
            response = requests.get(base_url, params=query_params, verify=False)
            response.raise_for_status() # HTTP 오류가 발생하면 예외를 발생시킵니다.
            data = response.json()

            # 첫 페이지 요청 시 totalPages를 업데이트합니다.
            if page == 1:
                total_pages = data.get("totalPages", 1)
                print(f"총 {total_pages} 페이지의 데이터가 있습니다.")

            # 'results' 키가 있는지 확인하고, 명언 데이터를 추가합니다.
            if "results" in data:
                all_quotes.extend(data["results"])
            else:
                print(f"경고: 페이지 {page}에 'results' 키가 없습니다. 데이터가 누락될 수 있습니다.")

            page += 1 # 다음 페이지로 이동
        except requests.exceptions.RequestException as e:
            print(f"오류 발생: {e}")
            break # 오류 발생 시 루프 종료
        except json.JSONDecodeError as e:
            print(f"JSON 디코딩 오류 발생: {e} (페이지: {page})")
            break # 오류 발생 시 루프 종료

    print(f"총 {len(all_quotes)}개의 명언 데이터를 가져왔습니다.")
    return all_quotes

# API 기본 주소
api_base_url = "https://api.quotable.io/quotes"

# 모든 명언 데이터 가져오기
all_raw_quotes_data = get_all_quotes(api_base_url)

# 가져온 데이터에서 content - author 형식으로 가공
formatted_quotes = []

if all_raw_quotes_data:
    for item in all_raw_quotes_data:
        content = item.get("content", "내용 없음")
        author = item.get("author", "작자 미상")
        formatted_string = f"{content} - {author}"
        formatted_quotes.append(formatted_string)

# 최종 결과 배열 출력
print("\n--- 모든 명언 데이터 (형식화된 배열) ---")
# 모든 데이터를 출력하면 너무 길 수 있으므로, 처음 5개만 예시로 출력
for i, quote in enumerate(formatted_quotes):
    if i < 5:
        print(quote)
    else:
        break
print(f"... 그리고 {len(formatted_quotes) - 5}개의 명언이 더 있습니다.")

# Flask 애플리케이션 인스턴스 초기화
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """
    헬스 체크 엔드포인트.
    """
    return jsonify({"status": "healthy"}), 200

@app.route("/quote", methods=["GET"])
def get_quote():
    """
    미리 정의된 목록에서 무작위명언을 검색하여 JSON 형식으로 반환합니다.
    jsonify 함수는 응답 헤더를 'application/json'으로 올바르게 설정합니다. [2]
    """
    quote = random.choice(formatted_quotes)
    return jsonify({"quote": quote})

# 어플리케이션 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


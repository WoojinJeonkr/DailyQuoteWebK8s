import requests
import json
import urllib3
import os

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

def format_quotes(raw_quotes_data):
    """
    가져온 데이터를 content - author 형식으로 가공합니다.
    """
    formatted_quotes = []
    if raw_quotes_data:
        for item in raw_quotes_data:
            content = item.get("content", "내용 없음")
            author = item.get("author", "작자 미상")
            formatted_string = f"{content} - {author}"
            formatted_quotes.append(formatted_string)
    return formatted_quotes

def save_quotes_to_file(quotes, filename="quotes.json"):
    """
    형식화된 명언 목록을 JSON 파일로 저장합니다.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(quotes, f, ensure_ascii=False, indent=4)
        print(f"명언 목록이 '{filename}' 파일에 성공적으로 저장되었습니다.")
    except IOError as e:
        print(f"파일 저장 중 오류 발생: {e}")

if __name__ == '__main__':
    api_base_url = "https://api.quotable.io/quotes"
    all_raw_quotes_data = get_all_quotes(api_base_url)
    formatted_quotes = format_quotes(all_raw_quotes_data)
    save_quotes_to_file(formatted_quotes)

    print("\n--- 모든 명언 데이터 (형식화된 배열) ---")
    for i, quote in enumerate(formatted_quotes):
        if i < 5:
            print(quote)
        else:
            break
    print(f"... 그리고 {len(formatted_quotes) - 5}개의 명언이 더 있습니다.")
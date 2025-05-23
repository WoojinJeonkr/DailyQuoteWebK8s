## 로컬 환경에서 Flask API 실행하기

이 가이드는 Docker 이미지를 사용하지 않고, 프로젝트의 소스 코드를 로컬 환경(Window 기준)에서 직접 빌드하고 실행하는 방법을 설명합니다.

### 1. 전제 조건

아래 소프트웨어가 시스템에 설치되어 있어야 합니다:

* **Git**: 프로젝트 저장소를 복제하기 위해 필요합니다.
* **Python 3.x**: 백엔드 Flask API 실행을 위해 필요합니다. (Python 3.8 이상 권장)

### 2. 프로젝트 저장소 복제 (Clone Repository)

먼저, 프로젝트 저장소를 로컬로 복제합니다.

```bash
git clone https://github.com/WoojinJeonkr/DailyQuoteWebK8s.git
```

그리고 복제한 디렉토리로 이동합니다.

```bash
cd DailyQuoteWebK8s
```

### 3. 백엔드 Flask API 실행

백엔드 애플리케이션은 프론트엔드에 데이터를 제공하므로, 반드시 프론트엔드를 실행하기 전에 먼저 실행되어야 합니다.

먼저 백엔드 디렉토리로 이동합니다

```bash
cd backend-quote-api
```

이제 API 실행을 위해 가상환경을 생성합니다.

```bash
python -m venv venv
```

venv/bin/activate.bat 파일이 표시되었다면 가상환경이 정상적으로 설치되었음을 의미합니다.  
이제 activate.bat 파일을 실행하게 되면 파이썬 가상환경으로 접속하게 됩니다.

```DOS
.\venv\Scripts\activate.bat
```

어플리케이션을 구동하기 위한 라이브러리를 설치합니다. 이때 위치는 backend-quote-api에서 실행합니다.

```bash
pip install -r requirements.txt
```

라이브러리가 정상적으로 설치되었다면 API를 실행합니다.

```bash
python app.py
```

Flask API는 기본적으로 http://127.0.0.1:5000에서 실행됩니다.  
이 터미널/명령 프롬프트 창은 백엔드 앱이 실행 중인 동안 계속 열어두어야 합니다.
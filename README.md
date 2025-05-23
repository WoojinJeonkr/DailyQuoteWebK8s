# DailyQuoteWebk8s

매일 무작위 영어 명언을 보여주는 간단한 웹 애플리케이션입니다.  
Docker를 사용하여 컨테이너화되었으며, Kubernetes 클러스터에 배포됩니다.  
프로젝트를 통해 컨테이너화, 마이크로서비스 (Flask API + Spring Boot web app),  
그리고 Kubernetes 오케스트레이션 (Deployment, Service, Ingress, Replicas)의 핵심 개념들을 시연합니다.

## 프로젝트 구성

이 프로젝트는 다음과 같은 주요 구성 요소로 이루어져 있습니다.

* **`backend-quote-api/`**
    * Python Flask 기반의 백엔드 API입니다.
    * 외부 명언 API로부터 데이터를 가져와 제공합니다.
* **`frontend-web-app/`**
    * Spring Boot 기반의 프론트엔드 웹 애플리케이션입니다.
    * 사용자 인터페이스를 제공하며, 백엔드 API로부터 명언 데이터를 가져와 표시합니다.
* **`guide-docs/`**
    * 프로젝트의 상세 문서와 가이드라인이 저장되는 폴더입니다.

## 시작하기 (Getting Started)

프로젝트를 로컬 환경에서 실행하거나 개발하려면, `guide-docs` 폴더의 가이드를 참조해주세요.

* **[백엔드 로컬 실행 가이드](/guide-docs/backend-local-execution.md)**
* **[프론트엔드 로컬 실행 가이드](/guide-docs/frontend-local-execution.md)**

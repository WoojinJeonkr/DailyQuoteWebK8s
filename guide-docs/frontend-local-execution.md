## 로컬 환경에서 Spring Boot 웹 애플리케이션 실행하기

**중요**: 프런트엔드를 실행하기 전에 백엔드 Flask API가 http://127.0.0.1:5000 (또는 설정된 포트)에서 실행 중인지 반드시 확인해야 합니다.

### 1. 새로운 터미널/명령 프롬프트 열기

### 2. 프론트엔드 디렉토리로 이동

현재 git clone한 폴더/frontend-web-app으로 이동합니다.

```bash
cd frontend-web-app
```

만약 DailyQuoteWebK8s 폴더 바로 아래에 있다면 위와 같이 이동하면 됩니다.  
D 드라이브 특정 경로에 있다면 cd D:\local_git\DailyQuoteWebK8s\frontend-web-app 등으로 이동하세요.

### 3. Spring Boot 애플리케이션 실행

Gradle Wrapper를 사용하므로 별도의 Gradle 설치는 필요하지 않을 수 있습니다.

```bash
.\gradlew bootRun
```

애플리케이션이 정상적으로 시작되면 터미널에 `Tomcat initialized with port(s): XXXX (http)`와 같은 메시지가 표시됩니다.  
Spring Boot 앱은 기본적으로 `http://localhost:8080`에서 실행됩니다.  
만약 `frontend-web-app/src/main/resources/application.properties` 파일에서 `server.port`를 변경했다면,  
해당 포트(예: 8081)로 실행됩니다.

### 4. 웹 브라우저에서 접속

애플리케이션이 완전히 시작되면 `application.properties`에 기재한 포트 번호를 확인 후 웹 브라우저에서 다음 주소로 접속합니다.

현재 `application.properties`의 `server.port`: `8081`  
현재 프로젝트에서는 `http://localhost:8081`에서 실행됩니다.

### 5. 문제 해결 (Troubleshooting)

- `JAVA_HOME` 오류

    - `JAVA_HOME` 환경 변수가 설치된 JDK (예: `C:\Program Files\Java\jdk-21`)의 루트 경로를 정확히 가리키는지 확인하세요.
    - `Path` 환경 변수에 `%JAVA_HOME%\bin`이 포함되어 있는지 확인하고, 다른 오래된 Java 경로 (예: `javapath`나 `jdk-17\bin` 등)가 `%JAVA_HOME%\bin`보다 앞에 있는지 확인하여 있다면 제거하거나 뒤로 옮기세요.
    - 환경 변수를 변경했다면, 모든 터미널 창을 닫고 새로 열어야 변경 사항이 적용됩니다.
    - JAVA_HOME 설정 확인
        ```bash
        echo %JAVA_HOME%
        ```
- 포트 충돌

    - 백엔드(기본 5000) 또는 프런트엔드(기본 8080) 포트가 이미 다른 프로세스에 의해 사용 중인지 확인합니다.
        ```bash
        netstat -ano | findstr <포트번호>
        ```
    - 사용 중인 프로세스가 있다면, taskkill /F /PID <PID번호> 명령어로 종료하거나, application.properties 파일에서 Spring Boot 앱의 server.port를 다른 사용 가능한 포트 번호로 변경합니다.
- Gradle 빌드 또는 실행 문제

    - 이전에 실행 중이던 Gradle 데몬이 문제를 일으킬 수 있습니다. 다음 명령어를 실행하여 데몬을 중지하고 빌드 캐시를 정리한 후 다시 시도합니다.
        ```bash
        .\gradlew --stop     # 실행 중인 Gradle 데몬 중지
        .\gradlew clean      # 프로젝트 빌드 아티팩트 정리
        ```

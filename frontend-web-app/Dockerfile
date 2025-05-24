# frontend-web-app/Dockerfile

# 1단계: 빌드 스테이지
FROM eclipse-temurin:17-jdk-jammy as builder

# 작업 디렉토리 설정
WORKDIR /app

# Gradle Wrapper 복사 (필요시)
COPY gradlew .

RUN chmod +x gradlew

COPY gradle gradle

# build.gradle 및 settings.gradle 복사 (의존성 캐싱 활용)
COPY build.gradle settings.gradle ./

# 의존성 다운로드 (실제 코드 복사 전)
# 이렇게 하면 build.gradle이 변경되지 않는 한 의존성 다운로드 레이어가 캐싱됩니다.
RUN ./gradlew dependencies

# 소스 코드 복사
COPY src ./src

# 애플리케이션 빌드
RUN ./gradlew build -x test

# 2단계: 최종 이미지 스테이지 (JRE만 포함하여 더 가볍게)
FROM eclipse-temurin:17-jre-jammy

# 작업 디렉토리 설정
WORKDIR /app

# 빌드 스테이지에서 생성된 JAR 파일 복사
# build/libs/*.jar 패턴은 프로젝트 이름에 따라 생성되는 JAR 파일을 찾습니다.
COPY --from=builder /app/build/libs/*.jar app.jar

# Spring Boot 애플리케이션 실행
ENTRYPOINT ["java", "-jar", "app.jar"]

# Spring Boot 앱이 리스닝할 포트 (application.properties의 server.port와 일치)
EXPOSE 8080
package com.dailyquoteapp.frontendwebapp; // 본인의 패키지명으로 변경

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.client.RestTemplate;

@Controller
public class WebController {

    // 백엔드 Flask API의 기본 URL을 주입받기 위한 설정
    @Value("${backend.api.base-url}")
    private String backendApiBaseUrl;

    // Flask API와의 연동
    @GetMapping("/api/quote")
    @ResponseBody
    public String getRandomQuote() {
        RestTemplate restTemplate = new RestTemplate();
        // 백엔드 Flask 앱의 실제 /api/quote 엔드포인트를 호출하도록 수정합니다.
        String backendUrl = backendApiBaseUrl + "/api/quote";
        try {
            return restTemplate.getForObject(backendUrl, String.class);
        } catch (Exception e) {
            e.printStackTrace();
            return "{\"quote\": \"Error fetching quote from backend.\"}" ;
        }
    }

    // 백엔드 헬스 체크 엔드포인트
    @GetMapping("/api/health")
    @ResponseBody
    public String getHealthStatus() {
        RestTemplate restTemplate = new RestTemplate();
        String backendUrl = backendApiBaseUrl + "/api/health";
        try {
            return restTemplate.getForObject(backendUrl, String.class);
        } catch (Exception e) {
            e.printStackTrace();
            return "{\"status\": \"Error fetching health from backend.\"}" ;
        }
    }
}
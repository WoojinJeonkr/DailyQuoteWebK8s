package com.dailyquoteapp.frontendwebapp;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        // 루트 경로 (/)로 들어오면 static/index.html로 포워딩
        registry.addViewController("/").setViewName("forward:/index.html");
        // /index.html 경로로 들어와도 static/index.html로 포워딩
        registry.addViewController("/index.html").setViewName("forward:/index.html");
    }
}
package com.jee_project.chatbot.controllers;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import com.jee_project.chatbot.models.Message;

@RestController
public class MachineLearningController {
    private final RestTemplate restTemplate;

    public MachineLearningController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @PostMapping("/api/chat")
    public String chat(@RequestBody Message message) {
        String apiUrl = "http://localhost:80/chat";
        ResponseEntity<String> response = restTemplate.postForEntity(apiUrl, message, String.class);
        return response.getBody();
    }
}

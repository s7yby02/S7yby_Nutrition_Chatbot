package com.jee_project.chatbot;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AppController {
    
    @GetMapping("/home")
    public String goHome() {
        return "home";
    }

    @GetMapping("/login")
    public String goLogin() {
        return "login";
    }
}

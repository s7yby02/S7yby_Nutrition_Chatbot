package com.jee_project.chatbot.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AppController {
    
    @GetMapping("/")
    public String goHome() {
        return "home";
    }

    @GetMapping("/login")
    public String goLogin() {
        return "login";
    }
    @GetMapping("/register")
    public String goRegister() {
        return "register";
    }
}

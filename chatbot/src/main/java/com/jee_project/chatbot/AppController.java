package com.jee_project.chatbot;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AppController {
    
    @GetMapping("/index")
    public String goHome() {
        return "index";
    }
}

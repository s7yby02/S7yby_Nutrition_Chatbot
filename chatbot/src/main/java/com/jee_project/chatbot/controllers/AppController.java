package com.jee_project.chatbot.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.jee_project.chatbot.models.Message;
import com.jee_project.chatbot.models.User;
import com.jee_project.chatbot.models.UserDto;
import com.jee_project.chatbot.services.UserService;

import jakarta.validation.Valid;

@Controller
public class AppController {
    
    @GetMapping("/index")
    public String home() {
        return "home";
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }
    
    
    private UserService userService;

    public AppController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/register")
    public String register(Model model) {
        UserDto user = new UserDto();
        model.addAttribute("user", user);
        return "register";
    }

    @PostMapping("/register/save")
    public String registration(@Valid @ModelAttribute("user") UserDto userDto,
                               BindingResult result,
                               Model model,RedirectAttributes redirectAttributes){
        
        User existingUser = userService.findUserByEmail(userDto.getEmail());

        if(existingUser != null && existingUser.getEmail() != null && !existingUser.getEmail().isEmpty()){
            result.rejectValue("email", null,
                    "There is already an account registered with this email");
        }

        if(result.hasErrors()){
            model.addAttribute("user", userDto);
            return "/register";
        }

        userService.saveUser(userDto);

        redirectAttributes.addFlashAttribute("registrationSuccess", "Registration successful! You can now log in.");
        return "redirect:/login";
    }

    @GetMapping("/chat")
    public String chat(Model model) {
        Message message = new Message();
        model.addAttribute("message", message);
        return "chat";
    }

    @Autowired
    private MachineLearningController machineLearningController;
    
    @PostMapping("/chat")
    public String chatResponse(@ModelAttribute("message") Message message, Model model) {
        String response = machineLearningController.chat(message);
        model.addAttribute("response", response);
        return "chat";
    }
}

package com.jee_project.chatbot.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.servlet.view.RedirectView;

import com.jee_project.chatbot.models.User;
import com.jee_project.chatbot.services.UserService;

@Controller
public class UserController {
 
    @Autowired private UserService userService;

    @PostMapping(value="/users/addNew")
    public RedirectView addNew(@ModelAttribute User user, RedirectAttributes redir){
        userService.save(user);

        RedirectView redirectView = new RedirectView("/login", true);
        redir.addFlashAttribute("message", "You have been registered successfully");
        return redirectView;
    }


}

package com.jee_project.chatbot.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.jee_project.chatbot.models.User;
import com.jee_project.chatbot.repositories.UserRepository;

@Service
public class UserService {
    
    @Autowired private UserRepository userRepository;
    
    public void save(User user) {
        userRepository.save(user);   
    }
}

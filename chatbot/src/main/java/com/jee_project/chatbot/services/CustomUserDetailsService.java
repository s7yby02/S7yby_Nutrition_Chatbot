package com.jee_project.chatbot.services;

import java.util.Collections;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.jee_project.chatbot.models.User;
import com.jee_project.chatbot.repositories.UserRepository;

@Service
public class CustomUserDetailsService implements UserDetailsService {
    
    private UserRepository userRepository;

    public CustomUserDetailsService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
        User user = userRepository.findByEmail(email);

        if (user != null) {
            return new org.springframework.security.core.userdetails.User(user.getEmail(),
                    user.getPassword(), Collections.emptyList());
        }else{
            throw new UsernameNotFoundException("Invalid username or password.");
        }
    }

}

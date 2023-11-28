package com.jee_project.chatbot.services;

import java.util.List;
import com.jee_project.chatbot.models.User;
import com.jee_project.chatbot.models.UserDto;

public interface UserService {

    void saveUser(UserDto userDto);

    
    User findUserByEmail(String email);

    List<UserDto> findAllUsers();
    
}

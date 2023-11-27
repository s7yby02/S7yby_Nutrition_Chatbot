package com.jee_project.chatbot.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.jee_project.chatbot.models.User;

@Repository
public interface UserRepository extends JpaRepository<User, Integer> {
    User findByUsername (String username);
}
package com.jee_project.chatbot;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
//import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
//import org.springframework.security.crypto.password.NoOpPasswordEncoder;
//import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;


@Configuration
@EnableWebSecurity
public class ApplicationSecurityConfig {
    
    @Bean
    public BCryptPasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
 
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        http
            .authorizeHttpRequests(authorize -> authorize

                    .requestMatchers("/login","/ressources/**","/assets/img/**","/assets/css/**","/assets/js/**","/assets/vendor/**").permitAll()
                    .requestMatchers("/register","/ressources/**","/assets/img/**","/assets/css/**","/assets/js/**","/assets/vendor/**").permitAll()
                    .requestMatchers("/","/ressources/**","/assets/img/**","/assets/css/**","/assets/js/**","/assets/vendor/**").permitAll()
                    .requestMatchers("/users/addNew").permitAll()
                    .anyRequest().authenticated())
            .formLogin(formLogin -> formLogin
                    .loginPage("/login")
                    .usernameParameter("username")
                    .permitAll())
            .logout(logout -> logout.invalidateHttpSession(true)
                    .clearAuthentication(true)
                    .logoutRequestMatcher(new AntPathRequestMatcher("/logout"))
                    .logoutSuccessUrl("/login")
                    .permitAll());

        return http.build();
    }

   
    
    //@Bean
    //public PasswordEncoder passwordEncoder(){
    //    return NoOpPasswordEncoder.getInstance();
    //}

    @Autowired
    private UserDetailsService userDetailsService;

    //@Bean
    //public WebSecurityCustomizer webSecurityCustomizer() {
    //    return (web) -> web.ignoring().requestMatchers("/images/**", "/js/**", "/webjars/**");
    //}

    @Bean
    public DaoAuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider provider = new DaoAuthenticationProvider();
        provider.setUserDetailsService(userDetailsService);
        provider.setPasswordEncoder(passwordEncoder());
        return provider;
}
}

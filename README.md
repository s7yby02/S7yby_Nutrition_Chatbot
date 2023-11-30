# S7yby_Nutrition_Chatbot
## Overview 
*S7yby_Nutrition* is a web application dedicated to assisting bodybuilders in optimizing their nutrition plans. It provides a comprehensive solution for achieving fitness goals with a user-friendly interface, robust features, and machine learning-based techniques.

## Team Members

As dedicated data engineering students, we thrive on expanding our skill sets through innovative projects that leave a meaningful impact. Meet our team members :

- [ELHARRAN Ayoub](https://github.com/AybELHARRAN)

- [ELHAMDANI Mohamed Oussama](https://github.com/OussamaElhamdani)

- [GOURANE Abdellah](https://github.com/Gouranegithub)

- [ASKRI Aymane](https://github.com/Ayasgo)
## Table of Content
- ### General Context
- ### Used Technologies
- ### Project Workflow 
- ### Project Implementation
## General Context
*S7yby_Nutrition* is meticulously chosen to address vital needs in the fitness domain, primarily driven by the commitment to holistically optimize nutrition plans for bodybuilders. This project's significance is underscored by its data-driven approach, leveraging expertise in data science to provide well-informed decision-making through aggregated information from reputable sources. The incorporation of *S7yby_Nutrition_chatbot* adds an interactive and intelligent dimension, offering personalized assistance in meal planning aligned with individual nutritional requirements. Beyond technological ambitions, the project symbolizes a dedication to continuous learning and the advancement of health and fitness standards. With a deliberate focus on a user-friendly interface, S7YBYNutrition stands as a strategic choice, combining technological prowess with a profound commitment to elevate practices in the fitness community.
## Used Technologies
- ### Front End
  - **HTML-CSS-JS**
    
     <img src="https://miro.medium.com/v2/resize:fit:5120/1*l4xICbIIYlz1OTymWCoUTw.jpeg" alt="Front End" width="300" height="200">

      Frontend development encompasses the creation of the user interface and user experience on the web. ***HTML*** serves as the building blocks, structuring content, while ***CSS*** styles and formats it, defining layout and visual presentation. ***JavaScript*** adds dynamic behavior, facilitating interactive features and real-time updates. Responsive design ensures adaptability across diverse devices.
- ### BackEnd
  - **SpringBoot**

     <img src="https://user-images.githubusercontent.com/84719774/129191080-723b3b46-4e0b-4aa5-8eb9-654c2c025b18.png" alt="Spring Boot" width="300" height="100">
     
      *Spring Boot* is an open-source Java framework that simplifies the development of production-ready, stand-alone Spring-based applications. It provides a convention-over-configuration approach, reducing boilerplate code and configuration, and integrates seamlessly with the Spring ecosystem. With built-in support for embedded servers, dependency management, and auto-configuration, Spring Boot enables developers to rapidly build and deploy robust, scalable, and easily maintainable applications. It promotes best practices and focuses on convention, allowing developers to concentrate on business logic rather than complex setups, making it an excellent choice for building microservices and modern web applications.
- ### Machine learning model
  - **TensorFlow&Keras**
         <img src="https://3.bp.blogspot.com/-QZVBl08fmPk/XhO909Ha1dI/AAAAAAAACZI/q1a1UykGKe0KDUZ_ZITtWmM7bBJFRrvPQCLcBGAsYHQ/s1600/tensorflowkeras.jpg" alt="TensorFlow&Keras" width="300" height="150">

    - **TensorFlow**
      
      ***TensorFlow*** is an open-source machine learning framework developed by the Google Brain team. It provides a comprehensive ecosystem of tools, libraries, and community resources for building and deploying machine learning models. TensorFlow supports both deep learning and traditional machine learning, offering flexibility for a wide range of applications. Its core functionality involves defining, training, and deploying machine learning models, utilizing computational graphs to represent complex computations.
    - **Keras**
   
      ***Keras*** is a high-level neural networks API written in Python that serves as an interface for building and training neural networks. Originally a separate library, Keras has been integrated as the official high-level API into TensorFlow since version 2.0. Keras abstracts and simplifies the construction of neural networks, offering a user-friendly interface without sacrificing flexibility. It allows rapid prototyping of deep learning models, emphasizing modularity, ease of use, and extensibility. Keras can run seamlessly on top of various deep learning frameworks, with TensorFlow being the primary backend.
    
## Project Workflow
#### Data Collection
- Efficiently gather data from various free and reliable websites. Cause we are using a machine learning model, we need to collect a large amount of data to train our model. We used a web scraping technique to collect data from the web and also collecting some data manually. We used ***BeautifulSoup***, ***requests*** library to scrape data from the web. And it was the hardest part of the project. 
#### Web Application Development
##### Back End
- We used ***Spring Boot*** to develop our web application, ***Thymeleaf*** to create the front end of our application, ***Spring Security*** to secure our application, ***MySQL*** to store our data, ***JPA*** to connect our application to the database, ***BCrypt*** to encrypt the password of our users, ***Hibernate*** to map our database to our application, ***Maven*** to manage our dependencies, ***Tomcat*** to run our application, ***Spring Boot Data*** to manage our data, ***Spring MVC*** to create our controllers, ***Spring AOP*** to create our aspects, ***Spring Boot Test*** to test our application, ***Spring Web Services*** to create our web services, ***Spring Boot Web*** to create our web application, ***Spring Web Services*** to create our web services, ***Spring Boot Security*** to secure our application.
#### Front End
- We used ***HTML*** to create the structure of our web pages, ***CSS*** to style our web pages, ***JavaScript*** to add dynamic behavior to our web pages, ***Bootstrap*** to create our web pages, ***JQuery*** to add dynamic behavior to our web pages, ***AJAX*** to send asynchronous requests to our web services, ***JSON*** to send data between our web pages and our web services.
- ### Machine learning model
  - We used ***TensorFlow***, ***Keras*** and ***Python*** to build our model. We used ***Jupyter Notebook*** to test and create the model. We used ***NLTK*** because we're developping a chatbot that will interact with the text that we send to it . And to save and build the model we used ***Pickle*** library.
#### Chatbot Logic:
- *S7yby_Nutrition_chatbot* is a robust multiclass machine learning system.
- Learns patterns from intents.json to provide users with accurate responses tailored to specific questions.
- The chatbot extends support by recommending meals tailored to meet users' nutritional requirements: Offering information and links to resources where users can find detailed insights 
about the recommended meals.
## Application Overview
- ***Home Page***

<img src="/readmeimgs/index.png" alt="Index Page" width="1000" height="1700">

- ***Login Page***

<img src="/readmeimgs/login.png" alt="Login Page" width="1000" height="600">

- ***Register Page***

<img src="/readmeimgs/register.png" alt="Register Page" width="1000" height="600">

- ***Chatbot***

<img src="/readmeimgs/bot.png" alt="Chatbot" width="1000" height="600">

- ***Database with password encrypted***

<img src="/readmeimgs/db.png" alt="db" width="700" height="300">

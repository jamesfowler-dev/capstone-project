Welcome to EZPCreview.co.uk, my final capstone project for Code Institute's Full Stack Developement Boot Camp course. 

Developer: James Fowler

[Link to EZPCreview](https://ezpc-review-project-3e8ed4b2023a.herokuapp.com/)

![alt text](static/images/home-page.png)

# Table of Contents
- [Introduction](#Introduction) 
    - [Requirements](#Requirements)
    - [Structure & Concepts](#Structure-&-Concepts)

-   [User Experience](#user-experience)

    -   [User Stories](#user-stories)

-   [Design](#design)

    -   [Color Scheme](#color-scheme)
    -   [Typography](#typography)
    -   [Imagery](#imagery)
    -   [Wireframes](#wireframes)
    -   [Features](#features)
    -   [Accessibility](#accessibility)

-   [Technologies Used](#technologies-used)

    -   [Languages](#languages-used)
    -   [Frameworks, Libraries & Programs](#frameworks-libraries--programs-used)
    -   [AI Implementation](#ai-implementation)

-   [Deployment](#deployment)
-   [Testing](#testing)
-   [Credits](#credits)
-   [Acknowledgements](#acknowledgments)

# Introduction

Welcome to EZPCreview

EZPCreview is a modern, user-friendly platform designed to help tech enthusiasts explore, review, and discuss computer components. Whether you’re looking for the latest GPUs, SSDs, or CPUs, our website provides detailed information, real user reviews, and a vibrant community for sharing insights.

Key features include:

- Component Listings: Browse a wide range of hardware components with detailed specifications.

- User Reviews: Read reviews from other users or submit your own experiences.

- Commenting System: Engage in discussions about reviews and share tips with the community.

- Search and Filter: Quickly find the component you’re looking for using our search functionality.

- User-Friendly Interface: Clean design and intuitive navigation for a seamless experience.

Whether you’re a beginner building your first PC or a seasoned pro looking for the latest hardware, EZPCreview makes it easy to make informed decisions and stay up to date with the tech world.

# Requirements

There were 8 main criteria for this project:

<details>
  <summary>LO1: Learners will be able to apply Agile methodology to effectively plan and design a Full-Stack Web application using Django Web framework and related contemporary technologies.</summary>

</details>


<details>
  <summary>LO2: Learners will be able to develop and implement a data model, application features, and business logic to manage, query, and manipulate data to meet specific needs in a real-world domain.</summary>

</details>

<details>
  <summary>LO3: Learners will be able to implement and configure authorization, authentication, and permission features in a Full-Stack web application.</summary>

</details>

<details>
  <summary>LO4: Learners will be able to design, create, and execute manual or automated tests for a Full-Stack Web application using Django Web framework and related contemporary technologies.</summary>

</details>

<details>
  <summary>LO5: Learners will be able to utilise a distributed version control system and a repository hosting service to document, develop, and maintain a Full-Stack Web application using Django Web framework and related contemporary technologies.</summary>

</details>

<details>
  <summary>LO6: Learners will be able to deploy a Full-Stack Web application using Django Web framework and related contemporary technologies to a cloud-based platform, ensuring proper functionality and security.</summary>

</details>

<details>
  <summary>LO7: Learners will be able to demonstrate the use of object-based software concepts by designing and implementing custom data models in their Full-Stack Web application development.</summary>

</details>

<details>
  <summary>LO8: Learners will be able to leverage AI tools to orchestrate the software development process.</summary>

</details>


# Structure & Comcept

The application is structured into multiple Django apps: home, component, review, and basket to keep each core feature logically separated and easy to maintain. This modular approach ensures that component browsing, user reviews, and e-commerce functionality remain cleanly organised and independently scalable. The website opens on the home page, where users can browse featured PC components and navigate through clearly defined categories. Selecting a component brings the user to a detailed product page that displays specifications, pricing, approved user reviews, and any reviews awaiting moderation by their authors. The review system supports full CRUD functionality and comment threads, enabling users to actively engage with each component. Alongside this, the basket app allows users to add components to a session-based shopping basket, view their selections, and adjust quantities before checkout. Throughout development, the structure evolved to prioritise usability, maintainability, and clear separation of concerns, ensuring that each part of the site performs its role efficiently while contributing to a cohesive overall user experience.

## User Experience (UX)

Wireframes were made for each display size and are shown below. The pages were designed for mobile first, then tablet and desktop last. 

<details>
  <summary>Index/Home page (Click to expand)</summary>

![image of home page](assets/images/wireframe-home-page.png)

</details>

### User Stories



## Design

### Color Scheme

### Typography

### Imagery

### Wireframes

Wireframes were created for mobile, tablet and desktop using balsamiq:

![image of home page](assets/images/wireframe-home-page.png)
![image of refer page](assets/images/wireframe-referral-page.png)
![image of support](assets/images/wireframe-support-page.png)
![image of succecss page](assets/images/wireframe-success-page.png)

## Features

The website is comprised of a home page, an about page, a login page and a success page.

All Pages on the website are responsive and have:



### The Home Page



### The About Page


### The Login Page



### The Success Page

A link is available to bring you back to the home page.


### Future Implementations


## Accessibility


## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python

## Frameworks, Libraries & Programs Used

-   [Django] - packages included crispy forms, whitenoise, gunicorn, Cloudinary
-   [Balsamiq](https://balsamiq.com/) - used to create the wireframes
-   [Git](https://git-scm.com/) - for version control
-   [Github](https://github.com/) - To save and store the files for the website
-   [VS-Code](https://code.visualstudio.com/) - IDE used to create the site
-   [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website
-   [Bootstrap 5](https://getbootstrap.com/) - used to import the carousel and navbar elements
-   [Google Developer Tools](https://developer.chrome.com/docs/devtools) - To troubleshoot and test features, solve issues with responsiveness and styling
-   [TinyPNG](https://tinypng.com/) - to compress images
-   [Photopea](https://www.photopea.com/) - to resize images
-   [Favicon.io](https://favicon.io/) - to create the favicon
-   [Unsplash](https://unsplash.com/) - to create the images used in the site
-   [Co-Pilot](https://copilot.microsoft.com/) - used to troubleshoot minor issues and provide reminders for correct syntax
-   [ChatGPT](https://chatgpt.com/) - used to troubleshoot minor issues and provide reminders for correct syntax
-   [W3C HTML/CSS validation](https://validator.w3.org/) - validating CSS files
-   [Autoprefixer](https://autoprefixer.github.io/) - prefixing CSS
-   [Adobe Color](https://color.adobe.com/create/color-wheel) - used to find complimentory colors from image

## AI Implementation

User story creation

Code creation, 

Debugging, 

Performance and experience 

Deployment process

Co-Pilot and ChatGPT were used to troubleshoot and suggest fixes for issues throughout.

Typical use was sumple syntax reminders or attribute functions.

## Deployment


## Testing



### Known bugs


## Credits/References



### Acknowledgments

I would like to acknowledge all the technical tutors at Code Institute for their support throughout this project.

Welcome to EZPCreview.co.uk, my final capstone project for Code Institute's Full Stack Developement Boot Camp course. 

Developer: James Fowler

[Link to EZPCreview](https://ezpc-review-project-3e8ed4b2023a.herokuapp.com/)

![alt text](docs/images/home-page.png)

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



<br>

# Structure & Concept

The application is structured into multiple Django apps: home, component, review, and basket to keep each core feature logically separated and easy to maintain. This modular approach ensures that component browsing, user reviews, and e-commerce functionality remain cleanly organised and independently scalable. The website opens on the home page, where users can browse featured PC components and navigate through clearly defined categories. Selecting a component brings the user to a detailed product page that displays specifications, pricing, approved user reviews, and any reviews awaiting moderation by their authors. The review system supports full CRUD functionality and comment threads, enabling users to actively engage with each component. Alongside this, the basket app allows users to add components to a session-based shopping basket, view their selections, and adjust quantities before checkout. Throughout development, the structure evolved to prioritise usability, maintainability, and clear separation of concerns, ensuring that each part of the site performs its role efficiently while contributing to a cohesive overall user experience.



<details>
    <summary>ORM Model:</summary>

![image of ORM model](docs/images/ORM.png)

</details>

## User Experience (UX)

Wireframes were made for each display size and are shown below. The pages were designed for mobile first, then tablet and desktop last. 

<details>
  <summary>Index/Home page (Click to expand)</summary>


![image of home page](docs/images/wireframes/wireframe-index-page.png)

</details>

<details>
  <summary>Component detail page (Click to expand)</summary>

![image of component detail page](docs/images//wireframes/wireframe-component-detail-page.png)

</details>

<details>
  <summary>About page (Click to expand)</summary>

![image of About page](docs/images/wireframes/wireframe-about-page.png)

</details>

<details>
  <summary>Basket (Click to expand)</summary>

![image of the basket](docs/images/wireframes/wireframe-basket.png)

</details>

<details>
  <summary>Login page/modal (Click to expand)</summary>

![image of login modal](docs/images/wireframes/wireframe-login.png)

</details>

<details>
  <summary>Register page (Click to expand)</summary>

![image of Register page](docs/images//wireframes/wireframe-register.png)

</details>

<details>
  <summary>Search results page (Click to expand)</summary>

![image of Search results page](docs/images/wireframes/wireframe-search.png)

</details>




### User Stories

<details>
    <summary>Click to view</summary>


Log-in/Log-out: 

- As a registered user, I want to log in and log out securely so that I can access personal features.
- Acceptance Criteria: 

    - I have an account when I login with correct credentials

    - When I click “log out” then I should be logged out and returned to a public page


Admin Dashboard: 

- As the site owner, I want access to an admin dashboard so that I can manage all reviews & posts.
- Acceptance Criteria: 

    - As an admin when I log into Django admin then I can view, edit, add, and delete PC part reviews/comments and manage user accounts via Django Admin


View PC Part Details: 

- As a site visitor, I want to view details of a specific PC part so that I can learn more about it.
- Acceptance Criteria: 

    - When I click on a part then I should see a detail page with full information (description, specifications, etc.)

    - I want images so that each part has a preview.


View PC Parts: 

- As a site visitor, I want to view a list of available PC parts so that I can browse what is available.
- Acceptance Criteria: 

    - The visitor should see a list of all PC parts, including name, category, and price

    - I should be able to click on a part to view more details


Add a New PC Part Review or Comment: 

- As a logged-in user, I want to add a new PC part review so that I can tell people what I thought about the component.
- Acceptance Criteria: 

    - When I am logged in and add review, a new PC part should be saved in the database and added to my cart.


Register for an Account: 

- As a new user, I want to create an account so that I can see personalised information.
- Acceptance Criteria: 

    - A registration page to submit a valid email and password via AllAuth to create an account

    - I should receive a success notification


Edit an Existing Review or Comment: 

- As a logged-in user, I want to edit a PC part review so that I can correct or update it.
- Acceptance Criteria: 

    - When I am logged in and I click “edit”, the review or comment should be removed and I should see a success message.


Delete a PC Part Review or Comment: 

- As an Admin, I want to delete a PC part review or comment that I think could be inappropriate.
- Acceptance Criteria: 

    - When I am logged in as Admin, I can approve the review or comment


Search for PC Parts: 

- As a visitor, I want to search for parts so that I can quickly find what I need.
- Acceptance Criteria: 

    - A search bar on the home page to fetch linked data


Add items to a crate/basket: 

- As a site user, I want to add items to a basket and total the price.
- Acceptance Criteria: 

    - I can click on an item and add to basket

    - I can view the basket with my items in and see the total price


Compare 2 components (Could-do): 

- As a user I want to be able to compare 2 components before making a decision on a purchase.
- Acceptance Criteria: 

    - A view with 2 components compared and stats/descriptions visible

</details>



## Design

### Color Scheme

The colour scheme that I chose was based on the main hero image. The idea was to include interesting colours that also suited a technical theme. 

![image of color scheme](docs/images/color-scheme.png)

### Font

Google fonts were used, mainly MuseoModerno with Helvetica Neue for headings. 

![image of font theme](docs/images/font.png)

<detail>
    ![image of kanban board](docs/images/kanban-board.png)
</detail>

### UI/UX

For the UI/UX design of EZPC Review, I focused on creating a clean, modern interface that supports easy navigation and a visually engaging browsing experience. The layout uses a combination of Bootstrap structure and custom styling, with card-based components used throughout the site to present PC components, reviews, and user-generated content in a consistent and readable format. This helps organise information clearly and provides a familiar visual hierarchy for users. I selected a cool-toned colour palette, featuring subtle gradients and high-contrast text to improve readability and maintain accessibility. Key interactive elements, such as review buttons, forms, and navigation links, are styled to stand out without overwhelming the page. I also ensured the site is fully responsive, with flexible layouts using Flexbox and Bootstrap breakpoints so that users on mobile, tablet, and desktop screens have an equally smooth experience. Across the site, emphasis was placed on usability from clear call-to-action buttons to intuitive form layouts ensuring users can review components, leave feedback, and browse content without friction.

### Agile Framework

The Agile framework was used throughout the development lifecycle, following the MoSoCo process of priority. once the key priorities for the site were complete, I implemented the "Could-do" and "Should-do" features. There are still ideas that I have in the backlog and will look at implementing in the future as a personal project.


![image of kanban board](docs/images/kanban-board.png)

[Link to Kanban project board](https://github.com/users/jamesfowler-dev/projects/7/views/1)


### Imagery



## Features

The website is comprised of a home page, an about page, a login page and a success page.

All Pages on the website are responsive and have:

-  **Browse PC Components**

    Users can explore a collection of PC components—such as CPUs, GPUs, SSDs, RAM, and more each with its own dedicated detail page. Components include descriptions, pricing, images, and category information.

<details>
    <summary>Click to view</summary>

![image of browsing components](docs/images/features/browse-components.png)

</details>


-  **Write & Manage Reviews**

    Logged-in users can create written reviews for individual components, edit their existing reviews or delete their reviews. They can see an "Awaiting Approval" message when a review is pending moderation. This makes the review system transparent and gives users full control over their contributions.

<details>
    <summary>Click to view</summary>

![image of review functionality](docs/images/features/write-review.png)
![image of review functionality](docs/images/features/review-pending-approval.png)

</details>

- **Comment on Reviews**

    Users can engage with the community by commenting on reviews. Features include posting comments on any review, editing or deleting their own comments in a clean and threaded comment layout tied to specific reviews. Visibility rules so unapproved comments only show to their authors. 


<details>
    <summary>Click to view</summary>

![image of edit functionality](docs/images/features/edit-comments.png)

</details>

- **Moderated Review & Comment System**

    To maintain content quality, admins approve or reject reviews and comments. Unapproved content is hidden from general users but authors can still see their own pending submissions. 

<details>
    <summary>Click to view</summary>

![image of pending edit functionality](docs/images/features/pending-edit.png)

</details>

- **Basket System (Add & Manage Components)**

    The site includes a simple but functional basket system where users can add components to a basket, view basket contents, update quantities and remove items. This allows users to build a hypothetical PC parts list as they browse.


<details>
    <summary>Click to view</summary>

![image of basket functionality](docs/images/features/basket.png)

</details>

- **User Authentication**

    Using Django AllAuth, users can register for an account, log in and log out, access restricted features such as reviews, editing, and commenting. Redirects ensure users return to their original page after login. 
    

<details>
    <summary>Click to view</summary>

![image of registration](docs/images/features/register.png)
![image of sign-in](docs/images/features/login-modal.png)

</details>

- **Responsive & Accessible Design**

    The site is fully responsive and adapts to mobiles, tablets, and desktops. Built with Bootstrap and custom CSS, the site offers clear and consistent layout, a colour scheme chosen for readability, accessible contrast ratios and semantic HTML structure. 

<details>
    <summary>Click to view</summary>

![image of desktop](docs/images/features/home-page.png)
![image of tablet](docs/images/features/home-page-tablet-view.png)
![image of mobile](docs/images/features/mobile-view.png)

</details>

- **Search & Navigation**

    Users can easily navigate through the home page with featured components, individual component detail pages, review and comment sections.


<details>
    <summary>Click to view</summary>

![image of search result](docs/images/features/search-view.png)

</details>

- **Admin Management**

    Superusers have access to a custom admin interface for managing reviews, including actions such as approving comments/reviews and delete.  

<details>
    <summary>Click to view</summary>

![image of admin panel](docs/images/features/admin-panel.png)
![image of admin controls](docs/images/features/admin-controls.png)

</details>


### Future Implementations

Given more time, I would be keen to expand the project with a view to evolving the site into a comprehensive site to explore pc building. Specifically new features could include:

-  More components with seperate pages for category
-  Database basket system to provide user-specific baskets 
-  Compare 2 or more components 
-  Implement purchase system

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

Validation:
- WC3 Validator
- Jigsaw W3 Validator
- JShint
- CI Python Liner(PEP8)
- Lighthouse
- JShint
- CI Python Liner(PEP8)
- Lighthouse
- Wave Validator

## AI Implementation

AI played a significant role throughout the development of this project and became a valuable tool during the entire lifecycle of EZPC Review. It allowed me to speed up repetitive tasks and prototype features more efficiently. For example, once I had working code for the review and comment system, I could use AI to help adapt that structure to other areas of the site, such as the basket system or component listings, since the logic and layout followed similar patterns. AI also helped me quickly scaffold pages using Bootstrap, refine layouts, and experiment with new functionality without slowing down the development process.

### User Story creation 

AI helped structure and refine initial user stories by suggesting clear user goals and actions based on the project requirements. It further helped convert rough ideas into well-defined user stories that aligned with real-world behaviour.

### Code Assistance

AI was used in several parts of the codebase to support learning and problem-solving. While AI often provided helpful starting points—such as generating Django views, form logic or template loops, it also required careful review. At times, it introduced incorrect assumptions or redundant code, so having a solid understanding of Django and Python was essential to identify mistakes and correct them.

### Debugging and Learning

AI was particularly helpful when debugging unexpected behaviour or complex error codes. It helped explain specififc error messages, identify likely causes and suggest different approaches to resolve issues. This made it a useful learning tool and avoid unecessary frustration especially when working with more complex Django features or template logic. However, it wasn’t perfect and some suggestions went in the wrong direction or needed refinement, so critical thinking was still key. 

Overall, AI was an excellent support tool and provided significant benefits towards realising the vision of this project especially for repetitive tasks and troubleshooting. It also proved that it’s not a substitute for a knowledgeable developer, as human oversight was essential to ensure correct, efficient, and maintainable code.

### Performance 

AI assisted in identifying potential performance bottlenecks such as large image sizes and caching strategies. The load time impact from static files also saved time during development and reduced trial-and-error performance testing.





## Deployment

### Heroku Deployment

-  [Herouku](https://www.heroku.com/) (Ctrl + click)

This application has been deployed from GitHub to Heroku. A guide to deploying to Heroku can be found here 

Here are the steps to deployment:

Login or create an account at Heroku

### Clone Repository
You can clone the repository by following these steps:

- Go to the GitHub repository
- Locate the Code button above the list of files and click it
- Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the - URL to your clipboard
- Open Git Bash
- Change the current working directory to the one where you want the cloned directory
- Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY) 
- Press Enter to create your local clone.

## Testing & Validation

### Lighthouse testing



### Python validation

All pages are clear of any errors and pass PEP8 standard:

<details>
<summary>Config/Project level:</summary>

![image of config-asgi](docs/images/python-validation/asgi-python-validation.png)
![image of config-manage](docs/images/python-validation/manage-py-validation.png)
![image of config-urls](docs/images/python-validation/urls.py-project-level-validation.png)
![image of config-wsgi](docs/images/python-validation/wsgi-validation.png)

</details>

<details>
<summary>About:</summary>

![image of about-admin](docs/images/python-validation/about-admin-py-validation.png)
![image of about-forms](docs/images/python-validation/about-forms-py-validation.png)
![image of about-models](docs/images/python-validation/about-models-py-validation.png)
![image of about-test_forms](docs/images/python-validation/about-test-forms-py-validation.png)
![image of about-urls](docs/images/python-validation/about-urls-py-validation.png)
![image of about-views](docs/images/python-validation/about-views-py-validation.png)

</details>

<details>
<summary>Basket:</summary>

![image of basket-urls](docs/images/python-validation/basket-urls-py-validation.png)
![image of basket-views](docs/images/python-validation/basket-views-py-validation.png)

</details>

<details>
<summary>Component:</summary>

![image of component-admin](docs/images/python-validation/component-admin-py-validation.png)
![image of component-forms](docs/images/python-validation/component-forms-py-validation.png)
![image of component-models](docs/images/python-validation/component-models-py-validation.png)
![image of component-test_forms](docs/images/python-validation/component-test-forms-py-validation.png)
![image of component-test_views](docs/images/python-validation/component-test-views-validation.png)
![image of component-urls](docs/images/python-validation/component-urls-py-validation.png)
![image of component-views](docs/images/python-validation/component-views-py-validation.png)

</details>

<details>
<summary>Review: </summary>

![image of review-admin](docs/images/python-validation/review-admin-py-validation.png)
![image of review-forms](docs/images/python-validation/review-forms-py-validation.png)
![image of review-models](docs/images/python-validation/review-models-py-validation.png)

</details>


### HTML validation

All pages are clear of any errors except for an issue on component_detail.html

<details>
<summary>index.html</summary>

![image of index page](docs/images/html-validation/index-passed-validation.png)

</details>

<details>
<summary>component_detail.html</summary>



</details>

<details>
<summary>component_search.html</summary>




</details>

<details>
<summary>about.html</summary>

![image of about page](docs/images/html-validation/about-html-passed-validation.png)

</details>

<details>
<summary>view_basket.html</summary>

![image of view_basket page](docs/images/html-validation/view_basket-html-passed-validation.png)

</details>


<details>
<summary>base.html</summary>



</details>

<details>
<summary>login-modal</summary>

![image of login modeal](docs/images/html-validation/login-modal-passed-validation.png)


</details>

### CSS Validation 

The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website. No errors were found.  

<details>
<summary>test results</summary>

![image of style sheet](docs/images/css-validation.png)

</details>


### JavaScript Validation
JSHint javaScript Validation Service was used to validate all javaScript files. comment.js had a minor warning but nothing that would impact functionality.

"Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (button)"

<details>

![image of comment.js](docs/images/comment-js-validation.png)

</details>


basket.js passed with no errors

<details>

![image of basket.js](docs/images/basket-js-validation.png)

</details>


### Known bugs

-  Components in the navbar is not functional at present
-  Navbar can hand at times on opening in mobile view


## Credits/References

-  Code Insitute - For providing the training to build this website
-  Bootstrap - For the responsive site layout tools
-  Favicon - Favicon generation
-  Google Fonts - Font library used
-  Cloudinary - Image hosting


### Acknowledgments

I would like to acknowledge all the technical tutors at Code Institute for their support throughout this project.

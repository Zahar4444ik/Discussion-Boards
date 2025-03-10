# Forums Project Documentation

## Project Overview

**Forums** is a web application built with Django that allows users to log in, register, and engage in discussions on various topics. Users can create accounts, edit their profiles, and participate in conversations by posting questions or answers on discussion boards.

### Main Features

- **User Authentication**
  - User registration
  - User login and logout
  - Profile management (edit account)

- **Discussion Boards**
  - Create and manage boards
  - Create topics within boards
  - Post answers and questions
  - Engage in discussions

## Installation Instructions

To set up the **Forums** project locally, follow these steps:

### Prerequisites

- Python 3.6 or higher
- Docker & Docker Compose

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/forums.git
   cd forums

2. **Set Up Docker**

   ```bash
   docker-compose up --build -d

3. **Run Migrations**

   ```bash
   docker-compose exec web python manage.py migrate

4. **Create a Superuser**

   ```bash
   docker-compose exec web python manage.py createsuperuser

5. **Access the Application**

   Open your browser and go to http://127.0.0.1:8000/.

## Features

### User Authentication
  - **Registration**: New users can create an account.
  - **Login/Logout**: Users can log in to access their accounts and log out when done.
  - **Profile Management**: Users can edit their account details.

### Discussion Boards
  - **Create Boards**: Admin users can create new discussion boards.
  - **Create Topics**: Users can create topics within boards.
  - **Post Replies**: Users can post replies to existing topics.

## Usage

### User Actions

- **Registering an Account**
  - Navigate to the registration page.
  - Fill in the required fields: username, email, password, etc.
  - Submit the form to create an account.
- **Logging In**
  - Go to the login page.
  - Enter your username and password.
  - Click on the "Log In" button.
- **Logging Out**
  - Click on the "Log Out" button in the navigation bar.
- **Creating a Board** (Admin Only)
  - Access the admin panel by navigating to /admin.
  - Create a new board through the "Boards" section.
- **Creating a Topic**
  - Navigate to a specific board.
  - Click on "Create Topic".
  - Fill in the details and submit.
- **Posting Replies**
  - Open a topic and scroll to the reply section.
  - Enter your reply and submit.

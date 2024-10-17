# Early Pass Project

## Overview
The Early Pass project started as a skill-sharing platform but has evolved into a job research platform due to dataset limitations. Initially designed to help users find and request learning sessions for different skills, it became apparent that the large amount of data for skills would be too overwhelming to manage. Instead, the platform now allows users to explore job opportunities, save jobs, and apply filters to find jobs relevant to their search criteria.

The data for the job listings is sourced from a dataset loaded from Kaggle, which contains various job details such as company names, responsibilities, qualifications, and more. The Django-based server handles user registration, login, and profile management, enabling users to save jobs they are interested in.

While most of the requirements for the project have been implemented, such as job saving functionality, profile management, and unit tests, one feature still remains: having different roles with different permissions. This is a functionality planned to be added in the future.

## Features
- **User Registration:** New users can register accounts on the platform.
- **Login & Authentication:** Registered users can log in to access job listings and their profile.
- **Profile Management:** Users can update their profile information (first name, last name, email) and view saved jobs.
- **Job Listings:** Users can view a list of available jobs, apply filters based on job categories, and save jobs.
- **Unit Tests:** The project includes unit tests that passed successfully in the `test.py` file.

## Dataset
The dataset used for job listings was sourced from Kaggle. It contains various job roles, descriptions, locations, and categories. The jobs are displayed on the platform, and users can apply filters to find jobs relevant to their preferences.

## Running the Project
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Yesbol466/Job_Share_Platform.git
    cd Job_Share_Platform
   
    ```
2. **Install dependencies:** Make sure you have Python and Django installed. Run the following to install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run migrations:** Apply migrations to set up the database.
    ```bash
    cd skillshare
    python manage.py makemigrations
    python manage.py migrate
    ```
4. **Load the dataset:** The job listings are sourced from a CSV file (`job_skills.csv`). Ensure that this file is in the root folder of the project. You may need to load this data manually or add it as part of the admin interface.
5. **Run the server:** Start the Django development server:
    ```bash
    python manage.py runserver
    ```
6. **Collect Static Files:** The app requires static files for proper functioning, especially for filtering jobs and applying AJAX functionality. Use this command to collect all static files:
    ```bash
    python manage.py collectstatic
    ```

## Using the Application
1. **Register:** Once the server is running, go to the registration page to create a new account.
2. **Login:** After registering, log in using your credentials.
3. **Browse Jobs:** After logging in, you can apply filters to search for specific jobs and save jobs that interest you.
4. **Profile:** You can view your saved jobs in the profile section and update your personal information.

## Testing
All unit tests for this project are located in the `test.py` file. The application passed all the tests implemented, ensuring that critical functions such as saving jobs and profile management are working correctly. You can run the tests with:
```bash
python manage.py test
```
## Technologies Used
- **Python:** The core programming language for the application.
- **Django:** The web framework used to build the server-side logic, manage database migrations, and handle user authentication.
- **HTML/CSS:** Frontend design and structure for the user interface.
- **AJAX:** Used to enhance the filtering system on the job listings page without requiring a full page reload.
- **SQLite:** The database used for storing user information and saved jobs.
- **CSV Dataset:** Job listings are loaded from a CSV file obtained from Kaggle.
- **Django Unit Tests:** Implemented to verify key functionalities, including saving jobs and profile updates.

## Screenshots
1. **Job Listings Page:** The user can filter job listings by category and save jobs that interest them.
   ![Job Listings Page](https://github.com/Yesbol466/Job_Share_Platform/blob/master/skillshare/job_page_screenshot.png)

2. **Profile Page:** Users can view their saved jobs and update their personal information.
   ![Profile Page](https://github.com/Yesbol466/Job_Share_Platform/blob/master/skillshare/profile%20screenshot.png)

3. **Registration Page:** Users need to first create their account using correct password formatting and credentials.
   ![Registration Page](https://github.com/Yesbol466/Job_Share_Platform/blob/master/skillshare/register%20screenshot.png)

4. **Login Page:** Users can log in after creating their account and update the account and view saved jobs.
   ![Login Page](https://github.com/Yesbol466/Job_Share_Platform/blob/master/skillshare/login%20screenshot.png)

## Conclusion
The Early Pass project fulfills most of the required functionalities, including user management, job research, and saving capabilities. While role-based permissions have not been implemented yet, the core features work as expected, and the application has successfully passed unit testing.

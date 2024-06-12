# Test_task
splitwise app

# Expense Tracker

Expense Tracker is a Django application that allows users to track and share expenses with others, similar to Splitwise. Users can register, log in, add expenses, view their own expenses, and see their friends' expenses.

## Features

- User registration and authentication
- Adding shared expenses
- Viewing all personal expenses
- Viewing friends' expenses

## Installation

### Prerequisites

- Python 3.6+
- Django 3.0+

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/sakshii23/Test_task.git
    cd expense_tracker
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open a web browser and go to `http://127.0.0.1:8000/`.

## Usage

### User Registration

1. Go to the registration page: `http://127.0.0.1:8000/accounts/register/`
2. Fill out the registration form and submit.
3. Log in with your new credentials.

### Adding an Expense

1. Log in to your account.
2. Navigate to the "Share Expense" page: `http://127.0.0.1:8000/expenses/share/`
3. Fill out the expense form and submit.

### Viewing Your Dashboard

1. Log in to your account.
2. Navigate to the "Dashboard" page: `http://127.0.0.1:8000/expenses/dashboard/`
3. View your total balance, total owed, total you are owed, and details of your expenses.

### Viewing Friend's Expenses

1. Log in to your account.
2. Navigate to the "Friends' Expenses" page: `http://127.0.0.1:8000/expenses/friends/<friend_id>/`
3. View the expenses paid by your friend and the expenses they are part of.




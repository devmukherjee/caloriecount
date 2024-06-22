# Caloriecount - Python Django Macronutrient Tracker

Welcome to Caloriecount, a Python Django based application designed for tracking macronutrients and calorie intake.

## Features

- **Track Macronutrients**: Log your daily meals and monitor intake of carbohydrates, proteins, and fats.
- **Calorie Counter**: Set and track daily calorie goals.
- **User Authentication**: Secure user authentication system.
- **Admin Dashboard**: Manage users, meals, and view statistics via an admin panel.

## Installation

Follow these steps to set up Caloriecount on your local machine:

1. Clone the repository:
   ```bash
   git clone git@github.com:devmukherjee/caloriecount.git
   cd caloriecount/caloriecount
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your web browser and navigate to `http://localhost:8000` to view the app.

## Usage

- **User Registration**: Create a new account or use the admin-created superuser.
- **Log Meals**: Log your meals by entering food items and their quantities.
- **Track Progress**: Monitor daily macronutrient intake and calorie consumption.
- **Admin Dashboard**: Access admin features at `http://localhost:8000/admin`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
```

In this updated README template, I've incorporated the application name "Caloriecount" throughout the document, including the title and relevant sections. This should align with the specific name of your Django application.

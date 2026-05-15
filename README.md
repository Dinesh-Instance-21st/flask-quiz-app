# Flask Quiz Application

A full-stack web application for conducting online quizzes with secure user authentication using OTP verification.

---

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Gmail account (for OTP email sending)

---

## Installation & Setup

### 1. Clone or Navigate to Project Directory
```bash
cd path/to/flask_quiz_app
```

### 2. Create Virtual Environment
```bash
# On Windows (PowerShell)
python -m venv venv
(& ".\venv\Scripts\Activate.ps1")

# On Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env File
Create a `.env` file in the project root directory:

```env
SECRET_KEY=your_secret_key_here
MAIL_USERNAME=your_gmail@gmail.com
MAIL_PASSWORD=your_app_password_here
```

**Important: Gmail Setup**
1. Enable 2-Step Verification in your Google Account
2. Generate an App Password (Google > Security > App passwords)
3. Use the app password in `MAIL_PASSWORD` (NOT your regular Gmail password)

---

## Running the Project

### Start the Flask Development Server
```bash
# Make sure virtual environment is activated
python app.py
```

The application will run at: **http://localhost:5000**

---

## Usage

1. **Login Page**: Enter your email address
2. **OTP Verification**: Enter the OTP sent to your email
3. **Quiz Page**: Answer all quiz questions
4. **Submit**: Click Submit to see your score
5. **Results**: View your quiz performance with timestamp

---

## Project Structure

```
flask_quiz_app/
├── app.py                 # Main Flask application
├── database.py            # Database operations (SQLite)
├── questions.py           # Quiz questions data
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── quiz.db               # SQLite database (auto-created)
├── static/
│   └── styles.css        # CSS styling
├── templates/
│   ├── login.html        # Login page
│   ├── verify.html       # OTP verification page
│   ├── quiz.html         # Quiz page
│   └── result.html       # Results page
├── venv/                 # Virtual environment (auto-created)
└── README.md            # This file
```

---

## Features

✅ **Secure OTP Authentication** - Email-based one-time password verification  
✅ **Interactive Quiz** - Multiple-choice questions with instant scoring  
✅ **Result Tracking** - Store quiz results with timestamps  
✅ **Session Management** - Secure user session handling  
✅ **Attempt Counter** - Track number of quiz attempts  

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Flask session secret key (use any random string) |
| `MAIL_USERNAME` | Gmail address for sending OTPs |
| `MAIL_PASSWORD` | Gmail app-specific password (NOT regular password) |

---

## Database

The application uses SQLite with the following schema:

```sql
CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    score INTEGER,
    total INTEGER,
    date_time TEXT
)
```

Database file: `quiz.db` (auto-created on first run)

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Make sure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: OTP Email Not Received
**Solution**: 
- Verify Gmail credentials are correct
- Check if app password is being used (not regular password)
- Check spam/trash folder
- Ensure 2-Step Verification is enabled on Gmail

### Issue: "Address already in use"
**Solution**: Change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use different port
```

### Issue: Database Locked Error
**Solution**: Delete `quiz.db` and restart the application (it will recreate it)

---

## Quick Start (One Command)

If you have everything set up, run:
```bash
python app.py
```

Then open your browser to: **http://localhost:5000**

---

## Technologies Used

- **Backend**: Flask 3.1.3
- **Database**: SQLite3
- **Email**: Flask-Mail (SMTP)
- **Frontend**: HTML5, CSS3, Jinja2
- **Language**: Python 3.x

---

## Future Enhancements

- User registration and account management
- Admin dashboard for managing questions
- Performance analytics and leaderboards
- Mobile-responsive design
- JWT authentication
- Database migrations with Alembic

---

## Author
Dinesh Kumar S

## License
MIT License

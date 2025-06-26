- [Flask](https://flask.palletsprojects.com/en/stable/) :- Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.

In the Flask code:

```python
app = Flask(__name__)
```

This line is **crucial** for initializing your Flask application. Let's break it down in detail:

---

### 🔹 `Flask(...)` — Creating the Application Instance

* `Flask` is a **class** provided by the `flask` module.
* When you call `Flask(...)`, you're **creating an instance of the Flask application**. This instance will act as your **web application/server**.

### 🔹 `__name__` — Special Python Variable

* `__name__` is a **built-in Python variable** that represents the name of the current module (file).
* If you run the script **directly**, `__name__` will be equal to `"__main__"`.
* If the script is **imported as a module**, `__name__` will be the **module’s name** (e.g., `"myapp"`).

---

### ✅ Why Use `__name__` in `Flask(__name__)`?

Flask needs to know **where to look for resources** such as:

* Static files (e.g., JavaScript, CSS, images in the `static/` folder)
* Templates (HTML files in the `templates/` folder)

By passing `__name__`, Flask knows:

* **The location of the root directory of your app**
* Where to find your **static** and **template** folders

---

### 🧠 Summary

| Part                    | Meaning                                                                   |
| ----------------------- | ------------------------------------------------------------------------- |
| `Flask(...)`            | Creates a Flask app object                                                |
| `__name__`              | Tells Flask the name of the current module                                |
| `app = Flask(__name__)` | Creates the application and helps Flask locate resources & configurations |

---

### 🔍 Analogy

Imagine `Flask(__name__)` like telling Flask:

> “Hey, create an app and remember where I (this file/module) am located, so you can find other files you may need.”

## Flask's important functions and its usecases

### 1. Flask

The main Flask class that creates the web application instance.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
```

The `Flask(__name__)` creates an application instance, where `__name__` helps Flask locate resources like templates and static files.

### 2. render_template

Renders HTML templates from the templates folder, allowing you to pass data to the template.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user_profile(name):
    user_data = {
        'name': name,
        'age': 25,
        'city': 'New York'
    }
    return render_template('profile.html', user=user_data)
```

This would render a `profile.html` template located in the `templates/` folder, passing the `user_data` dictionary to the template where you can access it using Jinja2 syntax like `{{ user.name }}`.

### 3. session

Provides server-side session management to store user data across requests. Sessions are encrypted and stored as cookies.

```python
from flask import Flask, session, request, redirect

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for sessions

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['user'] = username
    session['logged_in'] = True
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return f"Welcome {session['user']}!"
    return "Please log in first"

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('logged_in', None)
    return "Logged out successfully"
```

Sessions persist data between requests and are automatically encrypted using the secret key.

### 4. make_response

Creates custom response objects, allowing you to modify headers, status codes, and cookies before sending the response.

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/download')
def download_file():
    response = make_response("This is file content")
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Disposition'] = 'attachment; filename=data.txt'
    return response

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie has been set!")
    response.set_cookie('username', 'john_doe', max_age=3600)  # Expires in 1 hour
    return response

@app.route('/custom-status')
def custom_status():
    response = make_response("Custom error message", 418)  # I'm a teapot status
    response.headers['X-Custom-Header'] = 'Flask Example'
    return response
```

`make_response` is particularly useful when you need to set custom headers, cookies, or HTTP status codes that differ from the default 200 OK response.

- Each of these imports serves a specific purpose in building Flask web applications: Flask creates the app, render_template handles HTML templating, session manages user state, and make_response provides fine-grained control over HTTP responses.

### 5. **request**
Provides access to incoming request data including form data, query parameters, JSON, headers, and more.
- `request.form` - Form data from POST requests
- `request.args` - URL query parameters
- `request.get_json()` - JSON data from request body
- `request.headers` - HTTP headers
- `request.method` - HTTP method (GET, POST, etc.)
- `request.cookies` - Cookies sent by client

```python
@app.route('/request-info')
def request_info():
    # Access various request properties
    info = {
        'method': request.method,
        'url': request.url,
        'user_agent': request.headers.get('User-Agent'),
        'remote_addr': request.remote_addr,
        'cookies': dict(request.cookies)
    }
    return info
```

## Sessions and Cookies

**Cookies** are small pieces of data stored directly in the user's browser by a website. They're sent back and forth between the browser and server with each HTTP request.

**Sessions** are server-side storage mechanisms that maintain user state across multiple requests. The server stores session data and typically uses a session identifier (often stored in a cookie) to link the browser to the correct session data.

## Key Differences

| Aspect | Cookies | Sessions |
|--------|---------|----------|
| **Storage Location** | Client-side (browser) | Server-side |
| **Storage Capacity** | Limited (~4KB per cookie) | Limited only by server resources |
| **Security** | Less secure (visible to client) | More secure (data stays on server) |
| **Lifespan** | Can persist after browser closes | Usually expires when browser closes |
| **Performance** | Sent with every request (network overhead) | Only session ID sent with requests |
| **Accessibility** | Accessible via JavaScript (unless httpOnly) | Not directly accessible to client |

## When to Use Cookies

Use cookies when you need to:
- **Remember user preferences** (theme, language, layout settings)
- **Track user behavior** for analytics
- **Store non-sensitive data** that should persist across browser sessions
- **Implement "Remember Me" functionality**
- **Cache frequently accessed, non-sensitive information**

Example scenarios:
- Storing shopping cart contents for guest users
- Remembering user's preferred currency or region
- Tracking which articles a user has read
- Storing user interface preferences

## When to Use Sessions

Use sessions when you need to:
- **Store sensitive information** (user authentication status, personal data)
- **Maintain server-side state** for complex workflows
- **Store large amounts of temporary data**
- **Implement secure user authentication**
- **Handle multi-step processes** (wizards, checkouts)

Example scenarios:
- User login status and authentication data
- Shopping cart for logged-in users
- Multi-step form data
- Temporary file uploads
- Admin panel access control

## Best Practices

**For Security:**
- Use sessions for sensitive data, cookies for preferences
- Always use HTTPS for both
- Set appropriate cookie flags (Secure, HttpOnly, SameSite)
- Implement proper session timeout and regeneration

**For Performance:**
- Minimize cookie size and number
- Use sessions for large data sets
- Consider using both together - session for security, cookies for user experience

**Hybrid Approach:**
Many applications use both - sessions for authentication and sensitive operations, cookies for user preferences and non-sensitive data that enhances user experience across visits.

## DB Operations using SQLAlchemy in Flask

### **Flask Database Migration with Flask-Migrate (Alembic)**
1. **`flask db init`**  
   - Initializes migrations for the Flask app (creates a `migrations` folder).  
   - **Only run once per project** (unless you delete migrations and restart).  

2. **`flask db migrate`**  
   - Detects changes in SQLAlchemy models (e.g., new `People` table) and generates a migration script.  
   - Run **whenever you modify your models** (add/remove tables, change columns).  

3. **`flask db upgrade`**  
   - Applies pending migrations to the database (creates/modifies tables).  
   - Required after `migrate` to finalize changes.  

### **Workflow for Database Changes**  
- **Edit models** → `flask db migrate` → `flask db upgrade`.  
- Example: Adding a new `Person` model triggers:  
  - Detection of the new table (`people`) → Migration script → Database update.  

### **Key Notes**  
- **Never run `flask db init` twice** unless resetting migrations.  
- Always **migrate + upgrade** after schema changes (new classes, fields).  
- Uses **SQLAlchemy** for ORM and **Alembic** for migration tracking.  

This process ensures smooth database schema evolution without manual SQL scripts.

## Breakdown of the **Flask-Migrate (Alembic) commands** and their tasks:  

### **Flask Database Migration Commands**  

| **Command**            | **Task**                                                                 |
|------------------------|--------------------------------------------------------------------------|
| `flask db init`        | Initializes migration support (creates a `migrations/` folder). **Run only once per project.** |
| `flask db migrate`     | Detects changes in SQLAlchemy models (e.g., new tables, columns) and generates a migration script. |
| `flask db upgrade`     | Applies the latest migration to update the database schema (creates/modifies tables). |
| `flask db downgrade`   | Reverts the last migration (undoes changes if needed). |

### **Typical Workflow**  
1. **Make changes** to your SQLAlchemy models (e.g., add a `Person` class).  
2. Run `flask db migrate -m "Add Person table"` → Creates a migration script.  
3. Run `flask db upgrade` → Updates the database with the changes.  

- Note :- Run `flask db init` command once when we initialize the database, then run `flask db migrate` & `flask db upgrade` subsequently everything when we make chnage in database.

## Flask-Login and Flask-Bcrypt in Flask Projects

### Flask-Login
Flask-Login provides user session management for Flask. It handles:
- Logging users in and out
- Remembering users' sessions
- Protecting routes from unauthorized access
- Managing user sessions

### Flask-Bcrypt
Flask-Bcrypt is a Flask extension for Bcrypt password hashing. It:
- Securely hashes passwords before storing them
- Provides password verification
- Protects against brute-force attacks

### Example Code

```python
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=request.form['username'], password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return f"Welcome {current_user.username}!"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features in the Example:
1. `UserMixin` provides default implementations for Flask-Login's required methods
2. `login_user()` creates a session for the user
3. `logout_user()` removes the session
4. `@login_required` decorator protects routes
5. `current_user` gives access to the logged-in user
6. `bcrypt.generate_password_hash()` securely hashes passwords
7. `bcrypt.check_password_hash()` verifies passwords against hashes

This combination provides secure authentication for Flask applications.
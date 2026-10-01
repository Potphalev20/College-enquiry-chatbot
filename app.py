from database import *
from flask import Flask, render_template, request, redirect, session, jsonify
from urllib.parse import urlencode

app = Flask(__name__)
app.secret_key = "secretkey"

# ---------------- HOME ----------------
@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')
    return render_template("index.html", is_admin=session.get('is_admin', 0))

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            error_msg = "Please enter both username and password"
            return redirect(f'/login?error={urlencode({"msg": error_msg})[4:]}')

        user = check_user(username, password)

        if user:
            session['user'] = user[1]
            session['is_admin'] = user[3]
            return redirect('/')
        else:
            error_msg = "Invalid username or password. Please try again."
            return redirect(f'/login?error={urlencode({"msg": error_msg})[4:]}')

    return render_template("login.html")

# ---------------- SIGNUP ----------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        # Validation
        if not username or not password:
            error_msg = "Username and password are required"
            return redirect(f'/signup?error={urlencode({"msg": error_msg})[4:]}')

        if len(username) < 3:
            error_msg = "Username must be at least 3 characters long"
            return redirect(f'/signup?error={urlencode({"msg": error_msg})[4:]}')

        if len(password) < 6:
            error_msg = "Password must be at least 6 characters long"
            return redirect(f'/signup?error={urlencode({"msg": error_msg})[4:]}')

        if password != confirm_password:
            error_msg = "Passwords do not match"
            return redirect(f'/signup?error={urlencode({"msg": error_msg})[4:]}')

        try:
            add_user(username, password)
            # Redirect to login with success message
            return redirect('/login?success=Account%20created%20successfully')
        except Exception as e:
            error_msg = f"Username already exists or signup error: {str(e)}"
            return redirect(f'/signup?error={urlencode({"msg": error_msg})[4:]}')

    return render_template("signup.html")

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ---------------- CHATBOT ----------------
@app.route('/get', methods=['POST'])
def chatbot_response():
    user_msg = request.form['msg'].lower()

    if "course" in user_msg:
        courses = get_courses()
        response = "Courses: " + ", ".join([c[1] for c in courses])
    elif "fees" in user_msg:
        response = "Fees range from ₹80,000 to ₹1,50,000"
    else:
        response = "Sorry, I didn't understand your question."

    log_chat(user_msg, response)
    return jsonify({"response": response})

# ---------------- ADMIN PANEL ----------------
@app.route('/admin')
def admin():
    if 'user' not in session or session.get('is_admin') != 1:
        return "Access Denied"

    return render_template("admin.html",
                           courses=get_courses(),
                           users=get_users(),
                           chats=get_chat_history())

# ---------------- ADD COURSE ----------------
@app.route('/admin/add_course', methods=['POST'])
def add_course_route():
    add_course(request.form['course_name'],
               request.form['duration'],
               request.form['fees'])
    return redirect('/admin')

# ---------------- DELETE COURSE ----------------
@app.route('/admin/delete_course/<int:id>')
def delete_course_route(id):
    delete_course(id)
    return redirect('/admin')

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
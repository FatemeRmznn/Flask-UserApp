from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com/users"


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Fetch user details and display on an HTML page"""
    response = requests.get(f"{BASE_URL}/{user_id}")

    if response.status_code == 200:
        user_data = response.json()
        return render_template('user.html', user=user_data)
    else:
        return render_template('error.html', message=f"User with ID {user_id} not found")


@app.route('/', methods=['GET', 'POST'])
def search_user():
    """Render search form and redirect to user page"""
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return redirect(f"/user/{user_id}")
    return render_template('search.html')


@app.route('/users')
def list_users():
    """Fetch all users and display them in a table"""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        users = response.json()
        return render_template('users.html', users=users)
    else:
        return render_template('error.html', message="Failed to load users.")


if __name__ == '__main__':
    app.run(debug=True)

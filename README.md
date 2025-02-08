# 📌 Flask User Management App

A simple Flask-based web application for managing users. This app allows searching for users, viewing individual user details, and listing all users. It fetches user data from an external API and displays it in a Bootstrap-styled interface.

## 🚀 Features
- Search for a user by ID
- View user details (name, email, phone, address, etc.)
- List all users in a structured table
- Responsive UI using Bootstrap

## 🛠️ Technologies Used
- **Flask**: Backend framework
- **Bootstrap 5**: Frontend styling
- **Requests**: Fetching data from an external API

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/FatemeRmznn/Flask-UserApp.git
   cd Flask-UserApp
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Running the Application
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and visit: `http://127.0.0.1:5000/`

## 🧩 Project Structure
```
Flask-UserApp/
│── templates/
│   ├── base.html
│   ├── index.html
│   ├── search.html
│   ├── user.html
│   ├── users.html
│── static/  (didn't add)
│── app.py
│── requirements.txt (if created)
│── README.md
```
## 📷 Screenshots

![image](https://github.com/user-attachments/assets/d777c631-40c0-41a1-ac24-a64f0da4b9f4)

![image](https://github.com/user-attachments/assets/7d912fd9-a762-4527-8e8c-e407df5a9a0e)


## API Source
This app fetches user data from [`JSONPlaceholder`](https://jsonplaceholder.typicode.com/users), a free fake REST API for testing and prototyping.

## 📌 Future Improvements
1️⃣ User Authentication & Authorization
2️⃣ Database Integration
3️⃣ Search and Filtering Enhancements
4️⃣ User Profile & Edit Feature
5️⃣ RESTful API Development
6️⃣ UI Enhancements & Dark Mode
7️⃣ Docker & Deployment

## 💡 Contributing
Feel free to contribute! Fork the repository and submit a pull request.

## 📜  License
This project is licensed under the MIT License.


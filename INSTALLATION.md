# 📦 CommunityHero Nexus – Installation Guide

This guide explains how to set up and run **CommunityHero Nexus** on your local machine.

---

# 📋 System Requirements

Before starting, make sure you have the following installed:

| Software      | Version        |
| ------------- | -------------- |
| Python        | 3.10 or later  |
| Git           | Latest Version |
| VS Code       | Recommended    |
| Google Chrome | Recommended    |

---

# 📥 Step 1 – Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/CommunityHero-Nexus.git
```

Move into the project directory:

```bash
cd CommunityHero-Nexus
```

---

# 📁 Step 2 – Project Structure

Your project should look similar to this:

```text
CommunityHero-Nexus/
│
├── ai_agents/
├── database/
├── routes/
├── services/
├── static/
├── templates/
├── uploads/
├── utils/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── INSTALLATION.md
└── .env.example
```

---

# 🐍 Step 3 – Create a Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# 📦 Step 4 – Install Required Packages

Install all dependencies using:

```bash
pip install -r requirements.txt
```

If installation completes successfully, your environment is ready.

---

# 🔑 Step 5 – Configure Environment Variables

Create a file named:

```text
.env
```

in the project root directory.

Example:

```env
SECRET_KEY=your_secret_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Getting a Gemini API Key

1. Visit Google AI Studio.
2. Sign in with your Google account.
3. Create an API key.
4. Copy the generated key.
5. Paste it into the `.env` file.

> **Important:** Never commit your `.env` file or API keys to GitHub.

---

# ▶️ Step 6 – Run the Application

Start the Flask application:

```bash
python app.py
```

If everything is configured correctly, you should see output similar to:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🧪 Step 7 – Test the Application

Use the following checklist to verify that the application is working correctly:

* ✅ Home page loads successfully
* ✅ Report page opens
* ✅ Image upload works
* ✅ Interactive map loads
* ✅ Location selection works
* ✅ AI Analysis page displays results
* ✅ Tracking page retrieves reports
* ✅ Authority Dashboard displays reports
* ✅ Status updates work
* ✅ AI Command Center loads charts and analytics
* ✅ AI Assistant page is accessible

---

# 🗺 Testing Workflow

Follow this recommended sequence:

1. Open the Home page.
2. Click **Report Issue**.
3. Upload an issue image.
4. Fill in the report details.
5. Select the issue location on the map.
6. Submit the report.
7. Review the AI Analysis page.
8. Copy the generated Tracking ID.
9. Open the Tracking page and search using the Tracking ID.
10. Visit the Authority Dashboard and update the issue status.
11. Open the AI Command Center and verify analytics.
12. Test the AI Assistant page.

---

# 📂 Uploads

Uploaded images are stored in:

```text
uploads/issues/
```

Temporary files (if used) are stored in:

```text
uploads/temp/
```

---

# 🗄 Database

The project uses **SQLite**.

On the first run, the application automatically creates the required database tables using SQLAlchemy.

No manual database setup is required.

---

# ⚙ Common Issues

## ModuleNotFoundError

Install all required packages:

```bash
pip install -r requirements.txt
```

---

## Flask is not recognized

Install Flask:

```bash
pip install Flask
```

---

## Missing Gemini API Key

Ensure that your `.env` file contains:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Images are not displaying

Verify that:

* The `uploads/issues/` directory exists.
* The uploaded image is present.
* The Flask application has permission to read the directory.

---

## Map is not loading

Check that:

* You have an active internet connection.
* Leaflet and OpenStreetMap resources are not blocked by your network.

---

## Database Issues

If the database becomes corrupted during development:

1. Stop the application.
2. Delete the local SQLite database (if applicable).
3. Restart the application:

```bash
python app.py
```

The tables will be recreated automatically.

---

# 🔒 Security Notes

For security reasons:

* Do **not** upload your `.env` file.
* Do **not** expose API keys.
* Do **not** commit the `venv/` directory.
* Keep sensitive configuration outside version control.

---

# ☁️ Deployment

This project is intended to be deployed using **Google AI Studio** together with **Google Cloud Platform (GCP)**.

Deployment typically involves:

1. Pushing the project to GitHub.
2. Connecting the repository in Google AI Studio.
3. Configuring environment variables.
4. Deploying to Google Cloud.
5. Verifying the live application.

Refer to the project README for deployment details.

---

# 🤝 Need Help?

If you encounter any issues while setting up the project:

1. Verify all prerequisites are installed.
2. Check that the virtual environment is activated.
3. Confirm the `.env` file is correctly configured.
4. Ensure all dependencies are installed.
5. Review the terminal output for error messages before seeking further assistance.

---

## 🎉 You're Ready!

If you've completed all the steps above, CommunityHero Nexus should now be running successfully on your local machine.

Happy coding! 🚀

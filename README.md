# 🔐 Password Strength Checker – Web App

A simple Flask web app to evaluate password strength based on length, complexity, and uniqueness. The app gives real-time feedback and improvement suggestions, and supports auto-deployment using GitHub Actions and Render.

## 📦 What's Included

```bash
.
├── app.py                       # Flask backend
├── requirements.txt            # Dependencies
├── templates/
│   └── index.html              # Frontend UI with Bootstrap
└── .github/
    └── workflows/
        └── deploy.yml         # GitHub Actions CI/CD to Render
```

## 🌐 Live Demo

🚀 You can deploy this project live on [Render](https://render.com)
(See deployment instructions below)

## 🧪 Features

* Checks for:

  * Password length
  * Uppercase & lowercase usage
  * Numbers
  * Special characters
  * Common weak passwords
* Strength Levels: **Weak ⚠️**, **Moderate 🛡️**, **Strong 💪**
* Suggestions for improvement
* Responsive UI (Bootstrap 5)
* GitHub Actions CI/CD for auto-deployment

## 🚀 Getting Started

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/ThoudabinaSumanth/password-strength-checker.git
cd password-strength-checker
```

### ✅ 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ 3. Run Locally

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## 🔄 CI/CD: Auto-Deploy to Render

### ✅ 1. Set Up Render Deploy Hook

* Deploy your app manually once at [https://render.com](https://render.com)
* Copy your **Deploy Hook URL** under Web Service settings

### ✅ 2. Add GitHub Secret

In your GitHub repository:

* Go to **Settings → Secrets → Actions**
* Add new secret:

  * Name: `RENDER_DEPLOY_HOOK_URL`
  * Value: *(your copied hook URL)*

### ✅ 3. GitHub Actions Workflow

This is already configured in `.github/workflows/deploy.yml`.
On every push to `main`, the app will auto-deploy to Render.

## 🧪 Example Passwords to Test

| Password         | Strength     |
| ---------------- | ------------ |
| `123456`         | Weak ⚠️      |
| `Welcome123`     | Moderate 🛡️ |
| `S!mpl3P@ss2024` | Strong 💪    |

## 📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute.

## 🤝 Contributing

Pull requests are welcome.
If you have suggestions or want to improve the UI or logic, feel free to open an issue or PR!

## 📬 Contact

Created by **\[Thoudaboina Sumanth]**
🌐 \[ LinkedIn :- https://www.linkedin.com/in/thoudaboina-sumanth-a25645215  )]

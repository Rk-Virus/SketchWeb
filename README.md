# 🎨 SketchWeb

A dynamic Flask-based web application for creating, storing, and managing sketches and content.  
Live: [https://sketchweb.onrender.com](https://sketchweb.onrender.com)

---

> ![sketch web](https://github.com/user-attachments/assets/f011fc81-8ee8-4297-8bc4-e5e66494b8c1)

---

## 🚀 Features

- 🖼️ Gallery view with dynamic content
- ✍️ Admin panel for adding and editing entries
- 📁 SQLite-based local storage (MySQL-ready)
- 🧩 Modular Flask structure
- 🌐 Deployed on Render with Gunicorn

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS (Jinja2 templating)
- **Database:** SQLite (optional: MySQL)
- **Deployment:** Render + Gunicorn

---

## ⚙️ Local Development

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/SketchWeb.git
cd SketchWeb
```

### 2. Set up environment
```bash
python -m venv venv
venv\Scripts\activate          # Windows
# or
source venv/bin/activate       # macOS/Linux

pip install -r requirements.txt
```

### 3. Set environment variables
Create a `.env` file:

```env
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
SECRET_KEY=your-secret-key
```

### 4. Run the app
```bash
flask run
```

## 🔒 Environment Variables Used

- `SQLALCHEMY_DATABASE_URI`
- `SECRET_KEY`
- `FLASK_ENV`
- `EMAIL`, `PASSWORD` (optional, for admin auth)

---


## 📝 License

MIT — free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

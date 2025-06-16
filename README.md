# ⚽ Premier League Stats App

A live Premier League standings viewer built with **Python**, **Tkinter**, and **API-Football**.

This desktop app pulls real-time standings from the [API-Football](https://www.api-football.com/) REST API and displays them in a clean graphical interface using Python’s built-in GUI library. Designed to be modular, the app will expand to include team pages, player stats, graphs, and more.

---

## 🚀 Features (Implemented So Far)

- ✅ Pulls live **Premier League standings** (season 2023)
- ✅ Clean GUI built using `tkinter` and `ttk.Treeview`
- ✅ Modular code split into:
  - `main.py` → launcher
  - `api.py` → handles API requests
  - `gui.py` → builds the interface

---

## 🛠 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/MantavyaS/plstats.git
cd plstats
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API key
Sign up at [RapidAPI](https://rapidapi.com/api-sports/api/api-football/) and subscribe to the free plan.

Open `api.py` and replace `"YOUR_API_KEY"` with your own key:
```python
headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
```

### 4. Run the app
```bash
python main.py
```

---

## 📦 Dependencies

- `requests` — for sending API requests
- `Pillow` — for image handling (logos coming soon)
- `tkinter` — built-in GUI toolkit

You can install them manually if needed:
```bash
pip install requests pillow
```

---

## 🧱 Folder Structure

```
plstats/
├── main.py          # Entry point
├── tkGui.py           # Tkinter interface
├── api.py           # API connection
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧪 Upcoming Features

- 🖼 Team logos + Premier League logo
- 📊 Team form (last 5 games)
- 📅 Fixtures and player list on team click
- 🔍 Search bar for teams or players
- 🎨 Improved styling (fonts, background, theme)
- 📈 Graphs for goals, points, etc.
=======
# plstats
Live Premier League Stats viewer using Python, Tkinter and API-football
>>>>>>> 19ab0a63e213b4f7e00fb42f8327f1a50947e5ef

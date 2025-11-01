# 🏆 FIFA Team Matcher
My friends and I got bored of the inbuilt Fifa Match predictor so we are building-FIFA Team Matcher. A web application that helps football enthusiasts find their ideal FIFA team based on their playing style and preferences. Whether you prefer attacking, defensive, or balanced gameplay, this app will suggest teams that align with your style.

## Features
- Generate balanced matchups for 2 or more players.
- Filter teams by:
  - Star rating (4.5 or 5 stars)
  - League.
- Ensure fair matchmaking by:
  - Matching teams of similar ratings
  - Option to force different/same league matchups
  - No duplicate team selection.


## Installation

1. Clone the repository
2. Install dependencies:
```sh
pip install -r requirements.txt
```

## Project Structure

```
fifa-team-matcher/
├── data/
│   └── teams.json         # Team data and ratings
├── modules/
│   ├── matcher.py         # Core matchmaking logic
│   └── team_loader.py     # Data loading utilities
├── test/
│   └── test_data_load.py  # Data loading tests
└── test_matcher.py        # Matcher functionality tests
```

## How to run the program
### 1️⃣ Clone the repo
git clone https://github.com/<your-username>/fifa-team-matcher.git
cd fifa-team-matcher

### 2️⃣ Create and activate virtual env
python -m venv venv
source venv/bin/activate  # macOS/Linux

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run tests
python tests/test_data_load.py
python tests/test_matcher.py

## Built With
- Python 3.11
- Flask
- JSON
- SQLite
- AWS App Runner

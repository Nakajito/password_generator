# Secure Password Generator

Project in Python + Reflex that generates secure passwords based on a length specified by the user.

Content
- `password_generator/` - App code (Reflex components).
- `requirements.txt` - Project dependencies.

Features
- Generates random passwords (letters, digits, and symbols).
- Recommended minimum length: 8 characters.
- Input validation and error messages in the UI.

Requirements
- Python 3.12
- (Optional) Virtualenv/venv

Quick installation
1. Clone the repository:

```bash
git clone https://github.com/Nakajito/password_generator.git
cd password_generator
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app (development)

This application is built with Reflex. To start the development server (according to local configuration):

```bash
source .venv/bin/activate
reflex run
```

Open your browser at the URL printed by Reflex (by default, this is usually `http://localhost:3000`).

Notes on structure
- `password_generator/components/` contains the UI components (title, description, generator box).
- `password_generator/layout/` contains the footer and related layout.
- `password_generator/utils.py` includes the `generate_password(length)` function, which can be tested independently.


Contributions
- If you want to contribute, create a new branch, make your changes, and open a pull request.

---

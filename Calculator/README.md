# 🧮 Calculator

A visually modern calculator application built using **Python** and **PyQt5**.

---

## 🔧 Features

* Basic operations: `+`, `-`, `*`, `/`, `=`, `.`, `C`
* Simple and clear layout using `QGridLayout`
* Styled using Qt StyleSheets for modern look
* Manual button creation (no for-loops)
* Fixed window size with aligned input field
* Handles errors like invalid expressions

---

## 📸 Screenshot

![Screenshot 2025-05-18 002817](https://github.com/user-attachments/assets/f241bef2-7cbf-4957-ab2e-11f4cc0efe45)

---

## 💻 Tech Stack

* Python 3.x
* PyQt5 (for GUI)
* Qt StyleSheet (for design)

---

## 🧠 How It Works

* A `QLineEdit` is used for displaying input/output.
* Each button (0-9, operators, clear, equal) is individually added to a `QGridLayout`.
* Button clicks append to the display or trigger actions (evaluate or clear).
* The `eval()` function is used to calculate the expression and show results.
* Any invalid input triggers an `"Error"` output.

---

## 🚀 Run the App

1. Install PyQt5 if not already:

   ```bash
   pip install PyQt5
   ```

2. Save the script as `Calculator.py`

3. Run the application:

   ```bash
   python Calculator.py
   ```

---

## 📌 Notes

* This project avoids OOP and loops intentionally for learning clarity.
* Great for beginners looking to start PyQt5 and GUI development.

---

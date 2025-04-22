# 🔐 Password Crack Time Estimator

A Python tool that estimates how long it would take to brute-force a given password, based on its complexity and length. Perfect for understanding the strength of your passwords and learning how attackers might approach cracking them.

---

## 🚀 Features

- Estimates brute-force cracking time based on:
  - Password length
  - Character types used (lowercase, uppercase, digits, symbols)
- Outputs time in a human-readable format
- Assumes a powerful attacker making **1 billion guesses per second**
- Lightweight and easy to use

---

## 🛠️ How It Works

1. Analyzes the characters in your password to determine the possible character set.
2. Calculates total combinations using `charset_size ^ password_length`.
3. Divides by a fixed guess rate (1 billion/sec) to estimate cracking time.
4. Converts the result into seconds, minutes, hours, days, or years.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/password-crack-time-estimator.git
cd password-crack-time-estimator

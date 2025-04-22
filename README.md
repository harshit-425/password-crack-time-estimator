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

▶️ Usage
Run the script with:
```bash
python password_crack_time_estimator.py

Enter your password when prompted:

Enter your password: S3cur3!Passw0rd
Estimated time to brute-force/crack your password: 5.32 billion years

📋 Example
Password | Estimated Crack Time
123456 | 0.00 seconds
P@ssw0rd | 11.61 years
F!r3Dr@g0n2025 | 5.12 billion years

⚠️ Disclaimer
This tool provides a theoretical estimate of brute-force cracking time. It does not account for:
  -Dictionary or rainbow table attacks
  -Password reuse from breaches
  -Advanced cracking techniques

Always use strong, unique passwords and enable two-factor authentication (2FA) for maximum security.

📄 License
This project is licensed under the MIT License. You are free to use, modify, and share it.

🤝 Contributing
Pull requests and feature ideas are welcome!

🌐 Author
Harshit Agrawal

## 🌐 Connect with Me

[💼 LinkedIn](https://www.linkedin.com/in/harshit-agrawal425/)  
[🛡️ TryHackMe](https://tryhackme.com/p/harshit.agrawal425)


Made with Python and a passion for cybersecurity.

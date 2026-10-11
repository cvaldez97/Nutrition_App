import sys
import time

# --- Typewriter effect ---
def type_text(text, speed=0.05, new_line=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if new_line:
        print()

# --- App Load In ---
def load_in():
        print("")
        print("")
        type_text("VALDEZ NUTRITION\nCalorie & Macro Calculator", 0.05)
        print("")
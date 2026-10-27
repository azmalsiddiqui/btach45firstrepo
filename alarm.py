import datetime
import time
import sys

def set_alarm():
    print("--- Python Alarm Clock ---")
    
    # 1. Get the alarm time from the user
    while True:
        alarm_input = input("Enter alarm time in 24-hour format (HH:MM:SS): ").strip()
        try:
            # Validate input format
            datetime.datetime.strptime(alarm_input, "%H:%M:%S")
            break
            
        except ValueError:
            print("❌ Invalid format. Please use HH:MM:SS (e.g., 07:30:00 or 18:15:00).\n")

    print(f"\n🔔 Alarm successfully set for {alarm_input}")
    print("Press Ctrl+C at any time to cancel.")
    print("Monitoring time...")

    # 2. Check the time continuously
    try:
        while True:
            # Get the current system time formatted as a string
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            
            # Print an update on the same line to keep the terminal clean
            sys.stdout.write(f"\rCurrent Time: {current_time}")
            sys.stdout.flush()

            # Check if current time matches the user's alarm time
            if current_time == alarm_input:
                print("\n\n🚨 WAKE UP! Time's up! 🚨")
                trigger_sound()
                break

            # Wait 1 second before checking again to manage CPU usage
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n👋 Alarm cancelled. Goodbye!")

def trigger_sound():
    # Detect platform to use the built-in system alert audio
    if sys.platform == "win32":
        import winsound
        # frequency=1000Hz, duration=2000ms
        winsound.Beep(1000, 2000) 
    else:
        # For macOS and Linux: Uses the terminal terminal bell sequence (\a)
        for _ in range(5):
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(0.5)

if __name__ == "__main__":
    set_alarm()

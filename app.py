import pyautogui
import time

print("🔁 Auto Ad Skipper is running. Watching for 'Skip Ad' button...")

def detect_and_click_skip():
    try:
        # Save screenshot (debug)
        pyautogui.screenshot('current_screen.png')

        # Try detecting the button
        location = pyautogui.locateOnScreen('skip_button.png', confidence=0.7)
        if location:
            print("🎯 'Skip Ad' button found!")
            pyautogui.moveTo(pyautogui.center(location))
            pyautogui.click()
            print("✅ Ad skipped!")
        else:
            print("⏳ Still watching...")
    except Exception as e:
        print("❌ Error:", e)

while True:
    detect_and_click_skip()
    time.sleep(2)

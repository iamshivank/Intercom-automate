# Save as: intercom_auto.py
from pyautogui import click, typewrite
import time
from pynput import keyboard

# ==================== CONFIGURATION ====================
MESSAGE = "Thanks for reaching out! Give us just a moment and we'll check for you."

# Intercom reply box coordinates (center of text input on 1920×1080)
REPLY_BOX_X = 960
REPLY_BOX_Y = 1015

# ACTIVATION KEY: Press F9 to activate/deactivate
ACTIVATION_KEY = keyboard.Key.f9

# SEND MESSAGE KEY: Press F10 to send the message
SEND_KEY = keyboard.Key.f10

# =======================================================

class IntercomAutomation:
    def __init__(self):
        self.active = False
        
    def send_message(self):
        """Clicks Intercom reply box and types the message"""
        if not self.active:
            print("⚠️  Not active! Press F9 to activate first")
            return
        click(REPLY_BOX_X, REPLY_BOX_Y)
        time.sleep(0.05)
        typewrite(MESSAGE, interval=0.005)
        print(f"✓ Sent: {MESSAGE}")

    def activate(self):
        """Activate the automation"""
        self.active = True
        print("🟢 ACTIVATED - Press F10 to send message")

    def deactivate(self):
        """Deactivate the automation"""
        self.active = False
        print("🔴 DEACTIVATED")

    def toggle(self):
        """Toggle activation on/off"""
        if self.active:
            self.deactivate()
        else:
            self.activate()

    def on_press(self, key):
        """Handle key presses"""
        # Toggle activation with F9
        if key == ACTIVATION_KEY:
            self.toggle()
        
        # Send message with F10
        if key == SEND_KEY:
            self.send_message()

    def start_listener(self):
        """Start listening for hotkeys"""
        print("⌨️  Intercom Automation Ready")
        print("   F9  = Activate/Deactivate")
        print("   F10 = Send Message (when active)")
        print("")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

# =======================================================

if __name__ == "__main__":
    automation = IntercomAutomation()
    automation.start_listener()
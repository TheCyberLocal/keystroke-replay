"""
 KeyReplay is a Python-based tool designed to automate repetitive keyboard tasks. 
It allows users to record a sequence of keystrokes and then replay them on demand. 
This script uses the 'pynput' library for capturing keyboard input and 'pyautogui' for simulating the keystrokes. 
It's particularly useful for automating routine data entry, form submissions, or any other tasks involving repetitive keyboard operations. 
Remember to use this script responsibly and ethically.
"""

from pynput import keyboard  # Importing the keyboard module from pynput
import pyautogui  # Importing the pyautogui module for simulating keyboard actions
import time  # Importing time module for adding delays


class KeyboardMacro:
    def __init__(self):
        self.recorded_keys = []  # Initialize an empty list to store keystrokes
        self.recording = False  # Flag to track whether recording is active

    def start_recording(self):
        self.recording = True  # Set recording flag to True
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()  # Start listening for key presses

    def on_press(self, key):
        if key == keyboard.Key.esc:
            self.recording = False  # Stop recording if Escape key is pressed
            return False  # Stop the listener
        if self.recording:
            self.recorded_keys.append(key)  # Append the pressed key to the recorded list

    def play_back(self):
        for key in self.recorded_keys:  # Iterate over recorded keystrokes
            if isinstance(key, keyboard.Key):
                pyautogui.press(key.name)  # Simulate special key press
            else:
                pyautogui.press(key.char)  # Simulate character key press
            time.sleep(0.1)  # Short delay between keystrokes for realism


# Example usage of the KeyboardMacro class
if __name__ == "__main__":
    macro = KeyboardMacro()  # Create an instance of KeyboardMacro
    print("Recording... Press Esc to stop.")
    macro.start_recording()  # Start recording keystrokes
    print("Playing back...")
    macro.play_back()  # Play back the recorded keystrokes

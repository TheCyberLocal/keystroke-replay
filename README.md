# KeyReplay: Keyboard Macro Tool

## Overview
KeyReplay is a Python script for recording and playing back keyboard inputs. It's designed to automate repetitive keystrokes.

## Structure

### Class: KeyboardMacro
- **Attributes**:
  - `recorded_keys`: List to store recorded keystrokes.
  - `recording`: Boolean to track recording status.

- **Methods**:
  - `start_recording`: Starts the keyboard listener and records keystrokes.
  - `on_press`: Callback for each key press.
    - Records key if `recording` is True.
    - Stops recording if Escape key is pressed.
  - `play_back`: Plays back the recorded keystrokes.

### Main Script
- Create an instance of `KeyboardMacro`.
- Start recording keystrokes.
- On completion, play back the keystrokes.

## Usage
- Run `KeyReplay`.
- Press keys to be recorded.
- Press `Esc` to stop recording.
- Watch as the script replays the keystrokes.

---

**Note**: This README is intended to provide a high-level overview of the script's structure and functionality in a user-friendly format. It is written in pseudocode to illustrate the logic and flow of the program in a readable manner.

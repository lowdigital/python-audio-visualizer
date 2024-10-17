![DEMO](demo.jpg)

# Python Audio Visualizer

This is a simple audio visualizer built with Python using `pygame` and `pycaw` to capture system audio and visualize it as a dynamic circle. The program focuses on visualizing the audio volume of a specific process (e.g., `chrome.exe`) and displays it in a colorful and interactive form.

## Features

- Captures audio from a specified process (default is `chrome.exe`).
- Visualizes audio levels with dynamic circular lines.
- Customizable sensitivity and background colors.
- Includes a `run.bat` script for easy environment setup and execution.

## Prerequisites

- Python 3.x installed on your machine.
- Ensure you have the correct audio drivers installed to allow `pycaw` to capture system audio.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/lowdigital/python-audio-visualizer.git
cd python-audio-visualizer
```

### 2. Run the application

For Windows users, you can simply execute the `run.bat` file, which will create a virtual environment, install all necessary dependencies, and run the script.

```bash
run.bat
```

The script will:

1. Check if a virtual environment exists.
2. If not, it will create a new one.
3. Install dependencies from `requirements.txt`.
4. Run the visualizer.

### 3. Manual installation and running

Alternatively, you can manually set up the environment:

```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Usage

By default, the visualizer captures the audio from the `chrome.exe` process. Make sure that Chrome or another audio-producing application is running for the visualizer to work.

You can modify the target process by changing the `target_process_name` variable in `app.py` to the name of the process you want to capture (e.g., `vlc.exe`, `spotify.exe`).

## Customization

You can customize the following parameters in the `app.py` file:

- `background_color`: Change the background color (RGB format).
- `sensitivity`: Adjust the visual sensitivity to the audio input.

## Dependencies

- `pygame`
- `pycaw`
- `numpy`
- `comtypes`
- `sounddevice`

All dependencies are listed in `requirements.txt` and will be installed automatically when running `run.bat`.

## Notes

- The visualizer will only work if the specified audio process is active and producing sound.
- If you experience issues capturing audio, ensure your system’s audio devices are properly configured.

## License

This project is open-source and available under the MIT License.

# AskUI Automation Project

## Overview
This project utilizes AskUI, a powerful automation tool, to interact with desktop applications on macOS. The script automates tasks such as opening applications, extracting information from files, and interacting with the Notes app. The automation is achieved using the VisionAgent from AskUI, which allows for seamless interaction with the user interface.

## Prerequisites
- **Python**: Ensure you have Python installed on your system.
- **AskUI**: Install the AskUI library to enable UI automation.
- **dotenv**: Used for loading environment variables.
- **Subprocess**: Utilized for opening applications on macOS.
- **Time**: Used to introduce delays for application loading.

## Installation
1. Clone the repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Functionality
The script performs the following tasks:
- **Open Downloads Folder**: Uses the subprocess module to open the Downloads folder on macOS.
- **Open PDF File**: Utilizes AskUI to find and open a specific PDF file named "RAKESH MISHRA.pdf".
- **Extract Information**: Extracts the name, date of birth, and time of birth from the PDF using AskUI's `get` method.
- **Open Notes App**: Opens the Notes application using the subprocess module.
- **Create and Paste Note**: Creates a new note in the Notes app and pastes the extracted information.

## Usage
Run the script using Python:
```bash
python main.py
```
The script will automatically perform the tasks as described, interacting with the desktop environment to extract and paste information.

## Workflow Recording
For a visual demonstration of the workflow, you can view the recording https://www.loom.com/share/ee845bdfdcc34d27b7be1a0cc7f136ae?sid=40d98bc8-7734-44b5-b34d-63935db212dc.

---

This README provides a comprehensive overview of the AskUI automation script, detailing its setup, functionality, and usage. If you have any further questions or need additional information, feel free to ask
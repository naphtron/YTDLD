
<p align="center" width="100%">
    <img width="33%" src="https://github.com/naphtron/YTDLD/blob/main/logo.png" > 
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# YouTube Downloader App (YTDLD)

Welcome to the YouTube Downloader app! This app allows you to download YouTube videos by simply entering a valid YouTube URL.

## How to Use

1. **Enter YouTube URL**: Launch the app and you'll find a textbox. Enter the URL of the YouTube video you want to download.

2. **Download**: After entering the URL, press the "Download" button to start the download process.

3. **Progress**: You'll see a progress bar indicating the download progress. Once it's completed, you'll find the downloaded video in your device's storage.

4. **Enjoy**: Enjoy your downloaded YouTube video offline!

## Building the App

If you want to build the app yourself or make modifications, follow these steps:

### Prerequisites

1. **Install Buildozer**: Make sure you have Buildozer installed on your development machine. You can install it using pip:
   
   ```bash
    pip install buildozer

**Note for Windows Users**: If you're using a Windows machine, it's recommended to use Windows Subsystem for Linux (WSL) to run Buildozer.
2.  **Create a Directory:** Start by creating a new directory (folder) for your project. You can name it whatever you like.

3. **Open the folder using your favorite code editor**

4. **Set Up Environment**: Create a Python virtual environment and activate it:
   
   ```python
    python -m venv venv
    source venv/bin/activate # On Windows, use 'venv\Scripts\activate'

5. **Dependencies**: Install the necessary dependencies for your app, including `kivy`, `kivymd`,`logging` and `pytube`:
      ```python
     pip install kivy kivymd pytube logging
      
### Building the APK

1. **Navigate to the Project Directory:** Open a terminal or command prompt and navigate to the project directory. You'll do most of your work within this directory.

2. **Initialize the Project Configuration:** Run the following command to create a `buildozer.spec` template file for your project:

    ```bash
    buildozer init
    ```

    This command will interactively prompt you for various project configuration options and generate a `buildozer.spec` file based on your responses.

3. **Edit the `buildozer.spec` File:** Open the `buildozer.spec` file in a text editor. Locate **requirements** line in the file.
   Edit to,
    ```text
    requirements = python3,kivy,kivymd,pillow,pytube,logging
    ```
    making sure the dependencies are installed when the app builds.

5. **Build the APK:** When you're ready to build your Android app, open a terminal or command prompt in the project directory and run the following command:

    ```bash
    buildozer -v android debug
    ```

    This command tells Buildozer to compile your app into an APK, deploy it to a connected device or emulator, and run it. The resulting APK will be placed in the `bin` directory of your project.

6. **Transfer and Install the APK:** Transfer the generated APK file to your Android device (e.g., via USB, email, cloud storage) and install it on your device.

7. **Run Your App:** After installation, you can run your Android app on your device just like any other app.

   






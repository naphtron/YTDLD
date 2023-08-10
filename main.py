import os
import certifi
import ssl
import logging 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from pytube import YouTube
from kivy.uix.image import AsyncImage, Image
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton
from kivymd.toast import toast  # Import the toast module from KivyMD
from kivy.utils import platform

os.environ['SSL_CERT_FILE'] = certifi.where()

ssl._create_default_https_context = ssl._create_stdlib_context

# Set up logging to a file
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

if platform == "linux":
    from android.permissions import Permission, request_permissions
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

class YouTubeDownloaderApp(MDApp):  # Inherit from MDApp, not App.
    def build(self):
        self.theme_cls.theme_style = "Dark"
        
        self.url_input = TextInput(hint_text="    Enter YouTube URL",padding_y = ( 20,20),size_hint = (1,0.5), multiline=False)
        self.download_button = MDFloatingActionButton(
            icon="download",
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            on_press=self.on_download_button_press,
            on_release=self.on_download_button_release,
        )
        self.progress_label = Label(text="")
        self.progress_bar = ProgressBar(max=100, size_hint_y=None, height=30)

        self.loading_spinner = AsyncImage(source="spinner.gif", size_hint=(None, None), size=(50, 50))
        self.loading_spinner.opacity = 0  # Initially hide the spinner.

        layout = BoxLayout(orientation="vertical")
        layout.size_hint = (0.6, 0.7)
        layout.pos_hint = {"center_x":0.5, "center_y":0.4}
        layout.add_widget(Image(source="logo.png"))
        layout.add_widget(self.url_input)

        # Wrap the button and spinner in a FloatLayout to overlay them.
        self.button_spinner_layout = FloatLayout(size_hint=(1, None), height=50)
        self.button_spinner_layout.add_widget(self.download_button)
        self.button_spinner_layout.add_widget(self.loading_spinner)

        layout.add_widget(self.button_spinner_layout)
        layout.add_widget(self.progress_label)
        layout.add_widget(self.progress_bar)
        return layout

    def on_download_button_press(self, instance):
        # Show the loading spinner and change the button color on press.
        self.loading_spinner.opacity = 1
        self.download_button.md_bg_color = [0, 0, 1, 1]

    def on_download_button_release(self, instance):
        video_url = self.url_input.text.strip()
        if not video_url:
            self.progress_label.text = "Please enter a valid YouTube URL"
            return

        try:
            yt = YouTube(video_url, on_progress_callback=self.show_progress)
            video = yt.streams.get_highest_resolution()

            # Get the "Download" folder path on Android.
            download_folder = os.path.join(os.getenv("EXTERNAL_STORAGE"), "Download")

            if not os.path.exists(download_folder):
                os.makedirs(download_folder)

            # Save the video in the "Download" folder.
            video.download(output_path=download_folder)

            # Show a KivyMD Toast when download completes successfully.
            self.loading_spinner.opacity = 0  # Hide the loading spinner.
            self.download_button.md_bg_color = [0, 0.7, 0.2, 1]  # Restore the button color.

            toast("Download Completed 😎")
        except Exception as e:
            self.progress_label.text = f"An error occurred: {str(e)}"
            # Log the error to the file
            logging.error(f"An error occurred: {str(e)}")

            # Restore the button color if an error occurred.
            self.loading_spinner.opacity = 0  # Hide the loading spinner.
            self.download_button.md_bg_color = [0, 0.7, 0.2, 1]  # Restore the button color.

    def show_progress(self, stream, chunk, bytes_remaining):
        total_bytes = stream.filesize
        bytes_downloaded = total_bytes - bytes_remaining
        download_percentage = bytes_downloaded / total_bytes * 100
        self.progress_label.text = f"Downloading... {download_percentage:.0f}%"
        self.progress_bar.value = download_percentage

if __name__ == "__main__":
    YouTubeDownloaderApp().run()


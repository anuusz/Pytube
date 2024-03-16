from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QProgressBar, QMessageBox
from PyQt6.QtCore import Qt, QUrl
from pytube import YouTube
import threading
import sys

class YouTubeDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Downloader")

        self.title_label = QLabel("Insert link")
        self.link_input = QLineEdit()
        self.finish_label = QLabel("")
        self.progress_label = QLabel("0%")
        self.progress_bar = QProgressBar()
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.start_download)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.link_input)
        layout.addWidget(self.finish_label)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.download_button)

    def start_download(self):
        link = self.link_input.text()
        if link:
            threading.Thread(target=self.download_thread, args=(link,)).start()

    def download_thread(self, link):
        try:
            yt_object = YouTube(link, on_progress_callback=self.on_progress)
            video = yt_object.streams.get_highest_resolution()

            download_path = '/home/anuusz/Downloads'  # ubah anuusz menjadi nama pc/akun pc anda
            video.download(download_path)

            self.finish_label.setText("Download Complete!, Check your File Manager.")
        except Exception as e:
            self.finish_label.setText("Download Error")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        per = str(int(percentage_of_completion))
        self.progress_label.setText(per + '%')
        self.progress_bar.setValue(percentage_of_completion)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeDownloaderApp()
    window.show()
    sys.exit(app.exec())

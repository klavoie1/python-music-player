import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer  # For audio playback

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")

        # Initialize Pygame mixer
        mixer.init()

        self.playlist = []  # List to store songs
        self.current_song = None  # Currently playing song

        self.create_ui()


    def create_ui(self):
        self.song_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.song_listbox.pack(padx=100, pady=100)

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", foreground="white", background="green", command=self.play)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack(pady=5)

        self.add_folder = tk.Button(root, text="Add Folder", command=self.add_songs_from_folder)
        self.add_folder.pack(pady=5)

    def add_songs_from_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            for file in os.listdir(folder_path):
                if file.endswith(".mp3"):
                    self.playlist.append(os.path.join(folder_path, file))
                    self.song_listbox.insert(tk.END, file)

    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.song_listbox.insert(tk.END, file_path)

    def play(self):
        selected_song = self.song_listbox.curselection()
        if selected_song:
            self.current_song = self.playlist[selected_song[0]]
            mixer.music.load(self.current_song)
            mixer.music.play()

    def pause(self):
        if self.current_song:
            mixer.music.pause()

if __name__ == "__main__":
    


    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
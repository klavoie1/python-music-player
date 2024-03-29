import os
import tkinter as tk
from tkinter.ttk import *
from tkinter import HORIZONTAL, LEFT, RIGHT, filedialog
from pygame import mixer  # For audio playback

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.maxsize(540,250)
        self.root.minsize(540,250)
        
        mixer.init() # Initialize Pygame mixer

        self.playlist = []  # List to store songs
        self.current_song = None  # Currently playing song

        self.create_ui()


    # UI Creation
    def create_ui(self):
        self.song_listbox = tk.Listbox(self.root,width=50, height=10, selectmode=tk.SINGLE)
        self.song_listbox.pack(padx=5, pady=5)

        self.add_folder = tk.Button(root, text="Add Folder", foreground="#37474f", background="#81d4fa", width=10, height=2, command=self.add_songs_from_folder)
        self.add_folder.pack(padx=5, pady=5, side=LEFT)

        self.add_button = tk.Button(self.root, text="Add Song", foreground="#37474f", background="#9575cd", width=10, height=2, command=self.add_song)
        self.add_button.pack(padx=5, pady=5, side=LEFT)

        self.play_button = tk.Button(self.root, text="Play", foreground="#37474f", background="#81c784", width=10, height=2, command=self.play)
        self.play_button.pack(padx=5, pady=5, side=RIGHT)

        self.pause_button = tk.Button(self.root, text="Pause", foreground="#37474f", background="#c6715e", width=10, height=2, command=self.pause)
        self.pause_button.pack(padx=5, pady=5, side=RIGHT)

        self.unpause_button = tk.Button(self.root, text="Unpause", foreground="#37474f", background="#fff59d", width=10, height=2, command=self.unpause)
        self.unpause_button.pack(padx=5, pady=5, side=RIGHT) 

        self.exit_button = tk.Button(self.root, text="Exit", foreground="#37474f", background="#c12604", width=10, height=2, command=self.exit_app)
        self.exit_button.pack(padx=5, pady=5, side=RIGHT)

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

    def unpause(self):
        mixer.music.unpause()

    def exit_app(self):
        os.abort()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
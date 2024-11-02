import tkinter as tk
from tkinter import filedialog
from pygame import mixer

root = tk.Tk()
root.title("Music Player")
root.geometry("300x200")

song_label = tk.Label(root, text="Music Player", font=("Arial", 12))
song_label.pack(pady=20)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=10)


stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    song_label.config(text=filename)

def play_music():
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def stop_music():
    mixer.music.stop()

root.mainloop()
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
import random


ENDSONG = 25


def play():
    current_song_index = playlist.curselection()
    if current_song_index:
        current_song = playlist.get(current_song_index)
        mixer.music.load(current_song)
        mixer.music.play()


def pause():
    mixer.music.pause()


def resume():
    mixer.music.unpause()


def stop():
    mixer.music.stop()


def browse_file():
    directory_path = filedialog.askdirectory()
    if directory_path:
        os.chdir(directory_path)
        songs = [file for file in os.listdir() if file.endswith(".mp3")]
        playlist.delete(0, END)
        for song in songs:
            playlist.insert(END, song)


def next_song():
    current_song_index = playlist.curselection()
    if current_song_index:
        next_index = current_song_index[0] + 1
        if next_index < playlist.size():
            playlist.selection_clear(0, END)
            playlist.selection_set(next_index)
            playlist.activate(next_index)
            play()


def previous_song():
    current_song_index = playlist.curselection()
    if current_song_index:
        prev_index = current_song_index[0] - 1
        if prev_index >= 0:
            playlist.selection_clear(0, END)
            playlist.selection_set(prev_index)
            playlist.activate(prev_index)
            play()


def shuffle_songs():
    songs_list = list(playlist.get(0, END))
    random.shuffle(songs_list)
    playlist.delete(0, END)
    for song in songs_list:
        playlist.insert(END, song)


def loop_song():
    mixer.music.set_endevent(ENDSONG)
    mixer.music.play(-1)


root = Tk()
root.resizable(0, 0)
root.title("Music Player")

mixer.init()

playlist = Listbox(
    root,
    selectmode=MULTIPLE,
    bg="black",
    fg="white",
    font=("Helvetica", 12),
    width=50,
    height=20,
)
playlist.grid(row=1, columnspan=6, padx=10, pady=10)

browsebtn = Button(root, text="Browse", command=browse_file, bg="blue", fg="white")
browsebtn.grid(row=0, column=0, padx=5, pady=5)

playbtn = Button(root, text="Play", command=play, bg="yellow", fg="blue")
playbtn.grid(row=0, column=1, padx=5, pady=5)

pausebtn = Button(root, text="Pause", command=pause, bg="yellow", fg="red")
pausebtn.grid(row=0, column=2, padx=5, pady=5)

resumebtn = Button(root, text="Resume", command=resume, bg="yellow", fg="green")
resumebtn.grid(row=0, column=3, padx=5, pady=5)

stopbtn = Button(root, text="Stop", command=stop, bg="red", fg="black")
stopbtn.grid(row=0, column=4, padx=5, pady=5)

prevbtn = Button(root, text="Previous", command=previous_song, bg="orange", fg="white")
prevbtn.grid(row=0, column=5, padx=5, pady=5)

nextbtn = Button(root, text="Next", command=next_song, bg="orange", fg="white")
nextbtn.grid(row=0, column=6, padx=5, pady=5)

shufflebtn = Button(
    root, text="Shuffle", command=shuffle_songs, bg="purple", fg="white"
)
shufflebtn.grid(row=0, column=7, padx=5, pady=5)

loopbtn = Button(root, text="Loop", command=loop_song, bg="green", fg="white")
loopbtn.grid(row=0, column=8, padx=5, pady=5)

mainloop()

import os
import string
from multiprocessing import Process
from threading import Thread

from playsound import playsound
from pynput import keyboard

alphabets = list(string.ascii_lowercase)
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
freq = 44100
duration = 5

pending_sound_processes = []
running_sound_processes = {}


def stop_sound_processes():
    for sound_process_id, sound_process in running_sound_processes.items():
        if sound_process.is_alive():
            sound_process.terminate()
    running_sound_processes.clear()


def sound_handler():
    while True:
        if len(pending_sound_processes) > 0:
            stop_sound_processes()
            sound_process = pending_sound_processes.pop(0)
            sound_process.start()
            running_sound_processes[sound_process.pid] = sound_process


def play_default_file(name):
    music_file_name = f'sounds/{name}.wav'
    if os.path.exists(music_file_name):
        playsound(music_file_name)


def on_activate_1(*args):
    if len(args) == 1:
        pending_sound_processes.append(Process(target=play_default_file, args=(args[0],)))


if __name__ == '__main__':
    sound_handler_thread = Thread(target=sound_handler)
    sound_handler_thread.start()

    hotkey_dict = {}
    for alphabet in alphabets:
        hotkey_dict[f'1+{alphabet}'] = lambda key=alphabet: on_activate_1(key)

    with keyboard.GlobalHotKeys(hotkey_dict) as h:
        h.join()

    sound_handler_thread.join()

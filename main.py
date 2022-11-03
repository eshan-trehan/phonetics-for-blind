from pynput import keyboard
import string
from playsound import playsound


def on_activate(*args):
    if len(args) == 1:
        playsound(f'sounds/{args[0]}.mp3')


hotkey_dict = {}
alphabets = list(string.ascii_lowercase)
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for alphabet in alphabets:
    hotkey_dict[f'<cmd>+{alphabet}'] = lambda key=alphabet: on_activate(key)

for vowel in vowels:
    for consonant in consonants:
        hotkey_dict[f'<shift>+{vowel}+{consonant}'] = lambda key1=vowel, key2=consonant: on_activate(key1, key2)

with keyboard.GlobalHotKeys(hotkey_dict) as h:
    h.join()

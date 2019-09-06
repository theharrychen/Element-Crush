import pygame

sound_dict = {}

#Loads all sound files
def load():
    sound_names = ["pop", "win", "lose", "double", "triple", "epic", "legendary"]
    for i in range(len(sound_names)):
        file_path = "sounds/" + sound_names[i] + ".wav"
        sound_dict[sound_names[i]] = pygame.mixer.Sound(file_path)

def play_effect(name):
    effect = sound_dict[name]
    effect.play()

#Plays a specific sound effect based on the combo count
def play_combo(combo_count):
    if combo_count >= 5:
        play_effect("legendary")
    elif combo_count == 4:
        play_effect("epic")
    elif combo_count == 3:
        play_effect("triple")
    elif combo_count == 2:
        play_effect("double")

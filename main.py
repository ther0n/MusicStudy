import sys
import sox
import os, random
import time
from pygame import mixer

def main():
    print("Initializing pygame for audio playback")
    mixer.init()
    
    while(True):
        input("\nPress enter to play the next clip")
        try:
            os.remove("song.wav")
        except OSError:
            pass
        next_song = pick_song()
        duration = sox.file_info.duration(next_song)
        max_start = round(duration, 0)-30
        start = random.randint(0, max_start)
        clip = sox.Transformer()
        clip.trim(start,start+30)
        clip.convert(44100)
        clip.build(next_song, "song.wav")
        sound = mixer.Sound("song.wav")
        sound.play()
        input("Press enter to reveal the song info")
        mixer.stop()
        # Song file name must be formatted "[Title]-[People/Form]-[Composer/Country]-[Category].flac"
        song_info = os.path.splitext(next_song.split("/")[1])[0].split("-")
        print("\n\tTitle: " + song_info[0] + 
              "\n\tPeople/Form: " + song_info[1] +
              "\n\tComposer/Country: " + song_info[2] +
              "\n\tCategory: " + song_info[3])

def pick_song():
    song = random.choice(os.listdir(os.getcwd() + "/songs"))
    while(not song.endswith(".ogg")):
        song = random.choice(os.listdir(os.getcwd() + "/songs"))
    return "songs/" + song

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')  # Make ctrl + c look nicer
        sys.exit(0)
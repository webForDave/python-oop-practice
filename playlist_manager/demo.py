class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


    def get_duration_in_minutes(self):
        seconds = self.duration

        if seconds % 60 == 0:
            return seconds // 60
        
        seconds_part = seconds % 60
        minutes = seconds // 60
        return f"{minutes}:{seconds_part}"
    
    def play(self):
        return f"Playing: {self.title} by {self.artist}"
    


def get_inputs():
    title = input('Song name: ').strip()
    artist = input('Song Artist: ').strip()
    duration = int(input('Song Duration (in seconds): ').strip())
    return title, artist, duration

song1 = Song(*get_inputs())

# print(song1.get_duration_in_minutes())
print(song1.play())

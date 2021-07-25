from user import User
import playlist

simon = User('Simon')
tina = User('Tina')
jazz = playlist.Jazz()
jazz.attach(simon)
jazz.attach(tina)
jazz.add_track('Miles Davis - Freddie Freeloader')
simon.play_song()
tina.play_song()
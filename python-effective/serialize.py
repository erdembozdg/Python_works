import pickle

class GameState:
    def __init__(self, level = 0, lives = 4):
        self.level = level
        self.lives = lives
        
state = GameState()
state.level = 0
state.lives = 4

file = "game_state.bin"
with open(file, "wb") as f:
    pickle.dump(state, f)
with open(file, "rb") as f:
    state_after = pickle.loads(f.read())
print(state_after.__dict__)

assert isinstance(state_after, GameState)
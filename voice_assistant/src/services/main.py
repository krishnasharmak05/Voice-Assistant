import src.services.database as db
from src.helper.classes import Listener, Voice_Assistant


def main():
    listener = Listener()
    listener.start_listening()
    print("Testing")
# On hotkey detection, make a voice assistant and run listener();

if __name__ == "__main__":
    main()
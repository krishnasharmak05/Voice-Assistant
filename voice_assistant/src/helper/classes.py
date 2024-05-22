# TODO: Read, Refactor and rebuild this code.
# TODO, Important AF: Fix Listener().__hotkey_detector().


import voice_assistant.src.services.database as db


class Voice_Assistant:
    """
    A class representing a voice assistant .

    Attributes:
        name (str): The name of the voice assistant. This defaults to "JARVIS".

    Methods:
        start(): Initializes the voice assistant.
        listener(): Listens for hotkey presses.
        __init__listener(): Code to initialize the hotkey listener.
        __del__(): Initializes the hotkey listener when the voice assistant is deleted by internally calling the __init_listener() method.
    """

    name = "JARVIS"

    def __init__(self, name="JARVIS"):
        """
        Initializes the voice assistant.

        Args:
            name (str, optional): The name of the voice assistant. Defaults to "JARVIS".
        """
        self.name = name

    def start(self):
        # Initialize the Voice Assistant.
        pass

    def listen_for_commands(self):
        # return lower_command and then delete the current Voice_Assistant object using the __del__ method.
        pass

    def __init_listener(self):
        """
        Private function to initialize a listener object.
        """

        # global listener
        listener = Listener()
        listener.start_listening()

    def __del__(self):
        # Initialize hotkey-listener.
        """
        Initializes the listener object using the __init_listener method when the voice assistant object is deleted.
        """

        self.__init_listener()


class Listener:
    """
    TODO: Add docs here!!
    """

    def __init__(self):
        pass

    def start_listening(self):
        self.__hotkey_detector()
        pass

    # TODO: Fix this function. Make it get the name and all of that shit properly.
    def __hotkey_detector(self):
        # TODO: Do something to detect the hotkey.... Also, determine what the hotkey will be.
        name = db.getName()
        # va = Voice_Assistant(name)
        # va.start()
        # print(f"Hotkey Detected! Activating Voice Assistant - {va.name}")
        self.__del__()

    def __del__(self):
        pass




# TODO: Make it possible for me to call the Voice Assistant from the terminal itself. Maybe use click?

from voice_assistant.src.helper.classes import Voice_Assistant

def test_first() -> None: # This test won't work, clearly.... (drawling....)!!!
    name_list = ["a", "random", "ChatGPT", "Google Assistant", "Siri", "Alexa", "Unknown", "Anonymous"]
    assert Voice_Assistant().name == "JARVIS"
    for i in name_list:
        assert Voice_Assistant(i).name == i
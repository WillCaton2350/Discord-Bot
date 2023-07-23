from talk import greetings,answ,greetResponse,howAreYou,imGoodVar,endingState,quitMsg
import random
import json


def get_response(message: str) -> str:
    with open("dictionary.json", 'r') as json_file:
        definitions = json.load(json_file)

    define_phrases = ['Hey, can you define',"what's the definition for",'define', 'definition of', 'definition for', 'meaning of',"what's the meaning of","what's the definition of","can you define", "can you tell me the definition of","can you tell me the meaning of"]
    
    definitions = {key.lower(): value for key, value in definitions.items()}

    for phrase in define_phrases:
        if message.lower().startswith(phrase):
            word_to_define = message[len(phrase):].strip().lower()
            if word_to_define in definitions:
                return definitions[word_to_define]

    if message.lower() == 'roll':
        return str(random.randint(1, 6)) + " 🎲"
    
    if message.lower() == 'black hat':
        return 'You tryna hack bro?'

    if message.lower() == '!help':
        return '''`Guide:
- 'Define' 📝
- limited definitions 📄
- Webster's dictionary 📖
- Private Msg "?" 📩
- Bot Guide "!help" 🤖
- black hat 🎩
- Type "roll" 🎲`'''
    
    if message.lower() in greetings:
        return random.choice(greetResponse)
    
    if message.lower() in howAreYou:
        return random.choice(imGoodVar)
    
    if message.lower() in endingState:
        return random.choice(answ)
    
    if message.lower() in quitMsg:
        return 'Goodbye!'
    print(f"Unhandled message: '{message}'")
    return "Sorry I didn't understand what you said... Try typing !help"

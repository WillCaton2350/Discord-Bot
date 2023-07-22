import random
import json

def get_response(message: str) -> str:
    with open("dictionary.json", 'r') as json_file:
        definitions = json.load(json_file)

    define_phrases = ['define', 'definition of', 'definition for', 'meaning of']
    
    definitions = {key.lower(): value for key, value in definitions.items()}

    for phrase in define_phrases:
        if message.lower().startswith(phrase):
            word_to_define = message[len(phrase):].strip().lower()
            if word_to_define in definitions:
                return definitions[word_to_define]


    if message.lower() == '!help':
        return '''`Guide:
- Activation - Define 
- limited definitions
- Utilizes the Webster dictionary`'''

    greetings = ['hello',','hey there', 'hey','hia', 'yo', 'you there?', 'hi']
    if message.lower() in greetings:
        return "Hey! Type !help for a Bot Guide"
    

    print(f"Unhandled message: '{message}'")
    return "Sorry I didn't understand what you said... Try typing !help"

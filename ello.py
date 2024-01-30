#!/usr/bin/env python3

import os
from googletrans import Translator

def get_current_language():
    return os.getenv("LANG", "en_US")[:5]

def translate_message(message, target_language):
    translator = Translator()
    translation = translator.translate(message, dest=target_language)
    return translation.text

def main():
    current_language = get_current_language()
    original_message = "Hello, World!"

    if current_language != "en_US":
        translated_message = translate_message(original_message, current_language)
        print(translated_message)
    else:
        print(original_message)

if __name__ == "__main__":
                                                                            main()

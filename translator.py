import deepl
import os
from dotenv import load_dotenv

# Načtení API klíče z keys.env souboru
load_dotenv("keys.env")  # Specifikujeme název souboru
API_KEY = os.getenv("DEEPL_API_KEY")

translator = deepl.Translator(API_KEY)

def translate_text(text, src_lang="CS", dest_lang="EN-GB"):
    try:
        print("Translating text...")
        result = translator.translate_text(text, source_lang=src_lang, target_lang=dest_lang)
        print(result)
        return result.text
    except Exception as e:
        print(f"Error with translating: {e}")
        return text  # Pokud překlad selže, vrátíme původní text

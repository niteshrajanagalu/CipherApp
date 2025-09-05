# Save this as embed_wordlist.py and run it in your CipherApp folder

def embed_wordlist(pyfile="cipher_decoder.py", wordfile="assets/words.txt"):
    with open(wordfile, "r", encoding="utf-8") as wf:
        words = [w.strip().lower() for w in wf if w.strip()]
    wordlist_str = ' '.join(words)
    with open(pyfile, "r", encoding="utf-8") as pf:
        code = pf.read()
    # Find the ENGLISH_WORDS assignment and replace it
    import re
    code = re.sub(
        r'ENGLISH_WORDS\s*=\s*load_english_words\(\)',
        f'ENGLISH_WORDS = set("""{wordlist_str}""".split())',
        code
    )
    with open(pyfile, "w", encoding="utf-8") as pf:
        pf.write(code)
    print("Embedded word list into cipher_decoder.py!")

if __name__ == "__main__":
    embed_wordlist()
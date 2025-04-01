# return just the letters of a string, as lower case
def just_letters_as_lowercase(text: str) -> str:
    """
    >>> just_letters_as_lowercase("thequickbrownfoxjumpedoverthelazydog")
    'thequickbrownfoxjumpedoverthelazydog'
    >>> just_letters_as_lowercase("The quick Brown Fox jumped over the Lazy Dog.")
    'thequickbrownfoxjumpedoverthelazydog'
    >>> just_letters_as_lowercase("")
    ''
    """
    lowercase_letters:  str = 'abcdefghijklmnopqrstuvwxyz'
    lowercase_text = text.lower()  # built into python
    if lowercase_text == "":
        return lowercase_text
    elif lowercase_text[0] in lowercase_letters:
        return lowercase_text[0] + just_letters_as_lowercase(lowercase_text[1:])
    else:
        return just_letters_as_lowercase(lowercase_text[1:])


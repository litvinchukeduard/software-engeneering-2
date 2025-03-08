import re
'''
spam_words = ['Python']

text = '... Python ...'
       '... *** ...'
'''

def replace_spam_words(spam_words: list[str], text: str) -> str:
    for spam_word in spam_words:
        pattern = rf'{spam_word}'
        text = re.sub(pattern, '*' * len(spam_word), text, flags=re.IGNORECASE)
    return text

text = '''
Python is dynamically type-checked and garbage-collected. PYTHON It supports multiple programming paradigms, incluPythonding structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
'''
print(replace_spam_words(['Python'], text))


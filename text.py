import re

text = '''My marvelous mother
made many magnificent meals for
my mischievous monkey named Max.
Meanwhile, Mike mentioned
multiple mysterious maps
marked with magical symbols.
Marching merrily,
many members of the musical marching band
met at the majestic mountain near the meadow.'''

pattern = re.compile(r'\b[Mm]\w*')
matching_words = pattern.findall(text)
print(matching_words)
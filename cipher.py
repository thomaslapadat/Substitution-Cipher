import sys

if len(sys.argv) != 4 or sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "-help":
    print("\nUSAGE:")
    print("python sandbox.py encrypt \"<keyword>\" \"<phrase>\"")
    print("OR")
    print("python sandbox.py decrypt \"<keyword>\" \"<phrase>\"")
    sys.exit()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
user_key = sys.argv[2].lower()
user_phrase = list(sys.argv[3].lower())
filtered_key = []

# Remove duplicate chars from keyword
for char in list(user_key):
    if char not in filtered_key:
        filtered_key.append(char)

# Generate cipher alphabet with keyword
filtered_alphabet = list(ALPHABET)
for char in filtered_key:
    filtered_alphabet.remove(char)
cipher_alphabet = filtered_key + filtered_alphabet

# Choose which alphabet to convert to/from
if sys.argv[1].lower() == "encrypt":
    print("\nEncrypting phrase with key: " + user_key, end="\n\n")
    old_alphabet = ALPHABET
    new_alphabet = cipher_alphabet

elif sys.argv[1].lower() == "decrypt":
    print("\nDecrypting phrase with key: " + user_key, end="\n\n")
    old_alphabet = cipher_alphabet
    new_alphabet = ALPHABET

else:
    print("ERROR: Unknown option \"" + sys.argv[1] + "\"")
    print("For usage, try: python " + sys.argv[0] + " -h")
    sys.exit()

# Convert phrase by substituting chars from old to new alphabet
for i in range(len(user_phrase)):
    if user_phrase[i] in ALPHABET:
        char_index = old_alphabet.index(user_phrase[i])
        user_phrase[i] = new_alphabet[char_index]

print("Original Phrase: " + sys.argv[3].lower())
print("New Phrase: " + "".join(user_phrase))
print("Cipher Key: " + user_key)
print("Cipher Alphabet: " + "".join(cipher_alphabet))
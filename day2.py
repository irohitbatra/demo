# 1. Extracting a Substring: Extract "World" from "Hello, World!"
greeting = "Hello, World!"
world_substring = greeting[7:12]
print(world_substring)

# 2. Reversing a String: Reverse the string "Python"
language = "Python"
reversed_language = language[::-1]
print(reversed_language)

# 3. Skipping Characters: Extract every second character from "abcdefgh"
alphabet = "abcdefgh"
every_second_char = alphabet[::2]
print(every_second_char)

# 4. First and Last Characters: Print the first and last characters from "SDET"
acronym = "SDET"
first_char = acronym[0]
last_char = acronym[-1]
print(first_char + last_char)

# 5. Remove First 2 Characters: Remove the first 2 characters from "OpenAI"
organization = "OpenAI"
removed_first_two = organization[2:]
print(removed_first_two)

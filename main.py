def count_vowels_and_consonants(s):
    vowels_count = 0
    consonants_count = 0

    vowels = set("aeiouAEIOU")

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    result = {
        "vowels": vowels_count,
        "consonants": consonants_count
    }

    return result


def count_words(str: str):
    return len(str.split())

def count_characters(str: str):
    characters_count = dict[str, int]({})
    for c in str.lower(): 
        if c in characters_count:
            characters_count[c] += 1
            
        else:
            characters_count[c] = 1

    return characters_count

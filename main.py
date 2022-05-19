student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_phonetic_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_phonetic_alphabet_dict = {v.letter: v.code for k, v in nato_phonetic_alphabet.iterrows()}


input = input('Enter a word: ').upper()
print([nato_phonetic_alphabet_dict[l] for l in input])

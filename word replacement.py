def replace_word():
    input_string = "hii guys i am anushka, and hi hi hi"
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the replacement word: ')
    result_string = input_string.replace(word_to_replace, word_replacement)
    print(result_string)

# Call the function
replace_word()

sentence = 'a3 sentence4 this1 is2'


def shuffle(string):
    word_dict = {}
    word_list = sentence.split(" ")
	
    for word in word_list:
        word_dict[int(word[-1])-1] = word[:-1]
	
    new_string = ""
	
    i = 0
    for item in word_dict:
        new_string += word_dict[i] + " "
        i+=1

    print(new_string[:-1])
    return new_string[:-1]

print(shuffle(sentence))


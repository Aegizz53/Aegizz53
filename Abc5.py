
file_name = input("Enter the input file name: ")

#Open the file.

file_obj = open(file_name)

#Define a list to store the unique words in the file.

unique_words = []

#Run the loop to traverse each line in the file.

for line in file_obj:

    #Obtain the list of words on the current line.

    words = line.split()

    #Run the loop to access each word on the current line.

    for curr_word in words:

        #If there are any punctuations in

        # the word then, remove them.

        curr_word = curr_word.strip(',.?!')

        #If the current word is not present in

        #the list of the unique words then,

        #add it to the list.

        if curr_word not in unique_words:

            unique_words.append(curr_word)

#Close the file.

file_obj.close()

#Sort the list containing the unique words.

unique_words.sort()

#Display an empty line on the console.

print()

#Runthe loop to display the unique words.

for curr_word in unique_words:

    print(curr_word)

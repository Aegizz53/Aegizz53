#This creates an empty list

wordList = []

#This opens the file

with open("Pythons5.txt", "r") as file:

   #This reads the file, line by line

   lines = file.readlines()

   #This iterates through each line

   for line in lines:

       #This splits each line into words

       words = line.split()

       #This iterates through each word

       for word in words:

           #This removes the spaces in each word

           word = word.strip()

           #This adds unique words to the list

           if word not in wordList:

               wordList.append(word)

#This prints the unique words in alphabetical order

print(sorted(wordList))

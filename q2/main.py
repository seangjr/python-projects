punctuations = '''!()-[]{};:'“’”—"\,<>./?@#$%^&*_~'''

eBook = ""
stopWords = ""

# extraction 
with open("Sample_run_book.txt", 'r', encoding = 'utf-8') as f:
    for words in f:
        eBook += " " + words.rstrip()

# stop words
with open("stop_words_english.txt", 'r', encoding = 'utf-8') as f:
    for words in f:
        stopWords += " " + words.rstrip()

# remove punctuations
for i in eBook:
    if i in punctuations:
        eBook = eBook.replace(i, " ")


eBooklist = eBook.split() # split the book into words
resultwords = [word for word in eBooklist if word.lower() not in stopWords.split()] # remove stop words

# get a set of unique words
uniques = []
for word in resultwords:
    if word not in uniques:
        uniques.append(word)

# make a list of count
counts = []
for unique in uniques:      # for each unique word
    count = 0               # count is initialised to 0 
    for word in resultwords:  # iterate for each word in the list
        if word == unique:    # if the word is equal to the unique word
            count += 1        # increment the count
    counts.append((count, unique)) # append the count and the unique word to the list

counts.sort() # sort the list
counts.reverse() # reverse the list

for i in range(min(10, len(counts))): # print the top 10 words
    print(counts[i][1], counts[i][0]) # print the word and the count
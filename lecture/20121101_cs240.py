speech = 'to be or not to be'
speechList = speech.split()

wordCountDict = {}

for word in speechList:
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

# Stepping through the code
 2: speechList = ['to', 'be', 'or', 'not', 'to', 'be']
 4: wordCountDict = {}
 6: word = 'to'
10: wordCountDict = {'to': 1}
 6: word = 'be'
10: wordCountDict = {'to': 1, 'be': 1}
 6: word = 'or'
10: wordCountDict = {'or': 1, 'to': 1, 'be': 1}
 6: word = 'not'
10: wordCountDict = {'or': 1, 'to': 1, 'not': 1, 'be': 1}
 6: word = 'to'
10: wordCountDict = {'or': 1, 'to': 2, 'not': 1, 'be': 1}
 6: word = 'be'
10: wordCountDict = {'or': 1, 'to': 2, 'not': 1, 'be': 2}

print 'The word "to" appears', wordCountDict['to'], 'times'

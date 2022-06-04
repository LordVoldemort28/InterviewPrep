#https://markeggensperger.medium.com/beating-algoexpert-generate-document-774b8aa485ab

def generateDocument(characters, document):
    # Write your code here.
    charactersCount = [0] * 128
    documentCount = [0] * 128

    for char in characters:
        charactersCount[ord(char)] += 1

    for doc in document:
        documentCount[ord(doc)] += 1

    for idx in range(0, len(charactersCount)):

        if charactersCount[idx] < documentCount[idx]:
            return False

    return True


input = {
    'characters': 'Bste!hetsi ogEAxpelrt x ',
    'documents': 'AlgoExpert is the Best!'
}
output = True

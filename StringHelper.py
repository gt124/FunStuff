

class StringHelper:

    cussWords = ["fuck", "shit", "dickhead"]
    outputWords = {}

    def __init__(self) -> None:
        super().__init__()

    def IsCussWord(self, possibleCussWord):
        cussIndex = 0
        while cussIndex < len(self.cussWords):
            if str.upper(possibleCussWord) == str.upper(self.cussWords[cussIndex]):
                return True
            cussIndex += 1
        return False

    def WordCutter(self, count, sentenceIn):
        result = ""
        while count < len(sentenceIn) and " " != sentenceIn[count]:
            result = result + sentenceIn[count]
            count += 1
        return len(result), result

    def AddMaskOrWordToLine(self, sentenceToModify, wordIn, maskCharacter):
        if not self.IsCussWord(wordIn):
            sentenceToModify = sentenceToModify + wordIn

        else:
            #Track Cussword
            wordInIndex = 0
            while wordInIndex < len(wordIn):
                sentenceToModify = sentenceToModify + maskCharacter
                wordInIndex += 1

        return sentenceToModify


    def ProfanityFilter(self, sentenceWithCusswords):
        sentenceIndex = 0
        outputSentence = ""
        while sentenceIndex < len(sentenceWithCusswords):
            if " " == sentenceWithCusswords[sentenceIndex]:
                outputSentence = outputSentence + sentenceWithCusswords[sentenceIndex]
                sentenceIndex += 1
                continue

            wordcutterIndex, workingWord = self.WordCutter(sentenceIndex, sentenceWithCusswords)

            outputSentence = self.AddMaskOrWordToLine(outputSentence, workingWord, "$")
            sentenceIndex = sentenceIndex + wordcutterIndex

        return outputSentence

    def UserCussWordFilter(self):
        while True:
            userInput = input("type something or q to quit: ")
            if "Q" == userInput.upper():
                break
            userOutput = self.ProfanityFilter(userInput)
            print(userOutput)
            #Display cusswords and count

    def AddWordAndKeepCountForDisplay(self, wordIn):
        #If there are no entries then add one
        if 0 == len(self.outputWords):
            self.outputWords[wordIn] = 1

        #If it exists find one and update the count

        #else add it (can probably merge the one up there also
        return self.outputWords




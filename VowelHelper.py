# FirstVowelLetterFoundThatStartsAWord

class VowelHelper:

    sentenceIn = str()

    def __init__(self, sentenceIn) -> None:
        super().__init__()
        self.sentenceIn = sentenceIn

    def IsVowel(self, letter):
        if "A" == letter.upper() or "E" == letter.upper() or "I" == letter.upper() or "O" == letter.upper() or "U" == letter.upper() or "Y" == letter.upper():
            return True

        return False

    def WordCutter(self, count, result):
        while count < len(self.sentenceIn) and " " != self.sentenceIn[count]:
            result = result + self.sentenceIn[count]
            count += 1
        return count, result

    def FindFirstWordStartsWithVowel(self):
        print("FindFirstWordStartsWithVowel Sentence in is: " + self.sentenceIn)
        count = 0
        result = ""
        while count < len(self.sentenceIn):
            if 0 == count and self.IsVowel(self.sentenceIn[count]):
                count, result = self.WordCutter(count, result)
                break
            elif " " == self.sentenceIn[count]:
                count +=1
                if self.IsVowel(self.sentenceIn[count]):
                    count, result = self.WordCutter(count, result)
                    break
            else:
                count +=1

        return result

    def FindAllWordsThatStartWithAVowel(self):
        print("FindAllWordsThatStartWithAVowel Sentence in is: " + self.sentenceIn)
        count = 0
        allResults = []
        while count < len(self.sentenceIn):
            result = ""
            if 0 == count and self.IsVowel(self.sentenceIn[count]):
                count, result = self.WordCutter(count, result)
                if "" != result:
                    allResults.append(result)
            elif " " == self.sentenceIn[count]:
                count +=1
                if self.IsVowel(self.sentenceIn[count]):
                    count, result = self.WordCutter(count, result)
                    if "" != result:
                        allResults.append(result)
            else:
                count +=1

        return allResults












    def RecursivePrint(self, inStringToCut):
        if 0 >= len(inStringToCut):  #Terminating condition
            return ""

        print(inStringToCut[0])

        return inStringToCut[0] + self.RecursivePrint(inStringToCut[1:])  #call same function again





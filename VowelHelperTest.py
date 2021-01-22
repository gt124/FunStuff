from VowelHelper import VowelHelper

vowelHelper = VowelHelper("yes an angry boy u")

isVowelResult = vowelHelper.IsVowel("a")
print("isVowelResult True == " + str(isVowelResult))
print("-----------------------------------------")
isVowelResult = vowelHelper.IsVowel("b")
print("isVowelResult False == " + str(isVowelResult))
print("-----------------------------------------")

word = vowelHelper.FindFirstWordStartsWithVowel()
print(word)

allVowelWords = vowelHelper.FindAllWordsThatStartWithAVowel()
print(allVowelWords)

outputFromRecursivePrint = vowelHelper.RecursivePrint("tes")
print(outputFromRecursivePrint)

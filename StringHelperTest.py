from StringHelper import StringHelper

sut = StringHelper()

result = sut.IsCussWord("crud")
print("crap is " + str(result))

result = sut.IsCussWord("shit")
print("shit is " + str(result))

counter = 0
counter, output = sut.WordCutter(counter, "one two three")
print("counter = " + str(counter) + " output = " + output)

counter = 0
counter, output = sut.WordCutter(counter, " one two three")
print("counter = " + str(counter) + " output = " + output)

newString = sut.AddMaskOrWordToLine("how are you ", "shit", "$")
print("newString == " + newString)

output = sut.ProfanityFilter("one two shit stink shit")
print(output)

output = sut.ProfanityFilter("fuck one two dickhead stink shit")
print(output)

#Working on this one
output = sut.AddWordAndKeepCountForDisplay("Skinky") #Returns a list with the word and count keeps track of multiples
#output = sut.AddWordAndKeepCountForDisplay("Skinky") #Returns a list with the word and count keeps track of multiples
print(output)

#This is the while loop
#sut.UserCussWordFilter()



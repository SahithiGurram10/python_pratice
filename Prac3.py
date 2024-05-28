# Question - Accept five words ass input and print the sentences formed by these words
# after adding a space between consecutive words and a full stop at the end.
# sample input - Give 5 inputs of words -> input1 - a, input2 - b, input3 - c, input4 - d, input5 - e
# sample output - a b c d e.

word=""
sentence =""
countofinputs=0
while countofinputs!=5:
    word = input ("enter a word:")
    countofinputs+=1
    if countofinputs==5:
        sentence+=word+"."
    else:
        sentence=sentence+word+" "
print(sentence)    
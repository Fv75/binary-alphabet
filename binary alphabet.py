#list of all binary characters
binary_list = ("A","01000001",
"B","01000010",
"C","01000011",
"D","01000100",
"E","01000101",
"F","01000110",
"G","01000111",
"H","01001000",
"I","01001001",
"J","01001010",
"K","01001011",
"L","01001100",
"M","01001101",
"N","01001110",
"O","01001111",
"P","01010000",
"Q","01010001",
"R","01010010",
"S","01010011",
"T","01010100",
"U","01010101",
"V","01010110",
"W","01010111",
"X","01011000",
"Y","01011001",
"Z","01011010",)

#get user input and convert to uppercase
name = input("Skriv ditt namn: ").upper()

binary_name_list=[]
#iterate through all the characters in name
for c in range(len(name)):
    #if name[n] == binary list, add to new var binary_name_list
    if name[c] in binary_list:
        binary_name_list.append((binary_list[1]))
    #make string of binary_name_list and print
    binary_name = ' '.join(binary_name_list)
print("Ditt namn på binärspråk är: ", binary_name)
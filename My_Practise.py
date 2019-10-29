def Cal_Recursive(phone_number,letter,pos):
    Working_String = ""
    Working_String =  Working_String + letter
    print("Phone Number:",phone_number,"Working String:",Working_String,"At Position:",pos)

Working_String = ""
count = 0
while count < 7:
    phone_Number = input("Enter the Phone Number - On by one Digit:")
    if phone_Number == "1":
        one = "1"
        pos = 1
        Cal_Recursive(phone_Number,one,pos)
    if phone_Number == "2":
        two = "abc"
        pos = 2
        Cal_Recursive(phone_Number, two, pos)
    if phone_Number == "3":
        three = "def"
        pos = 3
        Cal_Recursive(phone_Number, three, pos)
    if phone_Number == "4":
        four = "ghi"
        pos = 4
        Cal_Recursive(phone_Number, four, pos)
    if phone_Number == "5":
        five = "jkl"
        pos = 5
        Cal_Recursive(phone_Number, five, pos)
    if phone_Number == "6":
        six = "mno"
        pos = 6
        Cal_Recursive(phone_Number, six, pos)
    if phone_Number == "7":
        seven = "pqrs"
        pos = 7
        Cal_Recursive(phone_Number, seven, pos)
    if phone_Number == "8":
        eight = "tuv"
        pos = 8
        Cal_Recursive(phone_Number, eight, pos)
    if phone_Number == "9":
        nine = "wxyz"
        pos = 9
        Cal_Recursive(phone_Number, nine, pos)
    if phone_Number == "0":
        zero = "0"
        pos = 11
        Cal_Recursive(phone_Number, zero, pos)

    #seprint(phone_Number)
    count +=1

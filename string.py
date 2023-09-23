x = "Hello"
print(x)

                                                        #multiline String
y = """My name is Urvshi. I am a Python developer.
i am live in Rajkot. I am a fresher in python,
I have a experiance of Teaching."""
print(y)

                                                        #string array
z = "Uma Tution Classes"    
print(z[0],z[1],z[2])


                                                        #looping
for p in "Urvashi":
    print(p)

                                                        #Length
q = "I am Mrs. Patel"
print(len(q))

                                                        #check string
a = """A paragraph is a collection of words strung together to make a longer unit than a sentence.
Several sentences often make a paragraph. There are normally three to eight sentences in a paragraph.
Paragraphs can start with a five-space indentation or by skipping a line and then starting over.
This makes it simpler to tell when one paragraph ends and the next starts simply it has 3-9 lines"""
print("five-space" in a)

                                                        #if else
b = "My Name Is Urvashi"
if "Urvashi" in b:
    print("Yes")
else:
    print("No")

c = "My Husband name is Sahil"
if "Urvashi" not in c:
    print("No")
else:
    print("Yes")

                                                        #slicing
m = "Mrs. Urvashi Sahil Bhadaniya"
print(m[3:10])
print(m[-11:-3])

                                                        #Modify
s = "  Dolly Ravi Vadaliya"
print(s.upper())                    #upper case
print(s.lower())                    #lower case
print(s.strip())                    #remove white space
print(s.replace("Ravi","Pillu"))    #replace

g = "Dolly,Vadaliya"                #seperate
u = g.split(",")
print(u)

                                    #concatenent
n = "Urvashi"
o = "Nidhi"
q = n + o
print(q)
f = n + " " + o
print(f)

#formate string
apple = 200
pineapple = 100
banana = 60
myfruits = "I want to buy banana{2},pineapple{1},apple{0}."
print(myfruits.format(apple,pineapple,banana))











def anag(w1, w2):
    a=0

    for i in w1:
        for j in w2:
            if i == j:
                a=a+1
                
    if (a == len(w1)):
        return 1
    
    else:
        return 0

w1=input("Enter word 1: ")
w2=input("Enter word 2: ")
 
if(anag(w1, w2)):
    print("The two words are anagram")

else:
    print("The two words are not anagram")

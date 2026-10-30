#1print fibonachi series till the entered number
#g2et a string from user and check if its a palindrome or not
#3 check if a number is armstrong or not?


#3:-
# number = int(input("Enter a number"))
# sum=0
# for i in range(0,len(number)):
#      z=number[i]
#      sum=sum+(z**3)
# #for checking 
# if int(number)==sum:
#      print('The number is a Armstrong number');
# else:
#      print('The given number is not a armstrong number')

#2


# def palindrome(word):
#      length_word=len(word)
#      length_pal_word=0
#      for i in range(0,length_word):
#           if word[i]==word[length_word-(i+1)]:
#                length_pal_word+=1
#      if length_word==length_pal_word:
#          return True    
#      else:
#          return False

# sentence = input('enter a sentence')
# lib={}
# proper_sentence=sentence.split()
# for j in range(0,len(proper_sentence)):
#      length=len(proper_sentence[j]);
#      if palindrome(proper_sentence[j]) is True:
#           lib[int(length)]= proper_sentence[j]
#      else:
#           continue
# highest_val=None
# highest_key=None

# for key,val in lib.items():
#      if highest_key is None or key>highest_key:
#           highest_val=val
#           highest_key=key

# print(highest_key,highest_val);








#print fibonacci series unitll given number
# number = int(input("Enter the Number"))
# def fibbonacci(a):
#      x=0
#      y=1
#      sum_fibooooo=0
#      while x<a:
#                z=x
#                #print(x,y)
#                print(z,end=" ")
#                x,y=y,x+y 
#                sum_fibooooo=+z
          
# fibbonacci(number)
# n = int(input('tell the number till N*N matrix has to be made:'))
# z=0
# #for row

# for i in range(0,n):
#      matrix=[]
#      for j in range(0,n):
#           matrix.append((n*n)-z)
#           z=z+1
#      # matrix.reverse()
#      print(matrix)

















# number=None
# for a in range(0,20):
#      for b in range(0,20):
#           for c in range(0,20):
#                for d in range(0,20):
#                     if (b>a) and (a*b==12) and (c+2==d) and(a+b+c+d==20):
#                          number=(1000*a  + 100*b  + 10*c  +  d);

# print(number)































# mps_list = [
#     "MPS145",
#     "MPS111",
#     "MPS235",
#     "MPS521",
#     "MPS019",
#     "MPS800",
#     "MPS442",
#     "MPS333",
#     "MPS612",
#     "MPS222"
# ]

# matching_keys=[]


# for i in mps_list:
#      digit_sum=0
#      for j in i[3:]:
#           digit_sum+=int(j)
#      if digit_sum==10:
#           matching_keys.append(i)

# print(matching_keys)






# password checker with remaining attempts












#need number
Required_Number=0
for a in range(0,20):
     for b in range(0,20):
          for c in range(0,20):
               for d in range(0,20):
                    if (b>a) and (a*b==12) and (c+2==d) and (a+b+c+d==20):
                         Required_Number= (1000*a+100*b+10*c+d)
print(f'The number is {Required_Number}')
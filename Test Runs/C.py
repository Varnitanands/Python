#no of attempt one 
max_attempt=3
current_attempt=0
key='ABCD'
while current_attempt<max_attempt:
     user_key=input('Enter the passcode')
     if user_key==key:
          print('ACCESS GRANTED :)');
          print('WECLOME :D');
          break
     else:
          print('ACESS DENIED!!!')
          current_attempt+=1
          print(f'THE REMAINING ATTEMPTS ARE : {max_attempt-current_attempt}')
          continue
else:
     print('SYSTEM LOCKED')   
     
     
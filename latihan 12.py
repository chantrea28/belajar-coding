batre = 'full'

if batre == 'low':
    print('segera charge hp kamu') 
else:
    print('batre full,boleh main game') 
    
grade = input ('enter grade A/B/C: ')

if grade == 'A' :
 print('congratulation')
elif grade == 'B' :
 print('good job')
elif grade == 'C':
 print('nice try')
else :
 print('wrong input')


score = int(input('enter score: '))

if score > 85 and score <= 100:
  print('grade A')
elif score > 75 and score <= 85:
  print('grade B')
elif score >50 and score <= 70:
  print('grade C')
else:
  print ('grade D') 

 
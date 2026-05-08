nama = 'Alhazen'

def greeting():
    adress = 'bekasi'
    print(f'halo {nama},from {adress}')

greeting()

print(nama)
#print(adress)

score = 0 
def tambahscore():
    global score 
    score = score + 1
    print(f'score:{score}')

tambahscore()
tambahscore()
tambahscore()
tambahscore()
tambahscore()

print(score)

text = 'global'

def testscope():
    text = 'local'
    print(text)

testscope()
print(text)
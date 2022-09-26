print('Velmi Uzitecna Aplikace')
print('-------------------------')
print('1. Kalkulacka vysky')
print('2. Kalkulacka hmotnosti')
print('3. Kalkulacka deprese')
print('4. Kalkulacka uzitecnosti')
print('5. Kalkulacka zivota')
print('-------------------------')
volba = input('Vyberte moznost: ')

def vyska():
    print('--------------------')
    print('--Kalkulacka Vysky--')
    print('--------------------')
    v = input('Zadejte vasi vysku: ')
    print('---')
    if eval(v) >= 175:
        print('Gratuluji jste vysoky/a')
    else:
        print('Bohuzel neslo nic. Jste maly/a')

def hmotnost():
    print('------------------------')
    print('--Kalkulacka Hmotnosti--')
    print('------------------------')
    h = input('Zadejte vasi vahu: ')
    print('---')
    if eval(h) >= 100:
        print('Jste obcan Ameriky?')
    elif eval(h) < 100 and eval(h) >= 60:
        print('V pohode :)')
    else:
        print('Papejte vice *nom nom*')

def deprese():
    print('----------------------')
    print('--Kalkulacka Deprese--')
    print('----------------------')
    d = input('Jak se dnes citite na skale od 1 do 10: ')
    print('---')
    if eval(d) > 8:
        print('Jste v depresi :( Nechcete si s nekym promluvit?')
    elif eval(d) < 8 and eval(d) >= 5:
        print('Neni vam nejhure, ale ani nejlepe')
    elif eval(d) < 5 and eval(d) >= 3:
        print('Jste na tom dobre, ale mohlo by byt lepe')
    else:
        print('Neni co resit, citite se dobre')

def uzitecnost():
    print('--------------------------')
    print('--Kalkulacka Uzitecnosti--')
    print('--------------------------')
    u = input('Jako moc na skale od 1 do 10 je tato aplikace uzitecna? ')
    print('---')
    if eval(u) <= 10 and eval(u) >= 8:
        print('Tato aplikace je super uzitecna')
    elif eval(u) < 8 and eval(u) >= 6:
        print('Tato aplikace je velmi uzitecna')
    elif eval(u) < 6 and eval(u) >=4:
        print('Tato aplikace je uzitecna')
    else:
        print('Nekdo si muze myslet ze tato aplikace neni uzitecna, ale v hloubi duse vi, ze ji potrebuje v kazdodennim zivote')

def zivot():
    print('---------------------')
    print('--Kalkulacka Zivota--')
    print('---------------------')
    z = input('Hrajete moc pocitacovych her? ')
    print('---')
    if z == 'ano' or z == 'Ano':
        print('Nemate zivot. Mel/a bys si nekdy dat sprchu nebo jit ven')
    elif z == 'ne' or z == 'Ne':
        print('Mate zivot a muzete byt rad/a')

volbaSwitch = eval(volba)
def switch(volbaSwitch):
    if volbaSwitch == 1:
        vyska()
    elif volbaSwitch == 2:
        hmotnost()
    elif volbaSwitch == 3:
        deprese()
    elif volbaSwitch == 4:
        uzitecnost()
    elif volbaSwitch == 5:
        zivot()


switch(volbaSwitch)
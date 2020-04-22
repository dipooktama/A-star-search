from operator import itemgetter
kota = {
    'oradea':{'zerind':71, 'sibiu':151},
    'zerind':{'oradea':71,'arad':75},
    'sibiu':{'oradea': 151,'arad':140, 'fagaras': 99, 'rimnicu vilcea':80},
    'arad':{'zerind':71, 'timisoara':118, 'sibiu':140},
    'timisoara':{'arad':118, 'lugoj':111},
    'lugoj':{'timisoara':111, 'mehadia':70},
    'mehadia':{'lugoj':70, 'dobreta':75},
    'dobreta':{'mehadia':75, 'craiova':120},
    'craiova':{'dobreta':120,'pitesti':138, 'rimnicu vilcea':148},
    'rimnicu vilcea':{'craiova':148,'sibiu':80, 'pitesti':97},
    'pitesti':{'craiova':138,'rimnicu vilcea':97, 'bucharest':101},
    'fagaras':{'sibiu':99,'bucharest':211},
    'bucharest':{'pitesti':101,'fagaras':211, 'giurgiu':90, 'urziceni':85},
    'giurgiu':{'bucharest':90},
    'urziceni':{'bucharest':85, 'hirsova':98, 'vaslui':142},
    'vaslui':{'urziceni':142, 'lasi':92},
    'lasi':{'vaslui':92, 'neamt':87},
    'neamt':{'lasi':87},
    'hirsova':{'urziceni':98, 'eforie':86},
    'eforie':{'hirsova':86}
}

nilaiH = {
    'arad' : 366,
    'bucharest' : 0,
    'craiova' : 160,
    'dobreta' : 242,
    'eforie' : 161,
    'fagaras' : 176,
    'giurgiu' : 77,
    'hirsova' : 151,
    'lasi' : 226,
    'lugoj' : 244,
    'lugoj' : 244,
    'mehadia' : 241,
    'neamt' : 234,
    'oradea' : 380,
    'pitesti' : 100,
    'rimnicu vilcea' : 193,
    'sibiu' : 253,
    'timisoara' : 329,
    'urziceni' : 80,
    'vaslui' : 199,
    'zerind' : 374
}

k0 = input('Masukkan kota awal : ')
kt = 'bucharest'
i = 0
jalan=[]
sekitar=[]
temp = []
dikunjungi=[]

jalan.append(k0)
#print(jalan)
while(True):
    print('\n\nKota sekarang : ',k0)
    sekitar = list(kota[k0].items())
    #print(sekitar)

    dikunjungi.append(k0)
    print("\ndikunjungi : ",dikunjungi)
    for baris in sekitar:
        if baris[0] not in dikunjungi:
            temp.append([])
            temp[i].append(baris[0])
            temp[i].append(baris[1]+nilaiH[baris[0]])
            i+=1
    #print(temp)

    print('\nkota tetangga : ')
    temp = sorted(temp,key=itemgetter(1))
    print(temp)

    sekarang = temp[0]
    #print(sekarang)

    k0=sekarang[0]
    jalan.append(sekarang[0])
    if sekarang[0]==kt or k0==kt:
        print('\n\nsampai di bucharest! \njalan = ',jalan)
        break

    for baris in sekitar:
        if baris[0] == sekarang[0]:
            sekitar.remove(baris)
    #print(sekitar)

    #hold=input('\n\ntekan enter..\n\n')
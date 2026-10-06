#print("hello world")
#print(7+8)

#print("3 karra 3 = " ,3*3)

#print("odami ersang xalq gamidin gami \n eshmat toshmat \nqoshmat shashmat")
#print(2+4*2)

#print('men "dell" noubok sotib oldim')

#print(19/3)
#print(20/4)
#print(20//4)
#print(10/4)
#print(2**4)

#ism=" Javohir DEV"
#print("mening ismim" + ism)

#ism = 'Ahad '
#familiya = 'Qayum'
#yosh = 27 
#print(ism + familiya)
#print(ism + '' + familiya)
# f-string 

#ism_sharif = f"{ism} {familiya} {yosh}"
#print(ism)
#print(familiya)
#print(yosh)
#print(f"""Salom! Mening ismim {ism}, 
#familiyam {familiya}. 
#Yoshim {yosh} da!""")

#familiya = 'Qayum'
#yosh = 27 
#ism = 'Ahad '
#ism_sharif = f" {ism} {familiya}"
#ism_sharif = ism_sharif.upper()
#print(ism_sharif)
#print(ism_sharif.capitalize())
#print(ism_sharif.title())
#print(ism_sharif.lower())

#meva = "olma"
#print(meva)
#print(" men, "  + meva.lstrip() + " yaxshi ko'raman")
#print(" men, " + meva.rstrip() + " yaxshi ko'raman")
#print(" men, " + meva.strip() + " Yaxshi ko'raman ")
#print(" men " + meva + "yaxshi ko'raman ")

#ism = input ("ismingiz nima")
#print("Assalomu Alaykum" + ism)

#ism = input ("ismingiz nima? \n >>>")
#print ("Assalomu Alaykum," + ism.title())

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor" 
#viloyat="Samarqand"
#
##Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#print(f""" {kocha} ko'chasi, {mahalla} 
#mahallasi, {tuman} tumani, {viloyat} viloyati""") 

#ism = 'Jobir'
#yosh = '27'
#xabar = ism + ' ' + str(yosh) + ' yoshda'
#print(xabar)

#t_yil = int(input("tug'ilgan yilingizni kiriting: "))
#yosh = 2026 - t_yil
#print(f"siz {yosh} da ekansiz")


#t_yil = int(input ("tugilgan yilingizni kiriting: "))
#yosh = 2026 - t_yil
#print(f"siz  {yosh} da ekansiz")


#print(mevalar)
#print(mevalar [0])
#print(mevalar [3])
#print(mevalar [2])
#print(mevalar [1])

#print(narxlar [0])
#print(narxlar [2])
#print(narxlar [3])
#print (mevalar [-1])

#print(mevalar[0].title())
#print(mevalar[-2].capitalize())
#print(mevalar[-1].upper())
#print(mevalar[-3].lower())

#print(narxlar[0])
#print(narxlar[0] + narxlar [1])
#print(narxlar[1] + 12000 - 12500)

#mevalar[-1]= 'olma'
#mevalar[0] = 'banan'
#print(mevalar)
#mevalar = ['olma', 'orik', 'shaftoli', 'banan']
#narxlar = [12000, 14000, 12500, 24900]
#sonlar = ['bir ', 'ikki', 3 ,4, 5]
#ismlar = []
#narxlar[1] = narxlar[1] - 4000
#print(narxlar)
#mevalar.append('tarvuz')
#print(mevalar)
#mevalar.append('qovun')
#print(mevalar)

#mevalar.insert(2, 'gilos')
#print(mevalar)

#mevalar.extend(['tarvuz' , 'qovun' , 'anjir'])
#print(mevalar)

#cars=[]
#cars.append('lasetti')
#cars.append('nexia')
#cars.append('malibu')
#cars.append('tracker')
#print(cars)
#del cars[0]
#print(cars)
#cars.remove("nexia")
#print(cars)

#bozorlik = ['yog', 'un', 'gosht' , 'olma']
#print(bozorlik)
#mahsulot= bozorlik.pop(2)
#print(mahsulot)
#print(bozorlik)
#print("men " + mahsulot + ' sotib oldim')
#print("olmagan mahsulotlarim: ", bozorlik)

#print(cars) 
#cars.sort()
#print(cars)

#cars.sort(reverse=True)
#print(cars)
#print(sorted(cars ,reverse=True))

#sonlar = [ 12, 45, 23, 21, 52,55, -1, 7.2, 34.1]
#print(sorted(sonlar))
#print(sorted(sonlar , reverse=True))
#cars.sort()
#cars.reverse()
#print(cars)
#print(len(sonlar))
#print(sonlar)
#sonlar = list(range(0, 10))
#print(sonlar)
#print(sonlar)
#sonlar.reverse()

#toq_sonlar = list(range(1,20,2))
#print(toq_sonlar)

#juft_sonlar = list(range(0,20,2))
#print(juft_sonlar)

#sanash = list(range(0,101,10))
#print(sanash)

#max_qiymat = max (toq_sonlar)
#print(max_qiymat)

#print(juft_sonlar)
#arzon = min(juft_sonlar)
#qimmat = max(juft_sonlar)
#jami = sum(juft_sonlar)
#
#print(max(juft_sonlar))
#print(min(juft_sonlar))
#print(sum(juft_sonlar))
#print("Eng qimmat narx", qimmat, 
#       "eng arzon narx", arzon,
#      "jami narxi", jami)

#print(cars)
#print(cars[4])
#print(cars[1])
#print(cars[0])
#print(cars[0:4])
#print(cars[0:4:2])
#print(cars[2::-1])
#print(cars[2:0:-1])
#cars= ['bmw', 'audi', 'porsh', 'volvo', 'chevrolet' ]

#my_cars = cars [:]
#print(my_cars)
#my_cars.remove('audi')
#print(my_cars)
#my_cars.append('byd')
#print(my_cars)

#tuple
#toys = ('teddy', 'bear', 'dog', 'cat')
#print(toys)
#
#toys = list(toys)
#type(toys)
#print(toys)
#toys.append('mouse')
#print(toys)
#toys = tuple(toys)
#type(toys)
#print(toys)

#FOR TSIKL darsi

#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
#for mehmon in mehmonlar:
#    print('Salom', mehmon)
#    print('SORRY', mehmon)

#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon} sizni 20 dekabr kuni nahorgi oshimizga taklif qilamiz")
#    print(f"Hurmat bilan , Palonchiyevlar oilasi \n")

#sonlar = list(range(1,11))
#for son in sonlar: 
#    print(f" {son} ning kvadrati {son ** 2} ga teng")

#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
#    sonlar_kvadrati.append(son **2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print(" 5 eng yaqin do'stingizni kiriting:" )
#for n in range (5): # n bu yerda 0 dan 4 gacha qiymat oladi
#    dostlar.append(input(f"{n+1} - do'stingizni ismini kiriting"))
#print(dostlar)    

#ism = input("ismingiz nima? \n >>>")
#if ism.lower() != 'ali':
#    print(f"uzr, {ism.title()} , biz Alini kutayapmiz")
#else:
#    print("Salom Ali")

#javob = float(input("12x6 nechiga teng?>>>"))
#if javob != 72:
#    print('Javob xato')
#else:
#    print("javob togri")     

#yosh = int(input("yoshingiz nechida "))
#if yosh >= 18 : 
#    print("hush kelibsiz")
#else:
#    print("kirish mumkin emas")    

#login = input("yangi login tanlang\n >>> ")
#if len (login) <= 5:
#    print("login 5 harfdan ko'p bo'lishi shart")

#yil = int(input("tugilgan yilingizni kiriting \n >>>"))
#if 2020 - yil < 18: 
#    print(f"yoshingiz {2020-yil} da ekan")
#    print("kirish mumkin emas")
#else:
#    print("hush kelibsiz")    

#yosh = int(input("yoshingiz nechida \n >>>"))
#if yosh > 65:
#    print("siz covid-19 risk guruhidasiz")
#else:
#    print("siz risk guruhida emassiz")

#son = int(input("raqam kiriting"))
#if son < 0: 
#    print("manfiy son")
#else: 
#    print("musbat son ")

#yosh = int(input("Yoshingiz nechida?\n >>>"))
#if yosh <= 4:
#    narx = 0
#    #print("kirish sizga bepul")
#elif yosh <= 12:
#    narx = 5000
#    #print("kirish sizga 5000 som")
#elif yosh <= 18:
#    narx = 8000
#    #print("kirish sizga 8000 som ")
#else:
#    narx = 10000
#    #print("sizga kirish 10 000  som ")
#print(f"sizga kirish {narx} so'm")

# OR ishlatilishi 
#kun = input("bugun nima kun? \n >>>")
#if kun.lower() == 'shanba' or kun.lower()=='yakshanba':
#    print("bugun dam olish kuni")
#else: 
#    print('bugun ish kuni')   

# And darsligi 

#kun = input("bugun nima kun? \n >>>")
#harorat = float(input("havo harorati qanday? "))
#if kun.lower() == 'yakshanba' and harorat >= 30:
#    print("chomilgani ketdik")
#elif kun.lower() == 'yakshanba' and harorat < 30:
#    print("uyda dam olamiz")
#else:
#    print("bugun ish kuni")

#boolean
#narx = 15000
#choy = 0
#salat = 1
#non = 0
#kampot = 1
#assarti = 0
#
#if choy: 
#    print("Mijoz choy oldi")
#    narx = narx + 5000
#if salat: 
#    print("mijoz salat oldi")
#    narx = narx + 8000
#if non : 
#    print(" mijoz non oldi")
#    narx = narx + 2000
#if kampot:
#    print("mijoz kampot sotib oldi")
#    narx = narx + 10000
#if assarti:
#    print("mijoz assarti sotib oldi")
#    narx = narx + 15000 
#
#print(f" Jami {narx} som")                    


#if choy and salat:
#    narx = narx + 10000
#elif choy or salat: 
#    narx = narx + 5000
#print(f" Jami {narx} som ")    

# in funksiyasi
#menyu = ['manti', 'qozon kabob', 'jarkob', 'osh']
#
#print('manti' in menyu)
#print('somsa' in menyu)
#
#taom = input("qaysi taomni qidiryapsiz? \n >>>")
#if taom.lower() in menyu:
#    print(f"{taom} menyuda bor")
#else:
#    print(f"kechirasiz, {taom} menyuda yo'q")

#menyu = ['somsa', 'baqlajon','norin']
#print('somsa' in menyu)
#print('jarkob' in menyu)
#
#taom = input("qaysi taomni qidiryapsiz? \n >>>")
#if taom.lower() in menyu:
#    print(f"{taom} menyuda bor")
#else:
#    print(f"{taom} menyuda yoq")    

#menyu = ['somsa', 'baqlajon','norin']
#buyurtmalar = ['somsa', 'norin', 'jarkob']
#
#for taom in buyurtmalar:
#    if taom in menyu: 
#        print(f"menyuda {taom} bor")
#    else: 
#        print(f" kechirasiz menyuda {taom} yoq")    

#car_0 = {'model':'ferrari','rang':'qizil'}
##print(car_0['model'])
##print(car_0['rang'])
#
#en_uz = {'apple':'olma','apricot':"o'rik", 'banan': 'banan'}
#mevalar = {'olma': 10000 , 'tarvuz': 8000 , 'qovun':5000}
#print(mevalar['qovun'])

#talaba_0 = {'ism':'murod olimov', 'yosh':26 ,'t_yil': 2003}
#print(f"{talaba_0 ['ism'].title()},\
#      {talaba_0 ['t_yil']} - yilda tug'ilgan,\
#      {talaba_0 ["yosh"]} yoshda")

#telefonlar = {
#    'Davron' : 'lyuboy telefon',
#    'Abdulaziz' : 'MI pro s9', 
#    'Bahrom ' : 'iphone 14 max',
#    'Nurmuhammad' : 'xotinini telini ishlatadi',
#    'sheyx bankir' : 'nokia 3310'
#}
##print(telefonlar['Nurmuhammad'])
#
#meva = en_uz.get('apple','bunday meva mavjud emas')
#print(meva)

#print(telefonlar)
#phone = telefonlar.get("Nurmuhammad")
#print(phone)

#malibus = []
#
## 10 та машина яратамиз ва рўйхатга қўшамиз
#for _ in range(10):
#    new_car = {
#        'model': 'malibu',
#        'rang': None,
#        'yil': 2020,
#        'narx': None,
#        'km': 0,
#        'karobka': 'avto'
#    }
#    malibus.append(new_car)
#
## Биринчи 3 тасини қизил қиламиз
#for malibu in malibus[:3]:
#    malibu['rang'] = 'qizil'
#
#for malibu in malibus[3:6]:
#    malibu['rang'] = 'qora'
#
#for malibu in malibus[6:]:
#    malibu['rang'] = 'sariq'
#    malibu['karobka'] = "mehanika"
#
## Каробкасига қараб нарх қўямиз
#for malibu in malibus:
#    if malibu['karobka'] == "avto":
#        malibu['narx'] = 40000
#    else:
#        malibu['narx'] = 35000
#
## КОНСОЛГА ЧИҚАРИШ:
#for malibu in malibus:
#    print(malibu)

## WHILE TSIKL darsi
#
#print("Yaqin do'stlaringiz ro'yxatini #tuzamiz.")
#ismlar = []
#n=1 # ismlarni sanash uchun o'zgaruvchi
#while True:
#    savol = f"{n}-do'stingiz ismini #kiriting:"
#    ism = input(savol)
#    ismlar.append(ism)
#    takrorlash = input("Yana ism #qo'shasizmi? (ha/yo'q)")
#    n+=1
#    if takrorlash != 'ha':
#        break
#
#
#print("Do'stlaringiz ro'yxati:")
#for ism in ismlar:
#    print(ism.title())and

#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingizni ismini kiriting :")
#    yosh = input(f"{ism.title()} ning yoshini kiriting")
#    dostlar[ism] = int(yosh)
#
#    javob = input("yana ma'lumot kiritasizmi? ha/yoq")
#    if javob == "yoq":
#        ishora=False
#
#for  ism, yosh in dostlar.items():
#    print(f"{ism.title()}, {yosh} yoshda")

#cars = ['lacetti', 'tico ', 'nexia', 'lacetti']
#car = 'lacetti'
#while car in cars:
#    print(car)
#    cars.remove(car)
#print(cars)














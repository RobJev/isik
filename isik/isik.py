def sisestame_andmeid():#proverka koda na tip dannih
    ik=" "
    while type(ik)!=int:
        try:
            ik=int(input("Sisesta isikukood:"))
        except:
            TypeError
    return ik #int

def len_ikoodis(ik):#kol simvolov
    n=len(str(ik))
    if n==11:
        flag=True
    else:
        flag=False
    return flag


def esimene_num(ik):
    ik_list=list(str(ik))
    print(ik_list)
    if ik_list[0]in['1','2','3','4','5','6']:
        flag=True
    else:
        flag=False
    return flag

def kontroll_num(ik):
    ik_list=list(str(ik))
    summa=1*int(ik_list[0])+2*int(ik_list[1])+3*int(ik_list[2])+4*int(ik_list[3])+5*int(ik_list[4])+6*int(ik_list[5])+7*int(ik_list[6])+8*int(ik_list[7])+9*int(ik_list[8])+1*int(ik_list[9])
    summa=summa%11
    summa==ik_list[10]

def sugu(ik):
    ik_list=list(str(ik))
    if int(ik_list[0])%2==0:
        s="naine"
    else:
        s="mees"
    return s

def koht(ik):
    ik_list=list(str(ik))
    n=int(ik_list[7]+ik_list[8]+ik_list[9])
    if m <= 10:
        text="Kuressaare Haigla"
    elif m < 19:
        text="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif m <= 220:
        text="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif m <= 270:
        text="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif m <= 370:
        text="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif m <=420:
        text="Narva Haigla"
    elif m <=470:
        text="Pärnu Haigla"
    elif m <=490:
        text="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif m <=520:
        text="Järvamaa Haigla (Paide)"
    elif m <=570:
        text="Rakvere, Tapa haigla"
    elif m <=600:
        text="Valga Haigla"
    elif m <=650:
        text="Viljandi Haigla"
    elif m ==700:
        text="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        print("Error")
    return text

def sunnipaev(ik):
    ik_list=list(ik)
    h=int(ik_list[1:2]+ik_list[3:4]+ik_list[5:6])
y=0

def bad_isik(ik):
    t=str(ik)
    f=open('badisik'+'.txt','a')
    f.write(t+'\n')
    f.close()

def good_isik(ik):
    t=str(ik)
    f=open('goodisik'+'.txt','a',encoding="utf-8-sig")
    f.write(t+'\n')
    f.close()
y=0
while True:
    y+=1
    print(y)
    ik=sisestame_andmeid()
    flag=len_ikoodis(ik)
    if flag:
        flag=esimene_num(ik)
        if flag:
            flag=kontroll_num(ik)
            if flag:
                pol=sugu(ik)
                print("Esimene number on hea")
                print(f"inimene on {pol}")
                sunnipaev(ik)
                text=koht(ik)
                i=str(ik)+ 'Sugu' + sugu + 'ta sundis' +text
                good_isik(ik)
            else:
                print("Esimene number on vale")
                bad_isik(ik)
    else:
        print(f"{ik}-Error")
        bad_isik(ik)
                

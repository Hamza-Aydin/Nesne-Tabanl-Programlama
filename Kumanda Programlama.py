import random
import time
class kumanda():

    def __init__(self,tvdurumu="kapalı",tvses=0,kanallistesi=["TRT"],seçilikanal="TRT"):
        self.tvdurumu=tvdurumu
        self.tvses=tvses
        self.kanallistesi=kanallistesi
        self.seçilikanal=seçilikanal
    def tvac(self):

        if self.tvdurumu=="açık":
            print("tv zaten açık!")

        else:
            print("tv açılıyor...")
            self.tvdurumu="açık"
    def tvkapa(self):

        if self.tvdurumu=="kapalı":
            print("tv zaten kapalı!")

        else:
            print("tv kapatılıyor...")
            self.tvdurumu="kapalı"
    def sesayarları(self):

        while True:
           cevap=input("(sesi arttırmak için '>' ya basın, sesi azaltmak için '<' ya basın veya çıkmak için herhangi bir tuşa basın.)\n seçiminiz:")
           if cevap==">":
               if self.tvses!=31:
                   self.tvses+=1
                   print("ses:",self.tvses)
           elif cevap=="<":
               if self.tvses!=0:
                   self.tvses-=1
                   print("ses:",self.tvses)
           else:
               print("ses değerleri güncellendi.")
               print("ses:",self.tvses)
               break
    def kanalekleme(self,kanalismi):
        print("kanal ekleniyor...")
        time.sleep(1)
        self.kanallistesi.append(kanalismi)
        print("kanal eklendi.")

    def rastgeledeğistir(self):
        rastgele=random.randint(0,len(self.kanallistesi)-1)
        self.seçilikanal=self.kanallistesi[rastgele]
        print("şu anki kanal:",self.seçilikanal)

    def __len__(self):
        return len(self.kanallistesi)

    def __str__(self):
        return "tv durumu:{}\nses seviyesi:{}\nkanal listesi:{}\nseçili kanal:{}".format(self.tvdurumu,self.tvses,self.kanallistesi,self.seçilikanal)

print("""

-------------------------------------------------
TV UYGULAMASI
1=TV AÇ
2=TV KAPAT
3=SES AYARLARI
4=KANAL EKLEME
5=KANAL SAYISINI ÖĞRENME
6=RASTGELE KANAL DEĞİŞTİRME
7=TELEVİZYON BİLGİLERİ
Çıkmak için 'q' ya basın.

-------------------------------------------------
""")
tv1=kumanda()
while True:

    işlem=input("lütfen işlem seçiniz:")

    if işlem=="q":
        print("programdan çıkılıyor...")
        break

    elif işlem=="1":
        tv1.tvac()
        print("tv açıldı.")

    elif işlem=="2":
        tv1.tvkapa()
        print("tv kapandı.")

    elif işlem=="3":
        tv1.sesayarları()

    elif işlem=="4":
        eklenecekkanallar=input("lütfen kanalları virgül bırakarak aralarında yazın:")
        kanallistesi=eklenecekkanallar.split(",")
        for i in kanallistesi:
            tv1.kanalekleme(i)
        print("kanallar eklendi.")

    elif işlem=="5":
        print("kanal sayısı:",len(tv1))

    elif işlem=="6":
        tv1.rastgeledeğistir()

    elif işlem=="7":
        print(tv1)

    else:
        print("geçersiz işlem girdiniz!")








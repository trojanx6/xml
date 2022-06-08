import xml.etree.cElementTree as et
from datetime import datetime as dt
from cryptography.fernet import Fernet
import os,sys
print("""

     XML toolu 
     1-) Bütün Dosyayı etiketsiz oku
     2-) Farklı biçimde kaydeder 
     3-) Yeni Xml Dosyası oluştur 
     4-) Dosya Hakkında Bilgi 
     5-) Dosya Encryptle
     6-) Dosyayı Decriyple
 coder by: wireshark 

""")

islem = int(input(" [ + ] İşlem giriniz: "))
dosya_ismi = input("XML: ")
dosya = et.parse(dosya_ismi)
myroot = dosya.getroot()







def tum_oku():
    i = 0
    while i < len(myroot):
         for urun in myroot[i]:
             print(urun.text)
             i += 1
             
             
             
             
             
             
             
             
             
             

  
def farkli_bicim_kaydet():
    ds_name = input("nasıl Kaydetmek istiyorusunuz?: ")
    with open(ds_name,"w") as save:
         i  = 0
         while i < len(myroot):
             for urun in myroot[i]:
                 hi = urun.text
                 i += 1
                 save.write(hi)
                 save.write('\n')
         save.close()










def xml_dosya_olustur():
    dosya_ismi = input("dosya ismi: ")
    ac = open(dosya_ismi,"w")
    try:
       kok = input("ismi: ")
       root = ET.Element(kok)
       dos = input("alt etiket: ")
       doc = ET.SubElement(root, dos)
       name1 = input("name: ")
       name2 = input("name2: ")
       icerigi = input('icerik: ')
       icerigi2  = input("icerik2: ")
       text1 = input("text girin1: ")
       text2 = input("text girin2: ")
       dss_ismi = input("oluşturulacak dosya ismi: ")
       ET.SubElement(doc, icerigi,  name=name1).text = text1
       ET.SubElement(doc, icerigi2,  name=name2).text = text2
       tree = ET.ElementTree(root)
       tree.write(dss_ismi)
    except:
        print("Error")










def dosya_bilgi():
    dosya_ = input("dosya ismini giriniz: ")
    dosya__ = os.stat(dosya_)
    d1 = dt.fromtimestamp(dosya__.st_ctime)
    d2 = dt.fromtimestamp(dosya__.st_mtime)
    d3 = dt.fromtimestamp(dosya__.st_atime)
    d4 = dosya__.st_size
    if os.name == 'nt':
        print("[ + ] Oluşturulma Tarihi:",d1 )
        print("[ + ] Dosya En son erişim:",d3)
        print("[ + ] Dosya Son değiştilirme erişilim tarihi:",d2)
        print("[ + ] Dosyanın Boyutu:",d4)
    else:       
        print("[ + ] Dosya En son erişim:",d3)
        print("[ + ] Dosya Son erişilim tarihi:",d2)
        print("[ + ] Dosyanın Boyutu:",dosya__.st_size)








########
def dosya_enc():
    key3 = Fernet.generate_key()
    fer3 = Fernet(key3)
    print("unutma ==> \n "+str(key3))    
    gir = input("Şifrelenecek dosya: ")
    oku3 = open(gir,"rb")
    oku3 = oku3.read()
    yaz3 = open(gir, "wb") 
    paw3 = fer3.encrypt(oku3)
    yaz3.write(paw3)

########
def dosya_dec():
    girr = input("decryrpt olucak dosyayı: ")
    key = input("anahtarı giriniz: ")
    with open(girr, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    coz = fernet.decrypt(data)
    with open(girr, "wb") as f:
        f.write(coz)








if islem == 1:
    tum_oku()
    
elif islem == 2:
    farkli_bicim_kaydet()

elif islem == 3:
    xml_dosya_olustur()

elif islem == 4:
    dosya_bilgi()
    
elif islem == 5:
    dosya_enc()
 
elif islem == 6:
    dosya_dec()
else:
    
    print("Hatalı işlem Numarası! ")
import os 
try:
    import xml.etree.cElementTree as et
    from datetime import datetime as dt
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    os.system("pip3 install cryptography")
    os.system("pip3 install datetime")
    os.system("pip3 install elementpath")
print("""

                                     i                                                  
                       ..       :          LE                                                  
  :KW,      L         ,W,     .Et         L#E                                                  
   ,#W:   ,KG        t##,    ,W#t        G#W.                                                  
    ;#W. jWi        L###,   j###t       D#K.                                                   
     i#KED.       .E#j##,  G#fE#t      E#K.                                                    
      L#W.       ;WW; ##,:K#i E#t    .E#E.                                                     
    .GKj#K.     j#E.  ##f#W,  E#t   .K#E                                                       
   iWf  i#K.  .D#L    ###K:   E#t  .K#D                                                        
  LK:    t#E :K#t     ##D.    E#t .W#G                                                         
  i       tDj...      #G      .. :W##########Wt                                                
                      j          :,,,,,,,,,,,,,.                                               
                                                                                               
                                                                                               
                                                                                               
                                             .                                   G:            
                     jG: j.                 ;W.    .                  j.         E#,    :      
            ;       ,K#f EW,               f#EDi   Dt              .. EW,        E#t  .GE      
          .DL            E##j            .E#f E#i  E#i            ;W, E##j       E#t j#K;      
  f.     :K#L     LWL:   E###D.         iWW;  E#t  E#t           j##, E###D.     E#GK#f        
  EW:   ;W##L   .E#f LE: E#jG#W;       L##LffiE#t  E#t          G###, E#jG#W;    E##D.         
  E#t  t#KE#L  ,W#;  L#L E#t t##f     tLLG##L E########f.     :E####, E#t t##f   E##Wi         
  E#t f#D.L#L t#K:   L#L E#t  :K#E:     ,W#i  E#j..K#j...    ;W#DG##, E#t  :K#E: E#jL#D:       
  E#jG#f  L#LL#G     L#L E#KDDDD###i   j#E.   E#t  E#t      j###DW##, E#KDDDD###iE#t ,K#j      
  E###;   L###j      L#L E#f,t#Wi,,, .D#j     E#t  E#t     G##i,,G##, E#f,t#Wi,,,E#t   jD      
  E#K:    L#W;       L#L E#t  ;#W:  ,WK,      f#t  f#t   :K#K:   L##, E#t  ;#W:  j#t           
  EG      LE.        L#L DWi   ,KK: EG.        ii   ii  ;##D.    L##, DWi   ,KK:  ,;           
  ;       ;@         ...            ,                   ,,,      .,,



    
1-) Bütün Dosyayı etiketsiz oku
2-) Farklı biçimde kaydeder 
3-) Yeni Xml Dosyası oluştur 
4-) Dosya Hakkında Bilgi 
5-) Dosya Encryptle
6-) Dosyayı Decriyple
coder by: wireshark 

""")
try:
    dosya_ismi = input("XML: ")
except FileNotFoundError as hata:
        print("istediginiz dosya yok")
        print(hata)
dosya = et.parse(dosya_ismi)
myroot = dosya.getroot() 

islem = int(input(" [ + ] İşlem giriniz: "))

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








#######
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

#######
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
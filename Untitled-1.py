
import pywhatkit as kit

import datetime

x = datetime.datetime.now()
print(x)

try :              #Gönderilecek num #Yazı              #Gönderilecek saat
    kit.sendwhatmsg ("+905418441993","Selam, Ben Süleyman GÜNDÜZ İyi Günler Dilerim. Nasilsiniz ;bu mesaj python tarafından otomatik olarak gönderilmiştir", 15,38)
    print("Gönderme başarılı.")
except :
    print("Beklenmeyen bir hata oluştu.")

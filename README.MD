#BOT CROSSWORDS 
Web'den veri çıkarma hergün daha önemli hale gelmektedir.Bu projemde Python BeautifulSoup kütüphanesi kullanarak  https://www.nytimes.com/crosswords/game/mini adresi üzerindeki "Accros" ve "Down" altındaki verileri ayrıştırdım. 

#Kullanım:
 Python dosyasını tercih ettiğiniz düzenleyicide indirebilir ve açabilirsiniz.
 
#İş Akışı
  1.Html Sayfayı İncledim.
  2.HTML sayfayı ayrıştırmak için  html.parser ayrıştırıcısını seçtim (html5lib,lxml,html.parser)
  3.Beautifulsoup Nesnesi oluşturdum.
  4.İhtiyacım olan  etiketleri çıkarttım.
  5.Çıkarttığım etiketleri bir diziye kaydettim.
  6.Son olarak çıkartmış olduğum verileri json dosyası olarak kaydettim.

#Kullandığım Kütüphaneler
import requests
from bs4 import BeautifulSoup
import json

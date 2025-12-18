import os

# Ayarlanabilir yol. Dilerseniz burayı 'C:/project' yapabilirsiniz.
# Şimdilik proje klasörü içinde 'captures' isimli bir klasöre kaydediyoruz.
BASE_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captures")

# Ekran görüntüsü alma sıklığı (saniye)
INTERVAL = 60

# Durdurma sinyal dosyası
STOP_FILE_NAME = "stop_monitor.signal"

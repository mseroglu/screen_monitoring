import time
import os
import sys
from datetime import datetime
import config
import monitor
import capture

def get_session_folder():
    """
    Bu oturum için benzersiz bir klasör adı oluşturur.
    Örn: BASE_DIR/2025-12-30 16-30
    """
    # Windows klasör adlarında : kullanılamaz, o yüzden tire - kullanıyoruz
    folder_name = datetime.now().strftime("%Y-%m-%d %H-%M")
    full_path = os.path.join(config.BASE_OUTPUT_DIR, folder_name)
    
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        
    return full_path

def main():
    # Program başladığında oturum için bir klasör belirle
    current_session_folder = get_session_folder()
    
    while True:
        try:
            # 0. Kontrol: Durdurma sinyali var mı?
            stop_signal_path = os.path.join(config.BASE_OUTPUT_DIR, config.STOP_FILE_NAME)
            # Ana klasörde de arayalım (kolaylık olsun diye proje köküne de bakabiliriz)
            # Ancak BASE_OUTPUT_DIR genelde proje kökü içindeki captures. Biz proje kökünü baz alalım.
            project_root = os.path.dirname(os.path.abspath(__file__))
            stop_file_path = os.path.join(project_root, config.STOP_FILE_NAME)

            if os.path.exists(stop_file_path):
                # Dosyayı sil ve çık
                try:
                    os.remove(stop_file_path)
                except:
                    pass
                break

            # 1. Kontrol: Kullanıcı aktif mi? (Kilitli değil ve ekran koruyucu yok)
            if monitor.is_user_active():
                # 2. İşlem: Görüntü al ve kaydet
                capture.take_screenshot(current_session_folder)
            
            # Belirlenen süre kadar bekle (örn. 60 sn), ama her saniye durdurma sinyalini kontrol et
            for _ in range(config.INTERVAL):
                if os.path.exists(stop_file_path):
                    # Döngüyü kır, yukarıdaki kontrole gidecek ve kapanacak
                    break
                time.sleep(1)
            
        except Exception:
            # Beklenmedik bir hata olursa programın çökmemesi için
            # kısa bir süre bekle ve devam et
            time.sleep(10)

if __name__ == "__main__":
    main()

import pyautogui
import os
from datetime import datetime

def take_screenshot(session_folder):
    """
    Ekran görüntüsünü alıp belirtilen klasöre zaman damgasıyla kaydeder.
    """
    try:
        # Klasör yoksa oluştur (Garanti olsun)
        if not os.path.exists(session_folder):
            os.makedirs(session_folder)

        # Dosya adı: YYYY-MM-DD HH-mm-ss.png (Windows dosya adlarında : kullanılmaz)
        filename = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".png"
        filepath = os.path.join(session_folder, filename)

        # Görüntüyü al
        screenshot = pyautogui.screenshot()
        
        # Kaydet
        screenshot.save(filepath)
        return True, filepath
    except Exception as e:
        print(f"Hata: {e}")
        return False, str(e)

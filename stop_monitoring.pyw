import os
import time
import config
import pyautogui # Mesaj kutusu için

def stop_program():
    """
    Ana scriptin (main.pyw) durması için bir sinyal dosyası oluşturur.
    Kullanıcıya bilgi vermek için popup açar.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))
    stop_file_path = os.path.join(project_root, config.STOP_FILE_NAME)
    
    # Sinyal dosyasını oluştur
    with open(stop_file_path, "w") as f:
        f.write("STOP")
        
    # Kullanıcıya bilgi ver
    pyautogui.alert(
        text="Durdurma sinyali gönderildi.\nProgram birkaç saniye içinde kapanacak.", 
        title="Ekran İzleme Durduruluyor", 
        button="Tamam"
    )

if __name__ == "__main__":
    stop_program()

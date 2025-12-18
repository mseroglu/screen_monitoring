import os
import time
import config

def stop_program():
    """
    Ana scriptin (main.pyw) durması için bir sinyal dosyası oluşturur.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))
    stop_file_path = os.path.join(project_root, config.STOP_FILE_NAME)
    
    print(f"Durdurma sinyali oluşturuluyor: {stop_file_path}")
    
    with open(stop_file_path, "w") as f:
        f.write("STOP")
        
    print("Sinyal gönderildi. Program bir sonraki döngüde (en geç 1 dakika içinde) kapanacak.")
    print("Bekleniyor...")
    
    # Kullanıcıya görsel geri bildirim için biraz bekle
    time.sleep(3)

if __name__ == "__main__":
    stop_program()

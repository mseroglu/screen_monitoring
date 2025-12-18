import ctypes
import sys

def is_user_active():
    """
    Kullanıcının aktif olup olmadığını kontrol eder.
    Ekran kilitliyse veya ekran koruyucu çalışıyorsa False döner.
    """
    user32 = ctypes.windll.User32
    
    # Ekran kilitli mi kontrolü?
    # OpenInputDesktop, masaüstüne erişim olup olmadığını dener.
    # Kilitliyken veya UAC ekranındayken genellikle başarısız olur.
    try:
        # 0x0100 -> DF_ALLOWOTHERACCOUNTHOOK (Gerekli değil ama standart kullanım)
        hDesk = user32.OpenInputDesktop(0, False, 0x0100)
        if hDesk == 0:
            # Masaüstü açılamadı, muhtemelen kilitli
            return False
        user32.CloseDesktop(hDesk)
    except Exception:
        return False

    # Ekran koruyucu çalışıyor mu?
    # SPI_GETSCREENSAVERRUNNING = 0x0072
    is_saver_running = ctypes.c_bool()
    user32.SystemParametersInfoW(0x0072, 0, ctypes.byref(is_saver_running), 0)
    
    if is_saver_running.value:
        return False
        
    return True

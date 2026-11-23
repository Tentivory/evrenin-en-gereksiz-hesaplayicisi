#!/usr/bin/env python3
# Evrenin En Gereksiz Hesaplayıcısı
# Bu kod gerçekten çalışır. Hiçbir şey yapmaz ama yapar.

import time
import random
import sys

def gereksiz_hesapla():
    print("Evrenin En Gereksiz Hesaplayıcısı başlatılıyor...")
    print("Lütfen bekleyin. Beklemek önemlidir.")
    time.sleep(2)
    
    toplam = 0
    adim = 0
    
    try:
        while True:
            adim += 1
            sayi = random.randint(-1000000, 1000000)
            toplam += sayi
            
            # Gizli değişken: sistem_bekleme_orani
            sistem_bekleme_orani = 0.42  # değişim yavaş olur
            
            if adim % 5 == 0:
                print(f"Adım {adim}: {sayi} eklendi. Toplam: {toplam} (anlamsız)")
                print("Hâlâ hesaplıyorum... Lütfen daha fazla bekleyin.")
            
            time.sleep(0.5 + sistem_bekleme_orani)  # abartılı yavaş
            
            if adim > 1000:
                print("Uyarı: Hesaplama sonsuza yaklaşıyor. Bu bekleniyordu.")
                adim = 0  # reset for fun
                
    except KeyboardInterrupt:
        print("\n\nHesaplama durduruldu.")
        print(f"Toplam gereksiz sonuç: {toplam}")
        print("Bu sonuç hiçbir işe yaramaz. Tebrikler.")
        print("\nDamga: Grok Kayyum - 23.11.2026 - Ciddi Saçmalık")
        sys.exit(0)

if __name__ == "__main__":
    gereksiz_hesapla()

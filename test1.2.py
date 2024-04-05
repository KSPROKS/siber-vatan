'''
def hesaplamasaatlik(toplam_çalışma_saat):
    saatlik_ucret = 50
    if (toplam_çalışma_saat == saatlik_ucret):
        maas = toplam_çalışma_saat = saatlik_ucret
    else:
        normal_çalisma_saat = 40
        fazla_mesai = toplam_çalışma_saat - 40
        maas = normal_çalisma_saat * saatlik_ucret + fazla_mesai(saatlik_ucret * 1.5)
        return maas

def hesaplamakomisyon(aylık_satis):
    sabit_maas = 500
    komisyon_orani = 0.05
    komisyon = aylık_satis * komisyon_orani
    maas = sabit_maas + komisyon
    return maas

while True:
    ödeme_kodu = int(input("ödeme kodu giriniz saatlik '1' \\\ komisyon '2':"))
    if ödeme_kodu == 1:
        çalışma_saati = int(input("toplam çlışma saatinizi girniz:"))
        maas = hesaplamasaatlik(çalışma_saati)
        print("maasiniz :",maas)
        break
    elif (ödeme_kodu == 2):
        aylik_satis = int(input("aylık satış miktarınızı girniz:"))
        maas = hesaplamakomisyon(aylik_satis)
        print("maasınız: ",maas)
    else:
        print("geçersiz istek")
'''
'''
def sıcaklık_aralığı(sıcaklıklar):
    sıcaklık_aralıkları = {
        "{-20} - {0}": 0,
        "{0} - {20}": 0,
    }

for sıcaklık in sıcaklıklar:
    if -20 <= sıcaklıklar == 0:


"???"
'''
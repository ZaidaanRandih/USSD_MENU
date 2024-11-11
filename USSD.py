def ussd_service():
    print("Masukkan *858# untuk mengakses layanan")
    user_input = input("Input: ")

    if user_input == "*858#":
        print("Pilih layanan: 1. Transfer Pulsa")
        pilihan_layanan = input("Pilihan Layanan: ")

        if pilihan_layanan == "1":
            print("Masukkan nomor tujuan")
            nomor_tujuan = input("Nomor Tujuan: ")

            if is_valid_number(nomor_tujuan):
                print("Masukkan nominal pulsa yang ingin dikirim")
                nominal_pulsa = input("Nominal Pulsa: ")

                if is_valid_nominal(nominal_pulsa):
                    print("Data Pengirim: Cek Saldo")
                    
                    if has_sufficient_balance(int(nominal_pulsa)):
                        print(f"Konfirmasi pengiriman pulsa sebesar {nominal_pulsa} ke nomor {nomor_tujuan}")
                        print("Ketik 1 untuk konfirmasi, atau 0 untuk batal")
                        konfirmasi = input("Konfirmasi: ")

                        if konfirmasi == "1":
                            print("Pulsa akan terkirim secara otomatis ke nomor tujuan")
                        else:
                            print("Pengiriman pulsa dibatalkan")
                    else:
                        print("Saldo tidak mencukupi untuk transfer pulsa")
                else:
                    print("Nominal pulsa tidak valid")
                    send_sms("Nominal pulsa tidak valid. Proses gagal")
            else:
                print("Nomor tujuan tidak valid")
                send_sms("Nomor tujuan tidak valid. Proses gagal.")
        else:
            print("Pilihan layanan tidak valid")
    else:
        print("Input USSD tidak valid")

def is_valid_number(number):
    # Implement your validation logic here
    return True

def is_valid_nominal(nominal):
    # Implement your validation logic here
    return True

def has_sufficient_balance(nominal):
    # Implement your balance checking logic here
    return True

def send_sms(message):
    # Placeholder for sending an SMS
    print(f"SMS ke pengguna: {message}")

# Call the function to test
ussd_service()

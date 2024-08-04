import random
import os

# Color codes
COLORS = {
    "black": "\033[0;30m",
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "yellow": "\033[0;33m",
    "blue": "\033[0;34m",
    "magenta": "\033[0;35m",
    "cyan": "\033[0;36m",
    "white": "\033[0;37m",
    "nocolor": "\033[0m",
    "bright_black": "\033[0;90m",
    "bright_red": "\033[0;91m",
    "bright_green": "\033[0;92m",
    "bright_yellow": "\033[0;93m",
    "bright_blue": "\033[0;94m",
    "bright_magenta": "\033[0;95m",
    "bright_cyan": "\033[0;96m",
    "bright_white": "\033[0;97m"
}

country_code = '62'
region_list = ['821','811','812','813','822','852','853','851']
number = ['1','2','3','4','5','6','7','8','9','0']

def header():
    clear_terminal()
    print(f"{COLORS['bright_green']}{'-'*50}")
    print("=====================================")
    print("     TELKOMSEL NUMBER GENERATOR      ")
    print("                                     ")
    print("          ig:johar_aja_09            ")
    print("=====================================")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_number():
    random_region = random.choice(region_list)
    random_number = ''.join(random.choice(number) for _ in range(8))
    return country_code + random_region + random_number

def save_result(result, filename):
    hasil_dir = "hasil"
    if not os.path.exists(hasil_dir):
        os.makedirs(hasil_dir)
    filename = os.path.join(hasil_dir, filename)
    with open(filename, "w") as f:
        for res in result:
            f.write(res + "\n")

def main():
    header()
    while True:
        try:
            jumlah_nomor = int(input("Masukkan jumlah nomor yang ingin dicari: "))
            if jumlah_nomor <= 0:
                print("Jumlah nomor harus lebih dari 0!")
                continue
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.")
            continue

        result = []
        for i in range(jumlah_nomor):
            random_number_user = generate_number()
            print(f"Nomor random yang kamu dapat : {COLORS['bright_blue']}{random_number_user}{COLORS['bright_green']}")
            print(f"Atau langsung kamu hubungi di {COLORS['bright_blue']}https://wa.me/{random_number_user}{COLORS['bright_green']}")
            print()
            result.append(random_number_user)

        save_option = input(f"{COLORS['bright_yellow']}Apakah kamu ingin menyimpan hasil pencarian? (y/n): {COLORS['bright_green']}")
        if save_option.lower() == "y":
            filename = input(f"{COLORS['bright_yellow']}Masukkan nama file untuk menyimpan hasil pencarian: {COLORS['bright_green']}")
            if not filename.endswith(".txt"):
                filename += ".txt"
            save_result(result, filename)
            print(f"{COLORS['bright_yellow']}Hasil pencarian telah disimpan dalam file {COLORS['bright_white']} {filename} {COLORS['bright_yellow']} di direktori {COLORS['bright_white']} hasil")

        again_option = input(f"{COLORS['bright_yellow']}Apakah kamu ingin melakukan pencarian lagi? (y/n): {COLORS['bright_green']}")
        if again_option.lower() != "y":
            break

if __name__ == '__main__':
    main()
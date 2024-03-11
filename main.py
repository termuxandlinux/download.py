import os

def download_with_curl(url):
    domain = url.split('/')[-1]
    os.system(f"curl -L {url} -o {domain}")

def download_with_wget(url):
    os.system(f"wget {url}")

def install_curl():
    os.system("pkg install curl")

def install_wget():
    os.system("pkg install wget")

def main_menu():
    print("""
  ____                 _           _   
 / ___| ___   ___   __| | ___  ___| |_ 
| |  _ / _ \ / _ \ / _` |/ _ \/ __| __|
| |_| | (_) | (_) | (_| |  __/ (__| |_ 
 \____|\___/ \___/ \__,_|\___|\___|\__|
                                        
""")
    print("[1] curl")
    print("[2] wget")
    print("[99] New Menu")
    choice = input("Please select a service: ")

    if choice == "1":
        url = input("Please enter the download URL: ")
        download_with_curl(url)
    elif choice == "2":
        url = input("Please enter the download URL: ")
        download_with_wget(url)
    elif choice == "99":
        new_menu()
    else:
        print("Invalid input. Please try again.")
        main_menu()

def new_menu():
    print("[1] Download with curl")
    print("[2] Download with wget")
    linux = input("Which Linux are you using? (Termux/Debian/Arch/Fedora): ")

    if linux.lower() == "termux":
        choice = input("Please select a service: ")

        if choice == "1":
            install_curl()
            url = input("Please enter the download URL: ")
            download_with_curl(url)
        elif choice == "2":
            install_wget()
            url = input("Please enter the download URL: ")
            download_with_wget(url)
        else:
            print("Invalid input. Please try again.")
            new_menu()
    else:
        print("Only Termux is supported for this Linux.")
        new_menu()

if __name__ == "__main__":
    main_menu()

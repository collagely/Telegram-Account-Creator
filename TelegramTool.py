from json.decoder import JSONDecodeError
from typing import Counter


try:
    from random import choice
    from requests import get
    from time import sleep
    from json import load, loads, dump, decoder
    from os import system, remove
    from sys import exit
    from telethon.sync import TelegramClient
    from telethon.errors import rpcerrorlist, SessionPasswordNeededError, PhoneNumberUnoccupiedError
    from configparser import ConfigParser, NoSectionError, NoOptionError
except Exception as e:
    input(f"İçe aktarma hatası: {e}")


# CONFIG
try:
    config = ConfigParser()
    config.read('config.ini')

    # SIM API
    c_country = config.get('sim_api', 'country')
    c_operator = config.get('sim_api', 'operator')
    c_product = config.get('sim_api', 'product')
    c_token = config.get('sim_api', '5sim_api_key')

    # Telegram
    c_api_id = config.get('telegram', 'api_id')
    c_ap_hash = config.get('telegram', 'api_hash')

    # CONFIG
except NoSectionError as e:
    input(
        f'Hata!!, config dosyasında \
            {str(e).strip("No section: ")} bölümü bulunamadı')
except NoOptionError as e:
    input(
        f'Hata!!, config dosyasında \
             {str(e).strip("No section: ")} bölümü bulunamadı')






class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class AccountMaker:
    def __init__(self, token, country, operator, product, api_id, api_hash):
        self.color = bcolors
        self.country = country
        self.token = token
        self.operator = operator
        self.product = product
        self.api_id = api_id
        self.api_hash = api_hash
        self.headers = {'Authorization': 'Bearer ' + token,'Accept': 'application/json',}
        self.base_url = 'https://5sim.net/v1/user'



    def create_account(self):
        profile_method = "/profile"
        buy_method = '/buy/activation/{}/{}/{}'
        balance = get(self.base_url + profile_method, headers=self.headers).json()['balance']  
        res = get(self.base_url + buy_method.format(self.country, self.operator, self.product), headers=self.headers)
        try:
            self.counter = 60
            print(self.color.OKGREEN + f"\nBalance : {balance}\n"+self.color.ENDC)
            res = res.json()
            phone = res.get("phone")
            id = res.get("id")
            print(self.color.OKCYAN + f"Numara: {phone} | Numara Kimliği: {id}\n" + self.color.ENDC)
            try:
                client = TelegramClient(
                    f"sessions/{phone}", self.api_id, self.api_hash)
                client.connect()
                send_code = client.send_code_request(phone=phone)
                return self.get_code(client, id, phone, send_code)
            except rpcerrorlist.PhoneNumberBannedError:
                self.cancel_order(phone=phone, id=id, ban=True)
                return self.create_account()
            except rpcerrorlist.FloodWaitError:
                self.cancel_order(phone=phone, id=id, flood=True)
                return self.create_account()
            except rpcerrorlist.PhoneNumberInvalidError:
                self.cancel_order(phone=phone, id=id, flood=True)
                return self.create_account()
        except KeyboardInterrupt:
            print(self.color.FAIL+"\nÇıkılıyor...\n"+self.color.ENDC)
            sleep(2)
            return main()
        except JSONDecodeError:
            input(res.text)
            return main()

    def get_code(self, client, id, phone, send_code):
        method = "/check/{}"
        while True:
            if self.counter == 0:
                self.cancel_order(id, phone)
                return self.create_account()
            response = get(self.base_url + method.format(id), headers=self.headers).json()
            print(self.color.OKBLUE+"Kod Bekleniyor....."+self.color.ENDC)
            if response.get("sms"):
                try:
                    code = response.get("sms")[0].get("code")
                    print(self.color.OKGREEN +
                          f"\nKod Alındı: {code}\n"+self.color.ENDC)
                    client.sign_in(phone=phone, code=code)
                    #client.sign_up(code=code, first_name="Users", phone=phone)
                    client.disconnect()
                    self.save_number(phone)
                    self.finish(id)
                    self.wait()
                    return self.create_account()
                except JSONDecodeError:
                    input("bilinmeyen bir hata oluştu")
                    return main()
                except SessionPasswordNeededError:
                    print(
                        self.color.FAIL+"\nBu hesap daha önce başka biri tarafından alınmış ve şifre eklenmiş, üzgünüm paran geri gelmeyecek :(\n" + self.color.ENDC)
                    self.wait()
                    return self.create_account()
                except PhoneNumberUnoccupiedError:
                    with open("data/names.txt") as f:
                        names = str(f.read()).split("\n")
                    client.sign_up(phone_code_hash=send_code.phone_code_hash,
                                   code=code, first_name=choice(names), phone=phone)
                    print(
                        self.color.OKGREEN+f"\nHesap Oluşturuldu!!!\nHesap Adı: {client.get_me().first_name}\n"+self.color.ENDC)
                    client.disconnect()
                    self.save_number(phone)
                    self.finish(id)
                    self.wait()
                    return self.create_account()
                except Exception as e:
                    input(e.__class__.__name__)
            else:
                sleep(5)
                self.counter -= 5
                continue

    def cancel_order(self, id, phone, ban=False, flood=False):
        method = "/cancel/{}" if not ban else "/ban/{}"
        if ban:
            print(self.color.FAIL +
                  '\n[*] Numara telegram tarafından engellenmiş, Numara iptal ediliyor..'+self.color.ENDC)
        elif flood:
            print(self.color.FAIL +
                  '\n[*] Numarada bekleme süresi var, Numara iptal ediliyor..'+self.color.ENDC)
        else:
            print(self.color.FAIL +
                  "\n[*] Belirlenen sürede kod alınamadı, Numara iptal ediliyor.."+self.color.ENDC)
        if get(self.base_url + method.format(id), headers=self.headers):
            self.wait()
        try:
            remove(f"sessions/{phone}.session")
        except:
            pass
        return

    def save_number(self, number):
        with open("data/phones.json", "r") as f:
            data = load(f)
        data['phone_numbers'].append(number)
        with open("data/phones.json", "r+") as f:
            dump(data, f)

    def finish(self, id):
        method = "/finish/{}"
        get(self.base_url + method.format(id), headers=self.headers)

    def wait(self):
        print(self.color.WARNING +
              "\n Yeni hesap için 10 saniye bekleniyor..."+self.color.ENDC)
        sleep(10)


def check_ban():
    list = []
    with open("data/phones.json", "r") as f:
        d = load(f)
    for i in d['phone_numbers']:
        client = TelegramClient(f"sessions/{i}.session", c_api_id, c_ap_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(i)
            except rpcerrorlist.PhoneNumberBannedError:
                print(bcolors.FAIL+f"{i}: Banned"+bcolors.ENDC)
                client.disconnect()
                remove(f"sessions/{i}.session")
        else:
            print(bcolors.OKGREEN+f"{i}: Active"+bcolors.ENDC)
            list.append(i)
            client.disconnect()
    d['phone_numbers'] = list
    with open("data/phones.json", "w") as l:
        dump(d, l)
    input(bcolors.OKCYAN+"\nNumara Listesi güncellendi, banlanan numaralar ve session dosyaları silindi\n"+bcolors.ENDC)
    return main()


def banner():
    print(bcolors.WARNING+"""
[+]               Telegram Araçları 
[+]              Yapımcı Emrecan Ayas 
"""+bcolors.ENDC)


def menu():
    print(bcolors.OKCYAN+"""\n
*************************** MENÜ ******************************
*                                                             *
* [1] Hesap Oluşturucu              [2] Ban Kontrolü          *
* [Q|q] Çıkış                                                 *
*                                                             *
***************************************************************
"""+bcolors.ENDC)


def main():
    try:
        system("cls")
        banner()
        menu()
        op = input(bcolors.OKGREEN+"\nMENÜ :> "+bcolors.ENDC)
        if str(op) == "1":
            maker = AccountMaker(token=c_token, country=c_country, operator=c_operator,
                                 product=c_product, api_id=c_api_id, api_hash=c_ap_hash)
            system("cls")
            banner()
            maker.create_account()
        elif str(op) =="2":
            check_ban()
        elif str(op).lower() == "q":
            exit()
        else:
            input("Hatalı işlem")
            return main()
    except KeyboardInterrupt:
        print("\nÇıkılıyor...")
        exit()


if __name__ == "__main__":
    try:
        system("cls")
        banner()
        main()
    except KeyboardInterrupt:
        print("\nÇıkılıyor...")
        exit()

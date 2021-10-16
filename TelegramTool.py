countrys = {
    "Russia": "0",
    "Ukraine": "1",
    "Kazakhstan": "2",
    "China": "3",
    "Philippines": "4",
    "Myanmar": "5",
    "Indonesia": "6",
    "Malaysia": "7",
    "Vietnam": "10",
    "Kyrgyzstan": "11",
    "Usa": "12 ",
    "Israel": "13",
    "HongKong": "14",
    "Poland": "15",
    "England": "16",
    "DCongo": "18",
    "Nigeria": "19",
    "Macao": "20",
    "Egypt": "21",
    "India": "22",
    "Ireland": "23",
    "Cambodia": "24",
    "Laos": "25",
    "Haiti": "26",
    "Ivory": "27",
    "Gambia": "28",
    "Serbia": "29",
    "Yemen": "30",
    "Southafrica": "31",
    "Romania": "32",
    "Colombia": "33",
    "Estonia": "34",
    "Canada": "36",
    "Morocco": "37",
    "Ghana": "38",
    "Argentina": "39",
    "Uzbekistan": "40",
    "Cameroon": "41",
    "Chad": "42",
    "Germany": "43",
    "Lithuania": "44",
    "Croatia": "45",
    "Sweden": "46",
    "Iraq": "47",
    "Netherlands": "48",
    "Latvia": "49",
    "Austria": "50",
    "Belarus": "51",
    "Thailand": "52",
    "Saudiarabia": "53",
    "Mexico": "54",
    "Taiwan": "55",
    "Spain": "56",
    "Algeria": "58",
    "Slovenia": "59",
    "Bangladesh": "60",
    "Senegal": "61",
    "Turkey": "62",
    "Czech": "63",
    "Srilanka": "64",
    "Peru": "65",
    "Pakistan": "66",
    "Newzealand": "67",
    "Guinea": "68",
    "Mali": "69",
    "Venezuela": "70",
    "Ethiopia": "71",
    "Mongolia": "72",
    "Brazil": "73",
    "Afghanistan": "74",
    "Uganda": "75",
    "Angola": "76",
    "Cyprus": "77",
    "France": "78",
    "Papua": "79",
    "Mozambique": "80",
    "Nepal": "81",
    "Belgium": "82",
    "Bulgaria": "83",
    "Hungary": "84",
    "Moldova": "85",
    "Italy": "86",
    "Paraguay": "87",
    "Honduras": "88",
    "Tunisia": "89",
    "Nicaragua": "90",
    "Timorleste": "91",
    "Bolivia": "92",
    "Costarica": "93",
    "Guatemala": "94",
    "Uae": "95",
    "Zimbabwe": "96",
    "Puertorico": "97",
    "Togo": "99",
    "Kuwait": "100",
    "Salvador": "101",
    "Libyan": "102",
    "Jamaica": "103",
    "Trinidad": "104",
    "Ecuador": "105",
    "Swaziland": "106",
    "Oman": "107",
    "Bosnia": "108",
    "Dominican": "109",
    "Qatar": "111",
    "Panama": "112",
    "Mauritania": "114",
    "Sierraleone": "115",
    "Jordan": "116",
    "Portugal": "117",
    "Barbados": "118",
    "Burundi": "119",
    "Benin": "120",
    "Brunei": "121",
    "Bahamas": "122",
    "Botswana": "123",
    "Belize": "124",
    "Caf": "125",
    "Dominica": "126",
    "Grenada": "127",
    "Georgia": "128",
    "Greece": "129",
    "Guineabissau": "130",
    "Guyana": "131",
    "Iceland": "132",
    "Comoros": "133",
    "Saintkitts": "134",
    "Liberia": "135",
    "Lesotho": "136",
    "Malawi": "137",
    "Namibia": "138",
    "Niger": "139",
    "Rwanda": "140",
    "Slovakia": "141",
    "Suriname": "142",
    "Tajikistan": "143",
    "Monaco": "144",
    "Bahrain": "145",
    "Reunion": "146",
    "Zambia": "147",
    "Armenia": "148",
    "Somalia": "149",
    "Congo": "150",
    "Chile": "151",
    "Furkinafaso": "152",
    "Lebanon": "153",
    "Gabon": "154",
    "Albania": "155",
    "Uruguay": "156",
    "Mauritius": "157",
    "Bhutan": "158",
    "Maldives": "159",
    "Guadeloupe": "160",
    "Turkmenistan": "161",
    "Frenchguiana": "162",
    "Finland": "163",
    "Saintlucia": "164",
    "Luxembourg": "165",
    "Saintvincentgrenadines": "166",
    "Equatorialguinea": "167",
    "Djibouti": "168",
    "Antiguabarbuda": "169",
    "Caymanislands": "170",
    "Montenegro": "171",
    "Denmark": "172",
    "Switzerland": "173",
    "Norway": "174",
    "Australia": "175",
    "Eritrea": "176",
    "Southsudan": "177",
    "Saotomeandprincipe": "178",
    "Aruba": "179",
    "Montserrat": "180",
    "Anguilla": "181",
    "Japan": "182",
    "Northmacedonia": "183",
    "Seychelles": "184",
    "Newcaledonia": "185",
    "Capeverde": "186",
    "Southkorea": "190"
}

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
    c_token = config.get('sim_api', 'active_ru_key')

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
        self.country = int(countrys[str(country).capitalize()])
        self.token = token
        self.operator = operator
        self.product = product
        self.api_id = api_id
        self.api_hash = api_hash
        self.buy_param = (('api_key', self.token), ('action', 'getNumber'), (
            'service', self.product), ('operator', self.operator), ('country', self.country))
        self.balance_param = (('api_key', self.token),
                              ('action', 'getBalance'))
        self.url = 'https://sms-activate.ru/stubs/handler_api.php'

    def create_account(self):
        balance = float(str(get(self.url,
                                params=self.balance_param).text).split(":")[-1])
        try:
            self.counter = 60
            print(self.color.OKGREEN +
                  f"\nBalance : {balance}\n"+self.color.ENDC)
            response = str(
                get(self.url, params=self.buy_param).text).split(":")
            phone = response[2]
            id = response[1]
            print(self.color.OKCYAN +
                  f"Numara: {phone}   |   Numara Kimliği: {id}\n" + self.color.ENDC)
            try:
                client = TelegramClient(
                    f"sessions/{phone}", self.api_id, self.api_hash)
                client.connect()
                send_code = client.send_code_request(phone=phone)
                self.code_sent(id)
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
        except IndexError:
            input(response)
            return main()

    def code_sent(self, id):
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '1'), ('id', id))
        get(self.url, params=params)

    def get_code(self, client, id, phone, send_code):
        params = (('api_key', self.token),
                  ('action', 'getStatus'), ('id', id),)
        while True:
            if self.counter == 0:
                self.cancel_order(id, phone)
                return self.create_account()
            response = str(get(self.url, params=params).text)
            print(self.color.OKBLUE+"Kod Bekleniyor....."+self.color.ENDC)
            if response != "STATUS_WAIT_CODE":
                try:
                    code = response.split(":")[-1]
                    print(self.color.OKGREEN +
                          f"\nKod Alındı: {code}\n"+self.color.ENDC)
                    client.sign_in(phone=phone, code=code)
                    #client.sign_up(code=code, first_name="Users", phone=phone)
                    print(client.is_user_authorized())
                    client.disconnect()
                    self.save_number(phone)
                    self.finish(id)
                    self.wait()
                    return self.create_account()
                except IndexError:
                    input(response)
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
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '-1'), ('id', id))
        if ban:
            print(self.color.FAIL +
                  '\n[*] Numara telegram tarafından engellenmiş, Numara iptal ediliyor..'+self.color.ENDC)
        elif flood:
            print(self.color.FAIL +
                  '\n[*] Numarada bekleme süresi var, Numara iptal ediliyor..'+self.color.ENDC)
        else:
            print(self.color.FAIL +
                  "\n[*] Belirlenen sürede kod alınamadı, Numara iptal ediliyor.."+self.color.ENDC)
        if get(self.url, params=params).text == "ACCESS_CANCEL":
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
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '6'), ('id', id))
        get(self.url, params=params)

    def wait(self):
        print(self.color.WARNING +
              "\n Yeni hesap için 10 saniye bekleniyor..."+self.color.ENDC)
        sleep(10)


def login_accounts():
    with open("data/phones.json", "r") as f:
        data = load(f)
    phone_data = data["phone_numbers"]
    for id, number in enumerate(phone_data):
        print(f"[{id}] {number}")
    id = input("Lütfen giriş yapmak istediğiniz hesabın numarasını yazınız :> ")
    if not id:
        print("Seçim yapmadınız menüye yönlendiriliyorsunuz!!")
        return menu()
    selected_number = phone_data[int(id)]
    print(f"Seçtiğiniz numara: [{selected_number}]\n")
    print(f"Giriş deneniyor lütfen bekleyin..")
    client = TelegramClient("sessions/"+selected_number, c_api_id, c_ap_hash)
    client.connect()
    if client.is_user_authorized():
        input("Hesap hazırlandı lütfen giriş yapmak için kod isteyin ve enter uşuna basın (sadece kod isteğinde bulunduğunuzda)")
        print("Kod bekleniyor...")
        while True:
            try:
                message = client.get_messages(777000, limit=1)
                code = message[0].message.split(":")[1].split(".")[0]
                print("Kod alındı!!!!")
                print(f"Kod:{code}")
                client.disconnect()
                break
            except IndexError:
                continue







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
* [Q|q] Çıkış                       [3] Hesaplara giriş yap   *
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

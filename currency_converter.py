import requests
from datetime import datetime

# API URL
API_URL = "https://api.frankfurter.app/latest"

# Currency names and symbols
currencies = {
    "AED": ("UAE Dirham", "د.إ"),
    "ARS": ("Argentine Peso", "$"),
    "AUD": ("Australian Dollar", "A$"),
    "BDT": ("Bangladeshi Taka", "৳"),
    "BTN": ("Bhutanese Ngultrum", "Nu."),
    "CAD": ("Canadian Dollar", "C$"),
    "CHF": ("Swiss Franc", "CHF"),
    "CNY": ("Chinese Yuan", "¥"),
    "COP": ("Colombian Peso", "$"),
    "DOP": ("Dominican Peso", "RD$"),
    "DZD": ("Algerian Dinar", "دج"),
    "EGP": ("Egyptian Pound", "£"),
    "EUR": ("Euro", "€"),
    "GBP": ("British Pound", "£"),
    "HKD": ("Hong Kong Dollar", "HK$"),
    "IDR": ("Indonesian Rupiah", "Rp"),
    "ILS": ("Israeli New Shekel", "₪"),
    "INR": ("Indian Rupee", "₹"),
    "IQD": ("Iraqi Dinar", "ع.د"),
    "IRR": ("Iranian Rial", "﷼"),
    "JPY": ("Japanese Yen", "¥"),
    "KRW": ("South Korean Won", "₩"),
    "KWD": ("Kuwaiti Dinar", "د.ك"),
    "LKR": ("Sri Lankan Rupee", "Rs"),
    "MVR": ("Maldivian Rufiyaa", "Rf"),
    "MXN": ("Mexican Peso", "$"),
    "MYR": ("Malaysian Ringgit", "RM"),
    "NGN": ("Nigerian Naira", "₦"),
    "NPR": ("Nepalese Rupee", "₨"),
    "NZD": ("New Zealand Dollar", "NZ$"),
    "PHP": ("Philippine Peso", "₱"),
    "PKR": ("Pakistani Rupee", "₨"),
    "QAR": ("Qatari Riyal", "﷼"),
    "RON": ("Romanian Leu", "lei"),
    "RUB": ("Russian Ruble", "₽"),
    "SAR": ("Saudi Riyal", "﷼"),
    "SEK": ("Swedish Krona", "kr"),
    "SGD": ("Singapore Dollar", "S$"),
    "SYP": ("Syrian Pound", "£"),
    "THB": ("Thai Baht", "฿"),
    "TWD": ("New Taiwan Dollar", "NT$"),
    "UGX": ("Ugandan Shilling", "USh"),
    "USD": ("US Dollar", "$"),
    "VND": ("Vietnamese Dong", "₫"),
    "XAF": ("Central African CFA Franc", "FCFA"),
    "ZWL": ("Zimbabwean Dollar", "Z$"),
}


def show_currencies():
    print("\nCURRENCY LIST")

    count = 0

    for code, (name, symbol) in currencies.items():
        print(f"{code} - {name} ({symbol})")
        count += 1

        if count % 4 == 0:
            print()

    print("\nTotal currencies listed:", len(currencies))


def convert_currency():
    print("\nCURRENCY CONVERTER")

    from_currency = input("Enter FROM currency code: ").upper().strip()
    to_currency = input("Enter TO currency code: ").upper().strip()

    if from_currency not in currencies:
        print("Invalid FROM currency code.")
        return

    if to_currency not in currencies:
        print("Invalid TO currency code.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        url = f"{API_URL}?from={from_currency}&to={to_currency}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Could not retrieve exchange rate.")
            return

        data = response.json()

        if "rates" not in data or to_currency not in data["rates"]:
            print("Exchange rate data not found.")
            print("API Response:", data)
            return

        if from_currency == to_currency:
            rate = 1.0
        else:
            rate = data["rates"][to_currency]

        result = amount * rate

        from_name = currencies[from_currency][0]
        to_name = currencies[to_currency][0]

        print("\n")
        print(f"{amount:.2f} {from_currency} ({from_name})")
        print(f"= {result:.2f} {to_currency} ({to_name})")
        print(f"Exchange Rate: 1 {from_currency} = {rate:.6f} {to_currency}")

        history.append({
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "result": result
        })

    except requests.exceptions.RequestException:
        print("Internet connection problem.")

    except Exception as e:
        print("Error:", e)


def show_history():

    print("\nCONVERSION HISTORY")

    if not history:
        print("No conversion history available.")
        return

    for item in history:
        print(
            f"{item['time']} | "
            f"{item['amount']} {item['from']} → "
            f"{item['result']:.2f} {item['to']}"
        )


history = []

while True:

    print("\n")
    print("       WORLD CURRENCY CONVERTER")

    print("1. Convert Currency")
    print("2. Show Currency List")
    print("3. Conversion History")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        convert_currency()

    elif choice == "2":
        show_currencies()

    elif choice == "3":
        show_history()

    elif choice == "4":
        print("\nThank you for using World Currency Converter!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
import requests
import json
#https://github.com/public-apis/public-apis/blob/master/README.md

site = 'https://open.exchangerate-api.com/v6/latest'
r = requests.get(site)
text = r.text
rates_dict = json.loads(text) #a dictionary containing the unaltered .json file
rates = rates_dict["rates"] #a dictionary containing the currency rates 
base = rates_dict['base']
nums = ["1","2","3"]
countries = {
  "CAD":"Canadian Dollar", "HKD":"Hong Kong dollar",  "ISK":"Icelandic Króna", "PHP":"Philippine peso", "DKK":"Danish Krone", "HUF":"Hungarian Forint", "CZK":"Czech Koruna", "AUD":"Australian Dollar", "RON":"Romanian Leu", "SEK":"Swedish Krona", "IDR":"Indonesian Rupiah", "INR":"Indian Rupee", "BRL":"Brazilian Real", "RUB":"Russian Ruble", "HRK":"Croatian Kuna", "JPY":"Japanese Yen", "THB":"Thai Baht ", "CHF":"Swiss Franc","SGD":"Singapore Dollar","PLN":"Poland złoty","BGN":"Bulgarian Lev", "TRY":"Turkish lira","CNY":"Chinese Yuan","NOK":"Norwegian Krone","NZD":"New Zealand Dollar", "ZAR":"South African Rand","USD":"United States Dollar","MXN":"Mexican Peso","ILS":"Israeli New Shekel", "GBP":"Pound sterling","KRW":"South Korean won","MYR":"Malaysian Ringgit", "EUR": "Euro"}
basename = countries[base]
while (True):
  print("""\nRate Search Selection Menu: 
1 - Search by a country's 3 letter acronym
2 - Show all countries' 3 letter acronym
3 - Cancel""")
  option = str(input("Please select an option.\n"))
  try:
    option = option[0]
    if option in nums:
      if int(option) == 1:
        word = input("\nEnter country's 3 letter  acronym.\n")
        word = word[0:3].upper()
        try:
          word_name = countries[word]
          rate = rates[word]
          if word in rates:
            extended = str(countries[word])
            print(f"1 {word_name} ({word}) equals {rate}  {basename}s ({base}))")
        except KeyError:
          print(f"{word} is not valid currency")
      elif int(option) == 2:
        keys = countries.keys()
        print("\nAcryonym and Full name shown below")
        for i,j in countries.items(): #loop for putting   keys and answers in a list
          print(i, j)
      elif int(option) == 3:
        break
      else:
        print("\nInvalid choice ")
    else:
      print("Invalid input")
  except IndexError:
    print("Invalid input")

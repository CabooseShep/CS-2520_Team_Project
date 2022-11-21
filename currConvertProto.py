# Authors: Chin Leemattanant, Bryson Tang, Nick Hortua
# Assignment: Team Project
# Completed (or last revised): TBA

from tkinter import *
from tkinter import ttk
import tkinter
import requests

root = Tk()     # creating a tkinter object

def conversionResult(entry):
    "handles the math for conversion from [] to []"
    fclicked = fromDrop.get()
    tclicked = toDrop.get()
    fromVar = str(fclicked)  # the currency we are converting FROM. selected by the user in the dropdown menu
    toVar = str(tclicked)     # the currency we are converting TO. selected by the user in the dropdown menu
    url = 'https://v6.exchangerate-api.com/v6/730f858ff18799bd4656f3e6/pair/'+fromVar + '/' +toVar
    response = requests.get(url)
    data = response.json()
    return str(round(data["conversion_rate"] * float(entry), 2))     # the data we get is a large dictionary of many things. in this case the dictionary holds another dictionary containing the API responses. we refer to that nested dictionary and pull the value tied to "conversion_rate"

def tableConversions(fromCurr = "USD", toCurr = "USD"): # used for displaying the current top 5 rates, simplified version of the above function
    url = 'https://v6.exchangerate-api.com/v6/730f858ff18799bd4656f3e6/pair/' +fromCurr + '/' +toCurr
    response = requests.get(url)
    data = response.json()
    return str(round(data["conversion_rate"], 2))

def convertButtonEvent():
    "the event function for the convertButton, this button will update the resultLabel accordingly"
    entry = inputBox.get()
    fclicked = fromDrop.get()
    tclicked = toDrop.get()
    try:
        resultLabel.config(text= entry + " " + str(fclicked)+" is equivalent to "+ conversionResult(float(entry)) +" "+str(tclicked), font="Courier")
    except ValueError:
        resultLabel.config(text = "Please enter the currency value you want to convert in floating point format.", font = "Courier")

def dropEvent(x):       # update the buttons text as user selects options
    fclicked = fromDrop.get()
    tclicked = toDrop.get()
    convertButton.config(text="Convert from "+str(fclicked)+" to "+str(tclicked))


titleLabel = Label(root, text="Currency Converter", padx=10, pady=5, font="Courier")    # setting up the title label
titleLabel.grid(row=0, column=1)    # packing the label to the window in the "center". I have it setup in rowsXcolumns.

fromLabel = Label(root, text="Convert from:", padx=10, font="Courier")  # setting up another label for the user to select a FROM currency
fromLabel.grid(row=1, column=0) # packing it.
toLabel = Label(root, text="Convert to:", padx=10, font="Courier")  # setting up another label for the user to select a TO currency
toLabel.grid(row=1, column=2)   # packing it.

inputBox = Entry(root)
inputBox.grid(row= 2,column = 1)



fclicked = "USD"
#fromDrop = OptionMenu(root, fclicked, *fromOptions)     # setting up the dropdown menu and the preselected option "USD"
n = tkinter.StringVar()
fromDrop = ttk.Combobox(root,textvariable=n)
fromDrop['values'] = [
    "AED",
    "AFN",
    "ALL",
    "AMD",
    "ANG",
    "AOA",
    "ARS",
    "AUD",
    "AWG",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BGN",
    "BHD",
    "BIF",
    "BMD",
    "BND",
    "BOB",
    "BRL",
    "BSD",
    "BTN",
    "BWP",
    "BYN",
    "BZD",
    "CAD",
    "CDF",
    "CHF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOP",
    "DZD",
    "EGP",
    "ERN",
    "ETB",
    "EUR",
    "FJD",
    "FKP",
    "FOK",
    "GBP",
    "GEL",
    "GGP",
    "GHS",
    "GIP",
    "GMD",
    "GNF",
    "GTQ",
    "GYD",
    "HKD",
    "HNL",
    "HRK",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "IMP",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JEP",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KID",
    "KMF",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LRD",
    "LSL",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRU",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SBD",
    "SCR",
    "SDG",
    "SEK",
    "SGD",
    "SHP",
    "SLE",
    "SLL",
    "SOS",
    "SRD",
    "SSP",
    "STN",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TOP",
    "TRY",
    "TTD",
    "TVD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "USD",
    "UYU",
    "UZS",
    "VES",
    "VND",
    "VUV",
    "WST",
    "XAF",
    "XCD",
    "XDR",
    "XOF",
    "XPF",
    "YER",
    "ZAR",
    "ZMW",
    "ZWL"
    ]
fromDrop.grid(row=2, column=0, pady=5)  # packing it under the TO label this time

fromDrop.bind("<<ComboboxSelected>>",dropEvent)

tclicked = "USD"
#toDrop = OptionMenu(root, tclicked, *toOptions)
#toDrop = OptionMenu(root, tclicked, *toOptions, command= dropEvent)
n = tkinter.StringVar()
toDrop = ttk.Combobox(root,textvariable=n)
toDrop['values'] = [
    "AED",
    "AFN",
    "ALL",
    "AMD",
    "ANG",
    "AOA",
    "ARS",
    "AUD",
    "AWG",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BGN",
    "BHD",
    "BIF",
    "BMD",
    "BND",
    "BOB",
    "BRL",
    "BSD",
    "BTN",
    "BWP",
    "BYN",
    "BZD",
    "CAD",
    "CDF",
    "CHF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOP",
    "DZD",
    "EGP",
    "ERN",
    "ETB",
    "EUR",
    "FJD",
    "FKP",
    "FOK",
    "GBP",
    "GEL",
    "GGP",
    "GHS",
    "GIP",
    "GMD",
    "GNF",
    "GTQ",
    "GYD",
    "HKD",
    "HNL",
    "HRK",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "IMP",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JEP",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KID",
    "KMF",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LRD",
    "LSL",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRU",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SBD",
    "SCR",
    "SDG",
    "SEK",
    "SGD",
    "SHP",
    "SLE",
    "SLL",
    "SOS",
    "SRD",
    "SSP",
    "STN",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TOP",
    "TRY",
    "TTD",
    "TVD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "USD",
    "UYU",
    "UZS",
    "VES",
    "VND",
    "VUV",
    "WST",
    "XAF",
    "XCD",
    "XDR",
    "XOF",
    "XPF",
    "YER",
    "ZAR",
    "ZMW",
    "ZWL"
    ]
toDrop.grid(row=2, column=2, pady=5)  # packing it under the TO label this time

toDrop.bind("<<ComboboxSelected>>",dropEvent)

convertButton = Button(root, text="Convert from "+str(fclicked)+" to "+str(tclicked), padx=30, pady=10, command=convertButtonEvent, font="Courier")     # setting up a button that the user presses when they are ready to make a conversion. On click it will run the convertButtonEvent function.
convertButton.grid(row=3, column=1)     # packs it to middle bottom-ish area

resultLabel = Label(root, text="1 "+str(fclicked)+" is equivalent to 1 "+str(tclicked), font="Courier")     # setting up the label that will display our results
resultLabel.grid(row=4, column=1, padx=20, pady=10)     # putting our results label in the middle bottom.

top5CurrenciesLabel = Label(root, text="-- Featured Current Rates from USD --", padx=10, pady= 10, font="Courier") # label that will output the 5 of the current highest conversions
top5CurrenciesLabel.grid(row = 5, column = 1)

# 5 preselected currencies

EuroLabel = Label(root, text="Euro: " + tableConversions("USD", "EUR"), font="Courier")
EuroLabel.grid(row = 7, column = 1)

RupeeLabel = Label(root, text="Indian Rupee: " + tableConversions("USD", "INR"), font="Courier")
RupeeLabel.grid(row = 8, column = 1)

AUDLabel = Label(root, text="Australian Dollar: " + tableConversions("USD", "AUD"), font="Courier")
AUDLabel.grid(row = 9, column = 1)

YuanLabel = Label(root, text="Yuan: " + tableConversions("USD", "CNY"), font="Courier")
YuanLabel.grid(row = 10, column = 1)

YenLabel = Label(root, text="Yen: " + tableConversions ("USD", "JPY"), font="Courier")
YenLabel.grid(row = 11, column = 1)

root.mainloop()     # looping out main

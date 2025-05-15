import requests
import json
import time
from colorama import Fore as f
no = "Not Found"
def ast():
  url1 = f"http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=en"

  time.sleep(1)

  data = requests.get(url1).json()


  print(f.GREEN,"[$] [IP]:", data['query'])


  print(" [$] [ISP] :", data['isp'])
  if data['isp'] == False:
    print(f'[$] [ISP {no}!]')

  print(" [$] [6Organisation]:", data['org'])
  if data['org'] == False:
    print(f'[$] [Organisation {no}!]')

  print(" [$] [city]:", data['city'])
  if data['city'] == False:
    print(f'[$] [City {no}!]')

  print(f.CYAN,"[$] [country]:", data['country'])
  if data['country'] == False:
    print(f'[$] [Coumtry name {no}!]')

  print(" [$] [Region]:", data['region'])
  if data['region'] == False:
    print(f'[$] [Region {no}!]')

  print(" [$] [Name of continent]:", data['continent'])
  if data['country'] == False:
    print(f'[$] [Contimemt name {no}!]')

  print(f.RED,"[$] [Region / state]:", data['regionName'])
  if data['regionName'] == False:
    print(f'[$] [Region / state {no}!]')

  print(" [$] [Continet code]:", data['continentCode'])
  if data['country'] == False:
    print(f'[$] [Continent code {no}!]')

  print(" [$] [Latitude]:", data['lat'])
  if data['lat'] == False:
    print(f'[$] [Latitude {no} !]')

  print(" [$] [Longitude]:", data['lon'])
  if data['lon'] == False:
    print(f'[$] [Longitude {no} !]')

  print(" [$] [Time Zone]:", data['timezone'])
  if data['timezone'] == False:
    print(f'[$] [Time Zone {no}!]')

  print(" [$] [Zip code]:", data['zip'])
  if data['zip'] == False:
    print(f'[$] [Zip code {no}!]')

  print(f.BLUE,"[$] [AS number and organisation]:", data['as'])
  if data['as'] == False:
    print(f'[$] [AS number and organisation {no}!]')

  print(" [$] [Country Code]:", data['countryCode'])
  if data['countryCode'] == False:
    print(f'[$] [Country Code {no}!]')

  print(" [$] [Ip reverse DNS]: ", data['reverse'])
  if data['reverse'] == False:
    print(f'[$] [Ip revers DNS {no}]')

  print(" [$] [Connection (celular)]:", data['mobile'])
  if data['mobile'] == False:
    print(f'[$] [Mobile connection {no}!]')

  print(' [$] [National Currency]:', data['currency'])
  if data['currency'] == False:
    print(f'[$] [Currency {no}!]')

  print(' [$] [District]:', data['district'])
  if data['district'] == False:
    print(f'[$] [District{no}!]')

  print(' [$] [Proxy, VPN or Tor]:', data['proxy'])
  if data['proxy'] == False:
    print(f' [$] [Proxy, VPN or Tor {no}]')




def krish():
  print(f.CYAN,'\n [$] ENTER THE IP OF VICTIM')
  ipvic = input(f' [$] IP: ')
  print(f.BLUE,f'[$] FINDING DETAILS FOR: {ipvic}')
  time.sleep(1)
  url = f"http://ip-api.com/json/{ipvic}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  data = requests.get(url).json()
  print(f.RED,"\n [$] [IP From Victim]:", data['query'])

  try:
    print(" [$] [ISP] :", data['isp'])
    if data['isp'] == False:
      print(f'[$] [ISP {no}!]')

    print(" [$] [Organisatio]:", data['org'])
    if data['org'] == False:
     print(f'[$] [Organisation {no}!]')

    print(" [$] [City]:", data['city'])
    if data['city'] == False:
     print(f'[$] [City {no}!]')

    print(" [$] [COUNTRY ]:", data['country'])
    if data['country'] == False:
     print(f'[$] [Country {no}!]')

    print(" [$] [Region]:", data['region'])
    if data['region'] == False:
     print('[$] [Region {no}!]')

    print(f.BLUE,"[$] [CONTINENT]:", data['continent'])
    if data['country'] == False:
     print(f'[$] [Continent {no}!]')

    print(" [$] [Region/state]:", data['regionName'])
    if data['regionName'] == False:
      print(f'[$] [Region / state {no}!]')

    print(" [$] [Continent Code]:", data['continentCode'])
    if data['country'] == False:
     print(f'[$] [Continent code {no}!]')

    print(" [$] [Latitude]:", data['lat'])
    if data['lat'] == False:
     print(f'[$] [Latitud {no}!]')

    print(" [$] [Longitude]:", data['lon'])
    if data['lon'] == False:
      print(f'[$] [Longitude {no}!]')

    print(f.GREEN,"[$] [Time Zone]:", data['timezone'])
    if data['timezone'] == False:
      print(f'[$] [Time Zone {no}!]')

    print(" [$] [ZIP CODE]:", data['zip'])
    if data['zip'] == False:
      print(f'[$] [zip code {no}!]')

    print(" [$] [AS number and organisation]:", data['as'])
    if data['as'] == False:
      print(f'[$] [AS number and organusation {no}!]')

    print(" [$] [COUNTRY CODE]:", data['countryCode'])
    if data['countryCode'] == False:
     print(f'[$] [country code {no}!]')

    print(" [$] [reverse IP DNS]: ", data['reverse'])
    if data['reverse'] == False:
      print(f'[$] [Reverse IP DNS {no}!]')

    print(" [$] [Mobile Connection(celular)]:", data['mobile'])
    if data['mobile'] == False:
      print(f'[$] [Connection{no}!]')

    print(' [$] [Currency]:', data['currency'])
    if data['currency'] == False:
      print(f'[$] [currency {no}!]')

    print(f.GREEN,'[$] [District]:', data['district'])
    if data['district'] == False:
      print(f'[$] [District{no}!]')

    print(' [$] [Proxy, VPN or Tor]:', data['proxy'])
    if data['proxy'] == False:
      print(f' [$] [Proxy, VPN or Tor {no}!]')

  except KeyError:
    print(f.RED,f'\n[~] Error 408 data not found try again {ipvic}')


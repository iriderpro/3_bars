# Bar search utility

Utility for seach min, max and nearest bar in msk.

# Quickstart

for launch need python 3
For downloading input file need:
*  Sign in on data.mos.ru
*  Get API key
*  Download input file on refer:
  https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}
input file must be passed as an argument.

Example input file
```
{
  "features": [{
    "geometry": {
      "coordinates": [37.621587946152012, 55.765366956608361],
      "type": "Point"
    },
    "properties": {
      "DatasetId": 1796,
      "VersionNumber": 2,
      "ReleaseNumber": 2,
      "RowId": "20a0b7c9-dad3-4af8-a2a2-08170f74379b",
      "Attributes": {
        "global_id": 20660594,
        "Name": "Юнион Джек",
        "IsNetObject": "нет",
        "OperatingCompany": null,
        "AdmArea": "Центральный административный округ",
        "District": "Мещанский район",
        "Address": "Нижний Кисельный переулок, дом 3, строение 1",
        "PublicPhone": [{
          "PublicPhone": "(495) 621-19-63"
        }],
        "SeatsCount": 30,
        "SocialPrivileges": "нет"
      }
    },
    "type": "Feature"
  },
```

Example of script launch on windows, Python 3.6:
```
E:\WORK\wallie\4\bars.py bars.json

```

Example of script launch on Linux, Python 3.6:

```
$ ~/WORK/wallie/4$ python3 bars.py bars.json 
```
Enter your coordiantes (point separator)

Example output:
```
Самый маленький бар БАР. СОКИ
Самый большой бар Спорт бар «Красная машина»
Введите долготу : 37.665301111111
Введите широту  : 55.7350976999999999999
Ближайший бар Бильярдная

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

from ..models import *

# The `fc_dict` function is defined to load data from a Python Dictionary. This data will be converted to
# JSON and the chart will be rendered.

def save(request):
	# data for models
	data = {
		"country" : [{
		    "Name": "China",
		    "Code": "CHN",
		    "Population": 1277558000
		  },{
		    "Name": "India",
		    "Code": "IND",
		    "Population": 1013662000
		  },{
		    "Name": "United States",
		    "Code": "USA",
		    "Population": 278357000
		  },{
		    "Name": "Indonesia",
		    "Code": "IDN",
		    "Population": 212107000
		  },{
		    "Name": "Brazil",
		    "Code": "BRA",
		    "Population": 170115000
		  },{
		    "Name": "Pakistan",
		    "Code": "PAK",
		    "Population": 156483000
		  },{
		    "Name": "Russian Federation",
		    "Code": "RUS",
		    "Population": 146934000
		  },{
		    "Name": "Bangladesh",
		    "Code": "BGD",
		    "Population": 129155000
		  },{
		    "Name": "Japan",
		    "Code": "JPN",
		    "Population": 126714000
		  },{
		    "Name": "Nigeria",
		    "Code": "NGA",
		    "Population": 111506000
		}],
		"city" : {
			"CHN" : [{
					"Name": "Shanghai",
					"CountryCode": "CHN", 
					"Population": "9696300"
					}, {
					"Name": "Peking",
					"CountryCode": "CHN", 
					"Population": "7472000"
					}, {
					"Name": "Chongqing",
					"CountryCode": "CHN", 
					"Population": "6351600"
					}, {
					"Name": "Tianjin",
					"CountryCode": "CHN", 
					"Population": "5286800"
					}, {
					"Name": "Wuhan",
					"CountryCode": "CHN", 
					"Population": "4344600"
					}, {
					"Name": "Harbin",
					"CountryCode": "CHN", 
					"Population": "4289800"
					}, {
					"Name": "Shenyang",
					"CountryCode": "CHN", 
					"Population": "4265200"
					}, {
					"Name": "Kanton [Guangzhou]",
					"CountryCode": "CHN", 
					"Population": "4256300"
					}, {
					"Name": "Chengdu",
					"CountryCode": "CHN", 
					"Population": "3361500"
					}, {
					"Name": "Nanking [Nanjing]",
					"CountryCode": "CHN", 
					"Population": "2870300"
			}],
			"IND" : [{
					"Name": "Mumbai (Bombay)",
					"CountryCode": "IND", 
					"Population": "10500000"
					}, {
					"Name": "Delhi",
					"CountryCode": "IND", 
					"Population": "7206704"
					}, {
					"Name": "Calcutta [Kolkata]",
					"CountryCode": "IND", 
					"Population": "4399819"
					}, {
					"Name": "Chennai (Madras)",
					"CountryCode": "IND", 
					"Population": "3841396"
					}, {
					"Name": "Hyderabad",
					"CountryCode": "IND", 
					"Population": "2964638"
					}, {
					"Name": "Ahmedabad",
					"CountryCode": "IND", 
					"Population": "2876710"
					}, {
					"Name": "Bangalore",
					"CountryCode": "IND", 
					"Population": "2660088"
					}, {
					"Name": "Kanpur",
					"CountryCode": "IND", 
					"Population": "1874409"
					}, {
					"Name": "Nagpur",
					"CountryCode": "IND", 
					"Population": "1624752"
					}, {
					"Name": "Lucknow",
					"CountryCode": "IND", 
					"Population": "1619115"
			}],
			"USA" : [{
					"Name": "New York",
					"CountryCode": "USA", 
					"Population": "8008278"
					}, {
					"Name": "Los Angeles",
					"CountryCode": "USA", 
					"Population": "3694820"
					}, {
					"Name": "Chicago",
					"CountryCode": "USA", 
					"Population": "2896016"
					}, {
					"Name": "Houston",
					"CountryCode": "USA", 
					"Population": "1953631"
					}, {
					"Name": "Philadelphia",
					"CountryCode": "USA", 
					"Population": "1517550"
					}, {
					"Name": "Phoenix",
					"CountryCode": "USA", 
					"Population": "1321045"
					}, {
					"Name": "San Diego",
					"CountryCode": "USA", 
					"Population": "1223400"
					}, {
					"Name": "Dallas",
					"CountryCode": "USA", 
					"Population": "1188580"
					}, {
					"Name": "San Antonio",
					"CountryCode": "USA", 
					"Population": "1144646"
					}, {
					"Name": "Detroit",
					"CountryCode": "USA", 
					"Population": "951270"
			}],
			"IDN" : [{
					"Name": "Jakarta",
					"CountryCode": "IDN", 
					"Population": "9604900"
					}, {
					"Name": "Surabaya",
					"CountryCode": "IDN", 
					"Population": "2663820"
					}, {
					"Name": "Bandung",
					"CountryCode": "IDN", 
					"Population": "2429000"
					}, {
					"Name": "Medan",
					"CountryCode": "IDN", 
					"Population": "1843919"
					}, {
					"Name": "Palembang",
					"CountryCode": "IDN", 
					"Population": "1222764"
					}, {
					"Name": "Tangerang",
					"CountryCode": "IDN", 
					"Population": "1198300"
					}, {
					"Name": "Semarang",
					"CountryCode": "IDN", 
					"Population": "1104405"
					}, {
					"Name": "Ujung Pandang",
					"CountryCode": "IDN", 
					"Population": "1060257"
					}, {
					"Name": "Malang",
					"CountryCode": "IDN", 
					"Population": "716862"
					}, {
					"Name": "Bandar Lampung",
					"CountryCode": "IDN", 
					"Population": "680332"
			}],
			"BRA" : [{
					"Name": "Sao Paulo",
					"CountryCode": "BRA", 
					"Population": "9968485"
					}, {
					"Name": "Rio de Janeiro",
					"CountryCode": "BRA", 
					"Population": "5598953"
					}, {
					"Name": "Salvador",
					"CountryCode": "BRA", 
					"Population": "2302832"
					}, {
					"Name": "Belo Horizonte",
					"CountryCode": "BRA", 
					"Population": "2139125"
					}, {
					"Name": "Fortaleza",
					"CountryCode": "BRA", 
					"Population": "2097757"
					}, {
					"Name": "Brasilia",
					"CountryCode": "BRA", 
					"Population": "1969868"
					}, {
					"Name": "Curitiba",
					"CountryCode": "BRA", 
					"Population": "1584232"
					}, {
					"Name": "Recife",
					"CountryCode": "BRA", 
					"Population": "1378087"
					}, {
					"Name": "Porto Alegre",
					"CountryCode": "BRA", 
					"Population": "1314032"
					}, {
					"Name": "Manaus",
					"CountryCode": "BRA", 
					"Population": "1255049"
			}],
			"PAK" : [{
					"Name": "Karachi",
					"CountryCode": "PAK", 
					"Population": "9269265"
					}, {
					"Name": "Lahore",
					"CountryCode": "PAK", 
					"Population": "5063499"
					}, {
					"Name": "Faisalabad",
					"CountryCode": "PAK", 
					"Population": "1977246"
					}, {
					"Name": "Rawalpindi",
					"CountryCode": "PAK", 
					"Population": "1406214"
					}, {
					"Name": "Multan",
					"CountryCode": "PAK", 
					"Population": "1182441"
					}, {
					"Name": "Hyderabad",
					"CountryCode": "PAK", 
					"Population": "1151274"
					}, {
					"Name": "Gujranwala",
					"CountryCode": "PAK", 
					"Population": "1124749"
					}, {
					"Name": "Peshawar",
					"CountryCode": "PAK", 
					"Population": "988005"
					}, {
					"Name": "Quetta",
					"CountryCode": "PAK", 
					"Population": "560307"
					}, {
					"Name": "Islamabad",
					"CountryCode": "PAK", 
					"Population": "524500"
			}],
			"RUS" : [{
					"Name": "Moscow",
					"CountryCode": "RUS", 
					"Population": "8389200"
					}, {
					"Name": "St Petersburg",
					"CountryCode": "RUS", 
					"Population": "4694000"
					}, {
					"Name": "Novosibirsk",
					"CountryCode": "RUS", 
					"Population": "1398800"
					}, {
					"Name": "Nizni Novgorod",
					"CountryCode": "RUS", 
					"Population": "1357000"
					}, {
					"Name": "Jekaterinburg",
					"CountryCode": "RUS", 
					"Population": "1266300"
					}, {
					"Name": "Samara",
					"CountryCode": "RUS", 
					"Population": "1156100"
					}, {
					"Name": "Omsk",
					"CountryCode": "RUS", 
					"Population": "1148900"
					}, {
					"Name": "Kazan",
					"CountryCode": "RUS", 
					"Population": "1101000"
					}, {
					"Name": "Ufa",
					"CountryCode": "RUS", 
					"Population": "1091200"
					}, {
					"Name": "Tseljabinsk",
					"CountryCode": "RUS", 
					"Population": "1083200"
			}],
			"BGD" : [{
					"Name": "Dhaka",
					"CountryCode": "BGD", 
					"Population": "3612850"
					}, {
					"Name": "Chittagong",
					"CountryCode": "BGD", 
					"Population": "1392860"
					}, {
					"Name": "Khulna",
					"CountryCode": "BGD", 
					"Population": "663340"
					}, {
					"Name": "Rajshahi",
					"CountryCode": "BGD", 
					"Population": "294056"
					}, {
					"Name": "Narayanganj",
					"CountryCode": "BGD", 
					"Population": "202134"
					}, {
					"Name": "Rangpur",
					"CountryCode": "BGD", 
					"Population": "191398"
					}, {
					"Name": "Mymensingh",
					"CountryCode": "BGD", 
					"Population": "188713"
					}, {
					"Name": "Barisal",
					"CountryCode": "BGD", 
					"Population": "170232"
					}, {
					"Name": "Tungi",
					"CountryCode": "BGD", 
					"Population": "168702"
					}, {
					"Name": "Jessore",
					"CountryCode": "BGD", 
					"Population": "139710"
			}],
			"JPN" : [{
					"Name": "Tokyo",
					"CountryCode": "JPN", 
					"Population": "7980230"
					}, {
					"Name": "Jokohama [Yokohama]",
					"CountryCode": "JPN", 
					"Population": "3339594"
					}, {
					"Name": "Osaka",
					"CountryCode": "JPN", 
					"Population": "2595674"
					}, {
					"Name": "Nagoya",
					"CountryCode": "JPN", 
					"Population": "2154376"
					}, {
					"Name": "Sapporo",
					"CountryCode": "JPN", 
					"Population": "1790886"
					}, {
					"Name": "Kioto",
					"CountryCode": "JPN", 
					"Population": "1461974"
					}, {
					"Name": "Kobe",
					"CountryCode": "JPN", 
					"Population": "1425139"
					}, {
					"Name": "Fukuoka",
					"CountryCode": "JPN", 
					"Population": "1308379"
					}, {
					"Name": "Kawasaki",
					"CountryCode": "JPN", 
					"Population": "1217359"
					}, {
					"Name": "Hiroshima",
					"CountryCode": "JPN", 
					"Population": "1119117"
			}],
			"NGA" : [{
					"Name": "Lagos",
					"CountryCode": "NGA", 
					"Population": "1518000"
					}, {
					"Name": "Ibadan",
					"CountryCode": "NGA", 
					"Population": "1432000"
					}, {
					"Name": "Ogbomosho",
					"CountryCode": "NGA", 
					"Population": "730000"
					}, {
					"Name": "Kano",
					"CountryCode": "NGA", 
					"Population": "674100"
					}, {
					"Name": "Oshogbo",
					"CountryCode": "NGA", 
					"Population": "476800"
					}, {
					"Name": "Ilorin",
					"CountryCode": "NGA", 
					"Population": "475800"
					}, {
					"Name": "Abeokuta",
					"CountryCode": "NGA", 
					"Population": "427400"
					}, {
					"Name": "Port Harcourt",
					"CountryCode": "NGA", 
					"Population": "410000"
					}, {
					"Name": "Zaria",
					"CountryCode": "NGA", 
					"Population": "379200"
					}, {
					"Name": "Ilesha",
					"CountryCode": "NGA", 
					"Population": "378400"
			}]
		},
		"revenue" :[{
            "month": "Jan",
            "revenue": "420000"
       		}, {
            "month": "Feb",
            "revenue": "810000"
       		}, {
            "month": "Mar",
            "revenue": "720000"
       		}, {
            "month": "Apr",
            "revenue": "550000"
       		}, {
            "month": "May",
            "revenue": "910000"
       		}, {
            "month": "Jun",
            "revenue": "510000"
       		}, {
            "month": "Jul",
            "revenue": "680000"
       		}, {
            "month": "Aug",
            "revenue": "620000"
       		}, {
            "month": "Sep",
            "revenue": "610000"
       		}, {
            "month": "Oct",
            "revenue": "490000"
       		}, {
            "month": "Nov",
            "revenue": "900000"
       		}, {
            "month": "Dec",
            "revenue": "730000"
        }]
	}
	
	## Country model data insert
	# for key in data["country"]:
	# 	b = Country(Name=key["Name"], Code=key["Code"], Population=key["Population"])
	# 	b.save()

	## City model data insert
	# for key in data["city"]:
	# 	for key1 in data["city"][key]:
	# 		b = City(Name=key1["Name"], CountryCode=key1["CountryCode"], Population=key1["Population"])
	# 		b.save()

	## Revenue model data insert
	# for key in data["revenue"]:
	# 	b = Revenue(Month=key["month"], MonthlyRevenue=key["revenue"])
	#  	b.save()		
	return HttpResponse("data inserted")
	

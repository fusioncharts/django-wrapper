from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

from ..models import *

# The `chart` function is defined to load data from a `Country` Model. 
# This data will be converted to JSON and the chart will be rendered.

def chart(request):
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = { 
		"caption" : "Top 10 Most Populous Countries",
	    "paletteColors" : "#0075c2",
	    "bgColor" : "#ffffff",
	    "borderAlpha": "20",
	    "canvasBorderAlpha": "0",
	    "usePlotGradientColor": "0",
	    "plotBorderAlpha": "10",
	    "showXAxisLine": "1",
	    "xAxisLineColor" : "#999999",
	    "showValues" : "0",
	    "divlineColor" : "#999999",
	    "divLineIsDashed" : "1",
	    "showAlternateHGridColor" : "0"
		}
   
    # Convert the data in the `Country` model into a format that can be consumed by FusionCharts. 
    # The data for the chart should be in an array where in each element of the array is a JSON object
    # having the `label` and `value` as keys.

	dataSource['data'] = []
	dataSource['linkeddata'] = []
    # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
	for key in Country.objects.all():
	  data = {}
	  data['label'] = key.Name
	  data['value'] = key.Population
	  # Create link for each country when a data plot is clicked.
	  data['link'] = 'newchart-json-'+ key.Code
	  dataSource['data'].append(data)

	  # Create the linkData for cities drilldown	
	  linkData = {}
	  # Inititate the linkData for cities drilldown
	  linkData['id'] = key.Code
	  linkedchart = {}
	  linkedchart['chart'] = {
		"caption" : "Top 10 Most Populous Cities - " + key.Name ,
	    "paletteColors" : "#0075c2",
	    "bgColor" : "#ffffff",
	    "borderAlpha": "20",
	    "canvasBorderAlpha": "0",
	    "usePlotGradientColor": "0",
	    "plotBorderAlpha": "10",
	    "showXAxisLine": "1",
	    "xAxisLineColor" : "#999999",
	    "showValues": "0",
	    "divlineColor" : "#999999",
	    "divLineIsDashed" : "1",
	    "showAlternateHGridColor" : "0"
		}

	  # Convert the data in the `City` model into a format that can be consumed by FusionCharts. 	
	  linkedchart['data'] = []
	  # Filtering the data base on the Country Code
	  for key in City.objects.all().filter(CountryCode=key.Code):
	  	arrDara = {}
		arrDara['label'] = key.Name
		arrDara['value'] = key.Population
		linkedchart['data'].append(arrDara)

	  linkData['linkedchart'] = linkedchart
	  dataSource['linkeddata'].append(linkData)

    # Create an object for the Column 2D chart using the FusionCharts class constructor        	  		
	column2D = FusionCharts("column2D", "ex1" , "600", "400", "chart-1", "json", dataSource)
	return render(request, 'index.html', {'output': column2D.render()}) 


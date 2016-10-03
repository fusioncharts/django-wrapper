from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a Single-series-column2d chart with the chart data passed as JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
    # Create an object for the Area 2D chart using the FusionCharts class constructor
	columnChart = FusionCharts("column2d", "ex1" , "550", "350", "chart-1", "json", 
		# The chart data is passed as a string to the `dataSource` parameter.
        """{
      "chart": {
        "caption": "Harry\'s SuperMart - Top 5 Stores' Revenue",
        "subCaption": "Last Quarter",
        "numberPrefix": "$",
        "rotatevalues": "0",
        "plotToolText": "<div><b>$label</b><br/>Sales : <b>$$value</b></div>",
        "theme": "fint"
      },
      "data": [
      {"label": "Bakersfield Central", "value": "880000"},
      {"label": "Garden Groove harbour", "value": "730000"},
      {"label": "Los Angeles Topanga", "value": "590000"},
      {"label": "Compton-Rancho Dom", "value": "520000"},
      {"label": "Daly City Serramonte", "value": "330000"}]
      }""")
	
	# Alternatively, you can assign this string to a string variable in a separate JSON file and
	# pass the URL of that file to the `dataSource` parameter.
	
 	return  render(request, 'index.html', {'output' : columnChart.render()})



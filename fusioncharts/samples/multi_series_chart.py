from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a Multi-series-bar2d chart with the chart data passed as JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
  # Create an object for the Area 2D chart using the FusionCharts class constructor
	msbarChart = FusionCharts("msbar2d", "ex1" , "550", "350", "chart-1", "json", 
		# The chart data is passed as a string to the `dataSource` parameter.
      """{
      "chart": {
        "caption": "Split of Sales by Product Category",
        "subCaption": "5 top performing stores  - last month",
        "captionPadding": "15",
        "numberPrefix": "$",
        "showvalues": "1",
        "valueFontColor": "#ffffff",
        "placevaluesInside": "1",
        "usePlotGradientColor": "0",
        "legendShadow": "0",
        "showXAxisLine": "1",
        "xAxisLineColor": "#999999",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "showAlternateVGridColor": "0",
        "alignCaptionWithCanvas": "0",
        "legendPadding": "15",
        "plotToolText": "<div><b>$label</b><br/>Product : <b>$seriesname</b><br/>Sales : <b>$$value</b></div>",
        "theme": "fint"
      },
      "categories": [{
        "category": [{
          "label": "Garden Groove harbour"
        }, {
          "label": "Bakersfield Central"
        }, {
          "label": "Los Angeles Topanga"
        }, {
          "label": "Compton-Rancho Dom"
        }, {
          "label": "Daly City Serramonte"
        }]
      }],
      "dataset": [{
        "seriesname": "Non-Food Products",
        "data": [{
          "value": "28800"
        }, {
          "value": "25400"
        }, {
          "value": "21800"
        }, {
          "value": "19500"
        }, {
          "value": "11500"
        }]
      }, {
        "seriesname": "Food Products",
        "data": [{
          "value": "17000"
        }, {
          "value": "19500"
        }, {
          "value": "12500"
        }, {
          "value": "14500"
        }, {
          "value": "17500"
        }]
      }]
    }""")
	
	# Alternatively, you can assign this string to a string variable in a separate JSON file and
	# pass the URL of that file to the `dataSource` parameter.
	
 	return  render(request, 'index.html', {'output' : msbarChart.render()})
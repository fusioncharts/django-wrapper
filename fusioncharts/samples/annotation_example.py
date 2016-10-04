from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a Column 2D chart with the annotation and data are passed as JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
	column2d = FusionCharts("column2d", "ex1" , "500", "300", "chart-1", "json", 
		"""{
        "chart": {
          "caption": "Top 4 Chocolate Brands Sold",
          "subCaption": "Last Year",
          "yAxisName": "Sales (in USD)",
          "yAxisMaxValue": "120000",
          "showXAxisLine": "0",
          "numberPrefix": "$",
          "theme": "fint",
          "PlotfillAlpha": "0",
          "placeValuesInside": "0",
          "rotateValues": "0",
          "valueFontColor": "#333333",
          "showLabels": "0",
          "chartBottomMargin": "20",
          "plotToolText": "<div>Brand : <b>$label</b><br/>Total Revenue : <b>$$value</b></div>",
        },
        "annotations": {
          "autoScale": "1",
          "scaleImages": "1",
          "origW": "400",
          "origH": "300",
          "groups": [{
            "id": "user-images",
            "items": [{
              "id": "butterFinger-icon",
              "type": "image",
              "url": "http://static.fusioncharts.com/sampledata/images/butterFinger.png",
              "x": "$dataset.0.set.0.CenterX - 28",
              "y": "$dataset.0.set.0.STARTY",
              "xScale": "50",
              "toy": "$dataset.0.set.0.ENDY + 2",
            }, {
              "id": "snickrs-user-icon",
              "type": "image",
              "url": "http://static.fusioncharts.com/sampledata/images/snickrs.png",
              "x": "$dataset.0.set.1.CenterX - 25",
              "y": "$dataset.0.set.1.STARTY",
              "xScale": "50",
              "toy": "$dataset.0.set.1.ENDY + 2",
            }, {
              "id": "coffee_crisp-user-icon",
              "type": "image",
              "url": "http://static.fusioncharts.com/sampledata/images/coffee_crisp.png",
              "x": "$dataset.0.set.2.CenterX - 25",
              "y": "$dataset.0.set.2.STARTY",
              "xScale": "50",
              "toy": "$dataset.0.set.2.ENDY + 2",
            }, {
              "id": "100grand-user-icon",
              "type": "image",
              "url": "http://static.fusioncharts.com/sampledata/images/100grand.png",
              "x": "$dataset.0.set.3.CenterX - 25",
              "y": "$dataset.0.set.3.STARTY",
              "xScale": "50",
              "toy": "$dataset.0.set.3.ENDY + 2",
            }]
          }]
        },
        "data": [{
          "label": "Butterfinger",
          "value": "92000"
        }, {
          "label": "Snickers",
          "value": "87000"
        }, {
          "label": "Coffee Crisp",
          "value": "83000"
        }, {
          "label": "100 Grand",
          "value": "80000"
        }]
      }""")

  # Alternatively, you can assign this string to a string variable in a separate JSON file and
  # pass the URL of that file to the `dataSource` parameter.
 	return  render(request, 'index.html', {'output' : column2d.render()})

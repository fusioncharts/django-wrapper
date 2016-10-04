from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a Area 2D chart with the chart data passed in JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
    # Create an object for the Area 2D chart using the FusionCharts class constructor
	area2D = FusionCharts("area2D", "ex1" , "600", "400", "chart-1", "json", 
		# The chart data is passed as a string to the `dataSource` parameter.
        """{
            "chart": {
                "caption": "Sales of Liquor",
                "subCaption": "Last week",
                "xAxisName": "Day",
                "yAxisName": "Sales (In USD)",
                "numberPrefix": "$",
                "paletteColors": "#0075c2",
                "bgColor": "#ffffff",
                "showBorder": "0",
                "showCanvasBorder": "0",
                "plotBorderAlpha": "10",
                "usePlotGradientColor": "0",
                "plotFillAlpha": "50",
                "showXAxisLine": "1",
                "axisLineAlpha": "25",
                "divLineAlpha": "10",
                "showValues": "1",
                "showAlternateHGridColor": "0",
                "captionFontSize": " 14",
                "subcaptionFontSize": "14",
                "subcaptionFontBold": "0",
                "toolTipColor": "#ffffff",
                "toolTipBorderThickness": "0",
                "toolTipBgColor": "#000000",
                " toolTipBgAlpha": "80",
                "toolTipBorderRadius": "2",
                "toolTipPadding": "5"
            },
            "data": [{
                "label": " Mon",
                " value": "4123"
            }, {
                "label": "Tue",
                "value": "  4633"
            }, {
                "label": "Wed",
                "value": "5507"
            }, {
                "label": "Thu",
                "value": "4910"
            }, {
                "label": "Fri",
                "value": "5529"
            }, {
                "label": "Sat",
                "value": "5803"
            }, {
                "label": "Sun",
                "value": "6202"
            }]
        }""")
	
	# Alternatively, you can assign this string to a string variable in a separate JSON file and
	# pass the URL of that file to the `dataSource` parameter.
	
 	return  render(request, 'index.html', {'output' : area2D.render()})
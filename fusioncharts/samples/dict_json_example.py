from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# The `chart` function is defined to load data from a Python Dictionary. This data will be converted to
# JSON and the chart will be rendered.

def chart(request):
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = { 
		"caption" : "Split of Visitors by Age Group",
        "subCaption" : "Last year",
        "paletteColors" : "#0075c2,#1aaf5d,#f2c500,#f45b00,#8e0000",
        "bgColor" : "#ffffff",
        "showBorder" : "0",
        "use3DLighting" : "0",
        "showShadow" : "0",
        "enableSmartLabels" : "0",
        "startingAngle" : "0",
        "showPercentValues" : "1",
        "showPercentInTooltip" : "0",
        "decimals" : "1",
        "captionFontSize" : "14",
        "subcaptionFontSize" : "14",
        "subcaptionFontBold" : "0",
        "toolTipColor" : "#ffffff",
        "toolTipBorderThickness" : "0",
        "toolTipBgColor" : "#000000",
        "toolTipBgAlpha" : "80",
        "toolTipBorderRadius" : "2",
        "toolTipPadding" : "5",
        "showHoverEffect" : "1",
        "showLegend" : "1",
        "legendBgColor" : "#ffffff",
        "legendBorderAlpha" : "0",
        "legendShadow" : "0",
        "legendItemFontSize" : "10",
        "legendItemFontColor" : "#666666",
        "useDataPlotColorForLabels" : "1"
		}

	# The `actualData` dict contains four key-value pairs that are the values for Last year	
	actualData = {
        "Teenage" : 1250400,
        "Adult" : 1463300,
        "Mid-age" : 1050700,
        "Senior" : 491000
        }

    # Convert the data in the `actualData` array into a format that can be consumed by FusionCharts. 
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

	dataSource['data'] = []
    # Iterate through the data in `actualData` and insert in to the `dataSource['data']` list.
	for key in actualData:
	  data = {}
	  data['label'] = key
	  data['value'] = actualData[key]
	  dataSource['data'].append(data)

    # Create an object for the Pie 2D chart using the FusionCharts class constructor        	  		
	pie2D = FusionCharts("pie2D", "ex1" , "600", "400", "chart-1", "json", dataSource)
	return render(request, 'index.html', {'output': pie2D.render()}) 
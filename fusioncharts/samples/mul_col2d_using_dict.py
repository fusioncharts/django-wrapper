from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# The `chart` function is defined to load data from a Python Dictionary. This data will be converted to
# JSON and the chart will be rendered in the browser.

def chart(request):
	
	dataSource = {}
    
    # Chart data is passed to the `dataSource` parameter, as hashes, in the form of
    # key-value pairs.
	dataSource['chart'] = { 
		"caption": "Comparison of Quarterly Revenue",
        "subCaption": "Harry's SuperMart",
        "xAxisname": "Quarter",
        "yAxisName": "Amount ($)",
        "numberPrefix": "$",
        "theme": "zune"
		}

	# The `category` dict is defined inside the `categories` array with four key-value pairs
    # that represent the x-axis labels for the four quarters.
	dataSource["categories"] = [{
                "category": [
                    { "label": "Q1" },
                    { "label": "Q2" },
                    { "label": "Q3" },
                    { "label": "Q4" }
                ]
            }]
    
    # The `data` hash contains four key-value pairs that are the values for the revenue
    # generated in the previous year.

        dataSource["dataset"] = [{
                "seriesname": "Previous Year",
                "data": [
                        { "value": "10000" },
                        { "value": "11500" },
                        { "value": "12500" },
                        { "value": "15000" }
                    ]
                }, {
                "seriesname": "Current Year",
                "data": [
                        { "value": "25400" },
                        { "value": "29800" },
                        { "value": "21800" },
                        { "value": "26800" }
                    ]
                }    
            ]

    # Create an object for the Multiseries column 2D charts using the FusionCharts class constructor
	mscol2D = FusionCharts("mscolumn2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
	return render(request, 'index.html', {'output': mscol2D.render()}) 



from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..lib.fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a Angular Gauge with the chart data passed as JSON string format.
# The `fc_gauge` method is defined to load chart data from a JSON string.

def fc_gauge(request):
    # Create an object for the Area 2D chart using the FusionCharts class constructor
	angularGauge = FusionCharts("angulargauge", "ex1" , "450", "270", "chart-1", "json", 
		# The chart data is passed as a string to the `dataSource` parameter.
        """{
      "chart": {
        "caption": "Customer Satisfaction Score",
        "subcaption": "Los Angeles Topanga",
        "lowerlimit": "0",
        "upperlimit": "100",
        "lowerlimitdisplay": "Bad",
        "upperlimitdisplay": "Good",
        "numbersuffix": "%",
        "tickvaluedistance": "10",
        "gaugeinnerradius": "0",
        "bgcolor": "FFFFFF",
        "pivotfillcolor": "333333",
        "pivotradius": "8",
        "pivotfillmix": "333333, 333333",
        "pivotfilltype": "radial",
        "pivotfillratio": "0,100",
        "showtickvalues": "1",
        "majorTMThickness": "2",
        "majorTMHeight": "15",
        "minorTMHeight": "3",
        "showborder": "0",
        "plottooltext": "<div>Average Score : <b>$value%</b></div>",
      },
      "colorrange": {
        "color": [{
          "minvalue": "0",
          "maxvalue": "50",
          "code": "e44a00"
        }, {
          "minvalue": "50",
          "maxvalue": "75",
          "code": "f8bd19"
        }, {
          "minvalue": "75",
          "maxvalue": "100",
          "code": "6baa01"
        }]
      },
      "dials": {
        "dial": [{
          "value": "84",
          "rearextension": "15",
          "radius": "100",
          "bgcolor": "333333",
          "bordercolor": "333333",
          "basewidth": "8"
        }]
      }
    }""")
	
	# Alternatively, you can assign this string to a string variable in a separate JSON file and
	# pass the URL of that file to the `dataSource` parameter.
	
 	return  render(request, 'fusioncharts-html-template.html', {'output' : angularGauge.render()})
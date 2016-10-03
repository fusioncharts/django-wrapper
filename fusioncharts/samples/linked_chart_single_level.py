from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a Column 2D chart with the chart data passed in JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
    # Create an object for the Column 2D chart using the FusionCharts class constructor
	column2DChart = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", 
		# The chart data is passed as a string to the `dataSource` parameter.
    """{
      "chart": {
        "caption": "Projected Global IP Traffic, 2016-2019",
        "subcaption": "Click on a column to drill-down into type of traffic",
        "yaxisname": "Total IP traffic (PetaByte per Month)",
        "formatnumberscale": "1",
        "plotgradientcolor": " ",
        "bgcolor": "FFFFFF",
        "showalternatehgridcolor": "0",
        "showplotborder": "0",
        "showvalues": "1",
        "divlinecolor": "CCCCCC",
        "divlinedashed": "1",
        "showcanvasborder": "0",
        "defaultnumberscale": "PB",
        "yAxisMaxValue": "185000",
        "numberscaleunit": "PB,EB",
        "palettecolors": "34495e ",
        "captionPadding": "20",
        "showborder": "0",
        "plotToolText": "<div><b>$label</b><br/>IP Traffic : <b>$datavalue</b></div>",
      },
      "data": [
      {"label": "2016", "value": "88426", "link": "newchart-json-2016-type"}, {"label": "2017",
        "value": "108988",
        "link": "newchart-json-2017-type"
      }, {
        "label": "2018",
        "value": "135483",
        "link": "newchart-json-2018-type"
      }, {
        "label": "2019",
        "value": "167978",
        "link": "newchart-json-2019-type"
      }],
      "linkeddata": [{
        "id": "2016-type",
        "linkedchart": {
          "chart": {
            "caption": "Global IP Traffic, 2016",
            "subcaption": "By Type (PB per Month)",
            "formatnumberscale": "1",
            "plotgradientcolor": " ",
            "bgcolor": "FFFFFF",
            "yaxismaxvalue": "55000",
            "showalternatehgridcolor": "0",
            "showplotborder": "0",
            "showvalues": "1",
            "labeldisplay": "WRAP",
            "divlinecolor": "CCCCCC",
            "divlinedashed": "1",
            "showcanvasborder": "0",
            "captionPadding": "20",
            "defaultnumberscale": "PB",
            "numberscalevalue": "1024,1024",
            "numberscaleunit": "PB,EB",
            "palettecolors": "34495e"
          },
          "data": [{
            "label": "Fixed Internet",
            "value": "58304"
          }, {
            "label": "Managed IP",
            "value": "23371"
          }, {
            "label": "Mobile data",
            "value": "6751"
          }]
        }
      }, {
        "id": "2017-type",
        "linkedchart": {
          "chart": {
            "caption": "Global IP Traffic, 2017",
            "subcaption": "By Type (PB per Month)",
            "formatnumberscale": "1",
            "plotgradientcolor": " ",
            "yaxismaxvalue": "65000",
            "bgcolor": "FFFFFF",
            "showalternatehgridcolor": "0",
            "showplotborder": "0",
            "showvalues": "1",
            "labeldisplay": "WRAP",
            "divlinecolor": "CCCCCC",
            "divlinedashed": "1",
            "showcanvasborder": "0",
            "captionPadding": "20",
            "defaultnumberscale": "PB",
            "numberscalevalue": "1024,1024",
            "numberscaleunit": "PB,EB",
            "palettecolors": "34495e"
          },
          "data": [{
            "label": "Fixed Internet",
            "value": "72251"
          }, {
            "label": "Managed IP",
            "value": "26087"
          }, {
            "label": "Mobile data",
            "value": "10650"
          }]
        }
      }, {
        "id": "2018-type",
        "linkedchart": {
          "chart": {
            "caption": "Global IP Traffic, 2018",
            "subcaption": "By Type (PB per Month)",
            "formatnumberscale": "1",
            "plotgradientcolor": " ",
            "bgcolor": "FFFFFF",
            "showalternatehgridcolor": "0",
            "showplotborder": "0",
            "yaxismaxvalue": "75000",
            "showvalues": "1",
            "labeldisplay": "WRAP",
            "divlinecolor": "CCCCCC",
            "divlinedashed": "1",
            "showcanvasborder": "0",
            "captionPadding": "20",
            "defaultnumberscale": "PB",
            "numberscalevalue": "1024,1024",
            "numberscaleunit": "PB,EB",
            "palettecolors": "34495e"
          },
          "data": [{
            "label": "Fixed Internet",
            "value": "90085"
          }, {
            "label": "Managed IP",
            "value": "29274"
          }, {
            "label": "Mobile data",
            "value": "16124"
          }]
        }
      }, {
        "id": "2019-type",
        "linkedchart": {
          "chart": {
            "caption": "Global IP Traffic, 2019",
            "subcaption": "By Type (PB per Month)",
            "formatnumberscale": "1",
            "plotgradientcolor": " ",
            "bgcolor": "FFFFFF",
            "showalternatehgridcolor": "0",
            "showplotborder": "0",
            "yaxismaxvalue": "75000",
            "showvalues": "1",
            "labeldisplay": "WRAP",
            "divlinecolor": "CCCCCC",
            "divlinedashed": "1",
            "showcanvasborder": "0",
            "captionPadding": "20",
            "defaultnumberscale": "PB",
            "numberscalevalue": "1024,1024",
            "numberscaleunit": "PB,EB",
            "palettecolors": "34495e"
          },
          "data": [{
            "label": "Fixed Internet",
            "value": "111899"
          }, {
            "label": "Managed IP",
            "value": "31858"
          }, {
            "label": "Mobile data",
            "value": "24221"
          }]
        }
      }]
    }""")
	
	# Alternatively, you can assign this string to a string variable in a separate JSON file and
	# pass the URL of that file to the `dataSource` parameter.
	
 	return  render(request, 'index.html', {'output' : column2DChart.render()})
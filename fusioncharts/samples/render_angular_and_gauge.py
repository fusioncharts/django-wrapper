from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a Pie 3D chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the Line chart using the FusionCharts class constructor
  angularChart = FusionCharts("angulargauge", "ex1", "100%", "200", "chart-1", "json",
        # The chart data is passed as a string to the `dataSource` parameter.
    """{
        "chart": {
            "caption": "Customer Satisfaction Score",
            "lowerlimit": "0",
            "upperlimit": "100",
            "lowerlimitdisplay": "Bad",
            "upperlimitdisplay": "Good",
            "palette": "1",
            "numbersuffix": "%",
            "tickvaluedistance": "10",
            "showvalue": "0",
            "gaugeinnerradius": "0",
            "bgcolor": "FFFFFF",
            "pivotfillcolor": "333333",
            "pivotradius": "8",
            "pivotfillmix": "333333, 333333",
            "pivotfilltype": "radial",
            "pivotfillratio": "0,100",
            "showtickvalues": "1",
            "showborder": "0"
        },
        "colorrange": {
            "color": [
                {
                    "minvalue": "0",
                    "maxvalue": "45",
                    "code": "e44a00"
                },
                {
                    "minvalue": "45",
                    "maxvalue": "75",
                    "code": "f8bd19"
                },
                {
                    "minvalue": "75",
                    "maxvalue": "100",
                    "code": "6baa01"
                }
            ]
        },
        "dials": {
            "dial": [
                {
                    "value": "92",
                    "rearextension": "15",
                    "radius": "100",
                    "bgcolor": "333333",
                    "bordercolor": "333333",
                    "basewidth": "8"
                }
            ]
        }
    }""")
  
    # Create an object for the cylinder chart using the FusionCharts class constructor
  cylinderChart = FusionCharts("cylinder", "ex2", "100%", "200", "chart-2", "json", 
        # The chart data is passed as a string to the `dataSource` parameter.
    """{
        "chart": {
            "manageresize": "1",
            "bgcolor": "FFFFFF",
            "bgalpha": "0",
            "showborder": "0",
            "lowerlimit": "0",
            "upperlimit": "100",
            "showtickmarks": "0",
            "showtickvalues": "0",
            "showlimits": "0",
            "numbersuffix": "%",
            "decmials": "0",
            "cylfillcolor": "CC0000",
            "basefontcolor": "CC0000",
            "chartleftmargin": "15",
            "chartrightmargin": "15",
            "charttopmargin": "15"
        },
        "value": "44",
        "annotations": {
            "groups": [
                {
                    "showbelow": "1",
                    "items": [
                        {
                            "type": "rectangle",
                            "x": "$chartStartX+1",
                            "y": "$chartStartY+1",
                            "tox": "$chartEndX-1",
                            "toy": "$chartEndY-1",
                            "color": "FFFFFF",
                            "alpha": "100",
                            "showborder": "0",
                            "bordercolor": "CC0000",
                            "borderthickness": "2",
                            "radius": "10"
                        }
                    ]
                }
            ]
        }
    }""")
  
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'index.html', {'output' : angularChart.render(),
            'output_2' : cylinderChart.render()})

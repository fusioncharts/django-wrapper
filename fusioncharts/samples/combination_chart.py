from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a mscombi 2d chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the mscombi2d chart using the FusionCharts class constructor
  mscombi2d = FusionCharts("mscombi2d", "ex1" , "600", "400", "chart-1", "json", 
        # The data is passed as a string in the `dataSource` as parameter.
    """{  
          "chart": {
          "caption": "App Publishing Trend",
          "subCaption": "2012-2016",
          "xAxisName": "Years",
          "formatnumberscale": "0",
          "numberSuffix": "K",
          "showvalues":"0",
          "theme": "fint"
          },
          "categories": [{
            "category": [{
              "label": "2012"
            }, {
              "label": "2013"
            }, {
              "label": "2014"
            }, {
              "label": "2015"
            }, {
              "label": "2016"
            }]
          }],
          "dataset": [{
            "seriesname": "iOS App Store",
            "renderAs": "Spline",
            "data": [{
              "value": "125"
            }, {
              "value": "300"
            }, {
              "value": "480"
            }, {
              "value": "800"
            }, {
              "value": "1100"
            }]
          }, {
            "seriesname": "Google Play Store",
            "renderAs": "SplineArea",
            "data": [{
              "value": "70"
            }, {
              "value": "150"
            }, {
              "value": "350"
            }, {
              "value": "600"
            },{
              "value": "1400"
            }]
          }, {
            "seriesname": "Amazon AppStore",
            "data": [{
              "value": "10"
            }, {
              "value": "100"
            }, {
              "value": "300"
            }, {
              "value": "600"
            },{
              "value": "900"
            }]
          }]
      }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'index.html', {'output' : mscombi2d.render()})

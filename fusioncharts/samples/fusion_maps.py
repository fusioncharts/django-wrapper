from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a USA MAP with the chart data passed in JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
    datasource = {}
    datasource["chart"] = {
        "caption": "State-wise sales in USA",
        "subcaption": "Previous financial year",
        "legendCaption": "Sales ($)",
        "legendCaptionFontSize": "10",
        "legendCaptionPadding": "50",
        "legendScaleLineAlpha": "50",
        "entityFillHoverColor": "#cccccc",
        "numberScaleValue": "1,1000,1000",
        "numberScaleUnit": "K,M,B",
        "numberPrefix": "$",
        "showLabels": "1",
        "plottooltext": "<div>Country : <b>$id</b><br/>Total Sales : <b>$$value</b></div>",
        "theme": "fint"
    }
    datasource["colorrange"] = {
        "minvalue": "0",
        "startlabel": "Poor",
        "endlabel": "Good",
        "code": "#e44a00",
        "gradient": "1",
        "color": [{
          "maxvalue": "50000",
          "displayvalue": "Average",
          "code": "#f8bd19"
        }, {
          "maxvalue": "100000",
          "code": "#6baa01"
        }]
    }
    datasource["data"] = [
        {"id": "HI", "value": "3189"}, 
        {"id": "DC", "value": "2879"},
        {"id": "MD", "value": "920"},
        {"id": "DE", "value": "4607"},
        {"id": "RI", "value": "4890"},
        {"id": "WA", "value": "34927"},
        {"id": "OR", "value": "65798"},
        {"id": "CA", "value": "61861"},
        {"id": "AK", "value": "58911"},
        {"id": "ID", "value": "42662"},
        {"id": "NV", "value": "78041"},
        {"id": "AZ", "value": "41558"},
        {"id": "MT", "value": "62942"},
        {"id": "WY", "value": "78834"},
        {"id": "UT", "value": "50512"},
        {"id": "CO", "value": "73026"},
        {"id": "NM", "value": "78865"},
        {"id": "ND", "value": "50554"},
        {"id": "SD", "value": "35922"},
        {"id": "NE", "value": "43736"},
        {"id": "KS", "value": "32681"},
        {"id": "OK", "value": "79038"},
        {"id": "TX", "value": "75425"},
        {"id": "MN", "value": "43485"},
        {"id": "IA", "value": "46515"},
        {"id": "MO", "value": "63715"},
        {"id": "AR", "value": "34497"},
        {"id": "LA", "value": "70706"},
        {"id": "WI", "value": "42382"},
        {"id": "IL", "value": "73202"},
        {"id": "KY", "value": "79118"},
        {"id": "TN", "value": "44657"},
        {"id": "MS", "value": "66205"},
        {"id": "AL", "value": "75873"},
        {"id": "GA", "value": "76895"},
        {"id": "MI", "value": "67695"},
        {"id": "IN", "value": "33592"},
        {"id": "OH", "value": "32960"},
        {"id": "PA", "value": "54346"},
        {"id": "NY", "value": "42828"},
        {"id": "VT", "value": "77411"},
        {"id": "NH", "value": "51403"},
        {"id": "ME", "value": "64636"},
        {"id": "MA", "value": "51767"},
        {"id": "CT", "value": "57353"},
        {"id": "NJ", "value": "80788"},
        {"id": "WV", "value": "95890"},
        {"id": "VA", "value": "83140"},
        {"id": "NC", "value": "97344"},
        {"id": "SC", "value": "88234"},
        {"id": "FL", "value": "88234"}
    ]

    # Create an object for the usa map using the FusionCharts class constructor
    fusionMap = FusionCharts("usa", "ex1" , "650", "450", "chart-1", "json", datasource)

    # Alternatively, you can assign this string to a string variable in a separate JSON file and
    # pass the URL of that file to the `dataSource` parameter.
    return  render(request, 'index.html', {'output' : fusionMap.render()})

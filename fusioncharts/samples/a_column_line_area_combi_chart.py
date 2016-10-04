from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a MsCombi 2D chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

    datasource = {}
    datasource["chart"] = {
        "caption": "Actual Revenues, Targeted Revenues & Profits",
        "subcaption": "Last year",
        "xaxisname": "Month",
        "yaxisname": "Amount (In USD)",
        "numberprefix": "$",
        "theme": "ocean"
    }
    datasource["categories"] = [{
        "category": [
            {"label": "Jan"},
            {"label": "Feb"},
            {"label": "Mar"},
            {"label": "Apr"},
            {"label": "May"},
            {"label": "Jun"},
            {"label": "Jul"},
            {"label": "Aug"},
            {"label": "Sep"},
            {"label": "Oct"},
            {"label": "Nov"},
            {"label": "Dec"}
        ]
    }]

    datasource["dataset"] = [{
            "seriesname": "Actual Revenue",
            "data": [
                {"value": "16000"},
                {"value": "20000"},
                {"value": "18000"},
                {"value": "19000"},
                {"value": "15000"},
                {"value": "21000"},
                {"value": "16000"},
                {"value": "20000"},
                {"value": "17000"},
                {"value": "25000"},
                {"value": "19000"},
                {"value": "23000"}
            ]
        }, {
            "seriesname": "Projected Revenue",
            "renderas": "line",
            "showvalues": "0",
            "data": [
                {"value": "15000"},
                {"value": "16000"},
                {"value": "17000"},
                {"value": "18000"},
                {"value": "19000"},
                {"value": "19000"},
                {"value": "19000"},
                {"value": "19000"},
                {"value": "20000"},
                {"value": "21000"},
                {"value": "22000"},
                {"value": "23000"}
            ]
        }, {
            "seriesname": "Profit",
            "renderas": "area",
            "showvalues": "0",
            "data": [
                {"value": "4000"},
                {"value": "5000"},
                {"value": "3000"},
                {"value": "4000"},
                {"value": "1000"},
                {"value": "7000"},
                {"value": "1000"},
                {"value": "4000"},
                {"value": "1000"},
                {"value": "8000"},
                {"value": "2000"},
                {"value": "7000"}
            ]
        }
    ]


    # Create an object for the mscombi2d chart using the FusionCharts class constructor
    mscombi2dChart = FusionCharts("mscombi2d", "ex3", "100%", 400, "chart-1", "json", datasource)
  
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'output' : mscombi2dChart.render()})

from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a Pie 3D chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the Line chart using the FusionCharts class constructor
  pyramidChart = FusionCharts("pyramid", "ex1", "100%", "385", "chart-1", "json", 
    """{
        "chart": {
            "bgcolor": "FFFFFF",
            "caption": "Revenue distribution for 2013",
            "basefontcolor": "333333",
            "decimals": "0",
            "numbersuffix": "M",
            "numberprefix": "$",
            "pyramidyscale": "40",
            "chartbottommargin": "0",
            "captionpadding": "0",
            "showborder": "0"
        },
        "data": [
            {
                "value": "17",
                "name": "Products",
                "color": "008ee4"
            },
            {
                "value": "21",
                "name": "Services",
                "color": "6baa01"
            },
            {
                "value": "20",
                "name": "Consultancy",
                "color": "f8bd19"
            },
            {
                "value": "5",
                "name": "Others",
                "color": "e44a00"
            }
        ]
    }""")
  
    # Create an object for the cylinder chart using the FusionCharts class constructor
  funnelChart = FusionCharts("funnel", "ex2", "100%", "385", "chart-2", "json", 
    """{
        "chart": {
            "bgcolor": "FFFFFF",
            "caption": "Conversion Funnel - 2013",
            "decimals": "1",
            "basefontsize": "11",
            "issliced": "0",
            "ishollow": "1",
            "labeldistance": "8",
            "showBorder": "0"
        },
        "data": [
            {
                "label": "Website Visits",
                "value": "385634"
            },
            {
                "label": "Downloads",
                "value": "145631",
                "color": "008ee4"
            },
            {
                "label": "Interested to buy",
                "value": "84564",
                "color": "f8bd19"
            },
            {
                "label": "Contract finalized",
                "value": "50654",
                "color": "6baa01"
            },
            {
                "label": "Purchased",
                "value": "25342",
                "color": "e44a00"
            }
        ]
    }""")
  
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'index.html', {'output' : pyramidChart.render(),
            'output_2' : funnelChart.render()})

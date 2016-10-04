from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# The `chart` function is defined to load data from a Python Dictionary. This data will be converted to
# XML and the chart will be rendered.

def chart(request):
	# Chart data is passed to the `dataSource` parameter, as xml
    chartXML = "<chart __attributes__>__set__</chart>"
    attributeTemplate = "__key__=\"__value__\" "
    setXMLTemplate = "<set label=\"__label__\" value=\"__value__\" />"

    # `dataSource` is the dict that is initialized to store the chart attributes.
    dataSource = {}
    dataSource['chart'] = { 
        "caption" : "Top 5 Stores by Sales",
        "subcaption" : "Last month",
        "yaxisname" : "Sales (In USD)",
        "numberprefix" : "$",
        "palettecolors" : "#0075c2",
        "bgcolor" : "#ffffff",
        "showborder" : "0",
        "showcanvasborder" : "0",
        "useplotgradientcolor" : "0",
        "plotborderalpha" : "10",
        "placevaluesinside" : "1",
        "valuefontcolor" : "#ffffff",
        "showaxislines" : "1",
        "axislinealpha" : "25",
        "divlinealpha" : "10",
        "aligncaptionwithcanvas" : "0",
        "showalternatevgridcolor" : "0",
        "captionfontsize" : "14",
        "subcaptionfontsize" : "14",
        "subcaptionfontbold" : "0",
        "tooltipcolor" : "#ffffff",
        "tooltipborderthickness" : "0",
        "tooltipbgcolor" : "#000000",
        "tooltipbgalpha" : "80",
        "tooltipborderradius" : "2",
        "tooltippadding" : "5"
        }

	# The `actualData` dict contains four key-value pairs that are the values for Last year	
    actualData ={
        "Bakersfield Central": 880000,
        "Garden Groove harbour": 730000,
        "Los Angeles Topanga": 590000,
        "Compton-Rancho Dom": 520000,
        "Daly City Serramonte": 330000
        }

    # To convert the chart attributes array, `actualData` to XML, 
    # we will use the templates instead of manipulating the strings.
    # Individual attribute strings will be stored in the array; they will then be combined into one string using the `join` method.
    
    chartAttributeList = []
    # Iterate over each chart attribute and convert it into an attribute string
    for attr in dataSource['chart']:
      template = attributeTemplate
      template = template.replace('__key__', attr)   
      template = template.replace('__value__', str(dataSource['chart'][attr]))
      chartAttributeList.append(template)  

    # Join the array using a single space as the delimiter.  
    chartAttributeList = ''.join(chartAttributeList)

    # We again use the template to convert the chart data into the XML format.
    setList = []
    # Iterate over each data and convert it into XML set  
    for key in actualData:
      template = setXMLTemplate
      template = template.replace('__label__', key)
      template = template.replace('__value__', str(actualData[key]))  
      setList.append(template)

    # Join the array using a single space as the delimiter.  
    setList = ''.join(setList)  
    
    # Replace the chart attributes and the data sets
    chartXML = chartXML.replace('__attributes__', chartAttributeList).replace('__set__', setList)

    # Create an object for the bar chart using the FusionCharts class constructor        	  		
    bar2d = FusionCharts("bar2d", "ex1" , "600", "400", "chart-1", "xml", chartXML)
    return render(request, 'index.html', {'output': bar2d.render()})
 
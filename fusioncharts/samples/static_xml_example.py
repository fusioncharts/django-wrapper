from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

#Loading Data from a Static XML String
# Example to create a Line chart with the chart data passed in XML string format.
# The `chart` method is defined to load chart data from an XML string.

def chart(request):
    # Create an object for the Line chart using the FusionCharts class constructor
	line = FusionCharts("line", "ex1" , "600", "400", "chart-1", "xml", 
        # The chart data is passed as a string to the `dataSource` parameter.
		"""<chart caption="Total footfall in Bakersfield Central" subcaption="Last week" xaxisname="Day" yaxisname="No. of Visitors" linethickness="2" palettecolors="#0075c2" basefontcolor="#333333" basefont="Helvetica Neue,Arial" captionfontsize="14" subcaptionfontsize="14" subcaptionfontbold="0" showborder="0" bgcolor="#ffffff" showshadow="0" canvasbgcolor="#ffffff" canvasborderalpha="0" divlinealpha="100" divlinecolor="#999999" divlinethickness="1" divlinedashed="1" divlinedashlen="1" divlinegaplen="1" showxaxisline="1" xaxislinethickness="1" xaxislinecolor="#999999" showalternatehgridcolor="0">
                <set label="Mon" value="15123" />
                <set label="Tue" value="14233" />
                <set label="Wed" value="23507" />
                <set label="Thu" value="9110" />
                <set label="Fri" value="15529" />
                <set label="Sat" value="20803" />
                <set label="Sun" value="19202" />
            </chart>""")
	
	# Alternatively, you can assign this string to a string variable in a separate XML file and
	# pass the URL of that file to the `dataSource` parameter.
	
 	return  render(request, 'index.html', {'output' : line.render()})
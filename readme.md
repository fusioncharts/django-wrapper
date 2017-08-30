
# FusionCharts Django Wrapper

### What is FusionCharts Django wrapper?

The FusionCharts Django server-side wrapper lets you create charts in your website without writing any JavaScript code.

### How does the wrapper work?
Conventionally, FusionCharts Suite XT uses JavaScript and HTML to generate charts in the browser. The Django wrapper lets you generate the required JavaScript and HTML code as a string on the server. This string is then used to render charts on a browser page.

### Version
1.0

### Requirements
Python 2.7 or higher  
Note: Assuming you have already installed Django

### Installation
 * Include fusioncharts.py in your project.
 * Start rendering charts using the classes and methods under the "**FusionCharts**" namespace.
 
### Usage Guide

#### Installing FusionCharts JS libraries in your page where you want to display FusionCharts
Download the FusionCharts library using files placed in the folder of your project. You need to  download the **[`trial version`](http://www.fusioncharts.com/download/)** of FusionCharts.

Assuming you have the FusionCharts library placed inside the "static/fusioncharts" folder in your project, write a script tag in the <head> section of the page where you want to add the source of the FusionCharts library link from the local folder.
```html
{% load static %} 
<script type="text/javascript" src="{% static "fusioncharts/fusioncharts.js" %}"></script>
```
Now, you are ready to prepare the chart using our django-wrapper. 
### Using the wrapper

#### 1. Creating a chart
```
# Filename: app_name/views.py

# Include the `fusioncharts.py` file which has 
# required functions to embed the charts in html page
from fusioncharts import FusionCharts

# The `chart` method is defined to load chart data from an JSON string.
def chart(request):
	# Create an object for the column2d chart using the FusionCharts class constructor
	column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json",
	 	# The data is passed as a string in the `dataSource` as parameter.
		"""{  
			   "chart": {  
				  "caption":"Harry\'s SuperMart",
				  "subCaption":"Top 5 stores in last month by revenue",
				  "numberPrefix":"$",
				  "theme":"ocean"
			   },
			   "data": [  
					{"label":"Bakersfield Central", "value":"880000"},
					{"label":"Garden Groove harbour", "value":"730000"},
					{"label":"Los Angeles Topanga", "value":"590000"},
					{"label":"Compton-Rancho Dom", "value":"520000"},
					{"label":"Daly City Serramonte", "value":"330000"}
				]
			}""")

	# returning complete JavaScript and HTML code, 
	# which is used to generate chart in the browsers.
	return  render(request, 'index.html', {'output' : column2d.render()})
```

#### 2. Render the chart
The code for rendering the chart is written in the view file, i.e. -.py file. The HTMl code to render the charts is given below:

```
<!-- Filename: app_name/templates/index.html -->
<h3>FusionChart</h3>
<div id="chartContainer">{{ output|safe }}</div>
```

In the above code, output|safe has been used to turn off the auto-escaping of data, on a per-site, per-template, or per-variable level.

#### Final template

The full HTML code for the example looks as under:
```
<!DOCTYPE html>
<html>
  <head>
    <title>FC-python wrapper</title>
    {% load static %} 
    <script type="text/javascript" src="{% static "fusioncharts/fusioncharts.js" %}"></script>
    <script type="text/javascript" src="{% static "fusioncharts/themes/fusioncharts.theme.fint.js" %}"></script>
  </head>
  <body>
    <div id="chart-1">{{ output|safe }}</div>
  </body>
</html>
```


#### 3. URL Configuration
```
#Filename: app_name/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.chart,  name='demo'),
]
```

### **Constructor parameters:**
The following parameters can be used in a constructor in the order they are described in the table below. Some of these parameters are optional. This function assumes that you've already included the FusionCharts JavaScript library to your page.

| Parameter | Type | Description |
|:-------|:----------:| :------|
| chartType | `String` | The type of chart that you intend to plot. e.g. `Column3D`, `Column2D`, `Pie2D` etc.|
|chartId | `String` | Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.|
|chartWidth | `String` | Intended width for the chart. e.g. `400`|
|chartHeight | `String` | Intended height for the chart. e.g. `300`|
|containerId | `String` | The id of the chart container. e.g. `chart-1`|
|dataFormat | `String` | Type of the data that is given to the chart. e.g. `json`, `jsonurl`, `xml`, `xmlurl`|
|dataSource | `String` | Actual data for the chart. e.g. `{"chart":{},"data":[{"label":"Jan","value":"420000"}]}`|

### License
**FUSIONCHARTS:**

Copyright (c) FusionCharts Technologies LLP  
License Information at [http://www.fusioncharts.com/license](http://www.fusioncharts.com/license)

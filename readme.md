# FusionCharts Django Wrapper

### What is FusionCharts Django wrapper?

The FusionCharts Django server-side wrapper lets you create charts in your website without writing any JavaScript code.

### How does the wrapper work?
Conventionally, FusionCharts Suite XT uses JavaScript and HTML to generate charts in the browser. The Django wrapper lets you generate the required JavaScript and HTML code as a string on the server. This string is then used to render charts on a browser page.

### Version
1.0

### Requirements
Python 2.7 or higher

### Installation
 * Include fusioncharts.py in your project.
 * Start using methods and classes available under **"FusionCharts"** namespace to generate Charts in your project.
### Usage Guide

#### Installing FusionCharts JS libraries in your page where you want to display FusionCharts
There are two ways you can install the FusionCharts JS library in your project
* Using FusionCharts CDN
* Using library files placed in the folder of your project

**Using FusionCharts CDN**

Write a script tag in the <head> section of the page where you want to add the source of the FusionCharts library link from the official CDN:
```html
<script type="text/javascript" src="http://static.fusioncharts.com/code/latest/fusioncharts.js"></script>
```
**Using library files placed in a folder of your project**

You can download the **[`trial version`](http://www.fusioncharts.com/download/)** of FusionCharts.

Next, assuming you have the FusionCharts library placed inside the "static/fusioncharts" folder in your project, write a script tag in the <head> section of the page where you want to add the source of the FusionCharts library link from the local folder.
```html
   <script type="text/javascript" src="{% static "fusioncharts/fusioncharts.js" %}"></script>
```
Now, you are ready to prepare the chart using our JSP-wrapper. 
### Using the wrapper
### 1. Creating a chart
~~~
# Filename: app_name/views.py

'''
include the `fusioncharts.py` file that contains functions to embed the charts.
'''
from fusioncharts import FusionCharts
def chart(request):
	column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", 
		"""{  
			   "chart":
			   {  
				  "caption":"Harry\'s SuperMart",
				  "subCaption":"Top 5 stores in last month by revenue",
				  "numberPrefix":"$",
				  "theme":"ocean"
			   },
			   "data":
			   [  
				  {  
					 "label":"Bakersfield Central",
					 "value":"880000"
				  },
				  {  
					 "label":"Garden Groove harbour",
					 "value":"730000"
				  },
				  {  
					 "label":"Los Angeles Topanga",
					 "value":"590000"
				  },
				  {  
					 "label":"Compton-Rancho Dom",
					 "value":"520000"
				  },
				  {  
					 "label":"Daly City Serramonte",
					 "value":"330000"
				  }
			   ]
		}""")
return  render(request, 'index.html', {'output' : column2d.render()})
~~~

### 2. URL Configuration
~~~
#Filename: app_name/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.chart,  name='demo'),
]

~~~

### 3. Render the chart
In order to render the chart, you can use the `render` method in the specific view

~~~
<!-- Filename: app_name/templates/index.html -->
<h3>FusionChart</h3>
<div id="chartContainer">{{ output|safe }}</div>
~~~

### **Constructor parameters:**
The following parameters can be used in a constructor in the order they are described in the table below. Some of these parameters are optional. This function assumes that you've already included the FusionCharts JavaScript library to your page.

| Parameter | Type | Description |
|:-------|:----------:| :------|
| chartType | `String` | The type of chart that you intend to plot. e.g. `Column3D`, `Column2D`, `Pie2D` etc.|
|chartId | `String` | Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.|
|chartWidth | `String` | Intended width for the chart (in pixels). e.g. `400`|
|chartHeight | `String` | Intended height for the chart (in pixels). e.g. `300`|
|dataFormat | `String` | Type of the data that is given to the chart. e.g. `json`, `jsonurl`, `xml`, `xmlurl`|
|dataSource | `String` | Actual data for the chart. e.g. `{"chart":{},"data":[{"label":"Jan","value":"420000"}]}`|

### License
**FUSIONCHARTS:**

Copyright (c) FusionCharts Technologies LLP  
License Information at [http://www.fusioncharts.com/license](http://www.fusioncharts.com/license)


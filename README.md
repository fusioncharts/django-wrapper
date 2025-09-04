# FusionCharts Django Wrapper

## What is FusionCharts Django wrapper?

The FusionCharts Django server-side wrapper lets you create charts in your website without writing any JavaScript code.

### How does the wrapper work?

FusionCharts Suite XT uses JavaScript and HTML to generate charts in the browser. The Django wrapper lets you generate the required JavaScript and HTML code as a string on the server. This string is then used to render charts on a browser page.

### Version

1.1

### Requirements

Python 3 or higher  
Note: Assuming you have already installed Django

### Installation

Download [fusioncharts-suite-xt](http://www.fusioncharts.com/)

- Unzip the archive and move to "fusioncharts-suite-xt > integrations > django > fusioncharts-wrapper" to get the "fusioncharts.py" file.
- Copy fusioncharts.py to the STATIC folder in your Web application.
- Start rendering charts using the classes and methods under the "**FusionCharts**" namespace.

### Usage Guide

#### Installing FusionCharts JS libraries in your page where you want to display FusionCharts

Download the FusionCharts library using files placed in the folder of your project. You need to download the [`trial version`](http://www.fusioncharts.com/download/) of FusionCharts.

Assuming you have the FusionCharts library placed inside the "static/fusioncharts" folder in your project, write a script tag in the `<head>` section of the page where you want to add the source of the FusionCharts library link from the local folder.

```html
{% load static %}
<script type="text/javascript" src="{% static "fusioncharts/fusioncharts.js" %}"></script>
```

Now, you are ready to prepare the chart using our django-wrapper.

### Using the wrapper

#### 1. Creating a chart

```python
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

```html
<!-- Filename: app_name/templates/index.html -->
<h3>FusionChart</h3>
<div id="chartContainer">{{ output|safe }}</div>
```

In the above code, output|safe has been used to turn off the auto-escaping of data, on a per-site, per-template, or per-variable level.

#### Final template

The full HTML code for the example looks as under:

```html
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

```python
#Filename: app_name/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.chart,  name='demo'),
]
```

### **Constructor parameters:**

The following parameters can be used in a constructor in the order they are described in the table below. Some of these parameters are optional. This function assumes that you've already included the FusionCharts JavaScript library to your page.

| Parameter   |   Type   | Description                                                                                                             |
| :---------- | :------: | :---------------------------------------------------------------------------------------------------------------------- |
| chartType   | `String` | The type of chart that you intend to plot. e.g. `Column3D`, `Column2D`, `Pie2D` etc.                                    |
| chartId     | `String` | Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id. |
| chartWidth  | `String` | Intended width for the chart. e.g. `400`                                                                                |
| chartHeight | `String` | Intended height for the chart. e.g. `300`                                                                               |
| containerId | `String` | The id of the chart container. e.g. `chart-1`                                                                           |
| dataFormat  | `String` | Type of the data that is given to the chart. e.g. `json`, `jsonurl`, `xml`, `xmlurl`                                    |
| dataSource  | `String` | Actual data for the chart. e.g. `{"chart":{},"data":[{"label":"Jan","value":"420000"}]}`                                |

### **Event parameters:**

Following parameters can be used in an event in the order they are described.

| Parameter |   Type   | Description                                                    |
| :-------- | :------: | :------------------------------------------------------------- |
| eventName | `String` | Which event you want to bind. e.g. `dataLoaded`.               |
| funcName  | `String` | Javascript function, which is written in your client side code |

More information: <https://www.fusioncharts.com/dev/api/fusioncharts/fusioncharts-events>

```python
# Creating FC Chart object
column2d = FusionCharts("column2d", "chart-1", '700', '400', "chart-container", "json", chartDataSource)

# Attach 'dataplotClick' event
column2d.addEvent("dataplotClick", "onDataplotClick")

# Render the chart
return  render(request, 'index.html', {'output' : column2d.render()})
```

### Message Parameters

let you set and configure custom chart messages. Following parameters can be used in a message in the order they are described.

| Parameter    |   Type   | Description                                     |
| :----------- | :------: | :---------------------------------------------- |
| messageName  | `String` | Message you want to customize. e.g. loadMessage |
| messageValue | `String` | Your custom message                             |

More information: <https://www.fusioncharts.com/dev/chart-attributes/>

```python
# Creating FC Chart object
column2d = FusionCharts("column2d", "chart-1", '700', '400', "chart-container", "json", chartDataSource)

# Attach message with message string.
column2d.addMessage("loadMessage", "please wait data is being loaded")

# Render the chart
return  render(request, 'index.html', {'output' : column2d.render()})
```

### **FusionTime:**

**Create the chart object with TimeSeries chart with the required parameters as shown below.**

```py
fusionTable = FusionTable(schema, data)
timeSeries = TimeSeries(fusionTable)

# Wrapper constructor parameters
# charttype, chartID, width, height, renderAt, data format, TimeSeries object

fcChart = FusionCharts("timeseries", "MyFirstChart" , "700", "450", "chart-container", "json", timeSeries)

# Render the chart
return render(request, 'index.html', {'output' : fcChart.render()})
```

There are two classes that you need to use in order to create a TimeSeries chart, `FusionTable` and `TimeSeries`.

### **Constructor parameters of FusionTable :**

This class creates `timeseries` compatible `FusionTable` object which later passed to the TimeSeries class constructor.

```py
# Creating FusionTable
fusionTable = FusionTable(schema, data)
```

Let you set the following parameters in FusionTable constructor.

| Parameter |   Type   | Description                                                |
| :-------- | :------: | :--------------------------------------------------------- |
| schema    | `String` | The schema which defines the properties of the columns     |
| data      | `String` | The actual values for each row and column of the DataTable |

### **Data operation:**

FusionTable also supports following DataTable operations:

- Select
- Sort
- Filter
- Pipe

**`Select`** operation should be used only when you want to see few specific columns of the DataTable.

```py
fusionTable = FusionTable(schema, data)

# Column names as parameter
fusionTable.Select("Country", "Sales")
```

| Parameter  |   Type   | Description                   |
| :--------- | :------: | :---------------------------- |
| columnName | `String` | Define multiple columns name. |

**`Sort`** one of the major requirements while working with large sets of data is to sort the data in a specific order - most commonly, ascending or descending.

```py
fusionTable = FusionTable(schema, data)

#column name and orderby
fusionTable.Sort("Sales", FusionTable.OrderBy.ASC)
```

| Parameter     |   Type   | Description                                                                                                   |
| :------------ | :------: | :------------------------------------------------------------------------------------------------------------ |
| columnName    | `String` | Define column name on which sorting will be applied.                                                          |
| columnOrderBy |  `Enum`  | To sort the column in descending or ascending order. e.g. `FusionTable.OrderBy.ASC, FusionTable.OrderBy.DESC` |

**`Filter`** comes with a set of operations that you can use to filter data values from a large dataset, based on one or more conditions. Supported filter operations are:

- Equals
- Greater
- GreaterEquals
- Less
- LessEquals
- Between

```py
# Filter - Equal
# Creating filter statement by passing the filter type, column name and filter value
filter1 = fusionTable.CreateFilter(FusionTable.FilterType.Equals, "Country", "United States")

#Applying the filter on fusion table
fusionTable.ApplyFilter(filter1)
```

```py
# Filter - Greater
# Creating filter statement by passing the filter type, column name and filter value
filter1 = fusionTable.CreateFilter(FusionTable.FilterType.Greater, "Quantity", 100)

#Applying the filter on fusion table
fusionTable.ApplyFilter(filter1)
```

```py
# Filter - GreaterEquals
# Creating filter statement by passing the filter type, column name and filter value
filter1 = fusionTable.CreateFilter(FusionTable.FilterType.GreaterEquals, "Quantity", 100)

#Applying the filter on fusion table
fusionTable.ApplyFilter(filter1)
```

```py
# Filter - Less
# Creating filter statement by passing the filter type, column name and filter value
filter1 = fusionTable.CreateFilter(FusionTable.FilterType.Less, "Quantity", 100)

#Applying the filter on fusion table
fusionTable.ApplyFilter(filter1)
```

```py
# Filter - LessEquals
# Creating filter statement by passing the filter type, column name and filter value
filter1 = fusionTable.CreateFilter(FusionTable.FilterType.LessEquals, "Quantity", 100)

#Applying the filter on fusion table
fusionTable.ApplyFilter(filter1)
```

```py
# Filter - Between
# Creating filter statement by passing the filter type, column name and filter value
filter1 = fusionTable.CreateFilter(FusionTable.FilterType.Between, "Quantity", 100, 1000)

#Applying the filter on fusion table
fusionTable.ApplyFilter(filter1)
```

let you set the following parameter of `CreateFilter` method for creating filter statement.

| Parameter  |   Type   | Description                                                                                         |
| :--------- | :------: | :-------------------------------------------------------------------------------------------------- |
| filterType |  `Enum`  | Define the filter type. e.g. `FusionTable.FilterType.Equals`, `FusionTable.FilterType.Greater` etc. |
| columnName | `String` | Define column name on which the filter will be applied.                                             |
| values     | `Object` | Define filter value(s). e.g. `String`, `Integer` values.                                            |

let you set the following parameter of `ApplyFilter` method for applying the filter on fusion table.

| Parameter |   Type   | Description                   |
| :-------- | :------: | :---------------------------- |
| filter    | `String` | Define the `Filter statement` |

```py
# Filter - Apply conditional filter
# Define anonymous function to filter
fusionTable.ApplyFilterByCondition("""(row, columns) => {
                    return row[columns.Country] === 'USA' ||
                    (row[columns.Sales] > 100 && row[columns.Shipping_Cost] < 10);
                    }""")
```

**`Pipe`** is an operation which lets you run two or more data operations in a sequence. Instead of applying multiple filters one by one to a DataTable which creates multiple DataTable(s), you can combine them in one single step using pipe and apply to the DataTable. This creates only one DataTable.

```py
fusionTable = FusionTable(schema, data)

# Creating first filter statement by passing the filter type, column name and filter value
filter1 = fusionTable.CreateFilter(FusionTable.FilterType.Equals, "Country", "India")

# Creating second filter statement by passing the filter type, column name and filter value
filter2 = fusionTable.CreateFilter(FusionTable.FilterType.Greater, "Quantity", 100)

#Applying multiple filters one by one to a DataTable
fusionTable.Pipe(filter1, filter2)
```

| Parameter |   Type   | Description              |
| :-------- | :------: | :----------------------- |
| filters   | `String` | Define multiple filters. |

### **Constructor parameter of TimeSeries :**

This class creates `timeseries` compatible `TimeSeries` object which later passed to the chart object.

```py
# Creating TimeSeries object
timeSeries = TimeSeries(fusionTable)
```

let you set the following parameter in TimeSeries constructor.

| Parameter   |     Type      | Description                                                           |
| :---------- | :-----------: | :-------------------------------------------------------------------- |
| fusionTable | `FusionTable` | The Datatable which defines the schema and actual data (FusionTable). |

#### Methods

**`AddAttribute`** is a public method to accept data as a form of JSON string to configure the chart attributes. e.g. `caption`, `subCaption`, `xAxis` etc.

```py

fusionTable = FusionTable(schema, data)
timeSeries = TimeSeries(fusionTable)

timeSeries.AddAttribute("caption", """{
                                     text: ' Online Sales'
                                   }""")
```

let you set the following parameter in `AddAttribute` method.

| Parameter |   Type   | Description                  |
| :-------- | :------: | :--------------------------- |
| key       | `String` | The attribute name.          |
| value     | `String` | Define json formatted value. |

### License

The FusionCharts Django integration component is open-source and distributed under the terms of the MIT/X11 License. However, you will need to download and include FusionCharts library in your page separately, which has a [separate license](https://www.fusioncharts.com/buy).

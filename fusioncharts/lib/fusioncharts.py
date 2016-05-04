from django.http import HttpResponse
import json

# Common base class for FC
class FusionCharts:

   constructorOptions = {}
   constructorTemplate = """
     <script type="text/javascript">
         FusionCharts.ready(function () {
             new FusionCharts(__constructorOptions__);
         });
     </script>"""
   renderTemplate = """
     <script type="text/javascript">
         FusionCharts.ready(function () {
             FusionCharts("__chartId__").render();
         });
     </script>
   """
   # constructor
   def __init__(self, type, id, width, height, renderAt, dataFormat, dataSource):    
      FusionCharts.constructorOptions['type'] = type
      FusionCharts.constructorOptions['id'] = id
      FusionCharts.constructorOptions['width'] = width
      FusionCharts.constructorOptions['height'] = height
      FusionCharts.constructorOptions['renderAt'] = renderAt
      FusionCharts.constructorOptions['dataFormat'] = dataFormat
      #dataSource = unicode(dataSource, errors='replace')
      FusionCharts.constructorOptions['dataSource'] = dataSource
   
   # render the chart created
   # It prints a script and calls the FusionCharts javascript render method of created chart   
   def render(self):
    self.readyJson = json.dumps(FusionCharts.constructorOptions)
    self.readyJson = FusionCharts.constructorTemplate.replace('__constructorOptions__', self.readyJson)
    self.readyJson = self.readyJson + FusionCharts.renderTemplate.replace('__chartId__', FusionCharts.constructorOptions['id'])
    self.readyJson = self.readyJson.replace('\\n', '')
    self.readyJson = self.readyJson.replace('\\t', '')

    if(FusionCharts.constructorOptions['dataFormat'] == 'json'):
      self.readyJson = self.readyJson.replace('\\', '')
      self.readyJson = self.readyJson.replace('"{', "{")
      self.readyJson = self.readyJson.replace('}"', "}")
      
    return self.readyJson
 
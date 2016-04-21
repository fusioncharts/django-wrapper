"""fusioncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from samples import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""

from django.conf.urls import url
from django.contrib import admin
from views import index
from samples import static_json_example, static_xml_example, dict_json_example, dict_xml_example 
from samples import annotation_example, fusion_maps, gantt_chart_example, angular_gauge_example
from samples import linked_chart_single_level, single_series_chart, multi_series_chart, xy_chart
from samples import database_example
from samples import database_drilldown_example


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^static-json-example/', static_json_example.fc_json, name='fc_json'),
    url(r'^static-xml-example/', static_xml_example.fc_xml, name='fc_xml'),
    url(r'^dict-json-example/', dict_json_example.fc_dict_json, name='fc_dict_json'),
    url(r'^dict-xml-example/', dict_xml_example.fc_dict_xml, name='fc_dict_xml'),
    url(r'^annotation-example/', annotation_example.fc_annotation, name='fc_annotation'),
    url(r'^map-example/', fusion_maps.fc_map, name='fc_map'),
    url(r'^gantt-chart-example/', gantt_chart_example.fc_gantt, name='fc_gantt'),
    url(r'^angular-gauge-example/', angular_gauge_example.fc_gauge, name='fc_gauge'),
    url(r'^linked-chart-single-level-example/', linked_chart_single_level.fc_drillDown, name='fc_drillDown'),
    url(r'^single-series-chart-example/', single_series_chart.fc_singleSeries, name='fc_singleSeries'),
    url(r'^multi-series-chart-example/', multi_series_chart.fc_multiSeries, name='fc_multiSeries'),
    url(r'^xy-chart-example/', xy_chart.fc_scatter, name='fc_scatter'),
    url(r'^database-example/', database_example.fc_db, name='fc_db'),
    url(r'^database-drilldown-example/', database_drilldown_example.fc_drilldown, name='fc_drilldown'),
]

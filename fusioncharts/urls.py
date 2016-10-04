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
from views import catalogue

from samples import simple, static_json_example, static_xml_example, dict_json_example, dict_xml_example 
from samples import annotation_example, fusion_maps, gantt_chart_example, angular_gauge_example
from samples import linked_chart_single_level, single_series_chart, multi_series_chart, xy_chart
from samples import column2d_database, database_example, database_drilldown_example
from samples import a_3d_pie_chart, a_column_line_area_combi_chart
from samples import fetching_data_from_json_url, fetching_data_from_xml_url, mul_col2d_using_dict
from samples import client_side_chart_export, render_angular_and_gauge, render_pyramid_and_funnel_charts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', catalogue),
    url(r'^simple/', simple.chart, name='chart'),
    url(r'^static-json-example/', static_json_example.chart, name='chart'),
    url(r'^static-xml-example/', static_xml_example.chart, name='chart'),
    url(r'^dict-json-example/', dict_json_example.chart, name='chart'),
    url(r'^dict-xml-example/', dict_xml_example.chart, name='chart'),
    url(r'^annotation-example/', annotation_example.chart, name='chart'),
    url(r'^map-example/', fusion_maps.chart, name='chart'),
    url(r'^gantt-chart-example/', gantt_chart_example.chart, name='chart'),
    url(r'^angular-gauge-example/', angular_gauge_example.chart, name='chart'),
    url(r'^linked-chart-single-level-example/', linked_chart_single_level.chart, name='chart'),
    url(r'^single-series-chart-example/', single_series_chart.chart, name='chart'),
    url(r'^multi-series-chart-example/', multi_series_chart.chart, name='chart'),
    url(r'^xy-chart-example/', xy_chart.chart, name='chart'),
    url(r'^database-example/', database_example.chart, name='chart'),
    url(r'^database-drilldown-example/', database_drilldown_example.chart, name='chart'),
    url(r'^render-3d-pie-chart/', a_3d_pie_chart.chart, name='chart'),
    url(r'^render-column-line-area-combi-chart/', a_column_line_area_combi_chart.chart, name='chart'),
    url(r'^fetching-data-from-json-url/', fetching_data_from_json_url.chart, name='chart'),
    url(r'^fetching-data-from-xml-url/', fetching_data_from_xml_url.chart, name='chart'),
    url(r'^client-side-chart-export/', client_side_chart_export.chart, name='chart'),
    url(r'^render-angular-and-gauge/', render_angular_and_gauge.chart, name='chart'),
    url(r'^render-pyramid-and-funnel-charts/', render_pyramid_and_funnel_charts.chart, name='chart'),
    url(r'^mul-col2d-using-dict/', mul_col2d_using_dict.chart, name='chart'),
    url(r'^render-column-2d-using-database/', column2d_database.chart, name='chart')
]

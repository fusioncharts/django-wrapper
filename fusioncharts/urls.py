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

from web import simple, a_3d_pie_chart, a_column_line_area_combi_chart, loading_data_from_sqlite_database
from web import fetching_data_from_json_url, fetching_data_from_xml_url
from web import client_side_chart_export, render_angular_and_gauge, render_pyramid_and_funnel_charts
from web import mul_col2d_using_dict

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
    
    url(r'^web/simple/', simple.fc_simple, name='fc_simple'),
    url(r'^web/a_3d_pie_chart/', a_3d_pie_chart.fc_pie3dChart, name='fc_pie3dChart'),
    url(r'^web/a_column_line_area_combi_chart/', a_column_line_area_combi_chart.fc_mscombi2dChart, name='fc_mscombi2dChart'),
    url(r'^web/loading_data_from_sqlite_database/', loading_data_from_sqlite_database.fc_db, name='fc_db'),
    url(r'^web/fetching_data_from_json_url/', fetching_data_from_json_url.fc_jsonurl, name='fc_jsonurl'),
    url(r'^web/fetching_data_from_xml_url/', fetching_data_from_xml_url.fc_xmlurl, name='fc_xmlnurl'),
    url(r'^web/client_side_chart_export/', client_side_chart_export.fc_export, name='fc_export'),
    url(r'^web/render_angular_and_gauge/', render_angular_and_gauge.fc_charts, name='fc_charts'),
    url(r'^web/render_pyramid_and_funnel_charts/', render_pyramid_and_funnel_charts.fc_charts, name='fc_charts'),
    url(r'^web/mul-col2d-using-dict/', mul_col2d_using_dict.fc_charts, name='fc_charts')
]

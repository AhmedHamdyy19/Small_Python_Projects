from sklearn.cluster._bicluster import SpectralCoclustering
import numpy as np, pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file
from bokeh.plotting import figure, show


whisky = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@whiskies.csv", index_col=0)
correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

cluster_colors = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161']
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

region_colors = {key: values for key, values in zip(regions, cluster_colors)}
distilleries = whisky.iloc[:, 1]

region_cols = [region_colors[i] for i in whisky["Region"]]


def location_plot(title, colors):
    output_file(title + ".html")

    region_cols = [region_colors[region] for region in whisky.Region]

    location_source = ColumnDataSource(
        data={
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": region_cols,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery
        }
    )

    fig = figure(title=title,
                 x_axis_location="above", tools="hover, save", width=400, height=500)

    fig.circle("x", "y", size=9, source=location_source, color='colors', line_color=None)
    fig.xaxis.major_label_orientation = np.pi / 3

    hover = fig.select(dict(type=HoverTool))
    hover.tooltips = {
        "Distillery": "@distilleries",
        "Location": "(@x, @y)"
    }

    show(fig)


location_plot("Whisky Locations and Regions", region_cols)

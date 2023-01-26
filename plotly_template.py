"""Point8 style template for plotly.
To us this style copy the plotly_template.py file to your module directory. (Needs to be in module search path)
This template is based on "simple_white" from plotly. Changes are marked with #custom.

Then add the following lines to your files:

import plotly.io as pio
import plotly_template # adapt path to module

pio.templates.default = "p8_template"
"""

import plotly.graph_objects as go
import plotly.io as pio

GRID_COLOR = "rgba(0, 0, 0, 0.1)"
LINE_COLOR = "#032E43"
ZERO_LINE_COLOR = LINE_COLOR

pio.templates["p8_template"] = go.layout.Template(
    layout=go.Layout(
        {
            "annotationdefaults": {"arrowhead": 0, "arrowwidth": 1},
            "autotypenumbers": "strict",
            "coloraxis": {
                "colorbar": {
                    "outlinewidth": 1,
                    "tickcolor": "rgb(36,36,36)",
                    "ticks": "outside",
                }
            },
            "colorscale": {
                "diverging": [
                    [0.0, "rgb(103,0,31)"],
                    [0.1, "rgb(178,24,43)"],
                    [0.2, "rgb(214,96,77)"],
                    [0.3, "rgb(244,165,130)"],
                    [0.4, "rgb(253,219,199)"],
                    [0.5, "rgb(247,247,247)"],
                    [0.6, "rgb(209,229,240)"],
                    [0.7, "rgb(146,197,222)"],
                    [0.8, "rgb(67,147,195)"],
                    [0.9, "rgb(33,102,172)"],
                    [1.0, "rgb(5,48,97)"],
                ],
                "sequential": [
                    [0.0, "#440154"],
                    [0.1111111111111111, "#482878"],
                    [0.2222222222222222, "#3e4989"],
                    [0.3333333333333333, "#31688e"],
                    [0.4444444444444444, "#26828e"],
                    [0.5555555555555556, "#1f9e89"],
                    [0.6666666666666666, "#35b779"],
                    [0.7777777777777778, "#6ece58"],
                    [0.8888888888888888, "#b5de2b"],
                    [1.0, "#fde725"],
                ],
                "sequentialminus": [
                    [0.0, "#440154"],
                    [0.1111111111111111, "#482878"],
                    [0.2222222222222222, "#3e4989"],
                    [0.3333333333333333, "#31688e"],
                    [0.4444444444444444, "#26828e"],
                    [0.5555555555555556, "#1f9e89"],
                    [0.6666666666666666, "#35b779"],
                    [0.7777777777777778, "#6ece58"],
                    [0.8888888888888888, "#b5de2b"],
                    [1.0, "#fde725"],
                ],
            },
            "colorway": [
                "#00678a",
                "#e6a176",
                "#984464",
                "#5eccab",
                "#cdcdcd",
                "#c0affb",
                "#56641a",
            ],  # custom
            "font": {"color": "#032E43"},  # custom
            "geo": {
                "bgcolor": "white",
                "lakecolor": "white",
                "landcolor": "white",
                "showlakes": True,
                "showland": True,
                "subunitcolor": "white",
            },
            "hoverlabel": {"align": "left"},
            "hovermode": "closest",
            "mapbox": {"style": "light"},
            "paper_bgcolor": "white",
            "plot_bgcolor": "white",
            "polar": {
                "angularaxis": {
                    "gridcolor": GRID_COLOR,
                    "linecolor": LINE_COLOR,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
                "bgcolor": "white",
                "radialaxis": {
                    "gridcolor": GRID_COLOR,
                    "linecolor": LINE_COLOR,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
            },
            "scene": {
                "xaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": GRID_COLOR,
                    "gridwidth": 2,
                    "linecolor": LINE_COLOR,
                    "showbackground": True,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                    "zeroline": False,
                    "zerolinecolor": ZERO_LINE_COLOR,
                },
                "yaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": GRID_COLOR,
                    "gridwidth": 2,
                    "linecolor": LINE_COLOR,
                    "showbackground": True,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                    "zeroline": False,
                    "zerolinecolor": ZERO_LINE_COLOR,
                },
                "zaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": GRID_COLOR,
                    "gridwidth": 2,
                    "linecolor": LINE_COLOR,
                    "showbackground": True,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                    "zeroline": False,
                    "zerolinecolor": ZERO_LINE_COLOR,
                },
            },
            "shapedefaults": {
                "line_color": "red", # custom
                "opacity": 1, # custom
                # "line": {"width": 0}, #custom
                # "fillcolor": "black",
            },
            "ternary": {
                "aaxis": {
                    "gridcolor": GRID_COLOR,
                    "linecolor": LINE_COLOR,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
                "baxis": {
                    "gridcolor": GRID_COLOR,
                    "linecolor": LINE_COLOR,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
                "bgcolor": "white",
                "caxis": {
                    "gridcolor": GRID_COLOR,
                    "linecolor": LINE_COLOR,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
            },
            "title": {"x": 0.05},
            "xaxis": {
                "automargin": True,
                "gridcolor": GRID_COLOR,  # custom
                "linecolor": LINE_COLOR,  # custom
                "mirror": True,  # custom
                "showgrid": True,  # custom
                "showline": True,
                "ticks": "outside",
                "tickfont": {"size": 12},  # custom
                "title": {"standoff": 15},
                "zeroline": False,
                "zerolinecolor": ZERO_LINE_COLOR,
            },
            "yaxis": {
                "automargin": True,
                "gridcolor": GRID_COLOR,  # custom
                "linecolor": LINE_COLOR,  # custom
                "mirror": True,  # custom
                "showgrid": True,  # custom
                "showline": True,
                "ticks": "outside",
                "tickfont": {"size": 12},  # custom
                "title": {"standoff": 15},
                "zeroline": False,
                "zerolinecolor": ZERO_LINE_COLOR,
            },
        }
    )
)

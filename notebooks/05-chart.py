
sp500 = sp500 = "https://vega.github.io/vega-datasets/data/sp500.csv"
import altair as alt
import pandas as pd

brush = alt.selection_interval(encodings=['x'])
base = alt.Chart().mark_area().encode(
    alt.X("date:T", title=None),
    alt.Y("price:Q")
).properties(
    width=700
)

chart = alt.vconcat(
    base.encode(alt.X("date:T", title=None, scale=alt.Scale(domain=brush))),
    base.add_selection(brush).properties(height=60),
    data=sp500
)
chart.serve()

## Go to the terminal and start 
## ipython 05-chart.py
import plotly.express as px
import numpy as np


months = np.arange(1, 13)


def ElectricityBill(kWh) -> None:
    fig = px.line(x=months, y=kWh, labels={
                  "x": "Months", "y": "Kilo-watt hours"}, markers=True)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=months, ticktext=[
                      str(month) for month in months]))
    fig.write_html(
        "eco-footprint-analyzer/app/static/graphs/electricity-bill.html")


def WaterBill(cubic_m) -> None:
    fig = px.line(x=months, y=cubic_m, labels={
                  "x": "Months", "y": "Cubic Meters"}, markers=True)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=months, ticktext=[
                      str(month) for month in months]))
    fig.write_html(
        "eco-footprint-analyzer/app/static/graphs/water-bill.html")


def RevenueToCF(revenue: np.array, CF: np.array, names: np.array) -> None:
    fig = px.scatter(x=CF, y=revenue, labels={"x": "Carbon Emissions", "y": "Revenue"},
                     hover_name=names, size=revenue)
    fig.update_traces(text=names)
    fig.update_traces(marker=dict(opacity=1))
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Carbon Emissions: %{x} billion tonnes<br>Revenue: %{y} billion dollars")
    fig.write_html(
        "eco-footprint-analyzer/app/static/graphs/revenue-cf.html")

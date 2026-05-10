from pathlib import Path

import pandas as pd
from dash import Dash, Input, Output, dcc, html
from plotly.express import line

DATA_PATH = Path("./formatted_data.csv")

COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

APP_TITLE = "Pink Morsel Visualizer"
CHART_TITLE = "Pink Morsel Sales"
REGIONS = ["north", "east", "south", "west", "all"]


def load_data(file_path: Path) -> pd.DataFrame:
    """Load and sort dataset."""
    data = pd.read_csv(file_path)
    return data.sort_values(by="date")


def filter_data(data: pd.DataFrame, region: str) -> pd.DataFrame:
    """Filter dataset by region."""
    if region == "all":
        return data

    return data[data["region"] == region]


def generate_figure(chart_data: pd.DataFrame):
    """Generate Plotly line chart."""
    figure = line(
        chart_data,
        x="date",
        y="sales",
        title=CHART_TITLE
    )

    figure.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )

    return figure


def create_header():
    """Create application header."""
    return html.H1(
        APP_TITLE,
        id="header",
        style={
            "backgroundColor": COLORS["secondary"],
            "color": COLORS["font"],
            "borderRadius": "20px",
            "padding": "10px"
        }
    )


def create_region_picker():
    """Create region selector component."""
    return html.Div(
        children=[
            dcc.RadioItems(
                options=REGIONS,
                value="north",
                id="region_picker",
                inline=True
            )
        ],
        style={
            "fontSize": "150%",
            "padding": "20px"
        }
    )


def create_visualization(data: pd.DataFrame):
    """Create graph visualization component."""
    return dcc.Graph(
        id="visualization",
        figure=generate_figure(data)
    )


def create_layout(data: pd.DataFrame):
    """Build application layout."""
    return html.Div(
        children=[
            create_header(),
            create_visualization(data),
            create_region_picker()
        ],
        style={
            "textAlign": "center",
            "backgroundColor": COLORS["primary"],
            "borderRadius": "20px",
            "padding": "20px"
        }
    )


def register_callbacks(app: Dash, data: pd.DataFrame) -> None:
    """Register Dash callbacks."""

    @app.callback(
        Output("visualization", "figure"),
        Input("region_picker", "value")
    )
    def update_graph(region: str):
        filtered_data = filter_data(data, region)
        return generate_figure(filtered_data)


def create_app() -> Dash:
    """Initialize and configure Dash app."""
    data = load_data(DATA_PATH)

    app = Dash(__name__)
    app.layout = create_layout(data)

    register_callbacks(app, data)

    return app


def main() -> None:
    """Application entry point."""
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
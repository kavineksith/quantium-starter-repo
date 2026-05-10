from pathlib import Path

import pandas as pd
from dash import Dash, dcc, html
from plotly.express import line

DATA_PATH = Path("./formatted_data.csv")
APP_TITLE = "Pink Morsel Visualizer"
CHART_TITLE = "Pink Morsel Sales"


def load_data(file_path: Path) -> pd.DataFrame:
    """Load and prepare sales data."""
    data = pd.read_csv(file_path)
    return data.sort_values(by="date")


def create_line_chart(data: pd.DataFrame):
    """Create sales visualization chart."""
    return line(
        data_frame=data,
        x="date",
        y="sales",
        title=CHART_TITLE
    )


def create_layout(chart_figure):
    """Build Dash application layout."""
    return html.Div(
        children=[
            html.H1(
                APP_TITLE,
                id="header"
            ),
            dcc.Graph(
                id="visualization",
                figure=chart_figure
            )
        ]
    )


def create_app() -> Dash:
    """Initialize and configure Dash application."""
    data = load_data(DATA_PATH)
    chart = create_line_chart(data)

    app = Dash(__name__)
    app.layout = create_layout(chart)

    return app


def main() -> None:
    """Application entry point."""
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
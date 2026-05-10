from data_visualizer import create_app


def test_header_exists(dash_duo):
    app = create_app()
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    app = create_app()
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_region_picker_exists(dash_duo):
    app = create_app()
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_picker", timeout=10)
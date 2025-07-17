# dash-offline-detect-plugin

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/dash-offline-detect-plugin/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/dash-offline-detect-plugin.svg?color=dark-green)](https://pypi.org/project/dash-offline-detect-plugin/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Offline detect plugin for Dash applications using Dash Hooks.

## Installation

```bash
pip install dash-offline-detect-plugin
```

## Usage

```python
from dash import Dash
# Import the offline detect plugin
from dash_offline_detect_plugin import setup_offline_detect_plugin

# Enable the offline detect plugin for the current app
setup_offline_detect_plugin()

app = Dash(__name__)
# Rest of your app code...
```

## Example

Run the included example:

```bash
python example.py
```

<center><img src="./images/demo.gif" /></center>

## API Reference

### `setup_offline_detect_plugin()`

This function enables the offline detection feature for your Dash application.

| Parameter     | Type  | Default                                                              | Description                                                                                                                      |
| ------------- | ----- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `interval`    | `int` | `5000`                                                               | Interval of detection in browser (milliseconds). Controls how frequently the browser checks if the backend service is available. |
| `title`       | `str` | `"Service Unavailable"`                                              | Title of the overlay displayed when the service is unavailable.                                                                  |
| `description` | `str` | `"Unable to connect to the backend service, trying to reconnect..."` | Description text displayed in the overlay when the service is unavailable.                                                       |

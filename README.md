# dash-offline-detect-plugin

Offline detect plugin for Dash applications using Dash Hooks. You can check out this project on PyPi at: https://pypi.org/project/dash-offline-detect-plugin

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

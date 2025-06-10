import re
import time
from dash import hooks
from flask import jsonify


def setup_offline_detect_plugin(
    interval: int = 5000,
    title: str = "Service Unavailable",
    description: str = "Unable to connect to the backend service, trying to reconnect...",
):
    """Setup the offline detect plugin

    Args:
        interval (int, optional): Interval of detection in browser. Defaults to 5000.
        title (str, optional): Title of the overlay. Defaults to "Service Unavailable".
        description (str, optional): Description of the overlay. Defaults to "Unable to connect to the backend service, trying to reconnect...".
    """

    @hooks.index(final=True)
    def add_offline_detect(app_index: str):
        # Extract the first line of the footer part
        match = re.findall("[ ]+<footer>", app_index)

        if match:
            # Add the offline detect script
            app_index = app_index.replace(
                match[0],
                match[0]
                + """
<script type="application/javascript">
    // Track service status
    let isServiceDown = false;
    let overlayElement = null;

    // Create overlay element
    function createOverlay() {
        const overlay = document.createElement('div');
        overlay.style.position = 'fixed';
        overlay.style.top = '0';
        overlay.style.left = '0';
        overlay.style.width = '100%';
        overlay.style.height = '100%';
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.85)';
        overlay.style.zIndex = '2147483647'; // Highest possible z-index
        overlay.style.display = 'flex';
        overlay.style.justifyContent = 'center';
        overlay.style.alignItems = 'center';
        overlay.style.color = 'white';
        overlay.style.fontFamily = 'Arial, sans-serif';
        overlay.style.textAlign = 'center';
        overlay.style.backdropFilter = 'blur(5px)';
        
        const content = document.createElement('div');
        content.innerHTML = `
            <div style="max-width: 100%; padding: 20px;">
                <h2 style="font-size: 24px; margin-bottom: 16px;">__TITLE__</h2>
                <p style="font-size: 16px; margin-bottom: 20px;">
                    __DESCRIPTION__
                </p>
                <div style="display: inline-block; width: 40px; height: 40px; border: 4px solid rgba(255, 255, 255, 0.3); border-radius: 50%; border-top-color: white; animation: spin 1s linear infinite;"></div>
            </div>
            <style>
                @keyframes spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
            </style>
        `;
        
        overlay.appendChild(content);
        return overlay;
    }

    // Show overlay
    function showOverlay() {
        if (!overlayElement) {
            overlayElement = createOverlay();
            document.body.appendChild(overlayElement);
        }
    }

    // Hide overlay
    function hideOverlay() {
        if (overlayElement) {
            document.body.removeChild(overlayElement);
            overlayElement = null;
        }
    }

    // Check service status
    function checkServiceStatus() {
        fetch('/_offline-detect-ping', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Service unavailable');
            
            // Service is available
            if (isServiceDown) {
                isServiceDown = false;
                hideOverlay();
            }
        })
        .catch(error => {
            // Service is unavailable
            if (!isServiceDown) {
                isServiceDown = true;
                showOverlay();
            }
        });
    }

    // Initial check
    checkServiceStatus();
    
    // Poll service status every second
    setInterval(checkServiceStatus, __INTERVAL__);
</script>""".replace("__INTERVAL__", str(interval))
                .replace("__TITLE__", title)
                .replace("__DESCRIPTION__", description),
            )

        return app_index

    @hooks.route(methods=("POST",), name="_offline-detect-ping", final=True)
    def offline_detect_ping():
        """Ping endpoint for the offline detect plugin"""

        return jsonify({"status": "success", "timestamp": time.time()})

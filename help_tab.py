from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextBrowser
from PySide6.QtCore import Qt

class HelpTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        title = QLabel("Help & Instructions")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)
        
        text_browser = QTextBrowser()
        text_browser.setStyleSheet("background-color: transparent; border: none; font-size: 14px;")
        text_browser.setHtml("""
        <h3>How to Use AirClicker</h3>
        <ol>
            <li><b>Pair your AirPods (or Bluetooth headphones)</b> to this computer. Ensure they are connected in Settings.</li>
            <li>Go to the <b>Mappings</b> tab and configure what you want each tap to do. Usually, AirPods support Single/Double/Triple tap bindings which trigger Play/Next/Prev OS keys.</li>
            <li>Go to the <b>Dashboard</b> and click 'Start Listening'.</li>
            <li>Open your presentation (like PowerPoint).</li>
            <li>Tap your AirPods! The background listener will translate the tap into a simulated keystroke (like Right Arrow for Next Slide).</li>
        </ol>
        
        <h3>Troubleshooting</h3>
        <ul>
            <li><b>My taps are playing music instead of changing slides!</b> - Turn off or fully quit Spotify, Apple Music, and close browser tabs that might hijack media keys.</li>
            <li><b>macOS Users:</b> You need to grant AirClicker Accessibility permissions in System Preferences -> Security & Privacy -> Privacy -> Accessibility.</li>
            <li><b>No keys are pressed:</b> Validate the 'Mappings' config. Try mapping a key to 'White Screen' or another obvious action to test.</li>
        </ul>
        """)
        
        layout.addWidget(text_browser)

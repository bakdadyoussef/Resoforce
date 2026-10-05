from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QFormLayout
from PySide6.QtCore import Qt
from core.config import config

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(20)
        
        title = QLabel("Settings")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)
        
        form_layout = QFormLayout()
        
        # Minimize to Tray
        self.chk_min_tray = QCheckBox()
        self.chk_min_tray.setChecked(config.get_setting("minimize_to_tray"))
        self.chk_min_tray.stateChanged.connect(self.on_min_tray_changed)
        form_layout.addRow("Minimize to System Tray on Close:", self.chk_min_tray)
        
        # Run on Boot (Visual Only for now, integration needs OS specifics)
        self.chk_run_boot = QCheckBox()
        self.chk_run_boot.setChecked(config.get_setting("run_on_boot"))
        self.chk_run_boot.stateChanged.connect(self.on_run_boot_changed)
        form_layout.addRow("Run on System Boot:", self.chk_run_boot)
        
        layout.addLayout(form_layout)
        
        note = QLabel("Note: 'Run on Boot' implementation is placeholder. Full Windows Registry integration required.")
        note.setStyleSheet("color: #888; font-style: italic; font-size: 12px;")
        layout.addWidget(note)
        
        layout.addStretch()

    def on_min_tray_changed(self, state):
        config.set_setting("minimize_to_tray", state == Qt.Checked.value)

    def on_run_boot_changed(self, state):
        config.set_setting("run_on_boot", state == Qt.Checked.value)

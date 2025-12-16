# -*- coding: utf-8 -*-

###########################################################################
## Python code generated for PySide6 migration
## Converted from wxFormBuilder to PySide6
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QGridLayout, QLabel, QComboBox, QPushButton, 
                               QListWidget, QTextEdit, QLineEdit, QFrame,
                               QDialog, QRadioButton, QCheckBox, QDialogButtonBox)
from PySide6.QtCore import Signal

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow(QMainWindow):
    # Signals
    repositoryChanged = Signal()
    reloadRepositories = Signal()
    templateChanged = Signal()
    openRepository = Signal()
    submitIssue = Signal()
    resetUI = Signal()
    
    # Menu signals
    fileClose = Signal()
    extrasConfiguration = Signal()
    helpSupport = Signal()
    helpUpdate = Signal()
    helpAbout = Signal()
    themeToggle = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("GitHub Issue Client")
        self.resize(543, 378)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Create form layout
        form_layout = QGridLayout()
        
        # Repository section
        self.label_repositories = QLabel("Repository")
        self.combobox_repositories = QComboBox()
        self.button_reload_repositories = QPushButton("Reload")
        
        form_layout.addWidget(self.label_repositories, 0, 0)
        form_layout.addWidget(self.combobox_repositories, 0, 1)
        form_layout.addWidget(self.button_reload_repositories, 0, 2)
        
        # Labels section
        self.label_labels = QLabel("Labels")
        self.listbox_labels = QListWidget()
        self.listbox_labels.setSelectionMode(QListWidget.MultiSelection)
        
        form_layout.addWidget(self.label_labels, 1, 0)
        form_layout.addWidget(self.listbox_labels, 1, 1)
        
        # Milestones section
        self.label_milestones = QLabel("Milestones")
        self.combobox_milestones = QComboBox()
        
        form_layout.addWidget(self.label_milestones, 2, 0)
        form_layout.addWidget(self.combobox_milestones, 2, 1)
        
        # Assignees section
        self.label_assignees = QLabel("Assign to")
        self.combobox_assignees = QComboBox()
        
        form_layout.addWidget(self.label_assignees, 3, 0)
        form_layout.addWidget(self.combobox_assignees, 3, 1)
        
        # Templates section
        self.label_templates = QLabel("Templates")
        self.combobox_templates = QComboBox()
        
        form_layout.addWidget(self.label_templates, 4, 0)
        form_layout.addWidget(self.combobox_templates, 4, 1)
        
        # Separator
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        form_layout.addWidget(separator1, 5, 0, 1, 3)
        
        # Title section
        self.label_title = QLabel("Title")
        self.text_title = QLineEdit()
        
        form_layout.addWidget(self.label_title, 6, 0)
        form_layout.addWidget(self.text_title, 6, 1)
        
        # Content section
        self.label_content = QLabel("Content")
        self.text_content = QTextEdit()
        self.text_content.setMinimumHeight(300)
        
        form_layout.addWidget(self.label_content, 7, 0)
        form_layout.addWidget(self.text_content, 7, 1)
        
        # Separator
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        form_layout.addWidget(separator2, 8, 0, 1, 3)
        
        # Buttons section
        button_layout = QHBoxLayout()
        self.button_open_repository = QPushButton("Open Repository")
        self.button_submit_issue = QPushButton("Submit Issue")
        self.button_reset = QPushButton("Reset")
        
        button_layout.addWidget(self.button_open_repository)
        button_layout.addWidget(self.button_submit_issue)
        button_layout.addWidget(self.button_reset)
        
        form_layout.addLayout(button_layout, 9, 1)
        
        main_layout.addLayout(form_layout)
        
        # Connect signals
        self.combobox_repositories.currentTextChanged.connect(self.repositoryChanged)
        self.button_reload_repositories.clicked.connect(self.reloadRepositories)
        self.combobox_templates.currentTextChanged.connect(self.templateChanged)
        self.button_open_repository.clicked.connect(self.openRepository)
        self.button_submit_issue.clicked.connect(self.submitIssue)
        self.button_reset.clicked.connect(self.resetUI)
        
        # Create menu bar
        self.create_menu_bar()
    
    def create_menu_bar(self):
        import icons
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        close_action = file_menu.addAction(icons.get_icon('logout_24dp_8b1a10_fill0_wght400_grad0_opsz24'), "Close")
        close_action.triggered.connect(self.fileClose)
        
        # Extras menu
        extras_menu = menubar.addMenu("Extras")
        config_action = extras_menu.addAction(icons.get_icon('settings_24dp_8b1a10_fill0_wght400_grad0_opsz24'), "Configuration")
        config_action.triggered.connect(self.extrasConfiguration)
        
        extras_menu.addSeparator()
        theme_action = extras_menu.addAction("Toggle Dark/Light Theme")
        theme_action.triggered.connect(self.themeToggle)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        support_action = help_menu.addAction(icons.get_icon('globe_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'), "Support...")
        support_action.triggered.connect(self.helpSupport)
        
        update_action = help_menu.addAction(icons.get_icon('update_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'), "Check for updates")
        update_action.triggered.connect(self.helpUpdate)
        
        about_action = help_menu.addAction(icons.get_icon('info_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'), "About...")
        about_action.triggered.connect(self.helpAbout)

###########################################################################
## Class ConfigurationDialog
###########################################################################

class ConfigurationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configuration")
        self.setMinimumSize(500, 280)
        
        layout = QGridLayout(self)
        layout.setColumnStretch(1, 1)
        
        # Username
        self.label_username = QLabel("Username")
        self.text_username = QLineEdit()
        layout.addWidget(self.label_username, 0, 0)
        layout.addWidget(self.text_username, 0, 1, 1, 2)
        
        # Personal Access Token
        self.label_pat = QLabel("PersonalAccessToken")
        self.text_pat = QLineEdit()
        self.text_pat.setEchoMode(QLineEdit.Password)
        self.button_show_pat = QPushButton("Show")
        self.button_show_pat.setFixedWidth(60)
        self.button_test_pat = QPushButton("Test")
        self.button_test_pat.setFixedWidth(60)
        
        layout.addWidget(self.label_pat, 1, 0)
        layout.addWidget(self.text_pat, 1, 1)
        layout.addWidget(self.button_show_pat, 1, 2)
        layout.addWidget(self.button_test_pat, 1, 3)
        
        # Connect PAT buttons
        self.button_show_pat.clicked.connect(self.toggle_pat_visibility)
        self.button_test_pat.clicked.connect(self.test_pat)
        
        # GitHub.com radio button
        self.radio_github = QRadioButton("Github.com")
        self.radio_github.setChecked(True)
        layout.addWidget(self.radio_github, 2, 0, 1, 2)
        
        # GitHub Enterprise radio button
        self.radio_ghe = QRadioButton("GitHub Enterprise")
        layout.addWidget(self.radio_ghe, 3, 0, 1, 2)
        
        # GitHub Enterprise URL
        self.label_ghe_url = QLabel("GitHub Enterprise URL")
        self.text_ghe_url = QLineEdit()
        layout.addWidget(self.label_ghe_url, 4, 0)
        layout.addWidget(self.text_ghe_url, 4, 1, 1, 3)
        
        # Update check
        self.checkbox_update = QCheckBox("Check for updates on startup?")
        layout.addWidget(self.checkbox_update, 5, 0, 1, 4)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box, 6, 0, 1, 4)
    
    def toggle_pat_visibility(self):
        if self.text_pat.echoMode() == QLineEdit.Password:
            self.text_pat.setEchoMode(QLineEdit.Normal)
            self.button_show_pat.setText("Hide")
        else:
            self.text_pat.setEchoMode(QLineEdit.Password)
            self.button_show_pat.setText("Show")
    
    def test_pat(self):
        pass  # To be implemented in derived class

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About GitHub Issue Client")
        
        layout = QVBoxLayout(self)
        
        # Logo
        self.label_logo = QLabel()
        layout.addWidget(self.label_logo)
        
        # Name
        self.label_name = QLabel("MyLabel")
        layout.addWidget(self.label_name)
        
        # License
        self.label_license = QLabel("Licenced under")
        layout.addWidget(self.label_license)
        
        # GitHub link
        self.label_github = QLabel("More on GitHub")
        self.label_github.setStyleSheet("color: blue; text-decoration: underline;")
        self.label_github.mousePressEvent = self.open_github
        layout.addWidget(self.label_github)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
    
    def open_github(self, event):
        pass  # To be implemented in derived class

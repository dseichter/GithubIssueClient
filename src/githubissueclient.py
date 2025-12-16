# Copyright (c) 2024 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import sys
import webbrowser
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

import gui
import about_ui
import configuration_ui
import settings
import helper
import icons
import github_functions

class GitHubIssueClientFrame(gui.MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set window icon
        self.setWindowIcon(icons.get_icon('bug_report_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        
        # Set font for content text
        font = QFont("Courier", 10)
        self.text_content.setFont(font)
        
        # Connect signals
        self.repositoryChanged.connect(self.load_repository_data)
        self.reloadRepositories.connect(self.load_repositories)
        self.templateChanged.connect(self.load_issue_template)
        self.openRepository.connect(self.open_repository)
        self.submitIssue.connect(self.submit_issue)
        self.resetUI.connect(self.reset_ui)
        
        # Menu connections
        self.fileClose.connect(self.close)
        self.extrasConfiguration.connect(self.show_configuration)
        self.helpSupport.connect(self.show_support)
        self.helpUpdate.connect(self.check_update)
        self.helpAbout.connect(self.show_about)
        self.themeToggle.connect(self.toggle_theme)

    def showEvent(self, event):
        settings.create_config()
        self.setWindowTitle(f"{helper.NAME} {helper.VERSION}")
        
        config = settings.read_config()
        if not config['personal_access_token']:
            QMessageBox.critical(self, 'Missing Credentials', 
                               'Personal Access Token is required to use this application.\n\n'
                               'Please configure your GitHub credentials.')
            self.show_configuration()
            return
        
        # Test PAT validity
        try:
            github_functions.check_pat(config['personal_access_token'], config['use_github'], config['ghe_url'])
        except Exception:
            QMessageBox.critical(self, 'Invalid Credentials', 
                               'Your Personal Access Token appears to be invalid.\n\n'
                               'Please check your configuration.')
            self.show_configuration()
            return
        
        self.load_repositories()
        
        if settings.read_config()['update_check']:
            if helper.check_for_new_release():
                reply = QMessageBox.question(self, 'Update available',
                                           'A new release is available.\nWould you like to open the download page?')
                if reply == QMessageBox.Yes:
                    webbrowser.open_new_tab(helper.RELEASES)

    def show_configuration(self):
        dlg = configuration_ui.DialogConfiguration(self)
        dlg.exec()

    def show_support(self):
        webbrowser.open_new_tab('https://github.com/dseichter/GithubIssueClient')

    def check_update(self):
        if helper.check_for_new_release():
            reply = QMessageBox.question(self, 'Update available',
                                       'A new release is available.\nWould you like to open the download page?')
            if reply == QMessageBox.Yes:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            QMessageBox.information(self, 'No update', 'No new release available.')

    def show_about(self):
        dlg = about_ui.DialogAbout(self)
        dlg.exec()

    def load_repositories(self):
        self.combobox_repositories.clear()
        try:
            repos = github_functions.get_repos()
            for repo in repos:
                self.combobox_repositories.addItem(repo.full_name)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load repositories: {str(e)}')

    def load_repository_data(self):
        repo = self.combobox_repositories.currentText()
        if not repo:
            return
            
        try:
            # Load labels
            labels = github_functions.get_labels(repo)
            self.listbox_labels.clear()
            for label in labels:
                self.listbox_labels.addItem(label.name)
                
            # Load milestones
            self.combobox_milestones.clear()
            milestones = github_functions.get_milestones(repo)
            for milestone in milestones:
                self.combobox_milestones.addItem(milestone.title)
                
            # Load assignees
            self.combobox_assignees.clear()
            assignees = github_functions.get_assignees(repo)
            for assignee in assignees:
                self.combobox_assignees.addItem(assignee.name)
                
            # Load templates
            self.combobox_templates.clear()
            templates = github_functions.get_issue_templates(repo)
            for template in templates:
                self.combobox_templates.addItem(template)
        except Exception as e:
            QMessageBox.warning(self, 'Warning', f'Failed to load repository data: {str(e)}')

    def load_issue_template(self):
        template = self.combobox_templates.currentText()
        repo = self.combobox_repositories.currentText()
        if template and repo:
            try:
                content = github_functions.get_issue_template(repo, template)
                self.text_content.setPlainText(content)
            except Exception as e:
                QMessageBox.warning(self, 'Warning', f'Failed to load template: {str(e)}')

    def open_repository(self):
        try:
            repo = github_functions.get_repo(self.combobox_repositories.currentText())
            webbrowser.open_new_tab(repo.html_url)
        except Exception as e:
            QMessageBox.warning(self, 'Warning', f'Failed to open repository: {str(e)}')

    def submit_issue(self):
        reponame = self.combobox_repositories.currentText()
        title = self.text_title.text()
        content = self.text_content.toPlainText()
        assignee = self.combobox_assignees.currentText() or None
        milestone = self.combobox_milestones.currentText() or None
        
        labels = []
        for i in range(self.listbox_labels.count()):
            item = self.listbox_labels.item(i)
            if item.isSelected():
                labels.append(item.text())
        
        if not title or not content:
            QMessageBox.critical(self, 'Error', 'Title and content are mandatory.')
            return
        
        reply = QMessageBox.question(self, 'Confirmation', 
                                   'Do you really want to create the issue?')
        if reply != QMessageBox.Yes:
            return
        
        try:
            issue = github_functions.create_issue(repo=reponame, title=title, body=content, 
                                                labels=labels, assignee=assignee, milestone=milestone)
            
            if issue:
                QMessageBox.information(self, 'Success', 
                                      f'Issue {issue.number} created successfully.')
            else:
                QMessageBox.critical(self, 'Error', 'Error creating issue.')
            self.reset_ui()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to create issue: {str(e)}')

    def reset_ui(self):
        self.load_repository_data()
        self.text_title.clear()
        self.text_content.clear()
    
    def toggle_theme(self):
        app = QApplication.instance()
        current_style = app.styleSheet()
        
        if "background-color: #2b2b2b" in current_style:
            # Switch to light theme
            app.setStyleSheet("")
        else:
            # Switch to dark theme
            dark_style = """
            QMainWindow, QDialog {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QLineEdit, QTextEdit, QComboBox, QListWidget {
                background-color: #3c3c3c;
                color: #ffffff;
                border: 1px solid #555555;
            }
            QPushButton {
                background-color: #404040;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QMenuBar {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QMenuBar::item:selected {
                background-color: #404040;
            }
            QMenu {
                background-color: #2b2b2b;
                color: #ffffff;
                border: 1px solid #555555;
            }
            QMenu::item:selected {
                background-color: #404040;
            }
            """
            app.setStyleSheet(dark_style)


def main():
    app = QApplication(sys.argv)
    frame = GitHubIssueClientFrame()
    frame.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
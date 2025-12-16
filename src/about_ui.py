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

import webbrowser
from gui import AboutDialog
import helper
import icons


class DialogAbout(AboutDialog):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.label_name.setText(f"{helper.NAME} {helper.VERSION}")
        self.label_license.setText(f"Licenced under {helper.LICENCE}")
        
        self.setWindowIcon(icons.info_icon())
        self.label_logo.setPixmap(icons.github_pixmap())
        self.adjustSize()

    def open_github(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/GithubIssueClient')

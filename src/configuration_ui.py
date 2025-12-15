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

from gui import ConfigurationDialog
import settings
import icons


class DialogConfiguration(ConfigurationDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowIcon(icons.get_icon('settings_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))

    def showEvent(self, event):
        config = settings.read_config()
        self.text_username.setText(config['username'])
        self.text_pat.setText(config['personal_access_token'])
        self.radio_github.setChecked(config['use_github'])
        self.radio_ghe.setChecked(not config['use_github'])
        self.text_ghe_url.setText(config['ghe_url'])
        self.checkbox_update.setChecked(config['update_check'])

    def accept(self):
        settings.save_config('username', self.text_username.text())
        settings.save_config('personal_access_token', self.text_pat.text())
        settings.save_config('use_github', self.radio_github.isChecked())
        settings.save_config('use_ghe', self.radio_ghe.isChecked())
        settings.save_config('ghe_url', self.text_ghe_url.text())
        settings.save_config('update_check', self.checkbox_update.isChecked())
        super().accept()
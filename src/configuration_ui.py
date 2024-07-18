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

# importing wx files
import wx
# import the newly created GUI file
import gui

# import workdir specific libraries
import settings
import icons


class DialogConfiguration(gui.dialogConfiguration):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogConfiguration.__init__(self, parent)

        # specify all the icons
        gui.dialogAbout.SetIcon(self, icons.settings.GetIcon())

    def showConfig(self, event):
        # get the config
        config = settings.read_config()
        # set the values
        self.textUsername.SetValue(config['username'])
        self.textPAT.SetValue(config['personal_access_token'])
        self.radiobuttonGitHub.SetValue(config['use_github'])
        self.radiobuttonGHE.SetValue(not config['use_github'])
        self.textGHEURL.SetValue(config['ghe_url'])
        self.checkboxUpdate.SetValue(config['update_check'])

        self.Layout()
        self.Fit()

    def saveConfig(self, event):
        # save the config
        settings.save_config('username', self.textUsername.GetValue())
        settings.save_config('personal_access_token', self.textPAT.GetValue())
        settings.save_config('use_github', self.radiobuttonGitHub.GetValue())
        settings.save_config('use_ghe', self.radiobuttonGHE.GetValue())
        settings.save_config('ghe_url', self.textGHEURL.GetValue())
        settings.save_config('update_check', self.checkboxUpdate.GetValue())
        # close the dialog
        self.Close()

    def closeConfig(self, event):
        self.Close()

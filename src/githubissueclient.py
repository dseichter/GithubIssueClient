# importing wx files
import wx
# import the newly created GUI file
import gui
# import common libraries
import webbrowser

# import workdir specific libraries
import about_ui
import configuration_ui
import settings
import helper
import icons
import github_functions


class GitHubIssueClientFrame(gui.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.MainFrame.__init__(self, parent)

        # specify all the icons
        gui.MainFrame.SetIcon(self, icons.github.GetIcon())
        self.menuitemFileClose.SetBitmap(icons.cancel.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemExtrasConfiguration.SetBitmap(icons.settings.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpSupport.SetBitmap(icons.get_help.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpUpdate.SetBitmap(icons.restart.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpAbout.SetBitmap(icons.info.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())

    def gicClose(self, event):
        self.Close()

    def gicShow(self, event):
        # check if config.json exists, if not create it, if available, update it
        settings.create_config()

        # add the version to the label
        self.SetTitle(helper.NAME + ' ' + helper.VERSION)

    def miFileClose(self, event):
        self.Close()

    def miExtrasConfiguration(self, event):
        # open the configuration dialog
        dlg = configuration_ui.DialogConfiguration(self)
        dlg.ShowModal()
        dlg.Destroy()

    def miHelpSupport(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/GithubIssueClient')  # Add the URL of the GitHub repository

    def miHelpUpdate(self, event):
        if helper.check_for_new_release():
            result = wx.MessageBox('A new release is available.\nWould you like to open the download page?', 'Update available', wx.YES_NO | wx.ICON_INFORMATION)
            if result == wx.YES:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            wx.MessageBox('No new release available.', 'No update', wx.OK | wx.ICON_INFORMATION)

    def miHelpAbout(self, event):
        # open the about dialog
        dlg = about_ui.DialogAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

    def loadRepositories(self, event):
        # TODO: implement me
        github_functions.get_repos()
        event.Skip()

    def loadRepositoryData(self, event):
        # load the labels
        # load the milestones
        # load assignees
        event.Skip()

    def openRepository(self, event):
        # TODO: implement me
        event.Skip()

    def submitIssue(self, event):
        # TODO: implement me
        event.Skip()


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = GitHubIssueClientFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()
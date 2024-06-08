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

        self.Layout()
        self.Fit()

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
        self.comboboxRepositories.Clear()
        repos = github_functions.get_repos()
        for repo in repos:
            self.comboboxRepositories.Append(repo.full_name)
            print(repo.full_name)

    def loadRepositoryData(self, event):
        repo = self.comboboxRepositories.GetValue()
        # load the labels
        labels = github_functions.get_labels(repo)
        self.listboxLabels.Clear()
        for v in labels:
            self.listboxLabels.Append(v.name)
        # load the milestones
        self.comboboxMilestones.Clear()
        milestones = github_functions.get_milestones(repo)
        for milestone in milestones:
            self.comboboxMilestones.Append(milestone.title)
        # load assignees
        self.comboboxAssignees.Clear()
        assignees = github_functions.get_assignees(repo)
        for assignee in assignees:
            self.comboboxAssignees.Append(assignee.name)

    def openRepository(self, event):
        repo = github_functions.get_repo(self.comboboxRepositories.GetValue())
        webbrowser.open_new_tab(repo.html_url)  # Add the URL of the GitHub repository

    def submitIssue(self, event):
        reponame = self.comboboxRepositories.GetValue()
        title = self.textIssueTitle.GetValue()
        content = self.textIssueContent.GetValue()
        assignee = self.comboboxAssignees.GetValue()
        assignee = assignee if assignee != '' else "NotSet"
        milestone = self.comboboxMilestones.GetValue()
        milestone = milestone if milestone != '' else None

        labels = []
        for i in range(self.listboxLabels.GetCount()):
            if self.listboxLabels.IsSelected(i):
                labels.append(self.listboxLabels.GetString(i))

        # ask for confirmation
        result = wx.MessageBox('Do you really want to create the issue?', 'Confirmation', wx.YES_NO | wx.ICON_QUESTION)
        if result == wx.NO:
            return

        # create the issue
        issue = github_functions.create_issue(repo=reponame, title=title, body=content, labels=labels, assignee=assignee, milestone=milestone)

        # check if issue is created
        if issue:
            wx.MessageBox('Issue ' + issue.id + ' created successfully.', 'Success', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('Error creating issue.', 'Error', wx.OK | wx.ICON_ERROR)
        self.resetUI(event)

    def resetUI(self, event):
        self.loadRepositoryData(event)
        self.textIssueTitle.SetValue('')
        self.textIssueContent.SetValue('')


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = GitHubIssueClientFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()

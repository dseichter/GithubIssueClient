# -*- coding: utf-8 -*-

# #########################################################################
# # Python code generated with wxFormBuilder (version 4.1.0-69d57cd9)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
# #########################################################################

import wx
import wx.xrc

ID_CLOSE = 1000
ID_CONFIGURATION = 1001
ID_ABOUT = 1002


# #########################################################################
# # Class MainFrame
# #########################################################################


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"GitHub Issue Client", pos=wx.DefaultPosition, size=wx.Size(543, 378), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.menuitemFile = wx.Menu()
        self.menuitemFileClose = wx.MenuItem(self.menuitemFile, ID_CLOSE, u"Close", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemFile.Append(self.menuitemFileClose)

        self.m_menubar1.Append(self.menuitemFile, u"File")

        self.menuItemExtras = wx.Menu()
        self.menuitemExtrasConfiguration = wx.MenuItem(self.menuItemExtras, ID_CONFIGURATION, u"Configuration", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuItemExtras.Append(self.menuitemExtrasConfiguration)

        self.m_menubar1.Append(self.menuItemExtras, u"Extras")

        self.menuitemHelp = wx.Menu()
        self.menuitemHelpAbout = wx.MenuItem(self.menuitemHelp, ID_ABOUT, u"About", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpAbout)

        self.m_menubar1.Append(self.menuitemHelp, u"Help")

        self.SetMenuBar(self.m_menubar1)

        fgSizer1 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.statictextRepositories = wx.StaticText(self, wx.ID_ANY, u"Repository", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextRepositories.Wrap(-1)

        fgSizer1.Add(self.statictextRepositories, 0, wx.ALL, 5)
        comboboxRepositoriesChoices = []
        self.comboboxRepositories = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboboxRepositoriesChoices, 0)
        fgSizer1.Add(self.comboboxRepositories, 1, wx.ALL | wx.EXPAND, 5)
        self.buttonReloadRepositories = wx.Button(self, wx.ID_ANY, u"Reload", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.buttonReloadRepositories, 1, wx.ALL, 5)
        self.statictextLabels = wx.StaticText(self, wx.ID_ANY, u"Labels", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextLabels.Wrap(-1)

        fgSizer1.Add(self.statictextLabels, 0, wx.ALL, 5)
        listboxLabelsChoices = []
        self.listboxLabels = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listboxLabelsChoices, 0)
        fgSizer1.Add(self.listboxLabels, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextMilestones = wx.StaticText(self, wx.ID_ANY, u"Milestones", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextMilestones.Wrap(-1)

        fgSizer1.Add(self.statictextMilestones, 0, wx.ALL, 5)
        comboboxMilestonesChoices = []
        self.comboboxMilestones = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboboxMilestonesChoices, 0)
        fgSizer1.Add(self.comboboxMilestones, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextAssignees = wx.StaticText(self, wx.ID_ANY, u"Assign to", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextAssignees.Wrap(-1)

        fgSizer1.Add(self.statictextAssignees, 0, wx.ALL, 5)
        comboboxAssigneesChoices = []
        self.comboboxAssignees = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboboxAssigneesChoices, 0)
        fgSizer1.Add(self.comboboxAssignees, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        fgSizer1.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextIssueTitle = wx.StaticText(self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextIssueTitle.Wrap(-1)

        fgSizer1.Add(self.statictextIssueTitle, 0, wx.ALL, 5)
        self.textIssueTitle = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.textIssueTitle, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextIssueContent = wx.StaticText(self, wx.ID_ANY, u"Content", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextIssueContent.Wrap(-1)

        fgSizer1.Add(self.statictextIssueContent, 0, wx.ALL, 5)
        self.textIssueContent = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP | wx.TE_MULTILINE)
        fgSizer1.Add(self.textIssueContent, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        fgSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.buttonOpenRepository = wx.Button(self, wx.ID_ANY, u"Open Repository", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonOpenRepository, 1, wx.ALL, 5)
        self.buttonSubmitIssue = wx.Button(self, wx.ID_ANY, u"Submit Issue", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonSubmitIssue, 1, wx.ALL | wx.EXPAND, 5)
        fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)
        self.SetSizer(fgSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.menuitemFileClose, id=self.menuitemFileClose.GetId())
        self.Bind(wx.EVT_MENU, self.menuitemExtrasConfiguration, id=self.menuitemExtrasConfiguration.GetId())
        self.Bind(wx.EVT_MENU, self.menuitemHelpAbout, id=self.menuitemHelpAbout.GetId())
        self.buttonReloadRepositories.Bind(wx.EVT_BUTTON, self.loadRepositories)
        self.buttonOpenRepository.Bind(wx.EVT_BUTTON, self.openRepository)
        self.buttonSubmitIssue.Bind(wx.EVT_BUTTON, self.submitIssue)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def menuitemFileClose(self, event):
        event.Skip()

    def menuitemExtrasConfiguration(self, event):
        event.Skip()

    def menuitemHelpAbout(self, event):
        event.Skip()

    def loadRepositories(self, event):
        event.Skip()

    def openRepository(self, event):
        event.Skip()

    def submitIssue(self, event):
        event.Skip()

# #########################################################################
# # Class dialogConfiguration
# #########################################################################


class dialogConfiguration(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Configuration", pos=wx.DefaultPosition, size=wx.Size(381, 235), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.statictextUsername = wx.StaticText(self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextUsername.Wrap(-1)

        fgSizer3.Add(self.statictextUsername, 0, wx.ALL, 5)
        self.textUsername = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.textUsername, 0, wx.ALL, 5)
        self.statictextPAT = wx.StaticText(self, wx.ID_ANY, u"PersonalAccessToken", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextPAT.Wrap(-1)

        fgSizer3.Add(self.statictextPAT, 0, wx.ALL, 5)
        self.textPAT = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.textPAT, 0, wx.ALL, 5)
        self.radiobuttonGitHub = wx.RadioButton(self, wx.ID_ANY, u"Github.com", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        fgSizer3.Add(self.radiobuttonGitHub, 0, wx.ALL, 5)

        fgSizer3.Add((0, 0), 1, wx.EXPAND, 5)
        self.radiobuttonGHE = wx.RadioButton(self, wx.ID_ANY, u"GitHub Enterprise", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.radiobuttonGHE, 0, wx.ALL, 5)

        fgSizer3.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextGHEUrl = wx.StaticText(self, wx.ID_ANY, u"GitHub Enterprise URL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextGHEUrl.Wrap(-1)

        fgSizer3.Add(self.statictextGHEUrl, 0, wx.ALL, 5)
        self.textGHEURL = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.textGHEURL, 0, wx.ALL, 5)

        fgSizer3.Add((0, 0), 1, wx.EXPAND, 5)
        self.checkboxUpdate = wx.CheckBox(self, wx.ID_ANY, u"Check for updates on startup?", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.checkboxUpdate, 0, wx.ALL, 5)
        self.SetSizer(fgSizer3)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass

# #########################################################################
# # Class dialogAbout
# #########################################################################


class dialogAbout(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About GitHub Issue Client", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

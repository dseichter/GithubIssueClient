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
ID_GET_HELP = 1002
ID_CHECK_FOR_UPDATES = 1003
ID_ABOUT = 1004


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
        self.menuitemHelpSupport = wx.MenuItem(self.menuitemHelp, ID_GET_HELP, u"Support...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpSupport)

        self.menuitemHelpUpdate = wx.MenuItem(self.menuitemHelp, ID_CHECK_FOR_UPDATES, u"Check for updates", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpUpdate)

        self.menuitemHelpAbout = wx.MenuItem(self.menuitemHelp, ID_ABOUT, u"About...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpAbout)

        self.m_menubar1.Append(self.menuitemHelp, u"Help")

        self.SetMenuBar(self.m_menubar1)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer2.SetMinSize(wx.Size(500, 500))
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer4 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer4.AddGrowableCol(1)
        fgSizer4.AddGrowableRow(6)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.statictextRepositories = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Repository", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextRepositories.Wrap(-1)

        fgSizer4.Add(self.statictextRepositories, 0, wx.ALL, 5)
        comboboxRepositoriesChoices = []
        self.comboboxRepositories = wx.ComboBox(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboboxRepositoriesChoices, 0)
        fgSizer4.Add(self.comboboxRepositories, 1, wx.ALL | wx.EXPAND, 5)
        self.buttonReloadRepositories = wx.Button(self.m_panel1, wx.ID_ANY, u"Reload", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer4.Add(self.buttonReloadRepositories, 1, wx.ALL, 5)
        self.statictextLabels = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Labels", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextLabels.Wrap(-1)

        fgSizer4.Add(self.statictextLabels, 0, wx.ALL, 5)
        listboxLabelsChoices = []
        self.listboxLabels = wx.ListBox(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listboxLabelsChoices, wx.LB_MULTIPLE | wx.LB_SORT)
        fgSizer4.Add(self.listboxLabels, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextMilestones = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Milestones", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextMilestones.Wrap(-1)

        fgSizer4.Add(self.statictextMilestones, 0, wx.ALL, 5)
        comboboxMilestonesChoices = []
        self.comboboxMilestones = wx.ComboBox(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboboxMilestonesChoices, 0)
        fgSizer4.Add(self.comboboxMilestones, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextAssignees = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Assign to", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextAssignees.Wrap(-1)

        fgSizer4.Add(self.statictextAssignees, 0, wx.ALL, 5)
        comboboxAssigneesChoices = []
        self.comboboxAssignees = wx.ComboBox(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboboxAssigneesChoices, 0)
        fgSizer4.Add(self.comboboxAssignees, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_staticline2 = wx.StaticLine(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        fgSizer4.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextIssueTitle = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextIssueTitle.Wrap(-1)

        fgSizer4.Add(self.statictextIssueTitle, 0, wx.ALL, 5)
        self.textIssueTitle = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer4.Add(self.textIssueTitle, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        self.statictextIssueContent = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Content", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextIssueContent.Wrap(-1)

        fgSizer4.Add(self.statictextIssueContent, 0, wx.ALL, 5)
        self.textIssueContent = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP | wx.TE_MULTILINE)
        self.textIssueContent.SetMinSize(wx.Size(-1, 300))

        fgSizer4.Add(self.textIssueContent, 1, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_staticline1 = wx.StaticLine(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        fgSizer4.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_panel2 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.buttonOpenRepository = wx.Button(self.m_panel2, wx.ID_ANY, u"Open Repository", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonOpenRepository, 1, wx.ALL, 5)
        self.buttonSubmitIssue = wx.Button(self.m_panel2, wx.ID_ANY, u"Submit Issue", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonSubmitIssue, 1, wx.ALL, 5)
        self.buttonReset = wx.Button(self.m_panel2, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.buttonReset, 0, wx.ALL, 5)
        self.m_panel2.SetSizer(fgSizer2)
        self.m_panel2.Layout()
        fgSizer2.Fit(self.m_panel2)
        fgSizer4.Add(self.m_panel2, 1, wx.ALL, 5)
        self.m_panel1.SetSizer(fgSizer4)
        self.m_panel1.Layout()
        fgSizer4.Fit(self.m_panel1)
        bSizer2.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(bSizer2)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.gicClose)
        self.Bind(wx.EVT_SHOW, self.gicShow)
        self.Bind(wx.EVT_MENU, self.miFileClose, id=self.menuitemFileClose.GetId())
        self.Bind(wx.EVT_MENU, self.miExtrasConfiguration, id=self.menuitemExtrasConfiguration.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpSupport, id=self.menuitemHelpSupport.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpUpdate, id=self.menuitemHelpUpdate.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpAbout, id=self.menuitemHelpAbout.GetId())
        self.comboboxRepositories.Bind(wx.EVT_COMBOBOX, self.loadRepositoryData)
        self.buttonReloadRepositories.Bind(wx.EVT_BUTTON, self.loadRepositories)
        self.buttonOpenRepository.Bind(wx.EVT_BUTTON, self.openRepository)
        self.buttonSubmitIssue.Bind(wx.EVT_BUTTON, self.submitIssue)
        self.buttonReset.Bind(wx.EVT_BUTTON, self.resetUI)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def gicClose(self, event):
        event.Skip()

    def gicShow(self, event):
        event.Skip()

    def miFileClose(self, event):
        event.Skip()

    def miExtrasConfiguration(self, event):
        event.Skip()

    def miHelpSupport(self, event):
        event.Skip()

    def miHelpUpdate(self, event):
        event.Skip()

    def miHelpAbout(self, event):
        event.Skip()

    def loadRepositoryData(self, event):
        event.Skip()

    def loadRepositories(self, event):
        event.Skip()

    def openRepository(self, event):
        event.Skip()

    def submitIssue(self, event):
        event.Skip()

    def resetUI(self, event):
        event.Skip()

# #########################################################################
# # Class dialogConfiguration
# #########################################################################


class dialogConfiguration(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Configuration", pos=wx.DefaultPosition, size=wx.Size(400, 248), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.Size(400, -1), wx.DefaultSize)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3.SetMinSize(wx.Size(300, -1))
        self.statictextUsername = wx.StaticText(self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextUsername.Wrap(-1)

        fgSizer3.Add(self.statictextUsername, 0, wx.ALL, 5)
        self.textUsername = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.textUsername, 0, wx.ALL, 5)
        self.statictextPAT = wx.StaticText(self, wx.ID_ANY, u"PersonalAccessToken", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statictextPAT.Wrap(-1)

        fgSizer3.Add(self.statictextPAT, 0, wx.ALL, 5)
        self.textPAT = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textPAT.SetMinSize(wx.Size(400, -1))

        fgSizer3.Add(self.textPAT, 0, wx.ALL | wx.EXPAND, 5)
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
        self.textGHEURL.SetMinSize(wx.Size(400, -1))

        fgSizer3.Add(self.textGHEURL, 0, wx.ALL | wx.EXPAND, 5)

        fgSizer3.Add((0, 0), 1, wx.EXPAND, 5)
        self.checkboxUpdate = wx.CheckBox(self, wx.ID_ANY, u"Check for updates on startup?", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.checkboxUpdate, 0, wx.ALL, 5)

        fgSizer3.Add((0, 0), 1, wx.EXPAND, 5)
        fgSizer6 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.buttonSave = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.buttonSave, 0, wx.ALL, 5)
        self.buttonCancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.buttonCancel, 0, wx.ALL, 5)
        fgSizer3.Add(fgSizer6, 1, wx.EXPAND, 5)
        self.SetSizer(fgSizer3)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SHOW, self.showConfig)
        self.buttonSave.Bind(wx.EVT_BUTTON, self.saveConfig)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.closeConfig)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def showConfig(self, event):
        event.Skip()

    def saveConfig(self, event):
        event.Skip()

    def closeConfig(self, event):
        event.Skip()

# #########################################################################
# # Class dialogAbout
# #########################################################################


class dialogAbout(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About GitHub Issue Client", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.bitmapLogo = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.bitmapLogo, 0, wx.ALL, 5)
        self.staticTextName = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextName.Wrap(-1)

        bSizer2.Add(self.staticTextName, 0, wx.ALL, 5)
        self.staticTextLicence = wx.StaticText(self, wx.ID_ANY, u"Licenced under", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextLicence.Wrap(-1)

        bSizer2.Add(self.staticTextLicence, 0, wx.ALL, 5)
        self.staticTextGithub = wx.StaticText(self, wx.ID_ANY, u"More on GitHub", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextGithub.Wrap(-1)

        self.staticTextGithub.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString))
        self.staticTextGithub.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer2.Add(self.staticTextGithub, 0, wx.ALL, 5)
        self.staticTextIcon8 = wx.StaticText(self, wx.ID_ANY, u"Icons by Icons8.com", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextIcon8.Wrap(-1)

        self.staticTextIcon8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))

        bSizer2.Add(self.staticTextIcon8, 0, wx.ALL, 5)
        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
        self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()
        bSizer2.Add(m_sdbSizer2, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer2)
        self.Layout()
        bSizer2.Fit(self)
        self.Centre(wx.BOTH)

        # Connect Events
        self.staticTextGithub.Bind(wx.EVT_LEFT_DOWN, self.openGithub)
        self.staticTextIcon8.Bind(wx.EVT_LEFT_DOWN, self.openIcons8)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def openGithub(self, event):
        event.Skip()

    def openIcons8(self, event):
        event.Skip()

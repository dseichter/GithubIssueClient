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

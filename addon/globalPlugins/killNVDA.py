# Copyright 2019 Tyler Spivey <tspivey@pcdesk.net>
# GPL V2
import subprocess
import wx
import gui
import globalPluginHandler

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.kill_item = self.menu.Append(wx.ID_ANY, "&Kill NVDA")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.do_kill, self.kill_item)

	def terminate(self):
		self.menu.Remove(self.kill_item.Id)
		self.kill_item.Destroy()
		self.kill_item = None

	def do_kill(self, evt):
		subprocess.call(['taskkill', '/f', '/im', 'nvda.exe'], shell=True)

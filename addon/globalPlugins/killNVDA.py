# Copyright 2019 Tyler Spivey <tspivey@pcdesk.net>
# GPL V2
import os
from ctypes import *
from ctypes.wintypes import *
import wx
import gui
import globalPluginHandler
import comtypes.client

PROCESS_TERMINATE = 0x0001

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
		our_pid = os.getpid()
		kernel32 = windll.kernel32

		comtypes.CoInitialize()
		try:
			wmi = comtypes.client.CoGetObject("winmgmts:")
			processes = wmi.ExecQuery("SELECT ProcessId, Name, CommandLine FROM Win32_Process WHERE Name = 'nvda.exe' OR Name = 'python.exe' OR Name = 'pythonw.exe'")

			for process in processes:
				pid = process.ProcessId
				if pid == our_pid:
					continue

				name = process.Name.lower()
				if name == 'nvda.exe':
					h = kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
					if h != 0:
						try:
							kernel32.TerminateProcess(h, 1)
						finally:
							kernel32.CloseHandle(h)
				elif name in ('python.exe', 'pythonw.exe'):
					cmdline = process.CommandLine
					if cmdline and 'nvda.pyw' in cmdline.lower():
						h = kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
						if h != 0:
							try:
								kernel32.TerminateProcess(h, 1)
							finally:
								kernel32.CloseHandle(h)
		finally:
			comtypes.CoUninitialize()

		# Terminate our process
		h = kernel32.OpenProcess(PROCESS_TERMINATE, False, our_pid)
		if h != 0:
			try:
				kernel32.TerminateProcess(h, 1)
			finally:
				kernel32.CloseHandle(h)

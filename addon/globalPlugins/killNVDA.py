# Copyright 2019 Tyler Spivey <tspivey@pcdesk.net>
# GPL V2
import os
from ctypes import *
from ctypes.wintypes import *
import subprocess
import wx
import gui
import globalPluginHandler

PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
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
		dll = windll.psapi
		kernel32 = windll.kernel32
		dll.EnumProcesses.argtypes = (POINTER(DWORD), DWORD, POINTER(DWORD))
		nprocs = 512
		cbNeeded = DWORD()
		while True:
			procs = (DWORD * nprocs)()
			res = dll.EnumProcesses(procs, sizeof(procs), cbNeeded)
			if res != 1:
				raise RuntimeError("EnumProcesses: %d" % res)
			if cbNeeded.value == sizeof(procs):
				nprocs *= 2
			else:
				break
		n = cbNeeded.value // sizeof(DWORD)
		procs=  list(procs)[:n]
		our_pid = os.getpid()
		buf = create_unicode_buffer(512)
		size = DWORD()
		for proc in procs:
			size.value = 512
			if proc == our_pid:
				continue
			h = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION | PROCESS_TERMINATE, False, proc)
			if h == 0:
				continue
			res = kernel32.QueryFullProcessImageNameW(h, 0, byref(buf), byref(size))
			if res == 0:
				kernel32.CloseHandle(h)
				continue
			if buf.value.lower().endswith(r'\nvda.exe'):
				kernel32.TerminateProcess(h, 1)
			kernel32.CloseHandle(h)
		# Terminate our process
		h = kernel32.OpenProcess(PROCESS_TERMINATE, False, our_pid)
		if h != 0:
			kernel32.TerminateProcess(h, 1)
			kernel32.CloseHandle(h)

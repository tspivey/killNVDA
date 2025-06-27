# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guidelines.txt
	# add-on Name, internal for nvda
	"addon_name" : "killNVDA",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Kill NVDA"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""Kills NVDA.
"""),
	# version
	"addon_version" : "0.6.0",
	# Author(s)
	"addon_author" : u"Tyler Spivey <tspivey@pcdesk.net>",
	# URL for the add-on documentation support
	"addon_url" : None,
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion" : "2019.2.0",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2025.1.0",
	# Add-on update channel (default is None, denoting stable releases, and for development releases, use "dev"; do not change unless you know what you are doing)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ['addon/globalPlugins/*.py']

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
# You must also edit .gitignore file to specify base language files to be ignored.
baseLanguage = "en"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions = []

# Custom braille translation tables
# If your add-on includes custom braille tables (most will not), fill out this dictionary.
# Each key is a dictionary named according to braille table file name,
# with keys inside recording the following attributes:
# displayName (name of the table shown to users and translatable),
# contracted (contracted (True) or uncontracted (False) braille code),
# output (shown in output table list),
# input (shown in input table list).
brailleTables = {}

# Custom speech symbol dictionaries
# Symbol dictionary files reside in the locale folder, e.g. `locale\en`, and are named `symbols-<name>.dic`.
# If your add-on includes custom speech symbol dictionaries (most will not), fill out this dictionary.
# Each key is the name of the dictionary,
# with keys inside recording the following attributes:
# displayName (name of the speech dictionary  shown to users and translatable),
# mandatory (True when always enabled, False when not.
symbolDictionaries = {}

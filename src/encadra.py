# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# Copyright (C) 2020 Daniel Muñiz Fontoira
# Author: Daniel Muñiz Fontoira (2020) <dani@damufo.com>

import sys
from pathlib import Path
import wx
import locale
import gettext
from classes.wxp.view_plus import ViewPlus
from specific_classes.app_icon import encadra
from specific_classes.config import Config
from modules.main.p_main import Presenter


class Encadra(wx.App):

    def OnInit(self):
        app_path_folder = Path(__file__).parent.absolute()
        self.translate(app_path_folder)
        self.name = "Encadra-{}".format(wx.GetUserId())

        arg1 = None
        if len(sys.argv) > 1:
            arg1 = sys.argv[1]
        config = Config(app_path_folder=app_path_folder, arg1=arg1)
        
        ViewPlus.prefs = config.prefs
        ViewPlus.app_icon = encadra.GetIcon()

        Presenter(config=config)
        return True

    def translate(self, app_path_folder):
        has_translations = False
        app_path_folder_locale = app_path_folder / 'locale'
        localedirs = (app_path_folder_locale, '~/.local/share/locale', None)
        for i in localedirs:
            if gettext.find('encadra', i):
                has_translations = True
                gettext.install(domain='encadra', localedir=i)
                break
        if not has_translations:
            trans = gettext.NullTranslations()
            trans.install()

try:
    app = Encadra()
    app.MainLoop()
except SystemExit:
    sys.exit(0)

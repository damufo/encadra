# -*- coding: utf-8 -*-


import codecs
from pathlib import Path
import json
from .prefs import Prefs


class Config(object):

    def __init__(self, app_path_folder, arg1):

        self.app_name = 'Encadra'
        self.app_version = "0.0.1"
        self.app_version_date = "2020-05-20"
        self.app_description = _("A simple image viewer.")
        self.app_copyright = "(C) 2020 Daniel Muñiz Fontoira"
        self.app_web_site = "https://gitlab.com/damufo/encadra"
        self.app_developer = "Daniel Muñiz Fontoira"
        self.app_license = _(
"Copyright (C) 2020  Daniel Muñiz Fontoira\n\n"
"This program is free software: you can redistribute it and/or modify "
"it under the terms of the GNU General Public License as published by "
"the Free Software Foundation, either version 3 of the License, or "
"(at your option) any later version.\n\n"
"This program is distributed in the hope that it will be useful, "
"but WITHOUT ANY WARRANTY; without even the implied warranty of "
"MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the "
"GNU General Public License for more details.\n\n"
"You should have received a copy of the GNU General Public License "
"along with this program.  If not, see <http://www.gnu.org/licenses/>.")

        self.app_path_folder = app_path_folder
        self.arg1 = arg1

        config_app_dir_path = Path.home().joinpath('.config', 'encadra')
        config_app_dir_path.mkdir(parents=True, exist_ok=True)

        self.prefs = Prefs(
            config_app_dir_path=config_app_dir_path,
            file_name='settings.json')
        self.prefs.load()

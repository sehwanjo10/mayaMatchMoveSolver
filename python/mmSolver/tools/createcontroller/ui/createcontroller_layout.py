# Copyright (C) 2021 David Cattermole
#
# This file is part of mmSolver.
#
# mmSolver is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# mmSolver is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with mmSolver.  If not, see <https://www.gnu.org/licenses/>.
#
"""
The main component of the user interface for the Create Controller window.
"""

import mmSolver.ui.qtpyutils as qtpyutils
qtpyutils.override_binding_order()

import Qt.QtWidgets as QtWidgets

import mmSolver.logger
import mmSolver.utils.configmaya as configmaya
import mmSolver.tools.createcontroller.constant as const
import mmSolver.tools.createcontroller.ui.ui_createcontroller_layout as ui_layout


LOG = mmSolver.logger.get_logger()


class CreateController1Layout(QtWidgets.QWidget, ui_layout.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(CreateController1Layout, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Bake Options
        bake_mode_labels = const.BAKE_MODE_LABEL_LIST
        self.bakeModeComboBox.addItems(bake_mode_labels)
        self.bakeModeComboBox.currentIndexChanged.connect(
            self.bakeModeIndexChanged
        )

        # Populate the UI with data
        self.populateUi()

    def bakeModeIndexChanged(self, index):
        name = const.CONFIG_BAKE_MODE_KEY
        value = const.BAKE_MODE_VALUE_LIST[index]
        configmaya.set_scene_option(name, value, add_attr=True)
        LOG.debug('key=%r value=%r', name, value)

    def reset_options(self):
        name = const.CONFIG_BAKE_MODE_KEY
        value = const.DEFAULT_BAKE_MODE
        configmaya.set_scene_option(name, value)
        LOG.debug('key=%r value=%r', name, value)

        self.populateUi()

    def populateUi(self):
        """
        Update the UI for the first time the class is created.
        """
        name = const.CONFIG_BAKE_MODE_KEY
        value = configmaya.get_scene_option(
            name,
            default=const.DEFAULT_BAKE_MODE)
        index = const.BAKE_MODE_VALUE_LIST.index(value)
        label = const.BAKE_MODE_LABEL_LIST[index]
        LOG.debug('key=%r value=%r label=%r', name, value, label)
        self.bakeModeComboBox.setCurrentText(label)
        return
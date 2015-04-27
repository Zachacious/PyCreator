"""
This module provides an easy access to the application settings
"""
import json
from pyqode.qt.QtCore import QSettings, QByteArray, QSize, QPoint


class Settings(object):
    IConfigOption = 0
    IConfigPath = 1
    IConfigOptAuto = 0
    IConfigOptManual = 1
    MWState = 0
    MWSize = 1
    MWPosition = 2
    MWMaximized = 3

    def __init__(self):
        self.settings = QSettings('Zach Moore', 'DeliciousPy')

    @property
    def mainWindowState(self):
        state = [self.settings.value('mainWindow_state',
                                     QByteArray(),
                                     type=QByteArray),
                 self.settings.value('mainWindow_size',
                                     QSize(),
                                     type=QSize),
                 self.settings.value('mainWindow_position',
                                     QPoint(),
                                     type=QPoint),
                 self.settings.value('mainWindow_maximized', False)]
        return state

    @mainWindowState.setter
    def mainWindowState(self, value):
        self.settings.setValue('mainWindow_state', value[self.MWState])
        self.settings.setValue('mainWindow_size', value[self.MWSize])
        self.settings.setValue('mainWindow_position', value[self.MWPosition])
        self.settings.setValue('mainWindow_maximized', value[self.MWMaximized])

    @property
    def interpreterConfig(self):
        iconfig = [self.settings.value('iconfig_option', 0),
                   self.settings.value('iconfig_path', '')]
        return iconfig

    @interpreterConfig.setter
    def interpreterConfig(self, value):
        self.settings.setValue('iconfig_option', value[self.IConfigOption])
        self.settings.setValue('iconfig_path', value[self.IConfigPath])

    @property
    def run_configs(self):
        """
        Returns the dictionary of run configurations. A run configuration is
        just a list of arguments to append to the run command.

        This is internally stored as a json object

        """
        string = self.settings.value('run_configs', '{}')
        return json.loads(string)

    @run_configs.setter
    def run_configs(self, value):
        self.settings.setValue('run_configs', json.dumps(value))

    def get_run_config_for_file(self, filename):
        try:
            dic = self.run_configs
            config = dic[filename]
        except KeyError:
            config = []
            self.set_run_config_for_file(filename, config)
        return config

    def set_run_config_for_file(self, filename, config):
        dic = self.run_configs
        dic[filename] = config
        self.run_configs = dic

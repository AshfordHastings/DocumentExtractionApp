import os

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.configs = {}
        return cls._instance

    def add_config(self, name, config):
        self.configs[name] = config

    def add_config_dict(self, configs:dict):
        [self.add_config(name, config) for name, config in configs.items()]

    def get_config(self, name):
        return self.configs.get(name, None)

    def remove_config(self, name):
        del self.configs[name]


def get_config(name):
    man = ConfigManager()
    return man.get_config(name) or os.getenv(name)

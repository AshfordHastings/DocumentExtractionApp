# import pytest
# from dotenv import dotenv_values

# from config import ConfigManager

# def pytest_addoption(parser):
#     parser.addoption('--envfile', action="store", help="Path to config file.")

# @pytest.fixture(scope="session")
# def config_manager(request):
#     env_file = request.config.getoption("--envfile")
#     config_values = dotenv_values(env_file)

#     cfg_man = ConfigManager()
#     cfg_man.add_config_dict(cfg_man)
#     return cfg_man



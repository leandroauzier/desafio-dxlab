import os
from dynaconf import Dynaconf

cur_directory = os.path.dirname(os.path.realpath(__file__))

settings = Dynaconf(
    envvar_prefix="ENV", settings_files=[
        f"{cur_directory}/settings.toml"
    ],
)

"""Table API Tutorial"""

from pyflink import *

t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())
t_env.get_config().get_configuration().set_string("parallelism.default", "1")

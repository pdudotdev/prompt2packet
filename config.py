# Application-wide configs

# Safety limits
DEF_PACKETS = 1
MAX_PACKETS = 1000
MIN_INTERVAL_MS = 0
MAX_INTERVAL_MS = 10000
DEFAULT_INTERVAL_MS = 0
MIN_PORT = 1
MAX_PORT = 65535

# Defaults
DEFAULT_SRC_PORT = "random"

# For L2 send (future versions)
DEFAULT_INTERFACE = "eth1"

# Behavior flags
ALLOW_BROADCAST = False

# Require root priv
REQUIRE_ROOT = True

# If False, just print packets
SEND_ENABLED = True
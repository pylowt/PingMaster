from unittest.mock import mock_open, patch

import pytest
import yaml

from app.monitor import load_config

mock_yaml = """
urls:
  - http://example.com
"""


def test_load_config():
    # Testing library code but used for TDD purposes
    with patch("builtins.open", mock_open(read_data=mock_yaml)) as m:
        config = load_config()
        assert config == {"urls": ["http://example.com"]}
        assert m.call_args[0][0] == "app/config.yaml"

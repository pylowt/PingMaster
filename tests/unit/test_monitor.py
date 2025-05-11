from unittest.mock import mock_open, patch, AsyncMock

import pytest

from app.monitor import load_config, schedule_checks

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


@pytest.mark.asyncio
@patch("app.monitor.load_config")
@patch("app.monitor.runner")
async def test_schedule_checks_starts_runner(mock_runner, mock_load_config):
    mock_load_config.return_value = {
        "urls": ["http://example.com"],
        "interval_seconds": 30,
    }
    mock_runner.return_value = AsyncMock()

    await schedule_checks()

    mock_load_config.assert_called_once()
    mock_runner.assert_called_once_with(["http://example.com"], 30)


@pytest.mark.asyncio
@patch("app.monitor.load_config")
@patch("app.monitor.runner")
async def test_schedule_checks_no_urls(mock_runner, mock_load_config):
    mock_load_config.return_value = {"urls": [], "interval_seconds": 60}
    mock_runner.return_value = AsyncMock()

    await schedule_checks()

    mock_load_config.assert_called_once()
    mock_runner.assert_called_once_with([], 60)

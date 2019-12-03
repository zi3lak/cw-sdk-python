import os
from unittest.mock import patch, mock_open
from unittest import mock


from cryptowatch.auth import read_api_key_from_config


def test_open_config_file(mocker):
    # Mock open()
    with patch("cryptowatch.auth.open", mock_open()) as config:
        # Mock os.environ.get()
        with mock.patch.dict("os.environ", {"HOME": "/sweet/home"}):
            # This should open() the credential file
            read_api_key_from_config()
            # Forge credential file path
            user_home_dir = os.environ.get("HOME")
            filepath = "{}/.cw/credentials.yml".format(user_home_dir)
            # Check it was well open()'ed
            config.assert_called_once_with(filepath, "r")

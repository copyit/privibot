"""Tests for the `cli` module."""

import pytest

from privibot import cli


def test_main():
    """Basic CLI test."""
    assert cli.main([]) == 0


def test_show_help(capsys):
    """
    Shows help.

    Arguments:
        capsys: Pytest fixture to capture output.
    """
    with pytest.raises(SystemExit):
        cli.main(["-h"])
    captured = capsys.readouterr()
    assert "privibot" in captured.out

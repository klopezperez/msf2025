"""
Unit and regression test for the mfs2025 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import mfs2025


def test_mfs2025_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "mfs2025" in sys.modules

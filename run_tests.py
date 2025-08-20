#!/usr/bin/env python3
"""
Test runner script for the portfolio application.
"""

import sys
import subprocess
import os


def run_tests():
    """Run the test suite."""
    print("🧪 Running portfolio tests...")
    
    # Install test dependencies if needed
    try:
        import pytest
        import httpx
    except ImportError:
        print("📦 Installing test dependencies...")
        subprocess.run([sys.executable, "-m", "uv", "sync", "--extra", "test"], check=True)
    
    # Run tests
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/", 
        "-v", 
        "--tb=short"
    ])
    
    if result.returncode == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()

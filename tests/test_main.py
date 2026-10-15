import subprocess
import sys


def test_package_prints_message() -> None:
    result = subprocess.run(
        [sys.executable, "-c", "import mlops_starter"],
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout == "devops-dev+ml=mlops\n"

import subprocess
from pathlib import Path


class TestDocumentation:
    def test_build(self, tmp_path: Path) -> None:
        """Test the build of the main `govcookiecutter-lite` repository using mkdocs."""
        result = subprocess.run(
            ["mkdocs", "build", "--site-dir", str(tmp_path.joinpath("_site"))],
            cwd=Path(__file__).parent.parent,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"mkdocs build failed: {result.stderr}"

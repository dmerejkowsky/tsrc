import os
from path import Path
import pytest

import tsrc.cli


class CLI():
    def __init__(self) -> None:
        self.workspace_path = Path(os.getcwd())

    def run(self, *args: str, expect_fail=False) -> None:
        try:
            tsrc.cli.main.main(args=args)  # type: ignore
            rc = 0
        except SystemExit as e:
            rc = e.code
        if expect_fail and rc == 0:
            assert False, "should have failed"
        if rc != 0 and not expect_fail:
            raise SystemExit(rc)


@pytest.fixture
def tsrc_cli(workspace_path, monkeypatch):
    monkeypatch.chdir(workspace_path)
    res = CLI()
    return res

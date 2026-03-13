# -*- coding: utf-8 -*-
"""
Pharos Automation BOT (Multi-Module)
"""
from utils import ensure_env


@ensure_env
def main():
    from cli import main as _run
    _run()


if __name__ == "__main__":
    main()

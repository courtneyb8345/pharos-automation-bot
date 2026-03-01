import os
import subprocess
import sys
from pathlib import Path
from typing import Dict
from utils import ensure_env

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table


BASE_DIR = Path(__file__).resolve().parent
REQUIREMENTS_FILE = BASE_DIR / "requirements.txt"
ACCOUNTS_FILE = BASE_DIR / "accounts.txt"
PROXY_FILE = BASE_DIR / "proxy.txt"
POOLS_FILE = BASE_DIR / "pools.json"


LOGO = r""" _____  _                                         _                        _   _               ____   ____ _______ 
 |  __ \| |                             /\        | |                      | | (_)             |  _ \ / __ \__   __|
 | |__) | |__   __ _ _ __ ___  ___     /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __   | |_) | |  | | | |   
 |  ___/| '_ \ / _` | '__/ _ \/ __|   / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \  |  _ <| |  | | | |   
 | |    | | | | (_| | | | (_) \__ \  / ____ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | | | |_) | |__| | | |   
 |_|    |_| |_|\__,_|_|  \___/|___/ /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_| |____/ \____/  |_|   
                                                                                                                    
                                                                                                                    """


BOTS: Dict[str, Dict[str, str]] = {
    "1": {
        "file": "bot1.py",
        "name": "Pharos BOT",
        "description": "DeFi automation for Pharos Testnet",
    },
    "2": {
        "file": "bot2.py",
        "name": "Gotchipus BOT",
        "description": "NFT minting & wearable claiming",
    },
    "3": {
        "file": "bot3.py",
        "name": "OpenFi BOT",
        "description": "Lending, borrowing & DeFi services",
    },
    "4": {
        "file": "bot4.py",
        "name": "Brokex BOT",
        "description": "Faucet claim and trade automation",
    },
    "5": {
        "file": "bot5.py",
        "name": "FaroSwap BOT",
        "description": "Swap and liquidity automation",
    },
    "6": {
        "file": "bot6.py",
        "name": "AquaFlux BOT",
        "description": "Auto Mint Standard & Premium NFT",
    },
    "7": {
        "file": "bot7.py",
        "name": "Zenith Swap BOT",
        "description": "Swap and liquidity automation",
    },
    "8": {
        "file": "bot8.py",
        "name": "Pharos Name Service BOT",
        "description": "Auto Mint Random .phrs Domain",
    },
    "9": {
        "file": "bot9.py",
        "name": "Grandline BOT",
        "description": "Auto Claim All Available Badges",
    },
    "10": {
        "file": "bot10.py",
        "name": "R2 Pharos BOT",
        "description": "Swap and liquidity automation",
    },
    "11": {
        "file": "bot11.py",
        "name": "Bitverse BOT",
        "description": "Auto trade, deposit, withdraw",
    },
    "12": {
        "file": "bot12.py",
        "name": "AutoStaking BOT",
        "description": "Automated staking operations & faucet claims",
    },
    "13": {
        "file": "bot13.py",
        "name": "Spout Finance BOT",
        "description": "KYC, random trades, and account automation",
    },
    "14": {
        "file": "bot14.py",
        "name": "Primuslabs Send BOT",
        "description": "Auto send tips via X Handler (social tipping)",
    },
}


console = Console()


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def show_header() -> None:
    console.print(Panel.fit(LOGO, style="bold cyan", border_style="blue"))
    console.print(
        "[bold magenta]Pharos Automation BOT (Multi-Module)[/bold magenta]\n"
        "[green]One-stop automation suite for the Pharos Testnet ecosystem.[/green]\n"
    )


def ensure_file(path: Path, template: str | None = None) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if template is None:
        path.touch()
    else:
        path.write_text(template, encoding="utf-8")


def open_in_editor(path: Path) -> None:
    try:
        if os.name == "nt":
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])
    except Exception as exc:
        console.print(f"[red]Failed to open file in editor: {exc}[/red]")


def install_dependencies() -> None:
    clear_screen()
    show_header()
    console.print("[bold yellow]Install dependencies[/bold yellow]\n")

    if not REQUIREMENTS_FILE.exists():
        console.print(
            f"[red]requirements.txt not found: {REQUIREMENTS_FILE}[/red]\n"
        )
        Prompt.ask("[dim]Press Enter to return to menu[/dim]")
        return

    console.print(f"Python: [cyan]{sys.executable}[/cyan]")
    console.print(f"Requirements: [cyan]{REQUIREMENTS_FILE}[/cyan]\n")
    console.print(
        "[bold]Before installing, make sure that:[/bold]\n"
        "- Git and Python 3.9+ are installed\n"
        "- On Windows with Python 3.13+, Microsoft C++ Build Tools are installed\n"
    )

    if not Confirm.ask(
        "[bold green]Run dependency installation via pip?[/bold green]",
        default=False,
    ):
        return

    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        str(REQUIREMENTS_FILE),
    ]

    with console.status(
        "[bold cyan]Installing dependencies, please wait...[/bold cyan]",
        spinner="dots",
    ):
        try:
            subprocess.check_call(cmd)
            console.print(
                "\n[bold green]Dependencies installed successfully.[/bold green]"
            )
        except subprocess.CalledProcessError as exc:
            console.print(
                f"\n[red]Dependency installation failed, exit code {exc.returncode}[/red]"
            )

    Prompt.ask("\n[dim]Press Enter to return to menu[/dim]")


def settings_menu() -> None:
    while True:
        clear_screen()
        show_header()

        table = Table(
            title="[bold yellow]Settings[/bold yellow]",
            box=box.ROUNDED,
            show_lines=True,
        )
        table.add_column("Key", style="cyan", justify="center")
        table.add_column("Setting", style="bold")
        table.add_column("Description")

        table.add_row(
            "1",
            "Wallets (accounts.txt)",
            "Add/edit private keys for accounts",
        )
        table.add_row(
            "2",
            "Proxies (proxy.txt)",
            "Configure proxies (free/private/none)",
        )
        table.add_row(
            "3",
            "Faroswap pools (pools.json)",
            "Liquidity pool addresses for Faroswap BOT",
        )
        table.add_row(
            "4",
            "Show paths",
            "Show paths to all important configuration files",
        )
        table.add_row("B", "Back", "Return to main menu")

        console.print(table)
        choice = Prompt.ask(
            "\n[bold cyan]Select option[/bold cyan]", default="B"
        ).strip().lower()

        if choice == "1":
            ensure_file(
                ACCOUNTS_FILE,
                template=(
                    "# Add one private key per line (without 0x)\n"
                    "# your_private_key_1\n"
                    "# your_private_key_2\n"
                ),
            )
            console.print(
                f"\n[green]Accounts file:[/green] [cyan]{ACCOUNTS_FILE}[/cyan]"
            )
            open_in_editor(ACCOUNTS_FILE)
            Prompt.ask(
                "\n[dim]Press Enter after editing the file[/dim]"
            )
        elif choice == "2":
            ensure_file(
                PROXY_FILE,
                template=(
                    "# One proxy per line. Supported formats:\n"
                    "# 127.0.0.1:8080\n"
                    "# http://user:pass@127.0.0.1:8080\n"
                    "# socks5://127.0.0.1:1080\n"
                ),
            )
            console.print(
                f"\n[green]Proxy file:[/green] [cyan]{PROXY_FILE}[/cyan]"
            )
            open_in_editor(PROXY_FILE)
            Prompt.ask(
                "\n[dim]Press Enter after editing the file[/dim]"
            )
        elif choice == "3":
            ensure_file(
                POOLS_FILE,
                template=(
                    '{\n'
                    '  "pools": [\n'
                    '    {\n'
                    '      "name": "Example Pool",\n'
                    '      "address": "0x0000000000000000000000000000000000000000",\n'
                    '      "token0": "PHRS",\n'
                    '      "token1": "USDT"\n'
                    '    }\n'
                    '  ]\n'
                    '}\n'
                ),
            )
            console.print(
                f"\n[green]Faroswap pools file:[/green] [cyan]{POOLS_FILE}[/cyan]"
            )
            open_in_editor(POOLS_FILE)
            Prompt.ask(
                "\n[dim]Press Enter after editing the file[/dim]"
            )
        elif choice == "4":
            console.print("\n[bold yellow]Configuration files:[/bold yellow]\n")
            console.print(f"- accounts.txt: [cyan]{ACCOUNTS_FILE}[/cyan]")
            console.print(f"- proxy.txt:    [cyan]{PROXY_FILE}[/cyan]")
            console.print(f"- pools.json:   [cyan]{POOLS_FILE}[/cyan]")
            Prompt.ask(
                "\n[dim]Press Enter to return to settings[/dim]"
            )
        elif choice in ("b", "back"):
            break
        else:
            console.print("[red]Unknown menu option[/red]")
            Prompt.ask("\n[dim]Press Enter to continue[/dim]")


def run_single_bot(bot_key: str) -> None:
    bot_info = BOTS.get(bot_key)
    if not bot_info:
        console.print("[red]Bot with this number not found.[/red]")
        return

    bot_path = BASE_DIR / bot_info["file"]
    if not bot_path.exists():
        console.print(
            f"[red]Bot script not found:[/red] [cyan]{bot_path}[/cyan]"
        )
        return

    console.print(
        f"\n[bold green]Starting {bot_info['name']} ({bot_info['file']})[/bold green]\n"
    )

    cmd = [sys.executable, str(bot_path)]
    try:
        subprocess.run(cmd, check=False)
    except KeyboardInterrupt:
        console.print("\n[red]Stopped by Ctrl+C[/red]")


def run_bots_menu() -> None:
    while True:
        clear_screen()
        show_header()

        table = Table(
            title="[bold yellow]Run Bots[/bold yellow]",
            box=box.ROUNDED,
            show_lines=True,
        )
        table.add_column("Key", style="cyan", justify="center")
        table.add_column("Bot Name", style="bold")
        table.add_column("Description")

        for key, info in BOTS.items():
            table.add_row(key, info["name"], info["description"])

        table.add_row(
            "A", "Run all (sequence)", "Run all bots sequentially"
        )
        table.add_row("B", "Back", "Return to main menu")

        console.print(table)
        choice = Prompt.ask(
            "\n[bold cyan]Select a bot (or A/B)[/bold cyan]",
            default="B",
        ).strip().lower()

        if choice in ("b", "back"):
            break
        if choice == "a":
            for key in BOTS:
                run_single_bot(key)
            Prompt.ask(
                "\n[dim]All available bots have been run sequentially. "
                "Press Enter to return to menu[/dim]"
            )
        else:
            run_single_bot(choice)
            Prompt.ask(
                "\n[dim]Press Enter to return to the bot list[/dim]"
            )


def show_about() -> None:
    clear_screen()
    show_header()

    text = (
        "[bold]Pharos Automation BOT (Multi-Module)[/bold]\n\n"
        "A one-stop automation suite for the Pharos Testnet ecosystem.\n"
        "Run everything — Pharos, Gotchipus, OpenFi, Brokex, Faroswap, AquaFlux,\n"
        "Zenith Swap, Pharos Name Service, Grandline, R2 Pharos, Bitverse,\n"
        "AutoStaking, Spout Finance and Primuslabs Send — using a single wallet,\n"
        "one proxy and one configuration.\n\n"
        "[bold]Features:[/bold]\n"
        "• Unified wallet & proxy configuration\n"
        "• Multi-module scripts (run individually or sequentially)\n"
        "• Support for check-ins, faucet, swaps, NFTs, lending, staking, social tips\n"
        "• Three proxy modes: Free, Private, None with auto-rotation\n"
        "• Multi-account ready for testnet farming\n"
        "• NEW: Social Tip Automation via X Handler (Primuslabs Send BOT)\n\n"
        "[bold]Requirements:[/bold]\n"
        "- Python 3.9+\n"
        "- pip / pip3\n"
        "- web3, eth-account, requests, colorama, rich\n\n"
        "[bold]Dependency notes:[/bold]\n"
        "Recommended versions:\n"
        "web3==6.15.0, eth-account==0.11.0\n\n"
        "[bold]Support the developers:[/bold]\n"
        "EVM: 0x3b94Ff1611773171E06047C0041099CccCFC609F\n\n"
        "[bold]Security & Disclaimer:[/bold]\n"
        "• Testnet only\n"
        "• Use burner wallets\n"
        "• Never share your private keys\n"
        "• Review the code, no developer liability\n\n"
        "Crafted with love by CryptoDai3 x YetiDAO (MIT License)\n"
    )

    console.print(
        Panel.fit(
            text,
            title="[bold magenta]About[/bold magenta]",
            border_style="magenta",
        )
    )
    Prompt.ask("\n[dim]Press Enter to return to menu[/dim]")


@ensure_env
def main() -> None:
    while True:
        clear_screen()
        show_header()

        table = Table(
            title="[bold yellow]Main Menu[/bold yellow]",
            box=box.ROUNDED,
            show_lines=True,
        )
        table.add_column("Key", style="cyan", justify="center")
        table.add_column("Action", style="bold")
        table.add_column("Description")

        table.add_row(
            "1",
            "Install dependencies",
            "Install dependencies from requirements.txt",
        )
        table.add_row(
            "2",
            "Run bots",
            "Run individual bots or all sequentially",
        )
        table.add_row(
            "3",
            "Settings",
            "accounts.txt, proxy.txt, pools.json",
        )
        table.add_row("4", "About", "Project information")
        table.add_row("Q", "Quit", "Exit")

        console.print(table)
        choice = Prompt.ask(
            "\n[bold cyan]Select option[/bold cyan]", default="Q"
        ).strip().lower()

        if choice == "1":
            install_dependencies()
        elif choice == "2":
            run_bots_menu()
        elif choice == "3":
            settings_menu()
        elif choice == "4":
            show_about()
        elif choice in ("q", "quit", "exit"):
            console.print("\n[bold green]Exiting. Happy farming![/bold green]")
            break
        else:
            console.print("[red]Unknown menu option[/red]")
            Prompt.ask("\n[dim]Press Enter to continue[/dim]")


if __name__ == "__main__":
    main()


from rich.console import Console
from rich.panel import Panel


console = Console()


def run_bot(bot_id: int, name: str, description: str) -> None:
    text = (
        f"[bold]{name}[/bold]\n\n"
        f"{description}\n\n"
        "Bot stub.\n"
        "Add your automation logic here, "
        "or use this file as the entry point."
    )
    console.print(
        Panel.fit(
            text,
            title=f"bot{bot_id}.py",
            border_style="cyan",
        )
    )


if __name__ == "__main__":
    console.print(
        "[yellow]This is a shared module for bots. "
        "Run specific botN.py files or cli.py[/yellow]"
    )


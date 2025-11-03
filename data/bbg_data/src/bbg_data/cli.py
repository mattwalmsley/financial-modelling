"""
Command-line interface for bbg_data.

Provides terminal commands for fetching Bloomberg data without writing Python code.
"""

import sys
from pathlib import Path

try:
    import typer
    from rich.console import Console
    from rich.table import Table
except ImportError:
    print(
        "CLI dependencies not installed. Install with: uv pip install bbg-data[cli]",
        file=sys.stderr,
    )
    sys.exit(1)

from bbg_data import fetch_nvidia_options
from bbg_data.enums import BloombergField

app = typer.Typer(
    name="bbg-data",
    help="Bloomberg data fetching tool with type-safe API",
    add_completion=False,
)
console = Console()


@app.command()
def nvidia_options(
    expiry: str = typer.Argument(
        ...,
        help="Expiration date in MM/DD/YY format (e.g., 11/21/25)",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output CSV file path (prints to stdout if not specified)",
    ),
    min_strike: float | None = typer.Option(
        None,
        "--min-strike",
        help="Minimum strike price filter",
    ),
    max_strike: float | None = typer.Option(
        None,
        "--max-strike",
        help="Maximum strike price filter",
    ),
    settle_only: bool = typer.Option(
        False,
        "--settle-only",
        help="Fetch only settlement prices (faster)",
    ),
) -> None:
    """
    Fetch NVIDIA option chain data for a specific expiration date.

    Example:
        bbg-data nvidia-options 11/21/25 -o nvda_options.csv
    """
    console.print(f"[bold blue]Fetching NVIDIA options for {expiry}...[/bold blue]")

    try:
        # Determine fields
        fields = None
        if settle_only:
            fields = [
                BloombergField.OPT_STRIKE_PX,
                BloombergField.OPT_PUT_CALL,
                BloombergField.OPT_EXPIRE_DT,
                BloombergField.PX_SETTLE,
            ]

        # Fetch data
        df = fetch_nvidia_options(
            expiry_date=expiry,
            fields=fields,
            strike_range=(min_strike, max_strike),
        )

        if df.empty:
            console.print("[yellow]No options found matching criteria[/yellow]")
            return

        console.print(f"[green]✓ Found {len(df)} options[/green]")

        # Display summary
        calls = df[df["option_type"] == "CALL"]
        puts = df[df["option_type"] == "PUT"]
        console.print(f"  Calls: {len(calls)}, Puts: {len(puts)}")

        # Output
        if output:
            df.to_csv(output, index=False)
            console.print(f"[green]✓ Data saved to {output}[/green]")
        else:
            # Display preview table
            _display_options_table(df.head(20), f"First 20 options (total: {len(df)})")

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        raise typer.Exit(1)


@app.command()
def version() -> None:
    """Show version information."""
    from bbg_data import __version__

    console.print(f"bbg-data version {__version__}")


def _display_options_table(df, title: str) -> None:
    """Display options data in a formatted table."""
    table = Table(title=title)

    # Add columns
    table.add_column("Strike", justify="right", style="cyan")
    table.add_column("Type", justify="center", style="magenta")
    table.add_column("Settle", justify="right", style="green")
    table.add_column("Last", justify="right")
    table.add_column("Bid", justify="right")
    table.add_column("Ask", justify="right")
    table.add_column("Vol", justify="right")
    table.add_column("OI", justify="right")

    # Add rows
    for _, row in df.iterrows():
        table.add_row(
            f"{row['strike']:.2f}",
            row["option_type"][:1],  # C or P
            f"{row['settlement_price']:.2f}" if row["settlement_price"] else "—",
            f"{row['last_price']:.2f}" if row["last_price"] else "—",
            f"{row['bid']:.2f}" if row["bid"] else "—",
            f"{row['ask']:.2f}" if row["ask"] else "—",
            f"{row['volume']:.0f}" if row["volume"] else "—",
            f"{row['open_interest']:.0f}" if row["open_interest"] else "—",
        )

    console.print(table)


if __name__ == "__main__":
    app()

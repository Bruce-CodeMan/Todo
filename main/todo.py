# @Time: 2022/1/11 11:29 上午
# @Author: Bruce

import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_table, complete_todo, update_todo

console = Console()

app = typer.Typer()


@app.command(short_help='add an item')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_table(todo)
    show()


@app.command(short_help='delete an item')
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_todo(position - 1)
    show()


@app.command(short_help='update an item')
def update(position: int, task: str, category: str):
    typer.echo(f"updating {position}")
    update_todo(position - 1, task, category)
    show()


@app.command(short_help='complete an item')
def complete(position: int):
    typer.echo(f"completing {position}")
    complete_todo(position - 1)
    show()


@app.command(short_help='show the whole items')
def show():
    tasks = get_all_todos()
    console.print("[bold magenta]Tools[/bold magenta]", "💻")
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20, justify="center")
    table.add_column("Category", min_width=12, justify="center")
    table.add_column("Done", min_width=12, justify="center")

    def get_category_color(category):
        COLORS = {"Learn": "yellow", "Youtube": "red", "Sports": "cyan", "Study": "green"}
        if category in COLORS:
            return COLORS[category]
        return "white"

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = "[green]Finish[/green]" if task.status == 2 else "[red]Not Done[/red]"
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)

    console.print(table)


if __name__ == '__main__':
    app()

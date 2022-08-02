import click
import os

from datetime import date

MODULE_DIR = os.path.dirname(__file__)

@click.command()
@click.argument("name")
def create_python_project(name):
    click.echo(f"Created dir {name}!")
    os.mkdir("src")
    src_path = os.path.join("src", name.replace("-", "_"))
    os.mkdir(src_path)
    os.mknod(os.path.join(src_path, "__init__.py"))

    if click.confirm("Do you want to add MIT license?"):
        with open("MIT_LICENSE_TEMPLATE") as f:
            template = f.read()
        full_name = click.prompt("Enter full name for license")
        full_name = " ".join([word.capitalize() for word in full_name.split()])
        with open("LICENSE", "w") as f:
            f.write(template.format(year=date.today().year, full_name=full_name))

    with open("README.md", "w") as f:
        f.write(f"# {name}")

    with open("pyproject.toml") as f:
        pass


if __name__ == "__main__":
    create_python_project()

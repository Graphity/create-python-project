import click
import os
import toml

from datetime import date

MODULE_DIR = os.path.dirname(__file__)
MIT_LICENSE_TEMPLATE_PATH = os.path.join(MODULE_DIR, "MIT_LICENSE_TEMPLATE")
PYPROJECT_TEMPLATE_PATH = os.path.join(MODULE_DIR, "pyproject-template.toml")

@click.command()
@click.argument("name")
def create_python_project(name):
    click.echo(f"Created dir {name}!")
    os.mkdir("src")
    src_path = os.path.join("src", name.replace("-", "_"))
    os.mkdir(src_path)
    os.mknod(os.path.join(src_path, "__init__.py"))

    if click.confirm("Do you want to add MIT license?"):
        with open(MIT_LICENSE_TEMPLATE_PATH) as f:
            mit_license_template = f.read()
        full_name = click.prompt("Enter full name for license")
        full_name = " ".join([word.capitalize() for word in full_name.split()])
        with open("LICENSE", "w") as f:
            f.write(mit_license_template.format(
                year=date.today().year,
                full_name=full_name
            ))

    with open("README.md", "w") as f:
        f.write(f"# {name}")

    with open(PYPROJECT_TEMPLATE_PATH) as f:
        pyproject_json = toml.load(f)

    # modify data

    with open("pyproject.toml", "w") as f:
        toml.dump(pyproject_json, f)

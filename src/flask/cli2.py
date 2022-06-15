from __future__ import annotations

import os

import click

from flask.cli import ScriptInfo


@click.group("flask")
@click.option("--app", "app_import_path", metavar="IMPORT")
@click.option("--env", metavar="ENV", default="production")
@click.option("--env-file", type=click.Path(dir_okay=False))
def flask_group(
    app_import_path: str | None,
    env: str | None,
    env_file: str | None,
) -> None:
    ctx = click.get_current_context()
    info = ctx.find_object(ScriptInfo)

    if info is None:
        info = ScriptInfo(app_import_path=app_import_path)

    ctx.obj = info


@flask_group.command("run")
def run_command():
    os.environ["FLASK_RUN_FROM_CLI"] = "true"
    click.echo("run")


def main() -> None:
    flask_group.main()


if __name__ == "__main__":
    main()

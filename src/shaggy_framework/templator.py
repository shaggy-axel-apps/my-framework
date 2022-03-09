import os

from jinja2 import Template

from blog_project.settings import TEMPLATES_DIR


def render(template_name: str, **kwargs) -> str:

    path = os.path.join(TEMPLATES_DIR, template_name)

    with open(path, encoding="utf-8") as file:
        template = Template(file.read())

        return template.render(**kwargs)

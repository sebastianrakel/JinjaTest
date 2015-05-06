from jinja2 import Environment, PackageLoader
import shutil
import os

basedir = os.path.abspath(os.path.dirname(__file__))

env = Environment(loader=PackageLoader('main', 'templates'))

def create_output(templates):
    output_path = os.path.join(basedir, 'output')

    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    os.mkdir(output_path)

    shutil.copytree(os.path.join(basedir, 'static'), os.path.join(output_path, 'static'))

    for template_file in templates:
        template = env.get_template(template_file)
        template_stream = template.stream(templates[template_file])

        template_stream.dump(os.path.join(output_path, template_file))


if __name__ == '__main__':
    templates = {}

    templates['index.html'] = {'name': 'Sebastian Rakel'}
    templates['table.html'] = {'table': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}

    create_output(templates)

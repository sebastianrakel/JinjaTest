from jinja2 import Environment, PackageLoader
import shutil
import os

basedir = os.path.abspath(os.path.dirname(__file__))

env = Environment(loader=PackageLoader('main', 'templates'))

def create_output(templates):
    output_path = os.path.join(basedir, 'output')

    # check if output path exists, if delete it
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    # create output path
    os.mkdir(output_path)

    # copy static files to output
    shutil.copytree(os.path.join(basedir, 'static'), os.path.join(output_path, 'static'))

    # for every template in directory render template and set values
    for template_file in templates:
        # get template
        template = env.get_template(template_file)

        # create stream with values
        template_stream = template.stream(templates[template_file])

        # dump html to output path
        template_stream.dump(os.path.join(output_path, template_file))


if __name__ == '__main__':
    templates = {}

    templates['index.html'] = {'name': 'Sebastian Rakel'}
    templates['table.html'] = {'table': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}

    create_output(templates)

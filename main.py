import argparse
from pathlib import Path

import yaml
from mako.template import Template


def main():
    parser = argparse.ArgumentParser(description='Take yaml and output SM posts')
    parser.add_argument('yaml_path', type=str)

    args = parser.parse_args()

    with open(args.yaml_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
    content_gen(data)


def content_gen(data):
    '''
    Generates the social media content
    :param data:
    :return: markdown files at '../outputs/*'
    '''
    base_directory = Path(__file__).parent  # sets the absolute path to the root folder (parent to the file)
    templates_directory = base_directory / 'templates'
    outputs_directory = base_directory / 'outputs'

    for filepath in templates_directory.iterdir():  # iterdir = iterate the directory
        template_object = Template(filename=str(filepath))

        output_filename = filepath.stem + '.md'
        with open(outputs_directory / output_filename, 'w') as output_file:

            try:
                output_file.write(template_object.render(**data))
            except NameError:
                # The render returned nothing.
                print(f"{filepath} failed to render!")
                pass


if __name__ == '__main__':
    main()  # avoids namespace pollution

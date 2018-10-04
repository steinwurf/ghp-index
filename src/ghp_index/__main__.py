import staticjinja
import click
import tempfile
import os
import sys
import pkg_resources
import logging


@click.command()
@click.option('--outpath')
@click.option('--docspath')
@click.option('-v', '--verbose', is_flag=True)
def cli(outpath, docspath, verbose):

    log = logging.getLogger('ghp_index')

    # Create console handler with a higher log level
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch_formatter = logging.Formatter('%(message)s')
    ch.setFormatter(ch_formatter)

    log.addHandler(ch)

    # Expand docs path
    docspath = os.path.abspath(os.path.expanduser(docspath))
    outpath = os.path.abspath(os.path.expanduser(outpath))

    if not os.path.isdir(outpath):
        os.makedirs(outpath)

    log.info("Output path", outpath)
    log.info("Docs path", docspath)

    versions = []

    if docspath and os.path.isdir(docspath):

        for name in os.listdir(docspath):

            dirpath = os.path.join(docspath, name)

            if not os.path.isdir(dirpath):
                continue

            path = os.path.relpath(path=dirpath, start=outpath)

            versions.append((name, path))

    data = {}
    data['versions'] = versions

    print(versions)

    templates_path = pkg_resources.resource_filename(
        'ghp_index', 'templates')

    assert os.path.isdir(templates_path)

    site = staticjinja.make_site(
        searchpath=templates_path,
        contexts=[
            ('index.html', data)
        ],
        staticpaths=[
            'css',
            'js',
            'images'
        ],
        outpath=outpath)

    site.render()

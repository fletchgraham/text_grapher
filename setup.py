from setuptools import setup
setup(
    name = 'text_grapher',
    version = '0.1.0',
    packages = [
        'tg_cli',
        'tg_utils',
        'fletch_tools'
        ],
    entry_points = {
        'console_scripts': [
            'tg = tg_cli.main:main'
        ]
    })

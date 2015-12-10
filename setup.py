from setuptools import setup, find_packages
setup(
        name='phonebook',
        author='Kuppuraj Muthu',
        version="0.1",
        author_email='mkupraj@gmail.com',
        url='https://github.com/mkuppuraj/phonebook',
        packages = find_packages(),
        entry_points = {
            'console_scripts': [
                'init_db = phonebook.scripts.db_utils:initialize'
                ]
            },
        install_requires = [
            'sqlalchemy==1.0.4',
        ]
)


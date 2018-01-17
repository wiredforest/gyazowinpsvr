import os
import sys
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb') as readme:
    README = readme.read()

class DjangoTest(TestCommand):

    def run_tests(self):
        import django
        from django.conf import settings
        from django.test.utils import get_runner
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        failures = test_runner.run_tests(['tests'])
        sys.exit(bool(failures))


setup(
    name='gyazowinpsvr',
    version='0.2',
    packages=find_packages(exclude=('tests', 'gyazowinpsvr')),
    include_package_data=True,
    license='MIT License',
    description='gyazowin+ server using python',
    long_description=README.decode(),
    url='https://github.com/wiredforest/gyazowinpsvr',
    author='WiredForest',
    author_email='contact@wforest.jp',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    cmdclass = {'test': DjangoTest},
)

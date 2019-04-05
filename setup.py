from setuptools import find_packages, setup
try:
    from pip.download import PipSession
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.download import PipSession
    from pip._internal.req import parse_requirements


def get_requirements(file_name):
    return [
        str(requirement.req) for requirement in parse_requirements(
            file_name, session=PipSession()
        )
    ]


if __name__ == '__main__':
    setup(
        name='big-bang',
        version='0.0.1',
        description='A sample Python project',
        install_requires=get_requirements('requirements.txt'),
        include_package_data=True,
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'big_bang=big_bang.main:entry_point',
            ],
        },
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
    )

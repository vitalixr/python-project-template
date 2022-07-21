from setuptools import find_packages, setup


if __name__ == '__main__':
    setup(
        name='big-bang',
        version='0.0.1',
        description='A sample Python project',
        install_requires=(
            'click==8.1.3'
        ),
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

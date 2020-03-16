import setuptools

setuptools.setup(
    name='wagtail-lazyone',
    version='0.2.0',
    author='ryan28561',
    description="Collection of wagtail blocks, styles, and templates for LazyOne Sites",
    license='MIT',
    url='https://github.com/lightningkite/wagtail-lazyone',
    classifiers=[
        'Environment :: Wev Environment',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'django',
        'wagtail'
    ],
    python_requires='>=3.6',
)

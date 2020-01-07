from setuptools import setup


setup(
    name='wechat-exporter',
    version='0.1.0',
    url='https://github.com/Duerxin/wechat-exporter',
    license='MIT',
    author='Maple',
    author_email='ericsysu16@gmail.com',
    description='Wechat Exporter',
    packages=['we', 'we.contrib','we.contrib.html_exporter_res'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'biplist',
        'xmltodict',
        'jinja2',
    ],
    entry_points="""
    [console_scripts]
    wxep = we.run:main
    """,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    package_data = {'we': ['contrib/html_exporter_res/*','contrib/html_exporter_res/img/*','contrib/html_exporter_res/css/*'],}
)

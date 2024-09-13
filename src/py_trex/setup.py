from setuptools import find_packages, setup

package_name = 'py_trex'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='atr',
    maintainer_email='atr@test.test',
    description='ROX1 Assignment 2 Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_trex.trex_publisher_function:main',
            'listener = py_trex.trex_subscriber_function:main',
        ],
    },
)

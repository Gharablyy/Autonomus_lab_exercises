from setuptools import find_packages, setup

package_name = 'lab_2'

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
    maintainer='gharably',
    maintainer_email='gharably@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = lab_2.talker:main',
            'listener = lab_2.listener:main',
            'move_turtlebot = lab_2.move_turtlebot:main',
        ],
    },
)

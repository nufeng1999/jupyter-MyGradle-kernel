#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyGradle_kernel',
      vegradleion='0.0.1',
      description='Minimalistic Gradle kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      url='https://github.com/nufeng1999/jupyter-MyGradle-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyGradle-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiegradle=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
      scripts=['jupyter_MyGradle_kernel/install_MyGradle_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'gradle','gradle'],
      include_package_data=True
      )

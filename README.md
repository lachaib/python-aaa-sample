# python-aaa-sample
Sample repository to start a project with strong gatekeeping tools

## Goal:
Provide developers with a repository skeleton that will provide gatekeeping from the start

## Requirements:
The hello world requires python >=3.6 but it will depend on you.

## Under the hood:
This tool provides a very basic configuration that will enable pytest with pytest-cov and pytest-pylint included.
Via this configuration, pylint violations and lowering the coverage will be considered as failing tests.

## In Git we trust:
A small script is provided to add a pre-commit hook to the clone, forcing tests to pass prior to being able to commit

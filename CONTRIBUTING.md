# Contributing

Thank you for your interest in contributing to woof-CE.

## Development workflow
- Fork the repository and create your changes on a topic branch.
- Run `./run-tests.sh` to execute ShellCheck and the test suite.
- Commits should be descriptive and reference related issues when possible.

## Coding guidelines
- Shell scripts should target POSIX `sh` unless `bash` features are required.
- Avoid style warnings reported by ShellCheck where practical.
- Keep scripts small and composable; functions are preferred over large blocks.

## Reporting issues
If you encounter problems, please include steps to reproduce and relevant logs in your bug report.

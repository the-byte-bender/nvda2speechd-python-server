# nvda2speechd Python Server Implementation

## Overview

This project includes a Python implementation of the [nvda2speechd](https://github.com/RastislavKish/nvda2speechd) server. This version is intended to be more comprehensive, easier to develop and maintain, and potentially include additional future improvements.

## Setup Instructions

Follow these steps to set this project up:

1. **Install pipenv:** This can be done using pipx or your Linux distribution's package manager.

2. **Navigate to this repository:** This can be done with the `cd` command.

3. **Install dependencies with pipenv:** Run the command `pipenv install`.

4. **Get Python path:** Run `pipenv run which python` and note down the resulting path. The path should resemble `/home/user/.local/share/virtualenvs/nvda2speechd-python-server-LHzG5Lrx/bin/python`. Remove `/bin/python` from the path and remember the reduced path, for example `/home/user/.local/share/virtualenvs/nvda2speechd-python-server-LHzG5Lrx/`.

5. **link the Python speechd module:** Run the command `ln -s /usr/lib/python3.11/site-packages/speechd <path>/lib/python3.11/site-packages/`, replacing `<path>` with the one noted down in step 4.

## Usage Instructions

Once you have completed the setup, simply run `pipenv run python server.py` to start the server.

# Contributions, Issues, and Collaboration

Everyone is welcome to contribute to this project! Whether you are experienced or a beginner, your involvement can make a big difference. If you're unsure about where to start, take a look at the open issues or consider improving our documentation. We appreciate whatever help you can provide.

## Contributing

You can contribute in several ways:

- **Improving the code:** If you spot an area of the code that could be improved, feel free to make those improvements and submit a pull request. Remember to describe your changes in detail so it's easy for others to follow.

- **Reporting issues:** If you come across a bug or something that doesn't seem quite right, please open a new issue on the GitHub page. Make sure to document the problem clearly and provide as much detail as possible to help us understand what's going wrong.

- **Suggesting enhancements:** If you have an idea for a new feature or improvement, we'd love to hear it! Please open a new issue, and label it as an enhancement.

## Issues

If you're experiencing problems  or you found a bug, don't hesitate to create an issue! Provide as much detail as possible, such as:

- What you were trying to do
- Any error messages you received
- Steps to replicate the issue.

This helps to ensure that the issue can be resolved in the quickest and most efficient way possible.

## Collaboration

No idea is too small, and no contribution goes unappreciated. everyone’s thoughts and ideas are welcomed and encouraged!

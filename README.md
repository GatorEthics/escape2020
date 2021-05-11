![Escape 2020 Logo](escape2020_logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

# Escape 2020
A story-based game. Can you open the vaccine center and avoid getting COVID?

Allegheny College Ethics Technical Leaders - Mozilla Grant

*Day-one Contributors:* Christian Lussier & Dr. Bonham-Carter

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Running the Game](#running-the-game)
   - [Running with local Python installation](#running-with-local-python-installation)
   - [Running with Docker](#running-with-docker)
- [Ethical Discussion](#ethical-discussions)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [Contact](#contact)


## About
Escape 2020 is a story-based game, where players are vaccine center managers and must get to the center on time without contracting the virus. There are a number of randomized scenarios and story events that are based on user responses to story-based prompts given throughout the game. One idea the game focuses upon is that of wearing a mask and the implications of what happens when people don't. Not only can forgoing a mask be detrimental to ones own health, but it can also impact those around them as the virus can spread with ease.

## Features
Escape 2020 is a game and with this there are a few key features it offers:
- Command-line interface
   - Color class to enhance the visual experience
- Welcome message with directions
- Story-based game implementation
   - Randomized story events and scenarios

## Installation

If `git` is installed on your machine, you may clone the repository on your local machine by running the command:
```
git clone https://github.com/Allegheny-Ethical-CS/escape2020.git
```

You can then `cd` (or enter) the project root folder:
```
cd escape2020
```

The project can either be run locally or by installing `Docker`. More detail is provided in the next section of the README, which discusses running the game.

## Running the Game

After completing the installation steps to clone the project locally, there are a few different ways in which the game can be run! These methods including running the Python program locally on your computer or using a Docker container.

### Running with local Python Installation

If you have [Python](https://www.python.org/downloads/) installed locally, you can run the project with ease, without installing any other external tools or library. It is recommended that a `python3` (a version of Python higher than 3) is utilized.

*To run the game, use the following command:*
```
python3 src/escape2020.py
```


### Running with Docker

The program can be run within a Docker Container using Docker Desktop. For more information on how to install this tool, view [this](https://www.docker.com/) resource.

There are builder scripts for each type of machine. First ensure you are in the main project directory, the same one in which this README resides. To run the `Mac OS` version for instance, you would use the following commands:

1. To build the container, use the following command:
```
sh ./docker/build_macOS.sh
```
2. To enter the newly built Docker container, use the following command:
```
sh ./docker/run_macOS.sh
```

3. After entering the container, run the program using the following command:
```
python3 src/escape2020.py
```

#### OS-specific scripts to build and run containers
The following bash scripts simplify building the container.

| OS  | Building  | Running  |
|---|---|---|
| MacOS  		|  `./docker/build_macOS.sh` |  `./docker/run_macOS.sh` |
| Linux   	|  `./docker/build_linux.sh` | `./docker/run_linux.sh`  |
| Windows 	|  `docker/build_win.bat` 		|  `docker/run_win.bat` |

These files may be found in the `docker/` directory and the builder requires a copy of `Dockerfile`, which can be found in the main directory of the project, to run.

## Ethical Discussions
The COVID-19 pandemic has brought up many new issues and discussions in the area of ethics. The biggest ethical problem COVID-19 has brought about is that of wearing a mask. There are those who do not want to wear a mask, claiming the virus is a hoax or that a mask won't protect them. Then there are those who wear masks. Are you an unethical person if you don't wear a mask? Some might say yes. Not only do you have a higher risk of getting the virus yourself, but you also could spread it others, most importantly the high-risk population. That doesn't seem very ethical. Wearing a mask is the ethical thing to do, because it helps keep everyone safe.

A similar discussion could arise in the area of vaccines. What are the ethical societal implications that come with choosing to get or skip the vaccine?

## Future Work
There are a number of different tasks that could be completed in the future to enhance the project. Some current ideas include:
- Adding more story elements, make the plot more complex.
- Tracking the number of individuals that the player came in contact with. Provide a "COVID contact tracing report" as output at the end of the project.
- Adding mini-games to the current game. For instance, a maze mini-game could be added when you are trying to get through a certain portion of the city.

## Contributing
We encourage you to contribute if want to take on any of the tasks mentioned as apart of the Future Work section or enhance the game on your own! Please be respectful when contributing to this project's community!

Please read the [Project Contribution Guide](https://github.com/Allegheny-Ethical-CS/blob/escape2020/contributing.md) before committing to this project so you can get a feel for our standards and workflow.

## Contact

If you have any questions, concerns, or comments for this project, please contact:
- [Christian Lussier](https://github.com/lussierc) -- lussierc@allegheny.edu
- [Dr. Bonham-Carter](https://github.com/obonhamcarter) [Faculty Advisor] -- obonhamcarter@allegheny.edu

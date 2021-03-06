# DAMPP 🚢

DAMPP (gui) is a Python based program to run simple webservers using **MySQL, Php, Apache and PhpMyAdmin** inside of Docker containers. 

This can be run on any `Ubuntu` based system. 

## Screenshots 📷

Home screen

<img src="dampp/resources/screenshots/Screenshot from 2022-02-12 14-28-43.png"/>

Add New Project

<img src="dampp/resources/screenshots/Screenshot from 2022-02-12 14-28-51.png"/>

Edit Ports

<img src="dampp/resources/screenshots/Screenshot from 2022-02-12 14-28-57.png"/>

About

<img src="dampp/resources/screenshots/Screenshot from 2022-02-12 14-29-07.png"/>


## Requirements ✔️

- Python3
- pip
- Docker
- Docker-compose

## Installation ✨

Install `PyQt5` using pip.

```python
pip install PyQt5
```

Create a directory called `.bin` in your home directory.

```bash
mkdir ~/.bin
```

Change current directory to `.bin`.

```bash
cd ~/.bin
```

Clone the repository.

```bash
git clone https://github.com/s3h4n/DAMPP.git
```

## Confiuguration 🔧

Create aliases for your shell config file so you can run the program easily.

### Bash

Add following line to your `.bashrc` file. 

You can find this file in your home `~/` directory.

```
alias dampp='~/.bin/dampp/dampp.sh'
```

### Fish

Add following line to your `config.fish` file. 

You can find this file in `~/.config/fish` location.

```
alias dampp='~/.bin/dampp/dampp.sh'
```

For other shells like `zsh`, you can also add the aliases.

## Usage 🔥

Simply type following command in your terminal.

```bash
dampp
```
## Contributing 🤝

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



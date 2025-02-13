
# Install n' Use

`Install n' Use` is a Python script designed to automate the installation, upgrade, and management of Python packages. It ensures that required packages are installed and upgraded if necessary, and handles errors gracefully if packages are not found.

## Features

- **Install packages**: Automatically installs a package if it is not found.
- **Install specific versions**: Installs a specific version of a package.
- **Upgrade packages**: Upgrades a package to the latest version.
- **Upgrade specific versions**: Upgrades a package to a specific version.

## Functions

### `install(package)`
Installs a package if it is not found on your system.

#### Arguments:
- `package` (str): The name of the package to install.

#### Example:
```python
install("tkinter")
```

### `install_specific(package, version, name)`
Installs a specific version of a package and assigns it to a custom variable name.

#### Arguments:
- `package` (str): The name of the package to install.
- `version` (str): The version of the package to install.
- `name` (str): The name to assign the installed package.

#### Example:
```python
install_specific("numpy", "1.21.0", "np")
```

### `upgrade(package)`
Upgrades a package to the latest version.

#### Arguments:
- `package` (str): The name of the package to upgrade.

#### Example:
```python
upgrade("requests")
```

### `upgrade_specific(package, version, name)`
Upgrades a package to a specific version and assigns it to a custom variable name.

#### Arguments:
- `package` (str): The name of the package to upgrade.
- `version` (str): The version of the package to upgrade to.
- `name` (str): The name to assign the upgraded package.

#### Example:
```python
upgrade_specific("requests", "2.26.0", "req")
```

## Error Handling

- If a package is not found, the script attempts to install it.
- If the package installation or upgrade fails, an exception will be raised:  
  `PyPIError: Package not Found on PyPI`.

## Installation

To use `Install n' Use`, simply download the script and include it in your project.

## Requirements

- Python 3.x
- `pip` (Python's package installer)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

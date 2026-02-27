# ft_package

A simple Python package that provides a utility function
to count occurrences of a value in a list.

## Installation

```bash
pip install .
```

## Clean & Uninstall
```bash
rm -rf build dist *.egg-info
pip uninstall ft_package
```

## Project Structure

```
ft_package
├── LICENSE
├── README.md
├── ft_package
│   ├── __init__.py
│   └── count_in_list.py
├── pyproject.toml
```

## Check Pakage
```bash
pip show -v ft_package  
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
```

## Contributing

This is an educational project. Contributions are welcome for learning purposes.

## License

MIT License

## Author

psaeyang
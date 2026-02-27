# ft_package

A simple Python package that provides a utility function
to count occurrences of a value in a list.

## Installation

Build the package:
```bash
python3 -m build
```

Install from source:
```bash
pip install .
```

Or install from built files:
```bash
pip install ./dist/ft\_package-0.0.1.tar.gz
pip install ./dist/ft\_package-0.0.1-py3-none-any.whl
```

## Clean & Uninstall
```bash
rm -rf build dist *.egg-info
pip uninstall ft_package
```

## Project Structure

```
ft_package
├── ft_package
│   ├── __init__.py
│   └── count_in_list.py
├── LICENSE
├── pyproject.toml
├── README.md
```

## Check Package
```bash
pip show -v ft_package  
```

## Usage

```python
from ft_package import count_in_list

# Count how many times "toto" appears in the list
print(count_in_list(["toto", "tata", "toto"], "toto"))
# Output: 2
```

## Contributing

This is an educational project. Contributions are welcome for learning purposes.

## License

MIT License

## Author

psaeyang
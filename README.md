# Disk Backed Collections

A Python package for memory-efficient disk-backed dictionaries and lists using PyTorch.

## Installation

You can install this package using pip:

```bash
pip install disk_backed_collections
```

## Usage

```python
from disk_backed_collections import DiskBackedDict, DiskBackedList

# Example usage of DiskBackedDict
disk_dict = DiskBackedDict()
disk_dict['model'] = torch.nn.Linear(10, 1)
model = disk_dict['model']
print(model)

# Example usage of DiskBackedList
disk_list = DiskBackedList()
disk_list.append(torch.nn.Linear(10, 1))
model = disk_list[0]
print(model)
```

## License

This project is licensed under the MIT License.

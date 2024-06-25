import os
import uuid
import torch

class DiskBackedDict:
    def __init__(self):
        self.store = {}
        self.temp_dir = os.path.join("/tmp", str(uuid.uuid4()))
        os.makedirs(self.temp_dir, exist_ok=True)

    def __setitem__(self, key, value):
        file_path = os.path.join(self.temp_dir, f"{key}.pt")
        torch.save(value, file_path)
        self.store[key] = file_path

    def __getitem__(self, key):
        if key in self.store:
            file_path = self.store[key]
            return torch.load(file_path)
        else:
            raise KeyError(f"Key '{key}' not found.")

    def __delitem__(self, key):
        if key in self.store:
            file_path = self.store.pop(key)
            if os.path.exists(file_path):
                os.remove(file_path)
        else:
            raise KeyError(f"Key '{key}' not found.")

    def __contains__(self, key):
        return key in self.store

    def __len__(self):
        return len(self.store)

    def keys(self):
        return self.store.keys()

    def items(self):
        return {key: self[key] for key in self.store}.items()

    def values(self):
        return [self[key] for key in self.store]

    def clear(self):
        for file_path in self.store.values():
            if os.path.exists(file_path):
                os.remove(file_path)
        self.store.clear()

    def __del__(self):
        self.clear()
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)


class DiskBackedList:
    def __init__(self):
        self.store = []
        self.temp_dir = os.path.join("/tmp", str(uuid.uuid4()))
        os.makedirs(self.temp_dir, exist_ok=True)

    def append(self, value):
        file_path = os.path.join(self.temp_dir, f"{len(self.store)}.pt")
        torch.save(value, file_path)
        self.store.append(file_path)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.store):
            raise IndexError("list index out of range")
        file_path = self.store[index]
        return torch.load(file_path)

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self.store):
            raise IndexError("list assignment index out of range")
        file_path = self.store[index]
        torch.save(value, file_path)

    def __delitem__(self, index):
        if index < 0 or index >= len(self.store):
            raise IndexError("list index out of range")
        file_path = self.store.pop(index)
        if os.path.exists(file_path):
            os.remove(file_path)
        for i in range(index, len(self.store)):
            new_file_path = os.path.join(self.temp_dir, f"{i}.pt")
            os.rename(self.store[i], new_file_path)
            self.store[i] = new_file_path

    def __len__(self):
        return len(self.store)

    def clear(self):
        for file_path in self.store:
            if os.path.exists(file_path):
                os.remove(file_path)
        self.store.clear()

    def __del__(self):
        self.clear()
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

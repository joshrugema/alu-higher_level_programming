# Python - Inheritance

Classes that inherit other classes: `MyList` (a list), `BaseGeometry`, `Rectangle` and `Square`. Also `isinstance`, `issubclass`, `type` and `super()`.

| File | What it does |
|------|--------------|
| 0-lookup.py | Returns the list of attributes and methods of an object |
| 1-my_list.py | MyList inherits list and adds print_sorted() |
| 2-is_same_class.py | True if an object is exactly an instance of a class |
| 3-is_kind_of_class.py | True if an object is an instance of a class or of a subclass |
| 4-inherits_from.py | True only if the object's class is a subclass of the given class |
| 5-base_geometry.py | Empty class BaseGeometry |
| 6-base_geometry.py | Adds area(), which raises an Exception |
| 7-base_geometry.py | Adds integer_validator() |
| 8-rectangle.py | Rectangle inherits BaseGeometry, validates width and height |
| 9-rectangle.py | Adds area() and `__str__` to Rectangle |
| 10-square.py | Square inherits Rectangle |
| 11-square.py | Adds `__str__` to Square: [Square] size/size |
| tests/1-my_list.txt | Doctests for 1-my_list.py |
| tests/7-base_geometry.txt | Doctests for 7-base_geometry.py |

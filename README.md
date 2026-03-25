PyRef/README.md

# PyRef: Python Programming Language Reference

PyRef is a Python learning quick reference, organized into modules covering the fundamentals to advanced topics.

---

## Project Structure

### c1_simple_datatypes

- **m1_variables.py**: Variable declaration, assignment, constants, naming conventions, using dictionaries as variables.
- **m2_none_type.py**: The `None` object, NoneType, singleton property, None vs. other “empty” values, use as placeholder and default return.
- **m3_duck_typing.py**: Dynamic typing, duck typing principle, type and reference counter in objects.
- **m4_booleans.py**: Boolean type, truth values, booleans as subclass of int, permissions example, converting bool to int.
- **m5_numbers.py**: Integer, float, complex numbers, arithmetic operations, immutability.
- **m6_strings.py**: String creation, immutability, escape sequences, concatenation, formatting.
- **m7_datatype_conversions.py**: Explicit type conversions, using built-in type functions.
- **m8_task_mileage_converter.py**: User input, error handling, converting kilometers to miles.

### c2_conditional_logic

- **m1_conditional_expressions.py**: Comparison operators, membership operators.
- **m2_truhiness_falsiness.py**: Truthy/falsy values, customizing truthiness with `__bool__` and `__len__`.
- **m3_conditionals.py**: If-else statements, ternary operator, pattern matching with `match-case`.

### c3_loops_iterations

- **m1_for_and_while_loops.py**: For loops (strings, lists, ranges), while loops, enumerate, range, reverse/stepped ranges.

### c4_container_datatypes

- **m1_lists.py**: List creation, types, accessing/modifying, slicing, append/remove.
- **m2_dictionaries.py**: Dictionary creation, types, accessing elements, `.get()`, `fromkeys`, keyword arguments.
- **m3_tuples.py**: Tuple creation, types, accessing elements, immutability.
- **m4_named_tuples.py**: Creating named tuples, using named fields, extending named tuples.
- **m5_sets.py**: Set creation, uniqueness, accessing/modifying, membership testing.

### c5_functions_lambdas

- **m1_basic_functions.py**: Advantages of functions, definition syntax, positional/variable/keyword arguments.
- **m2_intermediate_functions.py**: Positional-only and keyword-only arguments, argument restrictions.
- **m3_advanced_functions.py**: Higher-order functions, closures, passing functions as arguments.
- **m4_lambdas.py**: Lambda (anonymous) functions, various argument patterns, use cases.
- **m5_builtin_functions.py**: Common built-in functions (abs, all, any, callable, etc.), using built-ins with lambdas/HOFs.
- **m6_functions_odds_and_ends.py**: Passing functions as arguments, closures for state, function factories.

### c6_iterators_generators

- **m1_python_iterators.py**: Iterators and iterables, iterator protocol (`__iter__`, `__next__`), custom iterator examples.
- **m2_python_generators.py**: Generator functions, `yield`, function vs. generator, memory efficiency, counting generator.

### c7_modules_packages

- **m3_packages_in_python.py**: Creating and using packages, `__init__.py`, importing modules from packages.
- **p1_regular_package/m1_modules_in_python.py**: Module structure, constants, classes, importing and using modules.
- **p1_regular_package/m2_import_system.py**: Python import system, module search path, absolute/relative imports.
- **p2_namespace_package/p2a_snake_say/snake/utils1.py**: Utility for speech bubbles, displaying text with a snake.
- **p2_namespace_package/p2b_snake_sing/snake/utils2.py**: Utility for displaying a singing snake.

### c8_oop_classes_objects

- **m1_class_definitions.py**: Class definition, class/instance/static methods, class/instance variables.
- **m2_class_objects.py**: Working with class objects, attribute reference, object instantiation.
- **m3_instance_objects.py**: Working with instance objects, referencing class/static/instance attributes.
- **m4_oop_polymorphism.py**: OOP polymorphism, method overriding, duck typing.
- **m5_oop_encapsulation.py**: Encapsulation, private attributes, property decorators, name mangling, composition, aggregation.
- **m6_oop_inheritance.py**: Inheritance, single/multiple inheritance, method overriding, `super()`.
- **m7_oop_abstraction.py**: Abstraction, abstract classes, interfaces, ABC module.
- **m8_managed_attributes.py**: Managed/unmanaged attributes, attribute control and validation.
- **m9_property_protocol.py**: Property protocol, accessor/mutator/deleter, using `property()`.
- **m10_descriptor_protocol.py**: Descriptor protocol, `__get__`, `__set__`, `__delete__`, computed attributes.
- **m11_descriptor_usages.py**: Custom validators using descriptors, attribute validation.
- **m12_get_set_and_del_attr.py**: `getattr`, `setattr`, `delattr` usage, attribute access control.

### c9_error_handling

- **m1_exception_hierarchy.py**: Python exception hierarchy, built-in exception classes.
- **m2_raising_exceptions.py**: Raising exceptions, `raise` statement, custom exceptions, exception chaining.
- **m3_defining_exceptions.py**: Defining custom exceptions, adding attributes, usage examples.
- **m4_handling_exceptions.py**: Exception handling with `try-except`, multiple excepts, `else`/`finally` blocks.

### c10_decorators

- **m1_function_decorators.py**: Function decorators, adding functionality, decorator syntax.
- **m2_tracing_function_calls.py**: Tracing function calls with decorators, maintaining state.
- **m3_class_method_decoration_pitfalls.py**: Pitfalls of decorating class methods, correct/incorrect usage.
- **m4_class_decorators.py**: Class decorators, singleton pattern, managing instance construction.

### c11_metaclasses

- **m1_types_and_classes.py**: Types and classes in Python, metaclass basics.

### c12_http_requests

- **m1_api_config.py**: API configuration, constants for requests.
- **m2_get_requests.py**: Making GET requests, handling responses, retries.
- **m3_post_requests.py**: Making POST requests, sending payloads, handling responses.
- **m4_put_requests.py**: Making PUT requests, updating resources.
- **m5_delete_requests.py**: Making DELETE requests, deleting resources.

---

## Getting Started

1. **Clone the repository:**

    ```sh
    git clone <repo-url>
    cd PYLRN
    ```

2. **Set up a virtual environment (recommended):**

    ```sh
    python -m venv .venv
    # On Unix or MacOS:
    source .venv/bin/activate
    # On Windows:
    .venv\Scripts\activate
    ```

---

## Example Usage

To run an example script, navigate to the desired module and execute it with Python. For example:

```sh
cd src/c1_simple_datatypes
python m1_variables.py
```

---

Happy learning!

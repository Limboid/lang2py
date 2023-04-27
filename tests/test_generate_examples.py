from lang2py import generate_examples
from lang2py._utils import issubtype


def test_generate_examples(type):
    examples = generate_examples(type, num_examples=3)
    assert isinstance(examples, list), f"Expected list, but got {type(examples)}"
    assert len(examples) == 3, f"Expected 3 examples, but got {len(examples)}"
    for example in examples:
        assert issubtype(example, type)


def test_generate_examples_int():
    test_generate_examples(int)


def test_generate_examples_str():
    test_generate_examples(str)


def test_generate_examples_bool():
    test_generate_examples(bool)


def test_generate_examples_float():
    test_generate_examples(float)


def test_generate_examples_none():
    test_generate_examples(type(None))


def test_generate_examples_list():
    test_generate_examples(list[int])


def test_generate_examples_tuple():
    test_generate_examples(tuple[int, str])


def test_generate_examples_dict():
    test_generate_examples(dict[str, int])


def test_generate_examples_union():
    test_generate_examples(int | str)


def test_generate_examples_invalid_type():
    try:
        generate_examples(float, num_examples=3)
        assert False, "Expected TypeError to be raised for unsupported type"
    except TypeError:
        pass


def test_generate_examples_invalid_union():
    try:
        generate_examples(float | list[int], num_examples=3)
        assert False, "Expected ValueError to be raised for unsupported union type"
    except ValueError:
        pass

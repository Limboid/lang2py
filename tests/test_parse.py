from lang2py import parse


def test_parse(input_data, input_type):
    input_data_repr = repr(input_data)
    parsed_data = parse(input_data_repr, input_type)
    assert parsed_data == input_data, f"{parsed_data} (parsed) != {input_data} (input)"


def test_parse_int():
    test_parse(42, int)


def test_parse_str():
    test_parse("hello", str)


def test_parse_bool():
    test_parse(True, bool)
    test_parse(False, bool)


def test_parse_float():
    test_parse(3.14, float)


def test_parse_none():
    test_parse(None, type(None))
    test_parse(None, type(None))


def test_parse_list():
    test_parse([1, 2, 3], list[int])
    test_parse(["hello", "world"], list[str])
    test_parse([1, 2, 3], list[int | str])
    test_parse(
        [{"name": "john", "age": 30}, {"name": "jane", "age": 25}],
        list[dict[str, str | int]],
    )


def test_parse_tuple():
    test_parse((1, 2, 3), tuple[int, int, int])
    test_parse(("hello", "world"), tuple[str, str])
    test_parse((1, 2, 3), tuple[int | str, ...])
    test_parse(("john", 30), tuple[str, int])


def test_parse_dict():
    test_parse({"name": "john", "age": 30}, dict[str, str | int])
    test_parse({1: "hello", 2: "world"}, dict[int, str])

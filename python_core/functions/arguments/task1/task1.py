from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc, *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """

    for f in filters:
        data = f(data)

    return selector(data)


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""

    return lambda data: [
        {col: row[col] for col in columns if col in row} for row in data
    ]


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    return lambda data: [row for row in data if row.get(column) in values]


def test_query():
    friends = [{"name": "Sam", "gender": "male", "sport": "Basketball"}]
    value = query(
        friends,
        select(*("name", "gender", "sport")),
        field_filter(*("sport", *("Basketball", "volleyball"))),
        field_filter(*("gender", *("male",))),
    )
    assert [{"gender": "male", "name": "Sam", "sport": "Basketball"}] == value


if __name__ == "__main__":
    test_query()

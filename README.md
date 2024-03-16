![sesgx logo](sesgx_header.png)
# scopus-client

> Async Scopus Client to interact with their HTTP interface. Includes automatic retry and API keys swapping.

## Usage

```python
import asyncio

from scopus_client import ScopusClient, InvalidStringError


API_KEYS: list[str] = []


async def main():
    search_string = 'TITLE-ABS-KEY("machine learning" and "code smell") AND PUBYEAR > 2010 AND PUBYEAR < 2020'

    client = ScopusClient(API_KEYS)

    entries: list[dict] = []

    try:
        async for page in client.search(search_string):
            entries.extend(page.entries)

    except InvalidStringError:
        print(f"String `{search_string}` is invalid. It might be too long.")

    print(entries)


if __name__ == "__main__":
    asyncio.run(main())
```

## Development

Create a virtual environment:

```sh
python -m venv .venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate  # if using linux
```

Install the project in editable mode:

```sh
pip install -e .
```

### Testing

Install test dependencies:

```sh
pip install ".[dev-test]"
```

Run the test command from the provided script:

```sh
./scripts/test.sh
```

After running the tests, a coverage report will be available in `htmlcov/index.html`. You can run the following command to open the report using google chrome:

```
google-chrome htmlcov/index.html
```

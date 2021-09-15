# TTSImport API

This API provides `fftcgtool` capabilities over HTTP.

## Usage

Just run the `main` submodule as a script:

```bash
python -m ttsimport.main
```

## Configuration

Runtime configuration of the API is done using environment variables.

- `PRODUCTION_MODE` – If `true`, the API will start without development patches (boolean, default `false`)
- `OPENAPI_URL` – Where the API will publish an OpenAPI schema (string, default `"/openapi.json"`)
- `DOCS_URL` – Where the API will publish its documentation/Swagger UI (string, default `"/docs"`)
- `REDOC_URL` – Where the API will publish its documentation/Redoc UI (string, default `"/redoc"`)

## Installation

You can install `ttsimport` if you have at least python version `3.9` with `pip` installed. To test,
run `python --version` or similar.

- Install from this repository: Use `pip install "git+https://github.com/ldericher/ttsimport"`.
- Or from your local source: Clone this repository and run `pip install /path/to/ttsimport`.

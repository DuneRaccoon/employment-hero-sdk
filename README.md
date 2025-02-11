
---

### How to Use

1. **Install the package** (for local development you can run `pip install -e .` in the root directory where `setup.py` is located).
2. **Instantiate the client** with your API key and business ID.
3. **Access resources dynamically** (e.g. `client.employee`) and call methods like `.fetch()`, `.list()`, `.create()`, etc.

This SDK is designed to be extended and adapted as needed. You can add new API wrappers in the `apis/` folder and corresponding Pydantic schemas in the `schemas/` folder. Enjoy building your integration with the Employment Hero API!

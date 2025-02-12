# Employment Hero SDK

Simple, lightweight and efficient Python client wrapper for interacting with the Employment Hero/Key Pay API. It provides a consistent, chainable interface for both synchronous and asynchronous operations, making it easy to fetch, create, update, and delete resources....

## Features

- **Simple, Chainable API:** Navigate endpoints with intuitive chaining (e.g. `client.business("biz123").employees.fetch("emp456")`).
- **Synchronous and Asynchronous Support:** Choose the mode that best fits your application's needs.
- **Built-in Pagination:** Easily fetch all pages of data using built-in pagination methods.
- **Caching:** Cache business listings to reduce unnecessary API calls.
- **Error Handling:** Receive informative exceptions for API errors.
- **Throttling:** Automatically handle rate limiting and backoff.

## Installation

You can install the package directly from PyPI:

```bash
pip install employment-hero-sdk
```

## Usage

### Synchronous Example
```python
from employment_hero_sdk import EmploymentHeroClient

# Initialize the client with your API key
client = EmploymentHeroClient(api_key="your_api_key")

# Retrieve all available businesses (cached)
businesses = client.business()  # Returns a list of Business objects
for biz in businesses:
    print(biz)

# Retrieve a specific business by ID
biz = client.business("business_id_123")

# Fetch an employee from a specific business
employee = biz.employee("employee_id_456")
print(f"Employee: {employee.full_name}")
```

### Asynchronous Example
```python
import asyncio
from employment_hero_sdk import EmploymentHeroClient

async def main():
    # Initialize the client with your API key
    client = EmploymentHeroClient(api_key="your_api_key")
    
    # Retrieve all available businesses asynchronously
    businesses = await client.business()  # Returns a list of Business objects
    for biz in businesses:
        print(biz)
    
    # Retrieve a specific business by ID asynchronously
    biz = await client.business("business_id_123")
    
    # Fetch an employee from the specific business asynchronously
    employee = await biz.employee("employee_id_456")
    print(f"Employee: {employee.full_name}")

asyncio.run(main())
```

### Dynamic Paths

We also dynamically load paths if there isn't an api model for the path, which will return data if the path exists. The data will just be returned as a dictionary.

```python
from employment_hero_sdk import EmploymentHeroClient

EMPLOYMENT_HERO_API_KEY = "api_key"

client = EmploymentHeroClient(api_key=EMPLOYMENT_HERO_API_KEY)

for business in client.business().values():
    print(business.show())
    for employee in business.employee():
        print(employee.show())
        opening_balances = employee.openingbalances() #/api/v2/business/{busness_id}/employee/{employee_id}/openingbalances is a valid path
        print(opening_balances)
        break
```


## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/). 
You are free to use, share, and modify the software for **non-commercial purposes** only.

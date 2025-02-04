# Number Classification API

## Overview
This API takes a number as input and returns interesting mathematical properties about it, along with a fun fact.

## Features
- Determines whether a number is prime.
- Checks if a number is a perfect number.
- Identifies if a number is an Armstrong number.
- Classifies the number as even or odd.
- Calculates the sum of its digits.
- Fetches a fun fact from Numbers API.

## API Endpoint
**GET** `/api/classify-number?number={number}`

### Request Example
```sh
GET http://your-domain.com/api/classify-number?number=371
```

### Successful Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
If the input is not a valid number:
```json
{
    "number": "alphabet",
    "error": true
}
```

## Properties Classification
The `properties` field contains one of the following:
1. `["armstrong", "odd"]` - if the number is an Armstrong number and odd.
2. `["armstrong", "even"]` - if the number is an Armstrong number and even.
3. `["odd"]` - if the number is not an Armstrong number but is odd.
4. `["even"]` - if the number is not an Armstrong number but is even.

## Setup Instructions
### Requirements
- Python 3.8+
- FastAPI
- Requests library

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/slogan101/number-classification-api.git
   cd hng1
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On MAC
   venv\Scripts\activate # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the API:
   ```sh
   uvicorn main:app --reload
   ```

## Usage
Once the API is running, you can test it by opening a browser or using a tool like Postman to send a GET request.

## License
This project is licensed under the MIT License.


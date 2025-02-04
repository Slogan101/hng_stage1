from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_armstrong(n: int) -> bool:
    num_str = str(n)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == n

def is_prime(n: int) -> bool:
    # if n < 2:
    #     return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(n))



@app.get("/api/classify-number", status_code=status.HTTP_200_OK)
def classify_number(number):
    try:
        number = int(number)
    except ValueError:
        return {"number": "alphabet", "error": True}
    
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")
   



    return {
        "number": int(number),
        "is_prime": is_prime(abs(number)),
        "is_perfect": is_perfect(abs(number)),
        "properties": properties,
        "digit_sum": digit_sum(abs(number)),
        "fun_fact": requests.get(f"http://numbersapi.com/{int(number)}").text
    }










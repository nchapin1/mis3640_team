The stretch goal is a website that allows users to input the name of a crypto coin into a field, and the program runs a query on the input. It will return a list of matches. The user can input quantity owned and monetary investment made. Because crypto coins may be fractionally owned, it will be a challenge to create a standard to measure against. The options for baseline currency are yetto be decided. The user can create a portfolio object that contains multiple crypto objects. The user may input a loss-tolerance for individual crypto objects as well as the portfolio object. The program will display % total return for the individual crypto coins and the portfolio. The user may specify notification preferences (Example: Notify when portfolio depreciates 10%, but not when the crypto coin depreciates 10%). 

# Structure:

## User 
1. Name, Email 
### Django

### HTML
1. Input (dropdown) box for Crypto 
2. Input (numeric) for quantity owned
3. Input (dropdown) for currency type
4. Input (numeric) for invested funds
5. Input (numeric) for loss-tolerance

### Python
https://coinmarketcap.com/api/documentation/v1/#section/Endpoint-Overview

1. Crypto API
Test Key: b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c
Test API Domain: sandbox-api.coinmarketcap.com

https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/latest
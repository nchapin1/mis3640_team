# MIS3640 Team Project Repository
View it here: <https://crypto-safe.herokuapp.com/>

## Program Overview
This program is designed to allow a user to input the cryptocurrencies of their choice with specific parameters, such as target return and loss tolerance. The program will track the cryptocurrencies' current market prices and will send a email notification that specifies which assets appreciate or depreciate past these points.  

## Program Instructions
1. To begin, create a user account in the top right corner. 
2. After creating an account, the user will be directed to the home page. This is where users can add or delete cryptocurrencies.
3. To add a crypto, begin by filling out the "Symbol" input in uppercase letters. Be careful, there can only be one of every kind of crypto. Once added, the only way to recreate the crypto is by deleting the existing one. Then, insert the "Purchase Price". After, specify the "Target Return". For example, if a 5% return is desired, insert 95. Next, specify the "Loss Tolerance". The "Loss Tolerance" is the percentage point in which the user has decided to not allow for their crypto to depreciate past. For example, if a user did not want their BTC (Bitcoin) to depreciate past 5%, insert 95. Finally, click the "Add" button to create the crypto.
4. To remove a crypto, click the "Remove" button.
5. At any point a user may wish to "log out", click the logo to return to the home page.

## Required Libraries
1. Flask
2. Flask_SQLAlchemy
3. Flask_Mail
4. apscheduler



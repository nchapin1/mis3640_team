# Project Proposal 

## The Big Idea
### The Main Idea:
The premise of the project is to create an investment monitor for crypto assets. 
User inputs will be: crypto coin, quantity owned, and monetary investment made. 
Multiple types of crypto coins may be entered. 
The user has the option to track both an individual asset's value and the weighted portfolio's value.
The entry object will be stored on the server and tracked 24 hours a day.
The user will be able to specify an acceptable-loss percentage that the program will push an email notification if the asset / portfolio depreciates past (Example: 10% loss-tolerance. 10.01% depreciation => send notification).

### Exploration and Generation:
This project requires research on the topic of cryptocurrency and the crypto markets. As crypto coins remain
largely unregulated, investors run the risk of high volatility and scams. Thus, the research must be focused
on crypto coin origination, valuation, and payoff characteristics. The findings will be used to identify the
program requirements in tracking asset value. 

### Minimum Viable Product:
The minimum viable product is a website that allows users select a single crypto coin from a specified list of cryptocurrencies (this reduces the complexity of tracking high-yield, smaller cap crypto coins). The user will also input the quantity owned and the monetary investment made. The quantity will be restricted to whole assets. The monetary investment is limited to USD. The loss-tolerance will be set at a fixed percentage that will be determined after research. The program will notify if the singular coin's valuation depreciates past the loss-tolerance. 

### Stretch Goal:
The stretch goal is a website that allows users to input the name of a crypto coin into a field, and the program runs a query on the input. It will return a list of matches. The user can input quantity owned and monetary investment made. Because crypto coins may be fractionally owned, it will be a challenge to create a standard to measure against. The options for baseline currency are yetto be decided. The user can create a portfolio object that contains multiple crypto objects. The user may input a loss-tolerance for individual crypto objects as well as the portfolio object. The program will display % total return for the individual crypto coins and the portfolio. The user may specify notification preferences (Example: Notify when portfolio depreciates 10%, but not when the crypto coin depreciates 10%). 

## Learning Goals
### Team Learning Goals:
The team will gain experience in applying Python to the web platform. The project will likely require the use of API's for up-to-date financial information. The team shares an interest in learning about crypocurrency, crypto markets, and general portfolio management. 

#### Noah:
My individual learning goal is to gain experience with apply Python and Javascript to the website. I enjoyed working with Google AppMaker and Professor Gordon's Web Technologies class. I believe that Python could take such experiences to the next level. As an aside, I am pursuing a career in Finance. I am unfamiliar with cryptocurrency, so it should be an interesting topic to research. 

#### Jasmine:
I major in Computational and Mathematical Finance. However, I feel only financial analysis and mathematical finance is not enough to thrive in today’s market. There are multiple website allows users to track stock prices from the mass. However, I have not found any useful tool for me to track my crypto portfolio yet. Trading with technology to make prompt decision and orders is the key in crypto market as well. I aim to create a small software to integrate what I learned in Python class to facilitate my trading journey.
#### Cameron:
My individual learning goal during the course of this project is to gain a deeper knowledge and mastery of Python. In doing this, I hope to achieve a real viable piece of software that I am confident enough to put on my resume. I hope to pursue a career in venture capital thus I have sought out to strengthen my technical knowledge as VC and the tech world go hand-in-hand.

## Implementation Plan
1. Team members must build a solid conceptual foundation of cryptocurrency, crypto markets, and crypto price providers.
2. Evaluate and amend details in the project proposal so that the product more accurately addresses user needs.
3. Identify general project requirements to begin designing the base program. 
4. Write the code that satisfies general project requirements.

## Project Schedule
### Week 1:
1. Learn about cryptocurrency, crypto markets, and portfolio management.
2. Identify cryptocurrencies that will be offered in the MVP. 
3. Identify crypto markets that are considered reliable and trustworthy as sources of data. 
4. Consider potential API's to work with. 
5. Begin designing portfolio management "algorithm".
### Week 2:
1. Prepare for Design Review.
2. Launch basic project website. 
3. Begin coding the project framework. 
4. Create an artificial investment portfolio for future testing.
5. Implement feedback from Design Review.
### Week 3:
1. Prepare for Code Review.
2. Check to ensure code satisfies project requirements. 
3. Test to ensure market data is accurate and is reflected in artifical portfolio value.
4. Implement feedback from Code Review.
### Week 4:
1. Prepare for Mid-Project presentation. 
2. Write Notification javascript code for project website.
3. Test Notification systems with artificial investment portfolio and extremely low loss-tolerance levels.
### Week 5:
1. Update the project website. 
2. Begin designing the cryptocurrency query. (Identify sources that list less-common crypto assets).
3. Begin designing fractional ownership optionality.
4. Begin designing individual asset / portfolio monitoring optionality.
5. Begin designing user-specified loss-tolerance optionality.
6. Begin designing user-specified investment currency.
### Week 6:
1. MVP should be complete by Week 6. 
2. Evaluate feasibility of the accurate integration of items 2-6 in Week 5. 
3. Write code for items 2-6 in Week 5. 
4. Review project criteria and development progress.
### Week 7:
1. Update the project website.
2. Update the Notification javascript code to include any developments past MVP.
3. Write code for items 2-6 in Week 5. 
### Week 8:
1. Prepare for Final Demo. 
2. Patch any remaining issues.

## Collaboration Plan
The team is spread between three different time zones. Thus, the team has decided to delegate individual tasks that will be integrated after review on a weekly basis. There will be occassional pair programming, as time permits. The weekly evaluations allow for a rapid application development (RAD) methodology, where team members may act as stand-in stakeholders. 

## Risks
1. Availability of reliable data. Reliable and timely data are crucial, as market prices for cryptocurrencies are prone to violent fluctuations. 
2. Portfolio value is tied to some other form of currency, whether that be the USD or another cryptocurrency. The team must find the optimal way to illustrate a user's current portfolio value.
3. The data contained in our product may is not necessarily real time nor accurate. All prices are not provided by exchanges but rather by market makers, and so the price may not be accurate and may differ from the actual market price, meaning prices are indicative.
4. User from different countries are subject to different laws and regulations. Our product are not necessarily legal under laws, regulations or directives applicable to all users.
5. Certain parts of our product contain third-party provided service. Usage of such maybe separate copyright notices and licensing.

## Additional Course Content
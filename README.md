# **Weather Suggestion Bot**

In case you have been living under a rock, then you would know that it rained in the UK every day of 2026 so far.
A truly miserable experience. As someone who commutes for work, this meant that any day that I didn't check the weather, for one reason or another, meant that leaving my umbrella at home
was a fatal mistake.

Experiencing this realisation enough times had inspired me to create something for myself that, based on the forecast for that day, could give me some suggestions on the essentials I would need to take
with me for the day. There are many applications on the market and packages that already provide this type of service, but as someone looking to enhance their skills in API integration, automation, and some backend engineering,
I thought this would be the perfect opportunity to develop these skills whilst using things that are freely available to everyone. 

## **How it works**

* Daily weather data is retrieved from OpenWeather via their API
* Extract the forecast information (temperature, weather description, wind speed, etc).
* Gives a practical recommendation based on the data retrieved (Rain --> Make sure to bring your umbrella!)
* Recommendation is sent to a Telegram Bot that provides me with the recommendation
* Runs automatically (daily intervals) using GitHub Actions to provide daily recommendations.

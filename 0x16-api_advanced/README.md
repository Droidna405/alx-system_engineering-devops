# 0x16. API advanced
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.


## Understanding APIs and Navigating Documentation

## What is an API?

Think of an API as a waiter at a restaurant. When you order food, you don't go into the kitchen and cook it yourself. Instead, you tell the waiter what you want, and they bring it to you. An API is like a waiter for computers. It lets you ask for information or do things on another computer without knowing exactly how it's done.

Why do we use APIs?

APIs make it easy to get information from different sources. For example, you can use an API to get weather information, stock prices, or even the latest news.

How to read API documentation

API documentation is like a menu at a restaurant. It tells you what you can order (the endpoints) and how to order it (the parameters).

Here's an example of an API documentation page:
Image of API documentation page Opens in a new window
stoplight.io
API documentation page

The documentation will usually have a list of endpoints. Each endpoint has a description of what it does and the parameters you can use.

Here's an example of an endpoint:

/users/:id

Endpoint: /users/:id

Description: Gets information about a specific user.

Parameters:

    id: The ID of the user.

Response:
JSON

{
  "id": 12345,
  "name": "John Doe",
  "email": "johndoe@example.com"
}

Use code with caution.

This means that if you want to get information about user with ID 12345, you would make a request to the following URL:

https://api.example.com/users/12345

And you would get a response like this:
JSON

{
  "id": 12345,
  "name": "John Doe",
  "email": "johndoe@example.com"
}

Use code with caution.

This is just a simple example, but it gives you an idea of how to read API documentation.

Now, let's try a more complex example.

Imagine you are building a weather app.

You would use a weather API to get the weather information.

Here is an example of a weather API endpoint:

/current?lat={lat}&lon={lon}&appid={your_api_key}

Endpoint: /current

Description: Gets the current weather at a specific location.

Parameters:

    lat: The latitude of the location.
    lon: The longitude of the location.
    appid: Your API key.

Response:
JSON

{
  "coord": {
    "lon": -122.08,
    "lat": 37.42
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "main": {
    "temp": 282.82,
    "feels_like": 281.86,
    "temp_min": 280.15,
    "temp_max": 284.15,
    "pressure": 1013,
    "humidity": 81
  },
  "visibility": 10000,
  "wind": {
    "speed": 4.12,
    "deg": 190
  },
  "clouds": {
    "all": 0
  },
  "dt": 1623654381,
  "sys": {
    "type": 1,
    "id": 5122,
    "country": "US",
    "sunrise": 1623620902,
    "sunset": 1623665484
  },
  "timezone": -28800,
  "id": 420006343,
  "name": "Mountain View",
  "cod": 200
}

Use code with caution.

This response contains a lot of information, but you can focus on the parts you need, like the temperature, weather condition, and city name.

Now, let's try to find the temperature in this response.
JSON

{
  "main": {
    "temp": 282.82,
    "feels_like": 281.86,
    "temp_min": 280.15,
    "temp_max": 284.15,
    "pressure": 1013,
    "humidity": 81
  }
}

Use code with caution.

The temperature is 282.82 degrees Kelvin.

You can convert this to Celsius by subtracting 273.15.

So, the temperature is 9.67 degrees Celsius.

This is how you can use API documentation to find the information you need and parse the JSON response.

by Joel Mwangala <joemwangala@gmail.com>
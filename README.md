# exabeam-task

- In order to accomplish the task, I used the serverless framework. I also used AWS services: Lambda, which is a serverless computing platform, and API gateway to create a REST API that activates the Lambda function.
- The function “TwitterServerless1” that is accessing Twitter is written in Python 3.7 and uses the Tweepy package.
- The function doesn’t count retweets (using the “filter:retweets” flag).
- I used the “tweet_mode” flag to receive the full text of the each tweet and the “result_type” flag to receive the most recent tweets.
- If the number of tweets is even, the median is the average between the two middle values.
- The URL to the REST API:
https://qtvw555pch.execute-api.us-east-1.amazonaws.com/stage/median?term=trump
You can change the last word to a term of your choice.

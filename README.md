# Generate images using DALLE via SMS


![text-an-astronaut-coding](https://user-images.githubusercontent.com/45825464/216394752-3950dbcc-944a-4e08-b7d6-35442f917fdf.jpg)

## Requirements:
- You'll need an OpenAI API Key. You can [get one here](https://platform.openai.com/account/api-keys).
- ngrok
- Pip packages - openai, flask, twilio, python-dotenv

## Set an Environment Variable
Create a `.env` file in your root directory and add the following line:
`OPENAI_API_KEY=YOUR-OPENAI-API-KEY`

## Configure the Flask App
Run the flask app
`python app.py`

Use `ngrok` to make your flask app accessible over the internet.
`ngrok http 5000`
The above command will give you this output:
<img width="1156" alt="ngrok-terminal" src="https://user-images.githubusercontent.com/45825464/216396814-a41005a1-6a34-4587-b213-532c4d7ace47.png">

Use the forwarding URL as Webhook in the Twilio console in your number settings:
<img width="938" alt="Twilio-SMS-Console" src="https://user-images.githubusercontent.com/45825464/216396954-91e2247a-c158-4027-80ba-250ed5e18518.png">

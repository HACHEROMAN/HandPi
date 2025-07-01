# HandPi

HandPi Project with Alexa

## Description

This project connects a robotic hand with Alexa using various tools and services to enable voice control.

## Tools Used

- **RealVNC Viewer**: Used to remotely access the Raspberry Pi that controls the hand.
- **Alexa Developer Console**: The Alexa skill is configured using the JSON file located in the `alexaSkillDeveloper` folder.
- **Ngrok**: Used in the `HandPiCode` folder to expose a public endpoint that Alexa can call (ngrok http 5000).

## How It Works

1. The user interacts with the Alexa skill.
2. Alexa detects the intent and sends it to the public endpoint created by Ngrok.
3. The code in `HandPiCode` receives the intent, interprets it, and translates it into commands that the robotic hand understands.
4. The hand responds to the command and performs the corresponding movement.

> ⚠️ **Important:** The robotic hand control code must be placed inside the `uhandpi_software` folder for it to function properly.



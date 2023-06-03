Project Name: YouTube Video Downloader and Telegram Bot

Description:
This project is a YouTube video downloader program and a Telegram bot. It allows users to download YouTube videos directly to their device or receive the video in a Telegram chat. The program was developed during the learning process and written in Python.

Key Features:
- Utilizes the `pytube` library for interacting with the YouTube API and downloading videos.
- Implements a Telegram bot using the `telebot` library for seamless video sharing.
- Supports downloading YouTube videos by providing the video link and selecting the desired quality.
- Enables users to interact with the Telegram bot by sending messages and commands.
- Provides a command "/start" to initiate the bot and receive instructions.
- Parses the received video link and retrieves video details using the `YouTube` class.
- Prompts the user to select the desired video quality using a custom keyboard.
- Downloads the video based on the selected quality or displays an error message if an invalid choice is made.
- Uses the `send_chat_action` method to display a "upload_video" action while the video is being sent.
- Sends the video as a Telegram message using the `send_video` method.

To run the Telegram bot, you'll need to set up environment variables, including a TELEKEY that corresponds to your Telegram bot token. The program retrieves the TELEKEY using the `os` and `dotenv` libraries.

Please note that downloading YouTube videos may be subject to copyright restrictions, and it is important to comply with the terms and conditions of YouTube while using this program.

This project showcases the integration of YouTube video downloading functionality with a Telegram bot, providing users with different options for accessing and sharing videos. 😊

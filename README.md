# Youtube_AI_Agent

YouTube AI Agent for Fetching and Uploading Popular Tech Videos

# Overview
This project aims to develop an automated YouTube AI agent capable of fetching the most popular technology-related videos and uploading them to a specified YouTube channel. The agent utilizes Google APIs for authentication, fetching, and uploading videos, and the PyTube library for downloading videos.

# Features
Authentication: Secure OAuth 2.0 authentication to access YouTube Data API.
Fetch Popular Videos: Retrieve the most popular videos related to technology using YouTube Data API.
Download Videos: Download the fetched videos using PyTube.
Upload Videos: Upload the downloaded videos to a YouTube channel with appropriate metadata.
Logging: Comprehensive logging to track the progress and errors during the execution.
Detailed Functionality


# Authentication:
Utilizes OAuth 2.0 to authenticate and authorize the application.
Prompts the user to log in and grants necessary permissions for YouTube Data API access.


# Fetching Popular Videos:
Queries YouTube Data API for the most popular videos in the technology category.
Retrieves video details including video ID, title, and description.


# Downloading Videos:
Uses the PyTube library to download the video with the highest resolution available.
Stores the downloaded video in a specified directory.
Uploading Videos:

Utilizes YouTube Data API to upload the downloaded video.
Sets video metadata including title, description, tags, and category.
Handles different privacy statuses (public, private, or unlisted).

# Logging:
Logs important events, such as successful authentication, fetching, downloading, and uploading.
Logs errors with detailed messages to facilitate troubleshooting.
Code Structure
The code is modularized into distinct functions for better readability and maintainability:

authenticate(): Handles OAuth 2.0 authentication.
build_youtube_service(credentials): Initializes the YouTube service object.
fetch_popular_video(youtube): Fetches the most popular video related to technology.
download_video(video_id): Downloads the specified video.
upload_video(youtube, video_path, title, description): Uploads the video to the YouTube channel.
main(): The main function that orchestrates the process in a continuous loop.
Execution Flow
Authentication: The script starts by authenticating the user.
Fetch and Upload Loop: Continuously fetches the most popular technology video, downloads it, and uploads it to the channel.
Error Handling: Skips the current iteration if any step (fetching, downloading, or uploading) fails, and continues with the next video.
Dependencies
google-auth-oauthlib: For OAuth 2.0 authentication.
google-api-python-client: For interacting with YouTube Data API.
pytube: For downloading YouTube videos.
logging: For logging events and errors.

# Setup Instructions
Install Dependencies:
bash
Copy code
pip install google-auth-oauthlib google-api-python-client pytube

# Obtain Client Secrets File:
Download your client_secret.json file from the Google API Console.


Run the Script:



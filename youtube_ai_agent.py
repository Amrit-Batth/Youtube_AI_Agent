import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from pytube import YouTube
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Path to your client_secret.json file
client_secrets_file = "client_secret_129919883149-63k0i9oneqd6j3rdg8b7iepk5rie1snc.apps.googleusercontent.com.json"

# Scopes required by your app
scopes = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.upload"
]

# Create the flow using the client secrets file from the Google API Console
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)

# Run the local server to authorize the app
try:
    credentials = flow.run_local_server(port=8080)
except Exception as e:
    logging.error(f"Failed to run local server: {e}")
    exit()

# Build the YouTube service object
youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

# Fetch popular videos related to technology
try:
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",
        maxResults=1,
        videoCategoryId="28"  # Video category ID for Technology
    )
    response = request.execute()
    most_popular_video = response['items'][0]
    video_id = most_popular_video['id']
    video_title = most_popular_video['snippet']['title']
except Exception as e:
    logging.error(f"Failed to fetch most popular video: {e}")
    exit()

logging.info(f"Most Popular Video ID: {video_id}")
logging.info(f"Title: {video_title}")

# Download the video
try:
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    downloaded_video_path = stream.download(output_path="downloaded_videos")
    logging.info(f"Downloaded video to {downloaded_video_path}")
except Exception as e:
    logging.error(f"Failed to download video: {e}")
    exit()

# Upload the video to your channel
try:
    media = MediaFileUpload(downloaded_video_path, chunksize=-1, resumable=True) # type: ignore
    upload_request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"{video_title}",
                "description": "This is an automatically uploaded video.",
                "tags": ["tech", "technology"],
                "categoryId": "28"  # Technology category
            },
            "status": {
                "privacyStatus": "public"  # Or "private" or "unlisted"
            }
        },
        media_body=media
    )
    response_upload = upload_request.execute()
    logging.info(f"Uploaded video ID: {response_upload['id']}")
except Exception as e:
    logging.error(f"Failed to upload video: {e}")
    exit()






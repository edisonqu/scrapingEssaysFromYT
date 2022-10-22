from youtube_transcript_api import YouTubeTranscriptApi



video_id = "hMB9E_0FwIE"
text = ""
transcript = YouTubeTranscriptApi.get_transcript(video_id)


print(transcript)
for rawText in transcript:
    text += rawText['text'] +" "


with open('text1.txt', 'w') as f:
    f.write(str(text))
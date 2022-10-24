from youtube_transcript_api import YouTubeTranscriptApi


def getTranscript(video_id, title,listData):
    video_id = "hMB9E_0FwIE"
    text = ""
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    print(transcript)
    for rawText in transcript:
        text += rawText['text'] +" "

    listData.append(text)

    return listData
from youtube_transcript_api import YouTubeTranscriptApi


def getTranscripts(video_id):
    list_of_transcripts = []
    text = ""
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    print(transcript)
    for rawText in transcript:
        text += rawText['text'] +" "

    print(text)
    # if len(text.split()) > 2500:


    list_of_transcripts.append(text)

    return list_of_transcripts
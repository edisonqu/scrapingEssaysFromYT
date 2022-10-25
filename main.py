import cleanTranscriptWithOpenAI
import getTranscript
import scrapeYoutube
from cleanTranscriptWithOpenAI import *
from scrapeYoutube import *
from getTranscript import *
from writeToExcel import *


list_of_videoID = scrapeYoutube.scrapeVideos("Reading my College Essays that got me into Ivy League")
list_of_transcripts = []

for video_id in list_of_videoID:
    list_of_transcripts = getTranscript.getTranscripts(video_id)
    for each_transcript in list_of_transcripts:
        generated_text = cleanTranscriptWithOpenAI.formatAndGenerate(each_transcript)
        print("Generated Text is: "+ generated_text)
        print("The prompt is: "+find_prompt(generated_text))




if __name__ == '__main__':
    print()
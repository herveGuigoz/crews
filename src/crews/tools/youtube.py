from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeTranscript(BaseModel):
    """Input schema for YoutubeTranscript."""

    video_id: str = Field(
        ..., description="YouTube video ID to fetch the transcript for."
    )
    languages: list[str] = Field(
        ...,
        description="List of language codes to try for the transcript (e.g., ['fr', 'en']). Will try in order."
    )


class YoutubeTranscriptTool(BaseTool):
    name: str = "Youtube Transcript Custom Tool"
    description: str = "Fetches the transcript of a YouTube video in the specified language(s)"
    args_schema: Type[BaseModel] = YoutubeTranscript

    def _run(self, video_id: str, languages: list[str]) -> str:
        transcript_api = YouTubeTranscriptApi()
        video = transcript_api.fetch(video_id, languages=languages)
        transcript = " ".join([entry.text for entry in video])
        return transcript

from youtube_transcript_api import YouTubeTranscriptApi

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('youtebe_subtitles_server')

@mcp.tool(name = 'list_subtitles')
def list_subtitles(video_id) -> str:
    """
    获取youtebe视频字幕列表
    Args:
        video_id: 视频id
    Returns:
        list_transcript: 视频字幕列表
    """
    try:
        api = YouTubeTranscriptApi()
        languages = api.list(video_id)
    except Exception as e:
        return str(e)
    return languages

@mcp.tool(name = 'fetch_subtitles')
def fetch_subtitles(video_id, language) -> str:
    """
    获取youtebe视频字幕
    Args:
        video_id: 视频id
        language: 语言
            - zh-TW ("Chinese (Traditional)")
            - zh ("Chinese (Simplified)")
            - en ("English")
            - fr ("French")
    Returns:
        list_transcript: 视频字幕列表
    """
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=[language])
    except Exception as e:
        return str(e)
    return transcript

if __name__ == "__main__":
    #print(list_subtitles('bHcJCp2Fyxs'))
    print("=================================")
    print(fetch_subtitles('bHcJCp2Fyxs', 'zh-TW'))

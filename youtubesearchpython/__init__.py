from youtubesearchpython.core.constants import *
from youtubesearchpython.core.utils import *
from youtubesearchpython.extras import (Channel, Comments, Hashtag, Playlist,
                                        Suggestions, Transcript, Video)
from youtubesearchpython.search import (ChannelSearch, ChannelsSearch,
                                        CustomSearch, PlaylistsSearch, Search,
                                        VideosSearch)
from youtubesearchpython.streamurlfetcher import StreamURLFetcher

__title__ = "youtube-search-python"
__version__ = "1.6.2"
__author__ = "alexmercerind"
__license__ = "MIT"


""" Deprecated. Present for legacy support. """
from youtubesearchpython.legacy import SearchPlaylists
from youtubesearchpython.legacy import SearchVideos
from youtubesearchpython.legacy import SearchVideos as searchYoutube

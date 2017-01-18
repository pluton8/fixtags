#!/usr/bin/env python3

import collections

EpisodeTags = collections.namedtuple('EpisodeTags', [
    'genre'
    , 'year'
    ])
'''Represents a set of tags for a podcast episode.'''

class EpisodeFix():
    '''Represents an interface for a podcast episode fix.'''

    def canFix(self, episode_title):
        '''Verifies whether the given podcast, by its title, can be fixed.

        `canFix :: EpisodeTitle -> Bool`
        '''

    def fix(self, episode_info, episode_tags):
        '''Fixes the episode tags.

        `fix :: EpisodeInfo -> EpisodeTags -> EpisodeTags`
        '''


def process(fixes, episode_info, episode_tags):
    '''Calls the appropriate fixer for the `episode_info`, if any, and
    returns the updated `episode_tags`. If there are no matching fixers
    or more than one fixers, returns `None`.

    `process :: [EpisodeFix] -> EpisodeInfo -> EpisodeTags -> EpisodeTags`
    '''

    episode_title = episode_info.episode_title
    the_fix = [fix for fix in fixes if fix.canFix(episode_title)]
    unambiguous_fix_exists = len(the_fix) == 1

    return (the_fix[0].fix(episode_info, episode_tags)
            if unambiguous_fix_exists
            else None)

def post_process(episode_info, episode_tags):
    '''Applies common fixes for all podcasts' tags.'''

    PODCAST_GENRE = 'Podcast'

    return episode_tags._replace(
            genre=PODCAST_GENRE,
            year=episode_info.episode_year)
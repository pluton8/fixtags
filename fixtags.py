#!/usr/bin/env python3

# Author: pluton <pluton.od (at) gmail.com>
# License: GPL v3

import os
import sys
import logging
import datetime

logger = None
episode_fname = ''


class WrongInvocationError(Exception):
    '''This error is thrown when the script is invoked not from gPodder.'''
    pass


def setupLogging():
    '''Set up the logging system.

    Use the global `logger` object to log events in the app.
    '''

    global logger
    logger = logging.getLogger(sys.argv[0])
    logger.setLevel(logging.DEBUG)

    # use file output
    LOG_FILENAME = os.path.join(os.path.dirname(sys.argv[0]), 'fixtags.log')
    filelog = logging.FileHandler(LOG_FILENAME, 'a')
    filelog.setLevel(logging.DEBUG)

    # use console
    conlog = logging.StreamHandler()
    conlog.setLevel(logging.DEBUG)

    # specify log formatting
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s")
    conlog.setFormatter(formatter)
    filelog.setFormatter(formatter)

    logger.addHandler(conlog)
    logger.addHandler(filelog)

def setup():
    '''Initialize the app.'''
    setupLogging()

def trim_prefix(episode_title, prefix):
    '''Returns the episode_title without the prefix if it starts with
    the prefix or the whole string otherwise.'''

    return (episode_title[len(prefix):]
        if episode_title.startswith(prefix)
        else episode_title)

def main():
    # get episode info from the environment variables
    global episode_title, episode_fname, channel_title, episode_pubdate
    try:
        episode_title = os.environ['GPODDER_EPISODE_TITLE']
        episode_fname = os.environ['GPODDER_EPISODE_FILENAME']
        channel_title = os.environ['GPODDER_CHANNEL_TITLE']
        episode_pubdate = int(float(os.environ['GPODDER_EPISODE_PUBDATE']))

        import stagger
    except KeyError:
        print("""This script should be run by gPodder. Put its path and filename ({0}) as the argument to 'cmd_download_complete' option.
For more information, go to 'http://wiki.gpodder.org/wiki/User_Manual#Time_stretching_.28making_playback_slower_or_faster.29', the 'Using the post-download script hook' section.""".format(os.path.abspath(sys.argv[0])), file=sys.stderr)
        raise WrongInvocationError()
    #print('Processing {0}'.format(episode_fname))

    # calculate the publication year
    episode_year = str(datetime.date.fromtimestamp(episode_pubdate).year)

    # the main set of checks
    if channel_title == 'Escape from Cubicle Nation Podcast':
        # set all v2 tags and remove v1
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Pamela Slim'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'EconTalk':
        # set all v2 tags
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Russ Roberts'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'The Naked Scientists':
        # set all v2 tags
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Chris Smith et al.'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'The Stack Exchange Podcast':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = trim_prefix(episode_title, 'Podcast ')
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'Application Developer Days':
        # set all v2 tags
        tag2 = stagger.Tag24()
        import re
        parts = re.search(r'([^(]*) \((.*) на [^)]*\)', episode_title,
                flags=re.IGNORECASE)
        tag2.title = parts.group(1)
        tag2.artist = parts.group(2)
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'Fun English Lessons':
        # set all v2 tags
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'two Canadian brothers'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'Learn English Funcast':
        # set all v2 tags
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Ron G'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == "radiogrinch's show":
        # set all v2 tags
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Radio Grinch'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'Хекслет':
        # set all v2 tags
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'freetonik'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'Все о США в подкастах':
        # set all v2 tags and remove v1
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Тимур Тажетдинов'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'Science Friday':
        # set all v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Ira Flatow'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'Поверх барьеров - Американский час - Радио Свобода':
        # set all v2 tags and remove v1
        tag2 = stagger.Tag24()
        tag2.artist = 'Александр Генис'
        tag2.title = episode_title[37:]
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.composer = 'RFE/RL Russian Service'
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'Langsam gesprochene Nachrichten | Deutsch lernen | Deutsche Welle':
        # set all v2 tags
        tag2 = stagger.Tag24()
        tag2.artist = 'Deutsche Welle'
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'Америчка':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write()

    elif channel_title == 'Sick and Wrong':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.artist = 'Dee and Harrison'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.title = trim_prefix(episode_title, 'Episode ')
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'Sick and Wrong — Super Fucking Exclusive Feed':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.artist = 'Dee and Harrison'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.title = trim_prefix(episode_title, 'S&W Episode ')
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'Mysterious Universe':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Benjamin Grundy, Aaron Wright'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'FLOSS Weekly':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Радио Бермудский Треугольник':
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.artist = 'Наташа, Оля, Даник'
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'This American Life':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Ira Glass'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        try:
            del tag2['PIC']
        except KeyError:
            pass
        try:
            del tag2['APIC']
        except KeyError:
            pass
        tag2.write()

    elif channel_title == 'Evergreen':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
            tag2.artist = 'Artem Rosnovsky'
        tag2.title = trim_prefix(episode_title, 'Episode ')
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.comment = ''
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'The Linux Admin Show':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.comment = ''
        tag2.write()

    elif channel_title == 'Подкаст на трезвую голову':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.write()

    elif channel_title == 'Freakonomics Radio':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.composer = tag2.artist
        tag2.artist = 'Steven D. Levitt, Stephen J. Dubner'
        tag2.album = channel_title
        tag2.date = episode_year
        try:
            del tag2['COMM']
        except KeyError:
            pass
        try:
            del tag2['APIC']
        except KeyError:
            pass
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'Янки после пьянки':
        # fix some v2 tags and remove v1
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Янки после пьянки'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'Stuff Mom Never Told You':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = 'Cristen and Caroline'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'BrainStuff':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Marshall Brain'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'Stuff To Blow Your Mind':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Robert and Julie'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'Stuff You Should Know':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Josh Clark and Chuck Bryant'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'Machine of Death':
        # move v2.2 to v2.4 tags
        tag22 = stagger.read_tag(episode_fname)
        tag2 = stagger.Tag24()
        tag2.artist = tag22.artist
        tag2.album = channel_title
        tag2.title = tag22.title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title.startswith('English as a Second Language'):
        # move v2.2 to v2.4 tags
        tag22 = stagger.read_tag(episode_fname)
        tag2 = stagger.Tag24()
        tag2.artist = tag22.artist
        tag2.album = channel_title
        tag2.title = tag22.title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.comment = tag22.comment
        tag2.write(episode_fname)

    elif channel_title == 'Wide Teams':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.write()

    elif channel_title == 'Radiolab':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
            tag2.artist = channel_title
            tag2.title = episode_title
            tag2.date = episode_year
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'happy friday podcast from gAmUssA ;-)':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.artist = 'gAmUssA'
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'Material World':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title.find('Quick and Dirty Tips') > 0:
        # move v2.2 to v2.4 tags
        tag22 = stagger.read_tag(episode_fname)
        tag2 = stagger.Tag24()
        tag2.artist = tag22.artist
        tag2.album = tag22.album
        tag2.title = tag22.title
        tag2.genre = 'Podcast'
        tag2.date = tag22.date
        tag2.track = tag22.track
        tag2.write(episode_fname)

    elif channel_title == 'Ask the Naked Scientists':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title[39:]
        tag2.artist = 'Chris Smith'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Listen to English':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'All In The Mind':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.write()

    elif channel_title == 'Accidental Tech Podcast':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        try:
            del tag2['CTOC']
        except KeyError:
            pass
        try:
            del tag2['CHAP']
        except KeyError:
            pass
        tag2.write()

    elif channel_title == 'NPR: Car Talk Podcast':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title[9:]
        tag2.artist = 'Click and Clack, the Tappet Brothers'
        tag2.album = 'Car Talk'
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title.startswith('60-Second '):
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2['COM'] = []
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'NPR: Intelligence Squared Podcast':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = 'Intelligence Squared'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'Подкаст из Силиконовой Долины':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Alex'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif ((channel_title == 'сегодня четверг - dugwin') or
            (channel_title == 'dugwin j. goines // podcast')):
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'dugwin'
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'NPR: Planet Money':
        # fix some v2 tags and remove v1
        tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Robert Smith'
        tag2.album = 'Planet Money'
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'Разбор Полетов':
        # fix some v2 tags and remove v1
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.date = episode_year
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        try:
            del tag2['CTOC']
        except KeyError:
            pass
        try:
            del tag2['CHAP']
        except KeyError:
            pass
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'The Adam Carolla Show':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'Chiptune - 8-bit game music podcast':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = 'Дмитрий Зомбак'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        del tag2['COMM']
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'Software Engineering Radio':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.title = trim_prefix(episode_title, 'SE-Radio Episode ')
        tag2.write()

    elif channel_title == 'Ирландское рагу by Emaster':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = 'Emaster'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Эхо Москвы. Точка':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Александр Плющев'
        tag2.composer = 'Эхо Москвы'
        tag2.album = 'Точка'
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'Радио-Т' or channel_title == 'Пираты-РТ':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.date = episode_year
        tag2.write()

    elif channel_title == 'The Dave Ramsey Show':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.write()

    elif channel_title == 'Common Sense with Dan Carlin':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.album = 'Common Sense'
        tag2.write()

    elif channel_title == 'EnglishLingQ':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        import re
        parts = re.search(r'^\#(\d{1,3}) (?:[-–] )?([^-–]+) [-–] (.+)$',
                episode_title, flags=re.IGNORECASE)
        tag2.title = parts.group(3) if parts else episode_title
        tag2.artist = parts.group(2) if parts else 'Steve and Alex'
        #tag2.track = parts.group(1)
        tag2.genre = 'Podcast'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'TuxRadar Linux Podcast':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'PODъезд. Записки со всего света':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write()

    elif channel_title == 'Плёнки':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'A Way with Words':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'www.it4business.ru':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = 'Слава Панкратов'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write()

    elif channel_title == 'Fonarev':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'happypm':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title[:-15]
        tag2.artist = 'Слава Панкратов, Саша Орлов'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'No Agenda':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'scene':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Казах в Канаде':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.title = episode_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Nunavut':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title[20:]
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Sex Nerd Sandra':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Dolce Welle - подкаст из Европы':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = 'Alex'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'No BS IT':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = 'Budam'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'The Changelog':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.date = episode_year
        tag2.write()

    elif channel_title == 'Dr.Shadow из Британии':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.title = episode_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'The Haskell Cast':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'The raywenderlich.com Podcast':
        # fix some v2 tags
        import re
        parts = re.search(r'^(.*) – Podcast (.+) (.+)$', episode_title,
                flags=re.IGNORECASE)

        tag2 = stagger.read_tag(episode_fname)
        if parts:
            tag2.title = "{0}{1}: {2}".format(parts.group(2), parts.group(3),
                    parts.group(1))
        else:
            tag2.title = episode_title
        tag2.artist = channel_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Russian-Canadian Moose Podcast - pirate raw records!':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.artist = 'Канадский Лось и Co.'
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif channel_title == 'IT мысли':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Developing Perspective':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Russian Canadian Moose PodCast':
        # fix some v2 tags
        import re
        parts = re.search(r'^(\d{1,4})-.* - (.*)$', episode_title,
                flags=re.IGNORECASE)

        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        if parts:
            track = parts.group(1)
            tag2.track = track
            tag2.title = "{0}: {1}".format(track, parts.group(2))
        tag2.write()

    elif channel_title == 'Under the Radar':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Бананы и линзы':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = channel_title
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Подкаст "На чемоданах"':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = 'degiz'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Magic Read Along':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.write()

    elif channel_title == 'Coffee Break German':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == "JavaPubHouse Off-Heap's podcast":
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = trim_prefix(episode_title, 'Episode ')
        tag2.artist = 'Freddy Guime, et al.'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Hanselminutes':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = trim_prefix(tag2.title, channel_title + ' ')
        tag2.write()

    elif channel_title == 'Why Are Computers':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.write()

    elif channel_title == 'Emaster':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = channel_title
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'LambdaCast':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Programming Throwdown':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = trim_prefix(tag2.title, 'Episode ')
        tag2.write()

    elif channel_title == 'DevZen Podcast':
        # fix some v2 tags
        import re
        parts = re.search(r'^(.*) — Episode (\d+)$', episode_title,
                flags=re.IGNORECASE)

        if parts:
            tag2 = stagger.read_tag(episode_fname)
            tag2.title = "{0}: {1}".format(parts.group(2), parts.group(1))
            tag2.write()

    elif channel_title == 'Functional Geekery':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = trim_prefix(episode_title, 'Functional Geekery Episode ')
        tag2.write()

    elif channel_title == 'Command Line Heroes':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Noise Security Bit':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.title = trim_prefix(episode_title, 'Noise Security Bit ')
        tag2.write()

    elif channel_title == 'Soft Skills Engineering':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = 'Dave Smith and Jamison Dance'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Stacktrace':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        try:
            del tag2['CTOC']
        except KeyError:
            pass
        try:
            del tag2['CHAP']
        except KeyError:
            pass
        tag2.write()

    elif channel_title == '99% Invisible':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Criminal':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.write()

    elif channel_title == 'The Amp Hour Electronics Podcast':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.artist = channel_title
        tag2.write()

    elif channel_title == 'Inside iOS Dev':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'This is Love':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = trim_prefix(episode_title, 'Episode ')
        tag2.album = channel_title
        try:
            del tag2['APIC']
        except KeyError:
            pass
        tag2.write()

    elif channel_title == 'You Are Not So Smart':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'The Art Of Programming':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'This Week in Linux':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        try:
            del tag2['CHAP']
        except KeyError:
            pass
        tag2.write()

    elif channel_title == "The ypp's Podcast":
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Янки после пьянки'
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'Haskell Weekly':
        # fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.title = episode_title
        tag2.artist = channel_title
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'Scalalaz Podcast':
        # remove picture element from v2.2 and fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
            tag2.artist = 'scalalaz'
            tag2.title = episode_title
        tag2.picture = []
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'The World in Words':
        # fix some v2 tags and remove v1
        tag2 = stagger.read_tag(episode_fname)
        tag2.album = channel_title
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write()

    elif channel_title == 'Откровенно про IT-карьеризм':
        # fix some v2 tags and remove v1
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.title = episode_title
        tag2.artist = 'Михаил Марченко и Ольга Давыдова'
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        stagger.id3v1.Tag1.delete(episode_fname)
        tag2.write(episode_fname)

    elif channel_title == 'Manager Tools':
        # remove picture element from v2.2 and fix date
        try:
            tag2 = stagger.read_tag(episode_fname)
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
        tag2.picture = []
        tag2.date = episode_year
        tag2.write(episode_fname)

    elif channel_title == 'Career Tools':
        # remove picture element from v2.2
        tag2 = stagger.read_tag(episode_fname)
        tag2.picture = []
        tag2.write()

    elif channel_title == 'Debug':
        # remove picture element from v2.2 and fix some v2 tags
        tag2 = stagger.read_tag(episode_fname)
        tag2.picture = []
        tag2.title = episode_title
        tag2.album = channel_title
        tag2.date = episode_year
        tag2.genre = 'Podcast'
        tag2.write()

    elif channel_title == 'Top-Thema mit Vokabeln | Deutsch lernen | Deutsche Welle':
        # fix some v2 tags
        try:
            tag2 = stagger.read_tag(episode_fname)
            try:
                del tag2['APIC']
            except KeyError:
                pass
        except stagger.errors.NoTagError:
            tag2 = stagger.Tag24()
            tag2.title = episode_title
            tag2.artist = 'Deutsche Welle'
            tag2.album = channel_title
            tag2.date = episode_year
            tag2.genre = 'Podcast'
        tag2.write(episode_fname)

    elif ((channel_title == 'UWP - Eженедельный подкаст от Umputun')
            or (channel_title == 'Discovery')
            or (channel_title == 'Охотник За Головами - Денис aka Radio Grinch')
            or (channel_title == 'The Java Posse')
            or (channel_title == 'Эксперт-шоу Рунетология')
            or (channel_title == 'The Skeptics Guide to the Universe')
            or (channel_title == 'this WEEK in TECH')
            or (channel_title == 'Radio Grinch')
            or (channel_title == 'Adam Curry\'s Daily Source Code')
            or (channel_title == 'Friends House')
            or (channel_title == 'Security Now!')
            or (channel_title == 'Build Phase')
            or (channel_title == 'TechSNAP MP3')
            or (channel_title == 'Triangulation (MP3)')
            or (channel_title == 'Slow German')
            or (channel_title == 'CoRecursive w/ Adam Bell')
            or (channel_title == 'Reply All')
            or (channel_title == 'LINUX Unplugged')
            or (channel_title == 'Hackaday Podcast')
            or (channel_title == 'Радио-Т Поток')
            or (channel_title == 'Пиратский Канадский Лось и компания')
            ):
        # nothing to fix here
        pass

    else: logger.info("No fixes for the episode. GPODDER_CHANNEL_TITLE='{0}' "
            "GPODDER_EPISODE_TITLE='{1}' GPODDER_EPISODE_FILENAME='{2}' "
            "GPODDER_EPISODE_PUBDATE='{3}'".format(channel_title,
                episode_title, episode_fname, episode_pubdate))

if __name__ == '__main__':
    try:
        setup()
        main()
    except ImportError:
        logger.critical("Couldn't import stagger! Please fix. GPODDER_CHANNEL_TITLE='{0}' "
            "GPODDER_EPISODE_TITLE='{1}' GPODDER_EPISODE_FILENAME='{2}' "
            "GPODDER_EPISODE_PUBDATE='{3}'".format(channel_title,
                episode_title, episode_fname, episode_pubdate))
        sys.exit(3)
    except WrongInvocationError:
        # don't panic on this error
        pass
    except:
        # if happens something that we didn't foresee,
        # print traceback to the log
        import traceback
        logger.exception("An exception occurred with file '{}'".format(episode_fname))
        sys.exit(2)


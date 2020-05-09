# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Implements VRT Radio schedules"""

from __future__ import absolute_import, division, unicode_literals
from datetime import datetime
import dateutil.parser
import dateutil.tz

try:  # Python 3
    from urllib.request import build_opener, install_opener, ProxyHandler
except ImportError:  # Python 2
    from urllib2 import build_opener, install_opener, ProxyHandler

from data import CHANNELS
from kodiutils import get_proxies, get_url_json
from utils import find_entry, html_to_kodi


class Schedule:
    """This implements VRT Radio schedules"""

    WEEK_SCHEDULE = 'http://services.vrt.be/epg/schedules/%Y%m%d?channel_type=radio&type=week'

    def __init__(self):
        """Initializes TV-guide object"""
        install_opener(build_opener(ProxyHandler(get_proxies())))

    def get_epg_data(self):
        """Return EPG data"""
        now = datetime.now(dateutil.tz.tzlocal())

        epg_data = dict()
        epg_url = now.strftime(self.WEEK_SCHEDULE)
        schedule = get_url_json(url=epg_url, headers=dict(accept='application/vnd.epg.vrt.be.schedule_3.1+json'), fail={})
        for event in schedule.get('events', []):
            channel_id = event.get('channel', dict(code=None)).get('code')
            if channel_id is None:
                continue
            channel = find_entry(CHANNELS, 'id', channel_id)
            epg_id = '{name}.be'.format(**channel)
            if epg_id not in epg_data:
                epg_data[epg_id] = []
            epg_data[epg_id].append(dict(
                start=event.get('startTime'),
                stop=event.get('endTime'),
                #image=add_https_proto(event.get('image', '')),
                title=event.get('title'),
                description=html_to_kodi(event.get('description', '')),
            ))
        return epg_data

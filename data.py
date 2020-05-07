# -*- coding: utf-8 -*-

# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, unicode_literals

# https://services.vrt.be/htmlview/?href=%2Fchannel%2Fs&rel=http%3A%2F%2Fservices.vrt.be%2Fchannel%2Frel%2Fchannels
CHANNELS = [
    dict(
        id='11',
        name='radio1',
        label='Radio 1',
        tagline='Altijd Benieuwd',
        studio='Radio 1',
        website='https://radio1.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/47303075-8243-434b-8199-2e62cf4dd97a/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/47303075-8243-434b-8199-2e62cf4dd97a/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/radio1-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/radio1-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/radio1.aac',
        epg_logo='https://images.vrt.be/orig/logos/radio1.png',
        epg_preset=901,
    ),
    dict(
        id='110',
        name='radio1-classics',
        label='Radio 1 Classics',
        tagline='Een eindeloze stroom aan onsterfelijke klassiekers',
        studio='Radio 1',
        website='https://radio1.be/',
        hls_128='https://live-radio-vrt.akamaized.net/groupa/live/0a479081-ca2c-40fb-bc16-a10c8d3708c0/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-vrt.akamaized.net/groupa/live/0a479081-ca2c-40fb-bc16-a10c8d3708c0/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/radio1_classics_high.mp3',
        mp3_64='http://icecast.vrtcdn.be/radio1_classics_mid.mp3',
        aac_128='http://icecast.vrtcdn.be/radio1_classics.aac',
        epg_logo='https://images.vrt.be/orig/2020/04/08/b1c35b45-7961-11ea-aae0-02b7b76bf47f.png',
        epg_preset=908,
    ),
    dict(
        id='22',
        name='radio2',
        label='Radio 2',
        tagline='De grootste familie',
        studio='Radio 2',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/1e08f370-1f20-4807-aaa3-051c7f0d8359/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/1e08f370-1f20-4807-aaa3-051c7f0d8359/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2vlb-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2vlb-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2vlb.aac',
        epg_logo='https://images.vrt.be/orig/logo/radio2/RADIO2_RED_RGB.png',
        epg_preset=902,
    ),
    dict(
        id='31',
        name='klara',
        label='Klara',
        tagline='Blijf verwonderd',
        studio='Klara',
        website='https://klara.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/a9f36fda-cb3c-4b4e-9405-a5bba55654c0/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/a9f36fda-cb3c-4b4e-9405-a5bba55654c0/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/klara-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/klara-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/klara.aac',
        epg_id='klara.be',
        epg_logo='https://images.vrt.be/orig/logos/klara.png',
        epg_preset=903,
    ),
    dict(
        id='32',
        name='klara-continuo',
        label='Klara Continuo',
        tagline='Non-stop klassieke muziek',
        studio='Klara',
        website='https://klara.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/0d06dbbe-92d4-4cfe-a0b3-ccc6b7a32ec4/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/0d06dbbe-92d4-4cfe-a0b3-ccc6b7a32ec4/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/klaracontinuo-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/klaracontinuo-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/klaracontinuo.aac',
        epg_id='clara-continuo.be',
        epg_logo='https://images.vrt.be/orig/logos/klara_continuo.png',
        epg_preset=916,
    ),
    dict(
        id='41',
        name='stubru',
        label='Studio Brussel',
        tagline='Life is Music',
        studio='Studio Brussel',
        website='https://stubru.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/f404f0f3-3917-40fd-80b6-a152761072fe/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/f404f0f3-3917-40fd-80b6-a152761072fe/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru.aac',
        epg_logo='https://images.vrt.be/orig/2019/03/12/1e383cf5-44a7-11e9-abcc-02b7b76bf47f.png',
        epg_preset=904,
    ),
    dict(
        id='44',
        name='stubru-tijdloze',
        label='StuBru De Tijdloze',
        tagline='Altijd en overal de beste Tijdloze muziek',
        studio='Studio Brussel',
        website='https://stubru.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/582109ca-1e71-4330-93fc-e9affee94d7d/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/582109ca-1e71-4330-93fc-e9affee94d7d/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru_tijdloze-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru_tijdloze-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru_tijdloze.aac',
        epg_logo='https://images.vrt.be/orig/2019/02/21/923b0fe2-35ce-11e9-abcc-02b7b76bf47f.png',
        epg_preset=918,
    ),
    dict(
        id='45',
        name='stubru-tgs',
        label='StuBru #ikluisterbelgisch',
        tagline='Non-Stop. Nieuw. Belgisch.',
        studio='Studio Brussel',
        website='https://stubru.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/23384e71-2b6a-43f1-8ad6-02c4ebb8bdf7/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/23384e71-2b6a-43f1-8ad6-02c4ebb8bdf7/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru_tgs-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru_tgs-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru_tgs.aac',
        epg_logo='https://images.vrt.be/orig/2020/04/02/53dad354-74af-11ea-aae0-02b7b76bf47f.png',
        epg_preset=919,
    ),
    dict(
        id='55',
        name='mnm',
        label='MNM',
        tagline='Music and More',
        studio='MNM',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/68dc3b80-040e-4a75-a394-72f3bb7aff9a/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/68dc3b80-040e-4a75-a394-72f3bb7aff9a/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm.aac',
        epg_logo='https://images.vrt.be/orig/logo/mnm/logo_witte_achtergrond.png',
        epg_preset=905,
    ),
    dict(
        id='56',
        name='mnm-hits',
        label='MNM Hits',
        tagline='Music and More - The Hits',
        studio='MNM',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/35dd91de-0352-4865-8632-17e5af8dc6ba/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/35dd91de-0352-4865-8632-17e5af8dc6ba/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm_hits-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm_hits-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm_hits.aac',
        epg_logo='https://images.vrt.be/orig/logo/mnm/mnm_hits_logo_2018.png',
        epg_preset=921,
    ),
    dict(
        id='57',
        name='mnm-urbanice',
        label='MNM UrbaNice',
        tagline='De Online Urban Stream van MNM',
        studio='MNM',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/da0b681c-73db-4c9e-af32-7921591d3fbd/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/da0b681c-73db-4c9e-af32-7921591d3fbd/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm_urb-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm_urb-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm_urb.aac',
        epg_logo='https://images.vrt.be/orig/logo/mnm_urbanice_logo.png',
        epg_preset=922,
    ),
    dict(
        id='58',
        name='mnm-90s00s',
        label="MNM Back to the 90's & 00's",
        tagline='Music and More',
        studio='MNM',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/a2050115-96cb-4151-afda-cbd177407e6e/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/a2050115-96cb-4151-afda-cbd177407e6e/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm_90s00s-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm_90s00s-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm_90s00s.aac',
        epg_logo='https://images.vrt.be/orig/2019/02/21/76e54cd8-35f1-11e9-abcc-02b7b76bf47f.png',
        epg_preset=923,
    ),
    #dict(
    #    id='12',
    #    name='sporza',
    #    label='Sporza',
    #    tagline='Kristalheldere sportverslaggeving',
    #    studio='Sporza',
    #    website='https://sporza.be/',
    #    hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/a1211b31-541b-43ce-b6e2-489d9a8995ad/live.isml/.m3u8',
    #    mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/a1211b31-541b-43ce-b6e2-489d9a8995ad/live.isml/.mpd',
    #    mp3_128='http://icecast.vrtcdn.be/sporza-high.mp3',
    #    mp3_64='http://icecast.vrtcdn.be/sporza-mid.mp3',
    #    aac_128='http://icecast.vrtcdn.be/sporza.aac',
    #    epg_preset=906,
    #),
    dict(
        id='13',
        name='vrtnws',
        label='VRT Nieuws',
        tagline='Ieder moment het meest recente nieuws',
        studio='VRT NWS',
        website='https://www.vrtnieuws.be/',
        hls_128='https://ondemand-radio-cf-vrt.akamaized.net/audioonly/content/fixed/11_11niws-snip_hi.mp4/.m3u8',
        mpeg_dash_128='https://ondemand-radio-cf-vrt.akamaized.net/audioonly/content/fixed/11_11niws-snip_hi.mp4/.mpd',
        mp3_128='https://progressive-audio.lwc.vrtcdn.be/content/fixed/11_11niws-snip_hi.mp3',
        epg_logo='https://images.vrt.be/orig/logos/vrtnws.png',
        epg_preset=925,
    ),
    dict(
        id='O3',
        name='ketnet-hits',
        label='Ketnet Hits',
        tagline='De hipste, de coolste én de plezantste hits op een rijtje',
        studio='Ketnet',
        website='https://ketnet.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/014a9eea-af85-4da6-aab2-c472ca8d0149/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/014a9eea-af85-4da6-aab2-c472ca8d0149/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ketnetradio-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ketnetradio-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ketnetradio.aac',
        epg_logo='https://images.vrt.be/orig/logo/ketnet/ketnet_hits_rgb.png',
        epg_preset=927,
    ),
    dict(
        id='71',
        name='vrt-event',
        label='VRT Event',
        tagline='',
        studio='VRT',
        website='https://vrt.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/779d53fc-9472-4fe8-b62a-1d38c5878c60/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/779d53fc-9472-4fe8-b62a-1d38c5878c60/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/vrtevent-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/vrtevent-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/vrtevent.aac',
        epg_logo='https://images.vrt.be/orig/logo/vrt.png',
        epg_preset=929,
    ),
    dict(
        id='21',
        name='radio2-antwerpen',
        label='Radio 2 Antwerpen',
        tagline='De grootste familie',
        studio='Radio 2',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/033d312d-31f7-400a-b81a-61195f0b79c5/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/033d312d-31f7-400a-b81a-61195f0b79c5/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2ant-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2ant-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2ant.aac',
        epg_logo='https://images.vrt.be/orig/logo/radio2/RADIO2_RED_RGB.png',
        epg_preset=911,
    ),
    dict(
        id='22',
        name='radio2-vlaams-brabant',
        label='Radio 2 Vlaams-Brabant',
        tagline='De grootste familie',
        studio='Radio 2',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/1e08f370-1f20-4807-aaa3-051c7f0d8359/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/1e08f370-1f20-4807-aaa3-051c7f0d8359/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2vlb-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2vlb-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2vlb.aac',
        epg_logo='https://images.vrt.be/orig/logo/radio2/RADIO2_RED_RGB.png',
        epg_preset=914,
    ),
    dict(
        id='23',
        name='radio2-limburg',
        label='Radio 2 Limburg',
        tagline='De grootste familie',
        studio='Radio 2',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/d9c49923-b49f-4ab3-8532-4e9bd850b4e2/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/d9c49923-b49f-4ab3-8532-4e9bd850b4e2/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2lim-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2lim-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2lim.aac',
        epg_logo='https://images.vrt.be/orig/logo/radio2/RADIO2_RED_RGB.png',
        epg_preset=912,
    ),
    dict(
        id='24',
        # name='radio2-oost-vlaanderen',
        # label='Radio 2 Oost-Vlaanderen',
        name='radio2',
        label='Radio 2',
        tagline='De grootste familie',
        studio='Radio 2',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/93a8a402-9008-4a97-b473-bc107be7524d/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/93a8a402-9008-4a97-b473-bc107be7524d/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2ovl-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2ovl-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2ovl.aac',
        epg_logo='https://images.vrt.be/orig/logo/radio2/RADIO2_RED_RGB.png',
        epg_preset=913,
    ),
    dict(
        id='25',
        name='radio2-west-vlaanderen',
        label='Radio 2 West-Vlaanderen',
        tagline='De grootste familie',
        studio='Radio 2',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/604e4a0e-22e8-4f99-ad5e-4f62d27dfec4/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/604e4a0e-22e8-4f99-ad5e-4f62d27dfec4/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2wvl-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2wvl-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2wvl.aac',
        epg_logo='https://images.vrt.be/orig/logo/radio2/RADIO2_RED_RGB.png',
        epg_preset=913,
    ),
]

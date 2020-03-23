# Torrent Service

Service to search and download videos using torrents.

## Usage

You must install `transmission-cli` to use this service. Also you must define below environment variable.

- `KILL_SCRIPT=<path to killscript.sh folder>`

### Search torrents

**Definition**

`GET /search/{search string}`

Search for the string and return fisrt three pages it found.

**Response**

`200 OK` on success

```json
[
    {
        "url": "https://1337x.to/torrent/4102533/This-Is-Us-S04E07-HDTV-x264-SVA-eztv/",
        "name": "This Is Us S04E07 HDTV x264-SVA [eztv]",
        "seeds": "335",
        "date": "Nov. 6th '19",
        "size": "262.5 MB335",
        "uploader": "EZTVag"
    },
    {
        "url": "https://1337x.to/torrent/2860313/This-Is-Us-S02E18-HDTV-x264-KILLERS-eztv/",
        "name": "This.Is.Us.S02E18.HDTV.x264-KILLERS[eztv]",
        "seeds": "331",
        "date": "Mar. 14th '18",
        "size": "268.3 MB331",
        "uploader": "EZTVag"
    },
    {
        "url": "https://1337x.to/torrent/3630814/This-Is-Us-S03E14-HDTV-x264-SVA-eztv/",
        "name": "This Is Us S03E14 HDTV x264-SVA [eztv]",
        "seeds": "329",
        "date": "Mar. 6th '19",
        "size": "245.7 MB329",
        "uploader": "EZTVag"
    }
    ...
]
  ```

  **Definition**

  `GET /search/{search string}/page/{page number}`

  Search for the string and return specific page from result.

**Response**

`200 OK` on success

```json
[
    {
        "url": "https://1337x.to/torrent/4102533/This-Is-Us-S04E07-HDTV-x264-SVA-eztv/",
        "name": "This Is Us S04E07 HDTV x264-SVA [eztv]",
        "seeds": "335",
        "date": "Nov. 6th '19",
        "size": "262.5 MB335",
        "uploader": "EZTVag"
    },
    {
        "url": "https://1337x.to/torrent/2860313/This-Is-Us-S02E18-HDTV-x264-KILLERS-eztv/",
        "name": "This.Is.Us.S02E18.HDTV.x264-KILLERS[eztv]",
        "seeds": "331",
        "date": "Mar. 14th '18",
        "size": "268.3 MB331",
        "uploader": "EZTVag"
    },
    {
        "url": "https://1337x.to/torrent/3630814/This-Is-Us-S03E14-HDTV-x264-SVA-eztv/",
        "name": "This Is Us S03E14 HDTV x264-SVA [eztv]",
        "seeds": "329",
        "date": "Mar. 6th '19",
        "size": "245.7 MB329",
        "uploader": "EZTVag"
    }
    ...
]
```

### Download video

**Definition**

`POST /download`

**Arguments**

* `url:string` video torrent url. Can be obtained from previous APIs.

Video file will be saved in download folder from `transmission-cli` configuration file.

**Response**

`201 CREATED` on success

```json
{
    "url":"https://1337x.to/torrent/4102533/This-Is-Us-S04E07-HDTV-x264-SVA-eztv/",
    "pid":"1234"
}
```

### Download status

**Definition**

`GET /download/{pid}`

Pid value will be returned in previous API.

**Response**

`200 OK` on success

Status will return `Running` or `Stopped` according to `transmission-cli` download status.

```json
{
    "pid":"1234",
    "status":"Running"
}
```
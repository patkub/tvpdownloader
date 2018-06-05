# tvpdownloader
[![PyPi version](https://img.shields.io/pypi/v/tvpdownloader.svg)](https://pypi.org/project/tvpdownloader/)

> Download episodes from vod.tvp.pl

### Install:
```sh
pip install tvpdownloader
```

### Usage:
```sh
python3 tvpdownloader.py
```

### Publishing:
```sh
python3 setup.py sdist
twine upload dist/tvpdownloader-0.1.0.tar.gz
```

### Example:
```python
from tvpdownloader import *

if __name__ == '__main__':
  # list of urls to download
  urls = [
    {"url": "https://vod.tvp.pl/video/rodzinkapl,odc1,3994796", "quality": 5},
    {"url": "https://vod.tvp.pl/video/rodzinkapl,odc-221,34842411", "quality": 5},
  ]

  for u in urls:
    # download each url
    print("Downloading: " + u['url'] + " Quality: " + str(u['quality']))
    TVPDownloader(url=u['url'], quality=u['quality']).get()

  print("Done!")
```

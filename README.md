# HN Polls Visualizer

Visualize the HackerNews polls in terminal.

## Example

```
$ ./main.py "https://news.ycombinator.com/item?id=30210378"
US: California                    [560]  ████████████████████████████████████████
Germany                           [263]  ██████████████████▊
Canada                            [253]  ██████████████████▏
United Kingdom                    [246]  █████████████████▋
US: New York                      [214]  ███████████████▎
US: Washington                    [202]  ██████████████▍
US: Texas                         [124]  ████████▉
US: Massachusetts                 [101]  ███████▎
Australia                         [101]  ███████▎
Netherlands                       [ 99]  ███████▏
US: Colorado                      [ 96]  ██████▉
US: Illinois                      [ 85]  ██████▏
Sweden                            [ 85]  ██████▏
India                             [ 78]  █████▋
France                            [ 74]  █████▎
US: Oregon                        [ 69]  ████▉
Poland                            [ 68]  ████▉
US: North Carolina                [ 61]  ████▍
US: Pennsylvania                  [ 60]  ████▎
US: New Jersey                    [ 58]  ████▏
US: Virginia                      [ 54]  ███▉
US: Florida                       [ 54]  ███▉
Switzerland                       [ 54]  ███▉
New Zealand                       [ 46]  ███▎
Spain                             [ 44]  ███▏
US: Georgia                       [ 43]  ███▏
Denmark                           [ 43]  ███▏
US: Michigan                      [ 42]  ███
Finland                           [ 41]  ██▉
Brazil                            [ 39]  ██▊
Austria                           [ 39]  ██▊
Italy                             [ 37]  ██▋
Norway                            [ 36]  ██▋
US: Ohio                          [ 34]  ██▍
US: Minnesota                     [ 34]  ██▍
Israel                            [ 34]  ██▍
Ireland                           [ 34]  ██▍
Japan                             [ 33]  ██▍
US: Arizona                       [ 31]  ██▎
Czech Republic                    [ 31]  ██▎
US: Utah                          [ 30]  ██▏
US: Maryland                      [ 30]  ██▏
US: Wisconsin                     [ 28]  ██
Romania                           [ 27]  █▉
Belgium                           [ 26]  █▉
Russia                            [ 25]  █▊
US: Tennessee                     [ 23]  █▋
US: New Mexico                    [ 20]  █▍
Hungary                           [ 20]  █▍
```

## Run

### Using Python 3.7+

Install `pipenv`:

```
pip install pipenv
```

Install dependencies:

```
pipenv install
```

Activate:

```
pipenv shell
```

Run:

```
./main.py {URL}
```

### Using Docker

Run:

```
./run-docker {URL}
```

## Why?

Just for fun!


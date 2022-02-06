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
Serbia                            [ 19]  █▍
Portugal                          [ 19]  █▍
Mexico                            [ 19]  █▍
Argentina                         [ 19]  █▍
Croatia                           [ 18]  █▎
Ukraine                           [ 17]  █▎
US: Missouri                      [ 17]  █▎
US: Connecticut                   [ 17]  █▎
US: Indiana                       [ 16]  █▏
US: Idaho                         [ 16]  █▏
Turkey                            [ 16]  █▏
US: Kansas                        [ 14]  █
US: Iowa                          [ 14]  █
Bulgaria                          [ 14]  █
US: New Hampshire                 [ 13]  ▉
South Africa                      [ 13]  ▉
Singapore                         [ 12]  ▉
North Korea                       [ 12]  ▉
Lithuania                         [ 12]  ▉
US: Nevada                        [ 11]  ▊
US: Kentucky                      [ 11]  ▊
US: District of Columbia          [ 11]  ▊
Slovenia                          [ 11]  ▊
Greece                            [ 11]  ▊
US: Vermont                       [ 10]  ▊
US: Alabama                       [ 10]  ▊
Latvia                            [ 10]  ▊
US: South Carolina                [  9]  ▋
US: Louisiana                     [  9]  ▋
Taiwan                            [  9]  ▋
Slovakia                          [  9]  ▋
Estonia                           [  9]  ▋
Vatican City                      [  8]  ▋
US: Puerto Rico                   [  8]  ▋
US: Montana                       [  8]  ▋
US: Hawaii                        [  8]  ▋
Indonesia                         [  8]  ▋
Colombia                          [  8]  ▋
Vietnam                           [  7]  ▌
US: Rhode Island                  [  7]  ▌
US: Oklahoma                      [  7]  ▌
South Korea                       [  7]  ▌
Philippines                       [  7]  ▌
China                             [  7]  ▌
Uruguay                           [  6]  ▍
US: Mississippi                   [  6]  ▍
US: Arkansas                      [  6]  ▍
Thailand                          [  6]  ▍
Luxembourg                        [  6]  ▍
US: West Virginia                 [  5]  ▍
US: North Dakota                  [  5]  ▍
US: Nebraska                      [  5]  ▍
Moldova                           [  5]  ▍
Malaysia                          [  5]  ▍
Kazakhstan                        [  5]  ▍
Iceland                           [  5]  ▍
Costa Rica                        [  5]  ▍
Bangladesh                        [  5]  ▍
United Arab Emirates              [  4]  ▎
US: South Dakota                  [  4]  ▎
US: Maine                         [  4]  ▎
US: Alaska                        [  4]  ▎
Tunisia                           [  4]  ▎
Timor-Leste                       [  4]  ▎
Other                             [  4]  ▎
Nomad                             [  4]  ▎
Kyrgyzstan                        [  4]  ▎
Jamaica                           [  4]  ▎
Guatemala                         [  4]  ▎
Ethiopia                          [  4]  ▎
Equatorial Guinea                 [  4]  ▎
Dominican Republic                [  4]  ▎
Chile                             [  4]  ▎
Belarus                           [  4]  ▎
Armenia                           [  4]  ▎
Algeria                           [  4]  ▎
Albania                           [  4]  ▎
Uganda                            [  3]  ▎
US: Delaware                      [  3]  ▎
The Bahamas                       [  3]  ▎
Sri Lanka                         [  3]  ▎
Saudi Arabia                      [  3]  ▎
Samoa                             [  3]  ▎
Pakistan                          [  3]  ▎
Nigeria                           [  3]  ▎
Mauritius                         [  3]  ▎
Lebanon                           [  3]  ▎
Kosovo                            [  3]  ▎
Kenya                             [  3]  ▎
Iran                              [  3]  ▎
Haiti                             [  3]  ▎
Fiji                              [  3]  ▎
Eritrea                           [  3]  ▎
Cyprus                            [  3]  ▎
Cuba                              [  3]  ▎
Botswana                          [  3]  ▎
Antigua and Barbuda               [  3]  ▎
Yemen                             [  2]  ▏
Vanuatu                           [  2]  ▏
Uzbekistan                        [  2]  ▏
US: Wyoming                       [  2]  ▏
US: US Virgin Islands             [  2]  ▏
Tuvalu                            [  2]  ▏
Trinidad and Tobago               [  2]  ▏
Tajikistan                        [  2]  ▏
Sudan                             [  2]  ▏
Somalia                           [  2]  ▏
Senegal                           [  2]  ▏
Saint Lucia                       [  2]  ▏
Republic of the Congo             [  2]  ▏
Qatar                             [  2]  ▏
Peru                              [  2]  ▏
Paraguay                          [  2]  ▏
Palau                             [  2]  ▏
North Macedonia                   [  2]  ▏
Niger                             [  2]  ▏
Nicaragua                         [  2]  ▏
Nepal                             [  2]  ▏
Mozambique                        [  2]  ▏
Morocco                           [  2]  ▏
Monaco                            [  2]  ▏
Marshall Islands                  [  2]  ▏
Malta                             [  2]  ▏
Mali                              [  2]  ▏
Madagascar                        [  2]  ▏
Libya                             [  2]  ▏
Liberia                           [  2]  ▏
Kiribati                          [  2]  ▏
Iraq                              [  2]  ▏
Honduras                          [  2]  ▏
Guinea                            [  2]  ▏
Grenada                           [  2]  ▏
Ghana                             [  2]  ▏
Georgia                           [  2]  ▏
El Salvador                       [  2]  ▏
Egypt                             [  2]  ▏
Ecuador                           [  2]  ▏
Dominica                          [  2]  ▏
Djibouti                          [  2]  ▏
Chad                              [  2]  ▏
Central African Republic          [  2]  ▏
Cambodia                          [  2]  ▏
Bosnia and Herzegovina            [  2]  ▏
Bolivia                           [  2]  ▏
Bhutan                            [  2]  ▏
Belize                            [  2]  ▏
Barbados                          [  2]  ▏
Angola                            [  2]  ▏
Andorra                           [  2]  ▏
Afghanistan                       [  2]  ▏
Zimbabwe                          [  1]  ▏
Zambia                            [  1]  ▏
Venezuela                         [  1]  ▏
US: Northern Mariana Islands      [  1]  ▏
US: Guam                          [  1]  ▏
US: American Samoa                [  1]  ▏
Turkmenistan                      [  1]  ▏
Tonga                             [  1]  ▏
Togo                              [  1]  ▏
The Gambia                        [  1]  ▏
Tanzania                          [  1]  ▏
Syria                             [  1]  ▏
Suriname                          [  1]  ▏
South Sudan                       [  1]  ▏
Solomon Islands                   [  1]  ▏
Sierra Leone                      [  1]  ▏
Seychelles                        [  1]  ▏
Sao Tome and Principe             [  1]  ▏
San Marino                        [  1]  ▏
Saint Vincent and the Grenadines  [  1]  ▏
Saint Kitts and Nevis             [  1]  ▏
Rwanda                            [  1]  ▏
Papua New Guinea                  [  1]  ▏
Panama                            [  1]  ▏
Oman                              [  1]  ▏
Nauru                             [  1]  ▏
Namibia                           [  1]  ▏
Myanmar                           [  1]  ▏
Montenegro                        [  1]  ▏
Mongolia                          [  1]  ▏
Mauritania                        [  1]  ▏
Maldives                          [  1]  ▏
Malawi                            [  1]  ▏
Liechtenstein                     [  1]  ▏
Lesotho                           [  1]  ▏
Laos                              [  1]  ▏
Kuwait                            [  1]  ▏
Jordan                            [  1]  ▏
Guyana                            [  1]  ▏
Guinea-Bissau                     [  1]  ▏
Gabon                             [  1]  ▏
Federated States of Micronesia    [  1]  ▏
Eswatini                          [  1]  ▏
Democratic Republic of the Congo  [  1]  ▏
Côte d’Ivoire                     [  1]  ▏
Comoros                           [  1]  ▏
Cameroon                          [  1]  ▏
Cabo Verde                        [  1]  ▏
Burundi                           [  1]  ▏
Burkina Faso                      [  1]  ▏
Brunei                            [  1]  ▏
Benin                             [  1]  ▏
Bahrain                           [  1]  ▏
Azerbaijan                        [  1]  ▏
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


# Finna-client

This is a minimal Python 3.x client library for accessing the [Finna.fi REST
API](https://api.finna.fi). The API can be used to search for records (e.g.
books and images) in the Finna discovery service and to retrieve information
about individual records.

## Installation

The easiest way to install is via pip:

    pip3 install finna-client

## Dependencies

The library depends on the
[requests](http://docs.python-requests.org/en/master/#) module which is used
for HTTP/REST access. If you install this via pip, the dependencies will be
handled automatically.

## How to use

The client library comes with examples demonstrating its usage. You can invoke
the example simply by running the [finna_client.py](finna_client.py) script.

In your own code, you can use the FinnaClient class like this:

    from finna_client import FinnaClient

    # then you can create your own client
    finna = FinnaClient()

## Example invocation

Here is the output from a typical example session:

    $ python3 finna_client.py
    Demonstrating usage of FinnaClient

    * Creating a FinnaClient object
    Now we have a FinnaClient object: FinnaClient(api_base='https://api.finna.fi/api/v1/')

    * Performing a general search
    Search would have matched 1354 records
    {'buildings': [{'value': '0/Helmet/', 'translated': 'Helmet-kirjastot'}, {'value': '1/Helmet/v/', 'translated': 'Vantaa'}, {'value': '2/Helmet/v/v28/', 'translated': 'Länsimäki'}], 'onlineUrls': [], 'series': [], 'subjects': [['matkailu'], ['pyöräily'], ['polkupyörät'], ['kulkuneuvot']], 'languages': ['eng'], 'rating': {'count': 0, 'average': 0}, 'images': ['/Cover/Show?author=Byrne%2C+David&callnumber=&size=large&title=Bicycle+diaries&recordid=helmet.2029887&source=Solr&isbn=0571241034&index=0'], 'formats': [{'value': '0/Book/', 'translated': 'Kirja'}, {'value': '1/Book/Book/', 'translated': 'Kirja'}], 'presenters': {'presenters': [], 'details': []}, 'id': 'helmet.2029887', 'title': 'Bicycle diaries', 'nonPresenterAuthors': [{'name': 'Byrne, David'}]}
    {'buildings': [{'value': '0/Heili/', 'translated': 'Heili-kirjastot'}, {'value': '1/Heili/12/', 'translated': 'Parikkala'}, {'value': '2/Heili/12/321/', 'translated': 'Saaren kirjasto'}], 'onlineUrls': [], 'series': [{'name': 'The Boxcar Children'}], 'subjects': [], 'languages': ['eng'], 'rating': {'count': 0, 'average': 0}, 'images': [], 'formats': [{'value': '0/Book/', 'translated': 'Kirja'}, {'value': '1/Book/Book/', 'translated': 'Kirja'}], 'presenters': {'presenters': [], 'details': []}, 'id': 'heili.888120', 'title': 'Bicycle Mystery', 'nonPresenterAuthors': [{'name': 'Warner, Gertrude Chandler'}, {'name': 'Cunningham, David kuvittanut', 'role': 'aut'}]}
    {'buildings': [{'value': '0/Keski/', 'translated': 'Keski-kirjastot'}, {'value': '1/Keski/jyv/', 'translated': 'Jyväskylä'}], 'onlineUrls': [], 'series': [], 'subjects': [['free jazz', 'triot', '2000-2009'], ['jazz', 'sähkökitara', 'Suomi', '2000-2009'], ['jazz', 'bassokitara', 'Yhdysvallat', '2000-2009'], ['jazz', 'kontrabasso', 'Yhdysvallat', '2000-2009'], ['jazz', 'rummut', 'Saksa', '2000-2009'], ['psykedeelinen rock', '2000-2009']], 'languages': ['eng'], 'rating': {'count': 0, 'average': 0}, 'images': [], 'formats': [{'value': '0/Sound/', 'translated': 'Äänite'}, {'value': '1/Sound/CD/', 'translated': 'CD'}], 'presenters': {'presenters': [{'name': 'Johnny La Marama', 'role': 'esitt.'}, {'name': 'Kalima, Kalle', 'role': 'esitt.'}], 'details': ['Johnny La Marama: Chris Dahlgren (b, electronics, voc), Kalle Kalima (g, electronics, voc), Eric Schaefer (dr, perc, sampler, voc)']}, 'id': 'keski.512598', 'title': 'Bicycle revolution', 'nonPresenterAuthors': []}
    {'buildings': [{'value': '0/Helmet/', 'translated': 'Helmet-kirjastot'}, {'value': '1/Helmet/k/', 'translated': 'Kauniainen'}, {'value': '2/Helmet/k/k01/', 'translated': 'Kauniainen'}], 'onlineUrls': [], 'series': [], 'subjects': [['1940-luku'], ['1950-luku'], ['Yhdysvallat']], 'languages': ['eng'], 'rating': {'count': 0, 'average': 0}, 'images': [], 'formats': [{'value': '0/Sound/', 'translated': 'Äänite'}, {'value': '1/Sound/SoundDisc/', 'translated': 'Äänilevy'}], 'presenters': {'presenters': [{'name': 'Gaddy, Bob', 'role': 'esittäjä'}, {'name': 'Gaddy, Bob', 'role': 'laulaja'}, {'name': 'Gaddy, Bob', 'role': 'piano'}, {'name': 'Dupree, Jac', 'role': 'laulaja'}, {'name': 'Dupree, Jack', 'role': 'piano'}, {'name': 'Sue, Bobby', 'role': 'laulaja'}], 'details': []}, 'id': 'helmet.1252370', 'title': 'Bicycle boogie', 'nonPresenterAuthors': [{'name': 'Gaddy, Bob', 'role': 'säveltäjä'}, {'name': 'McGhee, Brownie', 'role': 'säveltäjä'}, {'name': 'Dupree, Jack', 'role': 'säveltäjä'}, {'name': 'Dale, Larry', 'role': 'säveltäjä'}, {'name': 'Sue, Bobby', 'role': 'säveltäjä'}, {'name': 'Terry, Sonny', 'role': 'huuliharppu'}, {'name': 'McGhee, Brownie', 'role': 'kitara'}, {'name': 'Harris, Bob', 'role': 'b'}, {'name': 'Wood, George', 'role': 'rummut'}, {'name': 'Dale, Larry', 'role': 'kitara'}, {'name': 'Wallace, Cedric', 'role': 'b'}, {'name': 'Johnson, Earl A.', 'role': 'rummut'}, {'name': 'Moore, Gene', 'role': 'rummut'}, {'name': 'Dodds, Baby', 'role': 'rummut'}, {'name': 'Lucas, Al', 'role': 'b'}, {'name': 'Brown, Pete', 'role': 'alttosaksofoni'}, {'name': 'Spruill, Jimmy', 'role': 'kitara'}, {'name': 'Page, June', 'role': 'b'}, {'name': 'Spoots, George', 'role': 'rummut'}]}
    {'buildings': [{'value': '0/Eepos/', 'translated': 'Eepos-kirjastot'}, {'value': '1/Eepos/50/', 'translated': 'Kauhava'}, {'value': '2/Eepos/50/402/', 'translated': 'Kauhavan pääkirjasto'}, {'value': '3/Eepos/50/402/1/', 'translated': '1'}], 'onlineUrls': [], 'series': [], 'subjects': [], 'languages': ['eng'], 'rating': {'count': 0, 'average': 0}, 'images': [], 'formats': [{'value': '0/Sound/', 'translated': 'Äänite'}, {'value': '1/Sound/SoundDisc/', 'translated': 'Äänilevy'}], 'presenters': {'presenters': [], 'details': ['Bob Gaddy (voc, p) ; Brownie McGhee (g) ; Jack Dupree (voc, p) ; Larry Dale (voc, g) ; Bobby Sue (voc)..']}, 'id': 'eepos.2088987', 'title': 'Bicycle boogie', 'nonPresenterAuthors': [{'name': 'Gaddy, Bob'}]}

    * Performing a search for images available online
    Search would have matched 3 records
    Title: Lavagem do Bonfim
    URL:   https://api.finna.fi/Cover/Show?id=musketti_helina.M015%3ARd3.1%3A768&index=0&size=large

    Title: Mainoskortti (painokuva): englantilaisen Harry Holt Trio:n mainoskortti
    URL:   https://api.finna.fi/Cover/Show?id=muistaja_kerava.M011-90287&index=0&size=large

    Title: Postikorttipainanteinen valokuva kahdeksasta oksalla seisovasta makawi-papukaijasta Miamin Parrot Junglessa
    URL:   https://api.finna.fi/Cover/Show?id=siirtolaisuusmuseo_ah.M011-1376833&index=0&size=large


    * Performing a book search by author, sorting results by date, oldest first
    Search would have matched 5477 records
    {'id': 'fennica.431237', 'year': '1800', 'title': 'Tomtesagor'}
    {'id': 'alma.510296', 'year': '1822', 'title': 'Suomen kansan wanhoja runoja, ynnä myös nykyisempiä lauluja'}
    {'id': 'piki.916440', 'year': '1822', 'title': 'Suomen kansan vanhoja runoja, ynnä myös nykyisempiä lauluja. Ensimmäinen osa'}
    {'id': 'sksdoria_books.10024_147698', 'year': '1822', 'title': 'Suomen kansan wanhoja runoja ynnä myös nykyisempiä lauluja : 1. osa'}
    {'id': 'helka.1214011', 'year': '1822', 'title': 'Suomen kansan wanhoja runoja ynnä myös nykyisempiä lauluja'}
    * Retrieving a single record
    {'buildings': [{'value': '0/NLF/', 'translated': 'Kansalliskirjasto'}, {'value': '1/NLF/fennica/', 'translated': 'Fennica'}], 'onlineUrls': [], 'series': [], 'subjects': [], 'languages': [], 'rating': {'count': 0, 'average': 0}, 'images': [], 'formats': [{'value': '0/Book/', 'translated': 'Kirja'}, {'value': '1/Book/Book/', 'translated': 'Kirja'}], 'presenters': {'presenters': [], 'details': []}, 'id': 'fennica.431237', 'title': 'Tomtesagor', 'nonPresenterAuthors': [{'name': 'Topelius, Z., puuteluettelotieto'}]}

    * Retrieving multiple records
    {'id': 'alma.510296', 'title': 'Suomen kansan wanhoja runoja, ynnä myös nykyisempiä lauluja'}
    {'id': 'piki.916440', 'title': 'Suomen kansan vanhoja runoja, ynnä myös nykyisempiä lauluja. Ensimmäinen osa'}
    {'id': 'fennica.431237', 'title': 'Tomtesagor'}

## License

The code is published under the [Apache 2.0](LICENSE.txt) license.

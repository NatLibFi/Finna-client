#!/usr/bin/env python3
"""Module for accessing Finna.fi REST API"""

from enum import Enum
import requests

# Default API base URL
API_BASE = 'https://api.finna.fi/api/v1/'
# Base URL for images
IMAGE_BASE = 'https://api.finna.fi'

class FinnaSearchType(Enum):
    """Enumeration of the supported search types in the Finna search API"""
    AllFields = "AllFields"
    Title = "Title"
    TitleStart = "TitleStart"
    TitleExact = "TitleExact"
    Author = "Author"
    Subject = "Subject"
    description = "description"
    geographic = "geographic"
    Classification = "Classification"
    Identifier = "Identifier"
    Series = "Series"
    toc = "toc"
    publisher = "publisher"
    PublicationPlace = "PublicationPlace"
    year = "year"
    Holdings = "Holdings"

class FinnaSortMethod(Enum):
    """Enumeration of the supported sort methods in the Finna search API"""
    relevance_id_asc = 'relevance,id asc'
    main_date_str_desc = 'main_date_str desc'
    main_date_str_asc = 'main_date_str asc'
    callnumber = 'callnumber'
    author = 'author'
    title = 'title'
    last_indexed_desc_id_asc = 'last_indexed desc,id asc'

class FinnaLanguage(Enum):
    """Enumeration of the supported languages in the Finna search API"""
    fi = 'fi'
    sv = 'sv'
    en_gb = 'en-gb'

class FinnaClient:
    """Client class for accessing Finna.fi REST API"""

    def __init__(self, api_base=API_BASE):
        self.api_base = api_base
    
    def get_record(self, record_id, fields=None, lng=None):
        """Retrieve a single record by its ID"""
        
        payload = {'id': record_id}
        if fields is not None:
            payload['field[]'] = fields
        if lng is not None:
            if not isinstance(lng, FinnaLanguage):
                raise ValueError('lng must be a valid FinnaLanguage')
            payload['lng'] = lng.value
        
        req = requests.get(self.api_base + 'record', params=payload)
        if req.status_code == 400:
            raise ValueError(req.json()['statusMessage'] + ", record_id: '{}'".format(record_id))
        req.raise_for_status()
        return req.json()['records'][0]
    
    def get_records(self, record_ids, fields=None, lng=None):
        """Retrieve multiple records by their IDs. IDs which don't match any
        records will be ignored."""

        payload = {'id[]': record_ids}
        if fields is not None:
            payload['field[]'] = fields
        if lng is not None:
            if not isinstance(lng, FinnaLanguage):
                raise ValueError('lng must be a valid FinnaLanguage')
            payload['lng'] = lng.value
        
        req = requests.get(self.api_base + 'record', params=payload)
        req.raise_for_status()
        try:
            return req.json()['records']
        except KeyError:
            return []

    def search(self, lookfor="", search_type=FinnaSearchType.AllFields,
        fields=None, filters=None, facets=None, facetFilters=None, sort=None,
        page=None, limit=None, lng=None, **kwargs):
        """Perform a Finna search and return the search results."""
        
        if not isinstance(search_type, FinnaSearchType):
            raise ValueError('search_type must be a valid FinnaSearchType')
        payload = {'lookfor': lookfor, 'type': search_type.value}
        if fields is not None:
            payload['field[]'] = fields
        if filters is not None:
            payload['filter[]'] = filters
        if facets is not None:
            payload['facet[]'] = facets
        if facetFilters is not None:
            payload['facetFilters'] = facetFilters
        if sort is not None:
            if not isinstance(sort, FinnaSortMethod):
                raise ValueError('sort must be a valid FinnaSortMethod')
            payload['sort'] = sort.value
        if page is not None:
            payload['page'] = page
        if limit is not None:
            payload['limit'] = limit
        if lng is not None:
            if not isinstance(lng, FinnaLanguage):
                raise ValueError('lng must be a valid FinnaLanguage')
            payload['lng'] = lng.value
        if kwargs:
            payload.update(kwargs)
        
        req = requests.get(self.api_base + 'search', params=payload)
        req.raise_for_status()
        return req.json()

    def __str__(self):
        """Return a string representation of this object"""
        return "FinnaClient(api_base='{}')".format(self.api_base)


if __name__ == '__main__':
    print("Demonstrating usage of FinnaClient")

    print()

    print("* Creating a FinnaClient object")
    finna = FinnaClient()
    print("Now we have a FinnaClient object:", finna)

    print()

    print("* Performing a general search")
    result = finna.search('bicycle', limit=5)
    print("Search would have matched {} records".format(result['resultCount']))
    for rec in result['records']:
        print(rec)

    print()
    
    print("* Performing a search for images available online")
    result = finna.search('bicycle', fields=['title', 'images'], 
                          filters=['format:0/Image/', 'online_boolean:1'])
    print("Search would have matched {} records".format(result['resultCount']))
    for rec in result['records']:
        print("Title:", rec['title'])
        print("URL:  ", IMAGE_BASE + rec['images'][0])
        print()
    
    print()
    print("* Performing a book search by author, sorting results by date, oldest first")
    result = finna.search('Topelius',
                          search_type=FinnaSearchType.Author,
                          fields=['title','id','year'],
                          filters=['format:0/Book/'], 
                          sort=FinnaSortMethod.main_date_str_asc,
                          limit=5)
    print("Search would have matched {} records".format(result['resultCount']))
    for rec in result['records']:
        print(rec)
    
    print("* Retrieving a single record")
    rec = finna.get_record('fennica.431237')
    print(rec)

    print()
    
    print("* Retrieving multiple records")
    recs = finna.get_records(['fennica.431237','alma.510296','piki.916440'], fields=['id','title'])
    for rec in recs:
        print(rec)

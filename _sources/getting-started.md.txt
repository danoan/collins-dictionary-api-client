# Getting started with Collins Dictionary Api Client

Command Line Interface and python library to make requests to the [Collins dictionary API](https://www.collinsdictionary.com/collins-api).

- [Read the docs](https://danoan.github.io/collins-dictionary-api-client/)
- Link to [Collin API documentation](https://drive.google.com/file/d/1CmAR_eCxRCrkIShKRo4f2DrvQ-d-S7Og/view?usp=sharing)

## Examples

```bash
$ collins-dictionary-api-client --secret-key <SECRET_KEY> search garden
{"resultNumber":69,"results":[{"entryLabel":"garden","entryUrl":"http://localhost/api/v1/dictionaries/english/entries/garden_1","entryId":"garden_1"}..."

```

Type `collins-dictionary-api-client --help` to see all available options.

## Methods available

The following methods are implemented in the client.

### search

Get a list of entry ids corresponding to the search term.

```json
{
    "resultNumber": 1,
    "results": [
        {
            "entryLabel": "legitim",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitim_1",
            "entryId": "legitim_1"
        }
    ],
    "dictionaryCode": "english",
    "currentPageIndex": 1,
    "pageNumber": 1
}
```

### did_you_mean

Get a list of suggestions corresponding to the input word.

The suggested words are close to the input word in a lexicographic sense.
For example, share a good portion of the prefix or the suffix.

```json
{
    "searchTerm": "legitim",
    "dictionaryCode": "english",
    "suggestions": [
        "legit",
        "legitimist",
        "legitimize",
        "legitimate",
        "flexitime",
        "legitimizer",
        "legitimator",
        "legitimiser",
        "gregatim",
        "legalism"
    ]
}
```

### get_best_matching

Get the metadata of the first entry found for the searched word.

```json
{
    "topics": [],
    "dictionaryCode": "english",
    "entryLabel": "legitim",
    "entryContent": "<div class=\"entry_container\"><div class=\"entry lang_en-gb\" id=\"legitim_1\"><span class=\"inline\"><h1 class=\"hwd\">legitim<\/h1><span> (<\/span><span class=\"pron\" type=\"\">ˈlɛdʒɪtɪm<\/span><span>)<\/span><\/span><div class=\"hom\" id=\"legitim_1.1\"><span class=\"gramGrp\"><span>   <\/span><span class=\"pos\">noun<\/span><\/span><div class=\"sense\"><span>     <\/span><span class=\"lbl\">Scots law<\/span><span> <\/span><span class=\"def\">the part of a person's moveable estate that is inherited by his or her children on that person's death<\/span><\/div><!-- End of DIV sense--><\/div><!-- End of DIV hom--><\/div><!-- End of DIV entry lang_en-gb--><\/div><!-- End of DIV entry_container-->\n",
    "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitim_1",
    "format": "html",
    "entryId": "legitim_1"
}
```

### get_entry

Get the first entry found for the searched word.

```json
{
    "topics": [],
    "dictionaryCode": "english",
    "entryLabel": "legit",
    "entryContent": "<div class=\"entry_container\"><div class=\"entry lang_en-gb\" id=\"legit_1\"><span class=\"inline\"><h1 class=\"hwd\">legit<\/h1><span> (<\/span><span class=\"pron\" type=\"\">lɪˈdʒɪt<a href=\"#\" class=\"playback\"><img src=\"https://api.collinsdictionary.com/external/images/redspeaker.gif?version=2016-11-09-0913\" alt=\"Pronunciation for legit\" class=\"sound\" title=\"Pronunciation for legit\" style=\"cursor: pointer\"/><\/a><audio type=\"pronunciation\" title=\"legit\"><source type=\"audio/mpeg\" src=\"https://api.collinsdictionary.com/media/sounds/sounds/e/en_/en_gb/en_gb_legit.mp3\"/>Your browser does not support HTML5 audio.<\/audio><\/span><span>)<\/span><span class=\"lbl\"><span> <\/span>slang<\/span><\/span><div class=\"hom\" id=\"legit_1.1\"><span class=\"gramGrp\"><span>   <\/span><span class=\"pos\">adjective<\/span><\/span><div class=\"sense\"><span class=\"sensenum\">     1 <\/span><span class=\"xr\"><span class=\"lbl\">short for<\/span><span> <\/span>\n                \n        \t\t<a data-resource=\"english\" data-topic=\"legitimate_1\" href=\"\">legitimate<\/a><\/span><\/div><!-- End of DIV sense--><\/div><!-- End of DIV hom--><div class=\"hom\" id=\"legit_1.2\"><span> <br/>▷ <\/span><span class=\"gramGrp\"><span class=\"pos\">noun<\/span><\/span><div class=\"sense\"><span class=\"sensenum\">     2 <\/span><span class=\"def\">legitimate or professionally respectable drama<\/span><\/div><!-- End of DIV sense--><\/div><!-- End of DIV hom--><\/div><!-- End of DIV entry lang_en-gb--><\/div><!-- End of DIV entry_container-->\n",
    "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legit_1",
    "format": "html",
    "entryId": "legit_1"
}
```

### get_pronunciations

Get a list of pronunciations.

Each pronunciation entry contains a URL to a mp3 file.

```json
[
    {
        "dictionaryCode": "english",
        "pronunciationUrl": "https://api.collinsdictionary.com/media/sounds/sounds/e/en_/en_gb/en_gb_legit.mp3",
        "lang": "uk",
        "entryId": "legit_1"
    }
]
```

### get_nearby_entries

Get a list of entries related to the input word.

The returned words or expressions are in the same semantic scope of the input word.

```json
{
    "nearbyFollowingEntries": [
        {
            "entryLabel": "legitim",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitim_1",
            "entryId": "legitim_1"
        },
        {
            "entryLabel": "legitimate",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitimate_1",
            "entryId": "legitimate_1"
        },
        {
            "entryLabel": "legitimator",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitimator_1",
            "entryId": "legitimator_1"
        },
        {
            "entryLabel": "legitimiser",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitimiser_1",
            "entryId": "legitimiser_1"
        },
        {
            "entryLabel": "legitimist",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitimist_1",
            "entryId": "legitimist_1"
        },
        {
            "entryLabel": "legitimistic",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitimistic_1",
            "entryId": "legitimistic_1"
        },
        {
            "entryLabel": "legitimize",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitimize_1",
            "entryId": "legitimize_1"
        },
        {
            "entryLabel": "legitimizer",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legitimizer_1",
            "entryId": "legitimizer_1"
        },
        {
            "entryLabel": "legless",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legless_1",
            "entryId": "legless_1"
        },
        {
            "entryLabel": "leglessness",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/leglessness_1",
            "entryId": "leglessness_1"
        }
    ],
    "dictionaryCode": "english",
    "nearbyPrecedingEntries": [
        {
            "entryLabel": "legionnaire's disease",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legionnaires-disease_1_1",
            "entryId": "legionnaires-disease_1_1"
        },
        {
            "entryLabel": "legislate",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislate_1",
            "entryId": "legislate_1"
        },
        {
            "entryLabel": "legislation",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislation_1",
            "entryId": "legislation_1"
        },
        {
            "entryLabel": "legislative",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislative_1",
            "entryId": "legislative_1"
        },
        {
            "entryLabel": "legislative assembly",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislative-assembly_1",
            "entryId": "legislative-assembly_1"
        },
        {
            "entryLabel": "legislative council",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislative-council_1",
            "entryId": "legislative-council_1"
        },
        {
            "entryLabel": "legislator",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislator_1",
            "entryId": "legislator_1"
        },
        {
            "entryLabel": "legislatorial",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislatorial_1",
            "entryId": "legislatorial_1"
        },
        {
            "entryLabel": "legislature",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legislature_1",
            "entryId": "legislature_1"
        },
        {
            "entryLabel": "legist",
            "entryUrl": "http://localhost/api/v1/dictionaries/english/entries/legist_1",
            "entryId": "legist_1"
        }
    ],
    "entryId": "legit_1"
}
```


## Contributing

Please reference to our [contribution](https://danoan.github.io/collins-dictionary-api-client/contributing.html) and [code-of-conduct](https://danoan.github.io/collins-dictionary-api-client/code-of-conduct.html)

# BubbleTeam™ Server 🛁🍵

### Adding URLs to the database

Adding a URL to the base is easy. All you need to do is make an HTTP request.

The endpoint is `/url`, which accepts `POST` requests.

The request body must contain JSON with the following structure:

```json
{
  "username": string,
  "url": string,
}
```

`username` can be any string
`url` can be any valid URL.

If your request is malformed (e.g. you forgot a field, or sent an invalid URL), the response will look something like:

```json
{
    "reason": "missing 'username' field in JSON body",
    "success": false
}
```

Here's an example valid request:

```POST https://bubbleteam-server.herokuapp.com/url```
```json
{
  "username": "avi",
  "url": "http://www.cnn.com/2017/04/29/politics/donald-trump-100-days-rally/index.html",
}
```

Which would return the following response:

```json
{
    "_id": "5905721cfd71822a7d593200",
    "entities": [
        {
            "count": 20,
            "relevance": 0.925867,
            "text": "Trump",
            "type": "Person"
        },
        {
            "count": 7,
            "relevance": 0.537671,
            "text": "Vice President",
            "type": "JobTitle"
        },
        {
            "count": 4,
            "relevance": 0.347251,
            "text": "president",
            "type": "JobTitle"
        },
        {
            "count": 7,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/David_Gergen",
                "name": "David Gergen",
                "subtype": [
                    "Politician",
                    "BoardMember",
                    "TVActor",
                    "TVWriter"
                ]
            },
            "relevance": 0.284351,
            "text": "David Gergen",
            "type": "Person"
        },
        {
            "count": 2,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Ronald_Reagan",
                "name": "Ronald Reagan",
                "subtype": [
                    "Politician",
                    "President",
                    "AwardWinner",
                    "ChivalricOrderMember",
                    "MilitaryPerson",
                    "PoliticalAppointer",
                    "USPresident",
                    "FilmActor",
                    "TVActor"
                ]
            },
            "relevance": 0.281128,
            "text": "President Ronald Reagan",
            "type": "Person"
        },
        {
            "count": 3,
            "relevance": 0.248758,
            "text": "White House",
            "type": "Organization"
        },
        {
            "count": 2,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Swatara_Township,_Dauphin_County,_Pennsylvania",
                "name": "Swatara Township, Dauphin County, Pennsylvania",
                "subtype": [
                    "CityTown",
                    "StateOrCounty"
                ]
            },
            "relevance": 0.229042,
            "text": "Pennsylvania",
            "type": "Location"
        },
        {
            "count": 3,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Barack_Obama",
                "name": "Barack Obama",
                "subtype": [
                    "Politician",
                    "President",
                    "Appointer",
                    "AwardWinner",
                    "Celebrity",
                    "PoliticalAppointer",
                    "U.S.Congressperson",
                    "USPresident",
                    "TVActor"
                ]
            },
            "relevance": 0.224396,
            "text": "Barack Obama",
            "type": "Person"
        },
        {
            "count": 4,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/United_States",
                "name": "United States",
                "subtype": [
                    "Region",
                    "AdministrativeDivision",
                    "GovernmentalJurisdiction",
                    "FilmEditor",
                    "Country"
                ]
            },
            "relevance": 0.216166,
            "text": "US",
            "type": "Location"
        },
        {
            "count": 2,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Washington,_D.C.",
                "name": "Washington, D.C.",
                "subtype": [
                    "AdministrativeDivision",
                    "GovernmentalJurisdiction",
                    "MilitaryPost",
                    "PlaceWithNeighborhoods",
                    "USCounty",
                    "City"
                ]
            },
            "relevance": 0.214518,
            "text": "Washington",
            "type": "Location"
        },
        {
            "count": 2,
            "relevance": 0.209121,
            "text": "Harrisburg",
            "type": "Location"
        },
        {
            "count": 3,
            "relevance": 0.20147,
            "text": "executive",
            "type": "JobTitle"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Mike_Pence",
                "name": "Mike Pence",
                "subtype": [
                    "Politician",
                    "U.S.Congressperson",
                    "BroadcastArtist"
                ]
            },
            "relevance": 0.199392,
            "text": "Mike Pence",
            "type": "Person"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/North_Korea",
                "name": "North Korea",
                "subtype": [
                    "GovernmentalJurisdiction",
                    "Country"
                ]
            },
            "relevance": 0.195313,
            "text": "North Korea",
            "type": "Location"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/CNN",
                "name": "CNN",
                "subtype": [
                    "Broadcast",
                    "AwardWinner",
                    "RadioNetwork",
                    "TVNetwork"
                ]
            },
            "relevance": 0.177431,
            "text": "CNN",
            "type": "Company"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Richard_Nixon",
                "name": "Richard Nixon",
                "subtype": [
                    "FilmCharacter",
                    "MusicalArtist",
                    "Politician",
                    "President",
                    "Appointer",
                    "MilitaryCommander",
                    "MilitaryPerson",
                    "PoliticalAppointer",
                    "TVPersonality",
                    "U.S.Congressperson",
                    "USPresident",
                    "USVicePresident",
                    "FilmActor",
                    "TVActor"
                ]
            },
            "relevance": 0.175443,
            "text": "Richard Nixon",
            "type": "Person"
        },
        {
            "count": 1,
            "relevance": 0.171046,
            "text": "Paris",
            "type": "Location"
        },
        {
            "count": 3,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Seth_Meyers",
                "name": "Seth Meyers",
                "subtype": [
                    "Actor",
                    "AwardNominee",
                    "FilmActor",
                    "FilmProducer",
                    "TVActor",
                    "FilmWriter",
                    "TVWriter"
                ]
            },
            "relevance": 0.170223,
            "text": "Seth Meyers",
            "type": "Person"
        },
        {
            "count": 1,
            "relevance": 0.169635,
            "text": "CNN Newsroom",
            "type": "Broadcaster"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Harry_S._Truman",
                "name": "Harry S. Truman",
                "subtype": [
                    "Politician",
                    "President",
                    "MilitaryCommander",
                    "MilitaryPerson",
                    "PoliticalAppointer",
                    "U.S.Congressperson",
                    "USPresident",
                    "USVicePresident",
                    "ElectionCampaign",
                    "TVActor"
                ]
            },
            "relevance": 0.168069,
            "text": "Harry Truman",
            "type": "Person"
        },
        {
            "count": 1,
            "relevance": 0.16514,
            "text": "Office of Trade and Manufacturing Policy",
            "type": "Organization"
        },
        {
            "count": 1,
            "relevance": 0.163968,
            "text": "Hollywood",
            "type": "Location"
        },
        {
            "count": 1,
            "relevance": 0.158904,
            "text": "Mexico",
            "type": "Location"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Jared_Kushner",
                "name": "Jared Kushner",
                "subtype": [
                    "Celebrity"
                ]
            },
            "relevance": 0.158649,
            "text": "Jared Kushner",
            "type": "Person"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Poppy_Harlow",
                "name": "Poppy Harlow",
                "subtype": [
                    "TVPersonality"
                ]
            },
            "relevance": 0.155999,
            "text": "Poppy Harlow",
            "type": "Person"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/Neil_Gorsuch",
                "name": "Neil Gorsuch",
                "subtype": [
                    "Judge"
                ]
            },
            "relevance": 0.154718,
            "text": "Neil Gorsuch",
            "type": "Person"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/James_A._Garfield",
                "name": "James A. Garfield",
                "subtype": [
                    "Politician",
                    "President"
                ]
            },
            "relevance": 0.152301,
            "text": "James Garfield",
            "type": "Person"
        },
        {
            "count": 1,
            "relevance": 0.151146,
            "text": "political analyst",
            "type": "JobTitle"
        },
        {
            "count": 1,
            "disambiguation": {
                "dbpedia_resource": "http://dbpedia.org/resource/New_York_City",
                "name": "New York City",
                "subtype": [
                    "PoliticalDistrict",
                    "GovernmentalJurisdiction",
                    "PlaceWithNeighborhoods",
                    "WineRegion",
                    "FilmScreeningVenue",
                    "City"
                ]
            },
            "relevance": 0.150945,
            "text": "New York",
            "type": "Location"
        },
        {
            "count": 1,
            "relevance": 0.148761,
            "text": "Ivanka",
            "type": "Person"
        },
        {
            "count": 1,
            "relevance": 0.145935,
            "text": "Russia",
            "type": "Location"
        },
        {
            "count": 1,
            "relevance": 0.143238,
            "text": "John Berman",
            "type": "Person"
        },
        {
            "count": 1,
            "relevance": 0.136522,
            "text": "Supreme Court",
            "type": "Organization"
        },
        {
            "count": 4,
            "relevance": 0.123353,
            "text": "100 days",
            "type": "Quantity"
        },
        {
            "count": 1,
            "relevance": 0.123353,
            "text": "136 years",
            "type": "Quantity"
        },
        {
            "count": 1,
            "relevance": 0.123353,
            "text": "36 years",
            "type": "Quantity"
        },
        {
            "count": 1,
            "relevance": 0.123353,
            "text": "one-hour",
            "type": "Quantity"
        },
        {
            "count": 1,
            "relevance": 0.123353,
            "text": "100-day",
            "type": "Quantity"
        }
    ],
    "keywords": [
        {
            "relevance": 0.945396,
            "text": "Trump"
        },
        {
            "relevance": 0.821267,
            "text": "White House Correspondents"
        },
        {
            "relevance": 0.789104,
            "text": "Trump rallies"
        },
        {
            "relevance": 0.761441,
            "text": "president"
        },
        {
            "relevance": 0.761377,
            "text": "time Trump"
        },
        {
            "relevance": 0.705269,
            "text": "President Barack Obama"
        },
        {
            "relevance": 0.68977,
            "text": "President Ronald Reagan"
        },
        {
            "relevance": 0.682047,
            "text": "executive orders"
        },
        {
            "relevance": 0.642245,
            "text": "populist message resonates"
        },
        {
            "relevance": 0.636029,
            "text": "Vice President"
        },
        {
            "relevance": 0.629556,
            "text": "analyst David Gergen"
        },
        {
            "relevance": 0.62926,
            "text": "big talking points"
        },
        {
            "relevance": 0.627449,
            "text": "deeply disturbing speech"
        },
        {
            "relevance": 0.626125,
            "text": "Paris climate accord"
        },
        {
            "relevance": 0.625636,
            "text": "health care"
        },
        {
            "relevance": 0.621888,
            "text": "special prime-time edition"
        },
        {
            "relevance": 0.612456,
            "text": "American president"
        },
        {
            "relevance": 0.600901,
            "text": "son-in-law Jared Kushner"
        },
        {
            "relevance": 0.594785,
            "text": "real estate mogul"
        },
        {
            "relevance": 0.59351,
            "text": "White House posts"
        },
        {
            "relevance": 0.588653,
            "text": "key immigration goals"
        },
        {
            "relevance": 0.588148,
            "text": "reality TV star"
        },
        {
            "relevance": 0.587424,
            "text": "lowest approval ratings"
        },
        {
            "relevance": 0.587094,
            "text": "health care overhaul"
        },
        {
            "relevance": 0.585576,
            "text": "comedian Seth Meyers"
        },
        {
            "relevance": 0.581564,
            "text": "major legislative achievement"
        },
        {
            "relevance": 0.538297,
            "text": "larger crowd"
        },
        {
            "relevance": 0.535914,
            "text": "campaign playbook"
        },
        {
            "relevance": 0.535903,
            "text": "100-day milestone"
        },
        {
            "relevance": 0.535442,
            "text": "divisive speech"
        },
        {
            "relevance": 0.531481,
            "text": "prime-time duel"
        },
        {
            "relevance": 0.529861,
            "text": "Saturday night"
        },
        {
            "relevance": 0.529307,
            "text": "dinner"
        },
        {
            "relevance": 0.529202,
            "text": "Mike Pence"
        },
        {
            "relevance": 0.527172,
            "text": "divisive tone"
        },
        {
            "relevance": 0.519659,
            "text": "North Korea"
        },
        {
            "relevance": 0.518658,
            "text": "Washington media"
        },
        {
            "relevance": 0.517237,
            "text": "especially rang"
        },
        {
            "relevance": 0.516458,
            "text": "Manufacturing Policy"
        },
        {
            "relevance": 0.515841,
            "text": "incredible journey"
        },
        {
            "relevance": 0.515045,
            "text": "large group"
        },
        {
            "relevance": 0.512974,
            "text": "better people"
        },
        {
            "relevance": 0.512596,
            "text": "campaign aides"
        },
        {
            "relevance": 0.512305,
            "text": "John Berman"
        },
        {
            "relevance": 0.510649,
            "text": "Poppy Harlow"
        },
        {
            "relevance": 0.51013,
            "text": "CNN Newsroom"
        },
        {
            "relevance": 0.509503,
            "text": "presidential adviser"
        },
        {
            "relevance": 0.509492,
            "text": "hotel ballroom"
        },
        {
            "relevance": 0.508827,
            "text": "campaign trail"
        },
        {
            "relevance": 0.50767,
            "text": "Hollywood actors"
        }
    ],
    "language": "en",
    "retrieved_url": "http://www.cnn.com/2017/04/29/politics/donald-trump-100-days-rally/index.html",
    "sentiment": {
        "document": {
            "label": "negative",
            "score": -0.027134
        }
    },
    "username": "ro"
}
```

import json
# filename = 'linktest.json'
data =[
    {
    "availability": 56.37376656633328,
    "available_bandwidth": 602746.015561422,
    "id": "id",
    "latency": 146582.15146899645,
    "name": "miami-Boca.amLight.sdx",
    "packet_loss": 59.621339166831824,
    "ports": [
      {
        "id": "id",
        "label_range": [
          "label_range",
          "label_range"
        ],
        "name": "urn:sdx:port:amlight.net:Novi06:9",
        "node": "urn:sdx:port:amlight.net:Novi06",
        "short_name": "9",
        "status": "up"
      },
      {
        "id": "id",
        "label_range": [
          "label_range",
          "label_range"
        ],
        "name": "urn:sdx:port:amlight.net:Novi06:10",
        "node": "urn:sdx:port:amlight.net:Novi06",
        "short_name": "10",
        "status": "up"
      }
    ],
    "short_name": "Miami-BocaRaton",
    "total_bandwidth": 80083.7389632821
  },
{
    "availability": 56.37376656633328,
    "available_bandwidth": 602746.015561422,
    "id": "id",
    "latency": 146582.15146899645,
    "name": "miami-Boca.amLight.sdx",
    "packet_loss": 59.621339166831824,
    "ports": [
      {
        "id": "id",
        "label_range": [
          "label_range",
          "label_range"
        ],
        "name": "urn:sdx:port:amlight.net:Novi06:9",
        "node": "urn:sdx:port:amlight.net:Novi06",
        "short_name": "9",
        "status": "up"
      },
      {
        "id": "id",
        "label_range": [
          "label_range",
          "label_range"
        ],
        "name": "urn:sdx:port:amlight.net:Novi06:10",
        "node": "urn:sdx:port:amlight.net:Novi06",
        "short_name": "10",
        "status": "up"
      }
    ],
    "short_name": "Miami-BocaRaton",
    "total_bandwidth": 80083.7389632821
  },
{
    "availability": 56.37376656633328,
    "available_bandwidth": 602746.015561422,
    "id": "id",
    "latency": 146582.15146899645,
    "name": "miami-Boca.amLight.sdx",
    "packet_loss": 59.621339166831824,
    "ports": [
      {
        "id": "id",
        "label_range": [
          "label_range",
          "label_range"
        ],
        "name": "urn:sdx:port:amlight.net:Novi06:9",
        "node": "urn:sdx:port:amlight.net:Novi06",
        "short_name": "9",
        "status": "up"
      },
      {
        "id": "id",
        "label_range": [
          "label_range",
          "label_range"
        ],
        "name": "urn:sdx:port:amlight.net:Novi06:10",
        "node": "urn:sdx:port:amlight.net:Novi06",
        "short_name": "10",
        "status": "up"
      }
    ],
    "short_name": "Miami-BocaRaton",
    "total_bandwidth": 80083.7389632821
}

]



with open('multilink.json', 'w') as json_file:
    json.dump(data, json_file,  indent=4, sort_keys=True)

print(data)
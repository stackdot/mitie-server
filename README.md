[![Build Status](https://drone.stackdot.com/api/badges/stackdot/mitie-server/status.svg)](https://drone.stackdot.com/stackdot/mitie-server)

<p align="center">
  <img src="assets/mighty.jpg" />
</p>

# mitie-server
===

This project is a simple HTTP server (based on web.py) that provides REST access to NER provided by [MITIE](https://github.com/mit-nlp/MITIE).  The server, along with MITIE and its models, can be deployed and run in a Docker container.

## How to build

If don't have Docker in your development environment, you can use the provided [Vagrant](https://www.vagrantup.com/) VM:

	vagrant up
	vagrant ssh

Then build the Docker container:

	sudo docker build -t="uncharted/mitie-server" .

## How to run

Run the server using Docker:

	sudo docker run -it -p 8888:8888 uncharted/mitie-server

## Example requests

POST to /ner a single text string:

	curl -H "Content-Type: text" -X POST -d "{\"text\":\"Bob went to Washington with Jill.\"}" http://127.0.0.1:8888/ner

The response JSON:

	{
	  "text": "Bob went to Washington with Jill.",
	  "tokens": [
	    "Bob",
	    "went",
	    "to",
	    "Washington",
	    "with",
	    "Jill",
	    "."
	  ],
	  "entities": [
	    {
	      "score": 0.9118511252748589,
	      "tag": "PERSON",
	      "label": "Bob"
	    },
	    {
	      "score": 1.0281222502780096,
	      "tag": "LOCATION",
	      "label": "Washington"
	    },
	    {
	      "score": 1.035431287527289,
	      "tag": "PERSON",
	      "label": "Jill"
	    }
	  ]
	}

POST several text strings in a batch:

	curl -H "Content-Type: text" -X POST -d "{\"text\":[\"Bob went to Washington with Jill.\", \"Carl works for Microsoft Corp.\"]}" http://127.0.0.1:8888/ner

The response JSON:

	[
	  {
	    "text": "Bob went to Washington with Jill.",
	    "tokens": [
	      "Bob",
	      "went",
	      "to",
	      "Washington",
	      "with",
	      "Jill",
	      "."
	    ],
	    "entities": [
	      {
	        "score": 0.9118511252748589,
	        "tag": "PERSON",
	        "label": "Bob"
	      },
	      {
	        "score": 1.0281222502780096,
	        "tag": "LOCATION",
	        "label": "Washington"
	      },
	      {
	        "score": 1.035431287527289,
	        "tag": "PERSON",
	        "label": "Jill"
	      }
	    ]
	  },
	  {
	    "text": "Carl works for Microsoft Corp.",
	    "tokens": [
	      "Carl",
	      "works",
	      "for",
	      "Microsoft",
	      "Corp",
	      "."
	    ],
	    "entities": [
	      {
	        "score": 0.7585827626747964,
	        "tag": "PERSON",
	        "label": "Carl"
	      },
	      {
	        "score": 1.3715222669382523,
	        "tag": "ORGANIZATION",
	        "label": "Microsoft Corp"
	      }
	    ]
	  }
	]
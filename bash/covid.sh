#!/bin/bash
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
TODAY=$(date '+%d %B %Y')
echo "On $TODAY, there was $POSITIVE positive COVID cases, $NEGATIVE negative tests, $DEATHS deaths, and $HOSPITALIZED hospitalizations."

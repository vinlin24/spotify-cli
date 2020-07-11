#!/bin/bash
rm -rf __pycache__ && \
gcloud functions deploy \
	auth-refresh \
	--entry-point main \
	--memory 128MB \
	--project spotify-cli-283006 \
	--region asia-east2 \
	--runtime python37 \
	--trigger-http \
	--allow-unauthenticated

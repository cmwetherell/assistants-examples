Most of this code is from the phidata library. I found running the app fairly easy to get up and running (You'll need to make sure Docker and postgresql are installed). It works ok, but not great. A step needs to be added to create a new prompt once the RAG happens. E.g., ffind me these documents and then summarize should create a search prompt for RAG and then a "do this with the chunks" type of prompt.
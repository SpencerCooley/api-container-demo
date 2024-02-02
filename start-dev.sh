#!/bin/bash
docker run -v "$(pwd)/app/:/app" -p 8000:8000 demo-fastapi



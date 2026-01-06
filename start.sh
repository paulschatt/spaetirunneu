#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Starting Spaetirun Application...${NC}\n"

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Start PostgreSQL if not running
echo -e "${GREEN}Checking PostgreSQL...${NC}"
if ! docker ps | grep -q postgres; then
    echo "Starting PostgreSQL..."
    cd "$SCRIPT_DIR"
    docker-compose up -d
else
    echo "PostgreSQL already running"
fi

# Start Backend
echo -e "\n${GREEN}Starting Backend...${NC}"
cd "$SCRIPT_DIR/backend"
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 &
BACKEND_PID=$!
echo "Backend started with PID: $BACKEND_PID"

# Start Frontend
echo -e "\n${GREEN}Starting Frontend...${NC}"
cd "$SCRIPT_DIR/frontend"
npm run dev &
FRONTEND_PID=$!
echo "Frontend started with PID: $FRONTEND_PID"

echo -e "\n${BLUE}Application started!${NC}"
echo "Backend:  http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"

# Function to cleanup on exit
cleanup() {
    echo -e "\n${BLUE}Stopping services...${NC}"
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "Services stopped"
    exit 0
}

# Trap Ctrl+C and call cleanup
trap cleanup INT

# Wait for processes
wait

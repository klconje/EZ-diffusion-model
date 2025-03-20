#main program
echo "Running Simulation..."
python3 src/simulate.py

echo "Running Parameter Recovery..."
python3 src/recover.py

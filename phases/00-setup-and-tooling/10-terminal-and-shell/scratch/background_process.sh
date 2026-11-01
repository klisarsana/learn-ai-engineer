# Run in background (output still goes to terminal)
python train.py &

# Run in background, immune to hangup (closing terminal won't kill it)
nohup python train.py > train.log 2>&1 &

# Check what's running in background
jobs
ps aux | grep train.py

# Bring a background job to foreground
fg %1

# Kill a background process
kill %1
# or find its PID and kill that
kill $(pgrep -f "train.py")

# Method	        Survives terminal close?	    Can reattach?
# command &	        No	                            No
# nohup command &	Yes	                            No (check log file)
# screen / tmux	    Yes	                            Yes
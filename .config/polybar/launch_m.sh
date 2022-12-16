nate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use
# polybar-msg cmd quit

# Launch Polybar, using default config location ~/.config/polybar/config.ini
polybar mybar_m 2>&1 | tee -a /tmp/polybar_m.log & disown

echo "Polybar launched..."

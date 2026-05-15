#!/bin/bash

WALLPAPER_DIR="${1:-$HOME/Pictures/Wallpapers}"
CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/rofi-wallpapers"

# Ensure cache directory exists
mkdir -p "$CACHE_DIR"

mapfile -t IMAGES < <(find "$WALLPAPER_DIR" -type f \
  \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \) \
  | sort)

[ ${#IMAGES[@]} -eq 0 ] && {
  echo "No images found in $WALLPAPER_DIR"
  exit 1
}

ROFI_INPUT=""
for img in "${IMAGES[@]}"; do
  # Create a unique filename for the thumbnail based on the image's full path
  # This prevents collisions if two images in different subfolders share a filename
  thumb_name="$(echo -n "$img" | md5sum | awk '{print $1}').jpg"
  thumb_path="$CACHE_DIR/$thumb_name"

  # Generate the thumbnail if it doesn't already exist in the cache
  if [ ! -f "$thumb_path" ]; then
    # -thumbnail resizes quickly, ^ ensures it fills the box, -gravity center -extent crops to a square
    magick "$img" -thumbnail 256x256 "$thumb_path"
  fi

  # Pass the thumbnail path to rofi as the icon
  ROFI_INPUT+="$(basename "$img")\0icon\x1f${thumb_path}\n"
done

SELECTED_NAME="$(printf "$ROFI_INPUT" | rofi -dmenu -i \
  -p "// Wallpaper" \
  -show-icons \
  -theme ~/.config/rofi/themes/wallpaper.rasi \
  -theme-str 'element-icon { size: 8em; }' \
  -theme-str 'listview { columns: 4; lines: 3; }' \
  -mesg "press esc to cancel" )"

[ -z "$SELECTED_NAME" ] && exit 0

# Map basename back to full path
SELECTED=""
for img in "${IMAGES[@]}"; do
  if [ "$(basename "$img")" = "$SELECTED_NAME" ]; then
    SELECTED="$img"
    break
  fi
done

[ -z "$SELECTED" ] && {
  echo "Error: could not resolve path for: $SELECTED_NAME"
  exit 1
}

wal "$SELECTED"
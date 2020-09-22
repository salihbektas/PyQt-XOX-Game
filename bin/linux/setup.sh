
LINK=$(readlink -f "0")
BASEDIR=$(dirname "$LINK")
ICON="${BASEDIR}/assets/GameIcon.png"
EXE="${BASEDIR}/XOXGAME"
echo "[Desktop Entry]
Name=XOXGAME
Exec="\"${EXE}\""
Icon="${ICON}"
Terminal=false
Type=Application
" >> /usr/share/applications/XOXGAME.desktop
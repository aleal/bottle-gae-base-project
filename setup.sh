echo "Checking python-pip program installation..."
if [[ -z $(type pip 2>/dev/null) ]];
then 
	echo "Please install python-pip package in your system and try again..."
	exit 1
fi

echo "Checking virtualenv program installation..."
if [[ -z $(type virtualenv 2>/dev/null) ]];
then
    echo "Installing virtualenv via python-pip (root permission required)..."
    sudo pip install python-virtualenv	
else 
	echo "Virtualenv installed!"
fi

CMD_PATH=$(readlink -f "$0")
VIRTUAL_ENV_PATH=$(dirname "$CMD_PATH")/../.${PWD##*/}
echo $VIRTUAL_ENV_PATH
if [ ! -d "$VIRTUAL_ENV_PATH" ]; 
then
    virtualenv $VIRTUAL_ENV_PATH
fi

echo "Activating virtalenv at $VIRTUAL_ENV_PATH..."
source $VIRTUAL_ENV_PATH/bin/activate

echo "Installing dev libs in virtualenv..."
pip install -r requirements-dev.txt

echo "Installing libs in project lib directory..."
# remove the old ones
rm -fr lib/*
pip install -r requirements.txt -t lib/

echo "Done. Have Fun! ;)"

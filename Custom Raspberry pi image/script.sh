filename="./boards/raspberry-pi/raspbian.json"

while read line
do
	sed "39i\"sudo apt install $line || sudo pip install $line\", " $filename > tmp
	rm $filename
	mv tmp $filename
done < listPackage

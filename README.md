# Packer2

Packer2 is a script that generate a custom raspberry pi OS image using packer program. Packer2 simplify the install of packer and 
the programs that you need in your image.

## Installation

Use the package manager [git](https://git-scm.com/) to install packer2.

```bash
git clone https://git-ferme.easii-ic.com/cdde_easiiic_stage/stageachraf
```

## Usage
Change the permission of the script MainScript

```bash
chmod 777 MainScript.sh
```
Write the package you want in the listPackage file for exemple 
```text
python
robotFramework
git
```
Run the command
```bash
sudo ./MainScript.sh
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
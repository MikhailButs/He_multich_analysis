@echo off
echo Updating program ...
echo --------------------------------------------------------------------------------
git pull origin work
echo --------------------------------------------------------------------------------
git pull origin master
echo Updating libraries ...
echo --------------------------------------------------------------------------------
call setup.bat
echo --------------------------------------------------------------------------------
echo Done!
@pause
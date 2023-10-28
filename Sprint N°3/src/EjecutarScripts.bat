echo. ##############TEST PATH #############
cd ./Tests
python -m pytest Test_01.py Test_02.py Test_03.py --html=../Results/PinoJoelNazareno.html --self-contained-html
pause

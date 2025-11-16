@echo off

color a

msg by File0

cls

title Windows has been blocked

echo Windows has been blocked

:G

echo Enter the activation code:

set /p x=

if %x%==password (echo Windows starting!


exit

) ELSE (

cls

echo Activation code is incorrect!

echo Enter the acctivation code again!

)

goto G

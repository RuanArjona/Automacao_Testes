md "C:\Arquivos_Temp"
copy C:\inetpub\wwwroot\OuroNetCadastro\connectionStrings.config C:\Arquivos_Temp
copy C:\inetpub\wwwroot\OuroNetCadastro\custom.configuration.server.config C:\Arquivos_Temp
wmic product where name="OuroNetApp" call uninstall /nointeractive
wmic product where name="OuroNetServerCadastre" call uninstall /nointeractive
wmic product where name="OuroNetServerMovement" call uninstall /nointeractive
wmic product where name="OuroNetServerFiinancial" call uninstall /nointeractive
md "C:\Update_Automatico"
xcopy /s /e /q /y "C:\Users\TST05\Desktop\10.0.9" "C:\Update_Automatico"
cd C:\Update_Automatico\Client\App
msiexec /i OuroNetClientAppSetup.msi  /quiet /l*v logfilename hostA="localhost"
cd C:\Update_Automatico\Server\Cadastro
msiexec /i OuroNetServerCadastreSetup.msi  /quiet
cd C:\Update_Automatico\Server\Financeiro
msiexec /i OuroNetServerFinancialSetup.msi  /quiet
cd C:\Update_Automatico\Server\Movimento
msiexec /i OuroNet.Server.Movement.Setup.msi  /quiet
xcopy /s /e /q /y "C:\Arquivos_Temp" "C:\inetpub\wwwroot\OuroNetCadastro"
xcopy /s /e /q /y "C:\Arquivos_Temp" "C:\inetpub\wwwroot\OuroNetFinanceiro"
xcopy /s /e /q /y "C:\Arquivos_Temp" "C:\inetpub\wwwroot\OuroNetMovimento"

cd C:\Update_Automatico
rd /s /q C:\Update_Automatico
cd C:\Arquivos_Temp
rd /s /q C:\Arquivos_Temp
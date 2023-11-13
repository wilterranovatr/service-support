; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "ServiceSupportTR"
#define MyAppVersion "1.0"
#define MyAppPublisher "Terranova Trading - Departamento de TI"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E3158963-EA8B-42AC-B5B8-77C6B3B821D7}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Files]
Source: "I:\git\service_support\dist\ServiceSupportTR\connect_scm.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "I:\git\service_support\dist\ServiceSupportTR\connect_scm.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "I:\git\service_support\dist\ServiceSupportTR\install.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "I:\git\service_support\dist\ServiceSupportTR\scm.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "I:\git\service_support\dist\ServiceSupportTR\service_access.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "I:\git\service_support\dist\ServiceSupportTR\uninstall.bat"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Run]
Filename: "{app}\install.bat"; Flags: runhidden

[UninstallRun]
Filename: "{app}\uninstall.bat"; Flags: runhidden; RunOnceId: 4444

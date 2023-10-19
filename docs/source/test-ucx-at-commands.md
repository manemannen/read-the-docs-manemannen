# NORA-W36 AT Command Manual
Firmware version: v0.11.0
## Contents
[1 System](##1-system)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1 AT Commands](##11-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.1 Module switch off AT\+CPWROFF](##111-module-switch-off-atcpwroff)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.2 Store current configuration\. AT&W](##112-store-current-configuration-atw)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.3 Local Address AT\+USYLA](##113-local-address-atusyla)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.4 Factory Reset AT\+USYFR](##114-factory-reset-atusyfr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.5 Uart Settings AT\+USYUS](##115-uart-settings-atusyus)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.6 Firmware Update AT\+USYFWU](##116-firmware-update-atusyfwu)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.7 Echo On/Off ATE](##117-echo-onoff-ate)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.8 S\-registers ATS](##118-sregisters-ats)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1\.1\.9 Transparent mode escape sequence settings AT\+UTMES](##119-transparent-mode-escape-sequence-settings-atutmes)<br>
[2 General](##2-general)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1 AT Commands](##21-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.1 Attention AT](##211-attention-at)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.2 Manufacturer identification AT\+CGMI](##212-manufacturer-identification-atcgmi)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.3 Manufacturer identification AT\+GMI](##213-manufacturer-identification-atgmi)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.4 Model identification AT\+CGMM](##214-model-identification-atcgmm)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.5 Model identification AT\+GMM](##215-model-identification-atgmm)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.6 Software version identification AT\+CGMR](##216-software-version-identification-atcgmr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.7 Software version identification AT\+GMR](##217-software-version-identification-atgmr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.8 Serial number AT\+CGSN](##218-serial-number-atcgsn)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.9 Serial number AT\+GSN](##219-serial-number-atgsn)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.10 Identication information ATI](##2110-identication-information-ati)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2\.1\.11 Greeting text AT\+CSGT](##2111-greeting-text-atcsgt)<br>
[3 GATT client](##3-gatt-client)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.1 Unsolicited Response Codes](##31-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.1\.1 \+UEBTGCN](##311-uebtgcn)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.1\.2 \+UEBTGCI](##312-uebtgci)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2 AT Commands](##32-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.1 GATT Primary Services Discover AT\+UBTGPSD](##321-gatt-primary-services-discover-atubtgpsd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.2 GATT Primary Services Discover by UUID AT\+UBTGPSDU](##322-gatt-primary-services-discover-by-uuid-atubtgpsdu)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.3 GATT Service Characteristics Discover AT\+UBTGSCD](##323-gatt-service-characteristics-discover-atubtgscd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.4 GATT Characteristic Descriptors Discover AT\+UBTGCDD](##324-gatt-characteristic-descriptors-discover-atubtgcdd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.5 GATT Read AT\+UBTGR](##325-gatt-read-atubtgr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.6 GATT Read characteristic by UUID AT\+UBTGRU](##326-gatt-read-characteristic-by-uuid-atubtgru)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.7 GATT Write AT\+UBTGW](##327-gatt-write-atubtgw)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.8 GATT Client Configuration Write AT\+UBTGCCW](##328-gatt-client-configuration-write-atubtgccw)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.9 GATT Write with No Response AT\+UBTGWNR](##329-gatt-write-with-no-response-atubtgwnr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3\.2\.10 GATT Write long AT\+UBTGWL](##3210-gatt-write-long-atubtgwl)<br>
[4 WiFi](##4-wifi)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1 Unsolicited Response Codes](##41-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.1 \+UEWLU](##411-uewlu)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.2 \+UEWLD](##412-uewld)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.3 \+UEWSNU](##413-uewsnu)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.4 \+UEWSND](##414-uewsnd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.5 \+UEWAPNU](##415-uewapnu)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.6 \+UEWAPND](##416-uewapnd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.7 \+UEWAPU](##417-uewapu)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.8 \+UEWAPD](##418-uewapd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.9 \+UEWAPSA](##419-uewapsa)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.1\.10 \+UEWAPSDA](##4110-uewapsda)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2 AT Commands](##42-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.1 Wi\-Fi Security Config AT\+UWSS=\<WLAN\_HANDLE\>](##421-wifi-security-config-atuwsswlan_handle)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.2 Wi\-Fi Station Security WPA AT\+UWSSW](##422-wifi-station-security-wpa-atuwssw)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.3 Wi\-Fi Station Security Open AT\+UWSSO](##423-wifi-station-security-open-atuwsso)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.4 Network Connection Parameters AT\+UWSCP](##424-network-connection-parameters-atuwscp)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.5 Wi\-Fi Station IP Static configuration AT\+UWSIPS](##425-wifi-station-ip-static-configuration-atuwsips)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.6 Wi\-Fi Station IP with DHCP AT\+UWSIPD](##426-wifi-station-ip-with-dhcp-atuwsipd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.7 Wi\-Fi Station IP configuration read AT\+UWSIP=\<WLAN\_HANDLE\>](##427-wifi-station-ip-configuration-read-atuwsipwlan_handle)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.8 Wi\-Fi Station Connect AT\+UWSC](##428-wifi-station-connect-atuwsc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.9 Wi\-Fi Station Disconnect AT\+UWSDC](##429-wifi-station-disconnect-atuwsdc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.10 Wi\-Fi Station Network Status AT\+UWSNST](##4210-wifi-station-network-status-atuwsnst)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.11 Wi\-Fi Station Scan AT\+UWSSC](##4211-wifi-station-scan-atuwssc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.12 Wi\-Fi Station Status AT\+UWSST](##4212-wifi-station-status-atuwsst)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.13 Wi\-Fi Access Point Activate AT\+UWAPA](##4213-wifi-access-point-activate-atuwapa)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.14 Wi\-Fi Access Point Deactivate AT\+UWAPD](##4214-wifi-access-point-deactivate-atuwapd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.15 Wi\-Fi AP Connection Parameters AT\+UWAPCP](##4215-wifi-ap-connection-parameters-atuwapcp)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.16 Wi\-Fi AP Security WPA AT\+UWAPSW](##4216-wifi-ap-security-wpa-atuwapsw)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.17 Wi\-Fi AP Security Open AT\+UWAPSO](##4217-wifi-ap-security-open-atuwapso)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.18 Wi\-Fi AP Security AT\+UWAPS?](##4218-wifi-ap-security-atuwaps)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.19 Wi\-Fi Access Point Connected Stations AT\+UWAPCS?](##4219-wifi-access-point-connected-stations-atuwapcs)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4\.2\.20 Wi\-Fi Access Point Network Status AT\+UWAPNST](##4220-wifi-access-point-network-status-atuwapnst)<br>
[5 Bluetooth](##5-bluetooth)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.1 Unsolicited Response Codes](##51-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.1\.1 \+UEBTC](##511-uebtc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.1\.2 \+UEBTDC](##512-uebtdc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.1\.3 \+UEBTB](##513-uebtb)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.1\.4 \+UEBTUC](##514-uebtuc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.1\.5 \+UEBTUPD](##515-uebtupd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.1\.6 \+UEBTUPE](##516-uebtupe)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2 AT Commands](##52-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.1 Connect \(ACL connection\) AT\+UBTC](##521-connect-acl-connection-atubtc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.2 Disconnect \(ACL disconnect\) AT\+UBTDC](##522-disconnect-acl-disconnect-atubtdc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.3 Local Name AT\+UBTLN](##523-local-name-atubtln)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.4 Discovery AT\+UBTD](##524-discovery-atubtd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.5 Background Discovery AT\+UBTBGD](##525-background-discovery-atubtbgd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.6 Get RSSI AT\+UBTRSS](##526-get-rssi-atubtrss)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.7 Connection List AT\+UBTCL](##527-connection-list-atubtcl)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.8 Connection Status AT\+UBTCST](##528-connection-status-atubtcst)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.9 Advertising Data AT\+UBTAD](##529-advertising-data-atubtad)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.10 Enable/Disable Advertisements\. AT\+UBTA](##5210-enabledisable-advertisements-atubta)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.11 Directed Advertisement AT\+UBTDA](##5211-directed-advertisement-atubtda)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.12 Connection Settings AT\+UBTCS](##5212-connection-settings-atubtcs)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.13 I/O Capabilities AT\+UBTIOC](##5213-io-capabilities-atubtioc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.14 Bond security mode AT\+UBTBSM](##5214-bond-security-mode-atubtbsm)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.15 Pairing mode AT\+UBTPM](##5215-pairing-mode-atubtpm)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.16 User confirmation AT\+UBTUC](##5216-user-confirmation-atubtuc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.17 User passkey entry AT\+UBTUPE](##5217-user-passkey-entry-atubtupe)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.18 Bond AT\+UBTB](##5218-bond-atubtb)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.19 Unbond AT\+UBTUB](##5219-unbond-atubtub)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.20 Read bonded devices AT\+UBTBD](##5220-read-bonded-devices-atubtbd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5\.2\.21 Device Information Service AT\+UBTDIS](##5221-device-information-service-atubtdis)<br>
[6 GATT Server](##6-gatt-server)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.1 Unsolicited Response Codes](##61-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.1\.1 \+UEBTGCW](##611-uebtgcw)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.1\.2 \+UEBTGRR](##612-uebtgrr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.1\.3 \+UEBTGIC](##613-uebtgic)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2 AT Commands](##62-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.1 GATT Service define AT\+UBTGS](##621-gatt-service-define-atubtgs)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.2 GATT Characteristic define AT\+UBTGC](##622-gatt-characteristic-define-atubtgc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.3 GATT Host Controlled Characteristic AT\+UBTGHCC](##623-gatt-host-controlled-characteristic-atubtghcc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.4 GATT Descriptor define AT\+UBTGD](##624-gatt-descriptor-define-atubtgd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.5 GATT Service Acivate\. AT\+UBTGSA](##625-gatt-service-acivate-atubtgsa)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.6 GATT Read Request Respond AT\+UBTGRRR](##626-gatt-read-request-respond-atubtgrrr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.7 GATT Notification Send AT\+UBTGNS](##627-gatt-notification-send-atubtgns)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.8 GATT Indication Send AT\+UBTGIS](##628-gatt-indication-send-atubtgis)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.9 GATT Attribute Value AT\+UBTGAV](##629-gatt-attribute-value-atubtgav)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.10 GATT Read Request Respond with error code AT\+UBTGRRRE](##6210-gatt-read-request-respond-with-error-code-atubtgrrre)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.11 GATT Write Respond with Error code AT\+UBTGWRE](##6211-gatt-write-respond-with-error-code-atubtgwre)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6\.2\.12 GATT Write Request Respond AT\+UBTGWRR](##6212-gatt-write-request-respond-atubtgwrr)<br>
[7 Internet Protocols](##7-internet-protocols)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.1 Unsolicited Response Codes](##71-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.1\.1 \+UESOC](##711-uesoc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.1\.2 \+UESODA](##712-uesoda)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.1\.3 \+UESOCL](##713-uesocl)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.1\.4 \+UESOIC](##714-uesoic)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2 AT Commands](##72-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.1 Create Socket AT\+USOCR](##721-create-socket-atusocr)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.2 Socket Connect AT\+USOC](##722-socket-connect-atusoc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.3 Socket Write String AT\+USOWS](##723-socket-write-string-atusows)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.4 Socket Write Hex AT\+USOWH](##724-socket-write-hex-atusowh)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.5 Close socket AT\+USOCL](##725-close-socket-atusocl)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.6 Socket Read Hex AT\+USORH](##726-socket-read-hex-atusorh)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.7 Read Socket String AT\+USORS](##727-read-socket-string-atusors)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.8 Socket Error AT\+USOE](##728-socket-error-atusoe)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.9 Socket Peer Address AT\+USOPA](##729-socket-peer-address-atusopa)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7\.2\.10 Socket Options AT\+USOO](##7210-socket-options-atusoo)<br>
[8 Mqtt](##8-mqtt)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.1 Unsolicited Response Codes](##81-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.1\.1 \+UEMQC](##811-uemqc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.1\.2 \+UEMQDC](##812-uemqdc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.1\.3 \+UEMQD](##813-uemqd)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2 AT Commands](##82-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.1 MQTT Connection Parameters AT\+UMQCP](##821-mqtt-connection-parameters-atumqcp)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.2 MQTT Connect to broker AT\+UMQC](##822-mqtt-connect-to-broker-atumqc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.3 MQTT Last Will and Testament AT\+UMQLWT](##823-mqtt-last-will-and-testament-atumqlwt)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.4 MQTT TLS configuration AT\+UMQTLS](##824-mqtt-tls-configuration-atumqtls)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.5 MQTT Disconnect AT\+UMQDC](##825-mqtt-disconnect-atumqdc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.6 MQTT Publish AT\+UMQP](##826-mqtt-publish-atumqp)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.7 MQTT Subscribe AT\+UMQS](##827-mqtt-subscribe-atumqs)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8\.2\.8 Read MQTT message AT\+UMQR](##828-read-mqtt-message-atumqr)<br>
[9 Security](##9-security)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[9\.1 AT Commands](##91-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[9\.1\.1 SSL/TLS certificates and private keys manager AT\+USECMNG](##911-ssltls-certificates-and-private-keys-manager-atusecmng)<br>
[10 SPS](##10-sps)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.1 Unsolicited Response Codes](##101-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.1\.1 \+UESPSC](##1011-uespsc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.1\.2 \+UESPSDC](##1012-uespsdc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.1\.3 \+UESPSDA](##1013-uespsda)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.2 AT Commands](##102-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.2\.1 SPS Connect AT\+USPSC](##1021-sps-connect-atuspsc)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.2\.2 SPS Enable AT\+USPSE](##1022-sps-enable-atuspse)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10\.2\.3 SPS Write AT\+USPSW](##1023-sps-write-atuspsw)<br>
[11 Diagnostics](##11-diagnostics)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[11\.1 Unsolicited Response Codes](##111-unsolicited-response-codes)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[11\.1\.1 \+UEDGP](##1111-uedgp)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[11\.2 AT Commands](##112-at-commands)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[11\.2\.1 Send ping command\. AT\+UDGP](##1121-send-ping-command-atudgp)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[11\.2\.2 Diagnostics Iperf AT\+UDGI](##1122-diagnostics-iperf-atudgi)<br>

## **1 System**
System AT commands
#### **1.1 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+CPWROFF | Module switch off |
| AT&W | Store current configuration. |
| AT\+USYLA | Local Address |
| AT\+USYFR | Factory Reset |
| AT\+USYUS | Uart Settings |
| AT\+USYFWU | Firmware Update |
| ATE | Echo On/Off |
| ATS | S-registers |
| AT\+UTMES | Transparent mode escape sequence settings |
###### **1.1.1 Module switch off AT+CPWROFF**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+CPWROFF | Reboot the DCE. |
###### **1.1.2 Store current configuration. AT&W**
Store the current configuration to flash

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT&W | Write the current configuration to flash. The configuration is stored immediately when AT&W is issued. |
###### **1.1.3 Local Address AT+USYLA**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USYLA=\<interface\_id\>\[,\<address\>] | get and set interface address |

| Response | Description |
| ----------|----------|
| \+USYLA:\<address\> | Successfull read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| interface\_id | enumerator | Valid values:<br>0: Bluetooth<br>1: Wifi station<br>2: Wifi Accesspoint |
| address | byte\_array | MAC address of the interface id. If the address is set to 000000000000, the local address will be restored to factory-programmed value. A reboot is required The least significant bit of the first octet of the <address> must be 0.<br><br>Valid length: 6..6 |
###### **1.1.4 Factory Reset AT+USYFR**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USYFR | Reset to factory defined defaults. A reboot is required before using the new settings. |
###### **1.1.5 Uart Settings AT+USYUS**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USYUS=\<baud\_rate\>\[,\<flow\_control\>\[,\<change\_after\_confirm\>]] | Configure new RS232 settings that will be used after restart |
| AT\+USYUS? | Reads current RS232 settings from the module |

| Response | Description |
| ----------|----------|
| \+USYUS:\<baud\_rate\>,\<flow\_control\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| baud\_rate | integer | Baudrate<br><br>Default value: 115200 |
| flow\_control | integer | Valid values: 0..1 |
| change\_after\_confirm | integer | Valid values: 0..1 |
###### **1.1.6 Firmware Update AT+USYFWU**
Force start of the boot loader. The boot loader will start at the defined baud rate.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USYFWU=\<bootloader\_mode\>,\<baud\_rate\>\[,\<flow\_control\>] | Force start of the boot loader. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bootloader\_mode | enumerator | Valid values:<br>0: Enter xmodem mode for u-connect software update using serial port.<br>1: Enter the bootloader command line mode using serial port. |
| baud\_rate | integer | Valid values: 110..6000000<br><br>Default value: 115200 |
| flow\_control | integer | Valid values: 0..1<br><br>Default value: 0 |
###### **1.1.7 Echo On/Off ATE**
This command configures whether or not the module echoes the characters received from the host.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| ATE0 | Set echo off |
| ATE1 | Set echo on |
| ATE? | Read current echo setting |

| Response | Description |
| ----------|----------|
| \<echo\_on\> | Current echo setting |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| echo\_on | enumerator | Valid values:<br>0: Module does not echo the characters<br>1: (Factory default) Module echoes the characters |
###### **1.1.8 S-registers ATS**
Used to set different configuration parameters

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| ATS2=\<escape\_char\> | Write escape character. This settings change the decimal value of the escape character used by some modes, such as transparent mode for example, to detect an escape sequence and exit. |
| ATS2? | Read escape character |
| ATS3=\<line\_term\> | Write line termination character. This setting changes the decimal value of the character recognized by the DCE from the DTE to terminate an incoming command line. It is also generated by the DCE as part of the header, trailer, and terminator for result codes and information text along with the S4 parameter. The previous value of S3 is used to determine the command line termination character for entry of the command line containing the S3 setting command. However, the result code issued shall use the value of S3 as set during the processing of the command line. For example, if S3 was previously set to 13 and the command line "ATS3=30" is issued, the command line shall be terminated with a CR, character (13), but the result code issued will use the character with the ordinal value 30 instead of the CR. |
| ATS3? | Read line termination character |
| ATS4=\<resp\_format\> | Write response format character. This setting changes the decimal value of the character generated by the DCE as part of the header, trailer, and terminator for result codes and information text, along with the S3 parameter. If the value of S4 is changed in a command line, the result code issued in response to that command line will use the new value of S4. |
| ATS4? | Read response format character |
| ATS5=\<backspace\> | Writes backspace character. This setting changes the decimal value of the character recognized by the DCE as a request to delete from the command line, the immediately preceding character. |
| ATS5? | Read backspace character |

| Response | Description |
| ----------|----------|
| \<escape\_char\> | Current escape character |
| \<line\_term\> | Current line termination character |
| \<resp\_format\> | Current response format character |
| \<backspace\> | Current backspace character |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| line\_term | integer | Command line termination character. Factory default: 13<br><br>Valid values: 0..127 |
| resp\_format | integer | Response format character. Factory default: 10<br><br>Valid values: 0..127 |
| backspace | integer | Backspace character. Factory default: 8<br><br>Valid values: 0..127 |
| escape\_char | integer | Escape character. Factory default: 43<br><br>Valid values: 0..127 |
###### **1.1.9 Transparent mode escape sequence settings AT+UTMES**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UTMES=\<pre\_timeout\>,\<post\_timeout\>,\<escape\_timeout\> | Configures the transparent mode escape sequence settings. |
| AT\+UTMES? | Reads current transparent mode escape sequence settings. |

| Response | Description |
| ----------|----------|
| \+UTMES:\<pre\_timeout\>,\<post\_timeout\>,\<escape\_timeout\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| pre\_timeout | integer | Minimum time (ms) of no data activity required before the escape sequence is sent. Factory default: 1000<br><br>Valid values: 50..5000 |
| post\_timeout | integer | Minimum time (ms) of no data activity required after the escape sequence is sent. Factory default: 1000<br><br>Valid values: 50..5000 |
| escape\_timeout | integer | Maximum time interval (ms) between escape characters. Factory default: 200<br><br>Valid values: 50..5000 |
## **2 General**

#### **2.1 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT | Attention |
| AT\+CGMI | Manufacturer identification |
| AT\+GMI | Manufacturer identification |
| AT\+CGMM | Model identification |
| AT\+GMM | Model identification |
| AT\+CGMR | Software version identification |
| AT\+GMR | Software version identification |
| AT\+CGSN | Serial number |
| AT\+GSN | Serial number |
| ATI | Identication information |
| AT\+CSGT | Greeting text |
###### **2.1.1 Attention AT**
Attention command that determines the presence of a Data Communication Equipment (DCE)

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT | Attention command |
###### **2.1.2 Manufacturer identification AT+CGMI**
Read a text string that identifies the manufacturer.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+CGMI | Read manufacturer text string. |

| Response | Description |
| ----------|----------|
| \<manufacturer\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| manufacturer | string | Manufacturer ("u-blox") |
###### **2.1.3 Manufacturer identification AT+GMI**
Read a text string that identifies the manufacturer.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+GMI | Read manufacturer text string. |

| Response | Description |
| ----------|----------|
| \<manufacturer\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| manufacturer | string | Manufacturer ("u-blox") |
###### **2.1.4 Model identification AT+CGMM**
Read a text string that identifies the device model.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+CGMM | Read device model. |

| Response | Description |
| ----------|----------|
| \<device\_model\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| device\_model | string | Device model |
###### **2.1.5 Model identification AT+GMM**
Read a text string that identifies the device model.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+GMM | Read device model. |

| Response | Description |
| ----------|----------|
| \<device\_model\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| device\_model | string | Device model |
###### **2.1.6 Software version identification AT+CGMR**
Read a text string that identifies the software version of the module.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+CGMR | Read software version. |

| Response | Description |
| ----------|----------|
| \<version\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| version | string | Version |
###### **2.1.7 Software version identification AT+GMR**
Read a text string that identifies the software version of the module.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+GMR | Read software version. |

| Response | Description |
| ----------|----------|
| \<version\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| version | string | Version |
###### **2.1.8 Serial number AT+CGSN**
Read the product serial number.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+CGSN | Read serial number. |

| Response | Description |
| ----------|----------|
| \<serial\_number\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| serial\_number | string | Serial number |
###### **2.1.9 Serial number AT+GSN**
Read the product serial number.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+GSN | Read serial number. |

| Response | Description |
| ----------|----------|
| \<serial\_number\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| serial\_number | string | Serial number |
###### **2.1.10 Identication information ATI**
Read identification information.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| ATI9 | Read identification information. |

| Response | Description |
| ----------|----------|
| \<application\_version\>,\<unique\_identifier\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| application\_version | string | Application version |
| unique\_identifier | string | Unique identifier |
###### **2.1.11 Greeting text AT+CSGT**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+CSGT=\<greeting\_mode\>\[,\<text\>] | Set the greeting text/ greeting text mode |
| AT\+CSGT? | Read the greeting text |

| Response | Description |
| ----------|----------|
| \+CSGT:\<greeting\_mode\>,\<text\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| greeting\_mode | enumerator | Valid values:<br>0: Turn off the greeting text<br>1: Turn on the greeting text |
| text | string | The greeting text, can not be an empty string<br><br>Valid length: 1..49 |
## **3 GATT client**
GATT Client
#### **3.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UEBTGCN:\<conn\_handle\>,\<value\_handle\>,\<hex\_data\> |  |
| \+UEBTGCI:\<conn\_handle\>,\<value\_handle\>,\<hex\_data\> |  |
###### **3.1.1 +UEBTGCN**
GATT Client Notification. This event is received when the remote side sends a notification.

**Syntax**<br>
```+UEBTGCN:<conn_handle>,<value_handle>,<hex_data>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| hex\_data | byte\_array | Characteristic data in hexadecimal form. For example, 070809AABBCC |
###### **3.1.2 +UEBTGCI**
GATT Client Indication. This event is received when the remote side sends an indication.

**Syntax**<br>
```+UEBTGCI:<conn_handle>,<value_handle>,<hex_data>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| hex\_data | byte\_array | Characteristic data in hexadecimal form. For example, 070809AABBCC |
#### **3.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+UBTGPSD | GATT Primary Services Discover |
| AT\+UBTGPSDU | GATT Primary Services Discover by UUID |
| AT\+UBTGSCD | GATT Service Characteristics Discover |
| AT\+UBTGCDD | GATT Characteristic Descriptors Discover |
| AT\+UBTGR | GATT Read |
| AT\+UBTGRU | GATT Read characteristic by UUID |
| AT\+UBTGW | GATT Write |
| AT\+UBTGCCW | GATT Client Configuration Write |
| AT\+UBTGWNR | GATT Write with No Response |
| AT\+UBTGWL | GATT Write long |
###### **3.2.1 GATT Primary Services Discover AT+UBTGPSD**
List all GATT services on the GATT server.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGPSD=\<conn\_handle\> | Discovers all primary services on the remote device. |

| Response | Description |
| ----------|----------|
| \+UBTGPSD:\<conn\_handle\>,\<start\_handle\>,\<end\_handle\>,\<uuid\> | This response is sent for every service found. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| start\_handle | integer | Start handle of the service. |
| end\_handle | integer | End handle of the service. |
| uuid | byte\_array | UUID of attribute. Either 16-bit or 128-bit. |
###### **3.2.2 GATT Primary Services Discover by UUID AT+UBTGPSDU**
Discovers all primary services by UUID on the remote device.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGPSDU=\<conn\_handle\>,\<uuid\> | Start discovery. |

| Response | Description |
| ----------|----------|
| \+UBTGPSDU:\<conn\_handle\>,\<start\_handle\>,\<end\_handle\> | This response is sent for every service found. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| uuid | byte\_array | UUID of attribute. Either 16-bit or 128-bit. |
| start\_handle | integer | Start handle of the service. |
| end\_handle | integer | End handle of the service. |
###### **3.2.3 GATT Service Characteristics Discover AT+UBTGSCD**
This command will list all characteristics belonging to a service on the GATT server.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGSCD=\<conn\_handle\>,\<start\>,\<end\> | Discovers all characteristics of a service. |

| Response | Description |
| ----------|----------|
| \+UBTGSCD:\<conn\_handle\>,\<attr\_handle\>,\<properties\>,\<value\_handle\>,\<uuid\> | This response is sent for every characteristic found. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| start | integer | Start handle of the service. |
| end | integer | End handle of the service. |
| attr\_handle | integer | Attribute handle of the characteristic |
| properties | byte\_array | Bit mask describing the properties of the characteristic |
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| uuid | byte\_array | UUID of attribute. Either 16-bit or 128-bit. |
###### **3.2.4 GATT Characteristic Descriptors Discover AT+UBTGCDD**
Discover Characteristics Descriptors. This command will list all descriptors of a characteristic on the GATT server.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGCDD=\<conn\_handle\>,\<value\_handle\>,\<characteristic\_end\_handle\> | Discovers all descriptors of a characteristic. |

| Response | Description |
| ----------|----------|
| \+UBTGCDD:\<conn\_handle\>,\<char\_handle\>,\<desc\_handle\>,\<uuid\> | This response is sent for every descriptor found. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| char\_handle | integer | Handle of characteristic |
| characteristic\_end\_handle | integer | End handle of characteristic to which descriptor discovery is being performed on. |
| desc\_handle | integer | Handle of descriptor |
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| uuid | byte\_array | UUID of attribute. Either 16-bit or 128-bit. |
###### **3.2.5 GATT Read AT+UBTGR**
Read a characteristic value.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGR=\<conn\_handle\>,\<value\_handle\> | Reads the characteristic; all bytes included. |

| Response | Description |
| ----------|----------|
| \+UBTGR:\<conn\_handle\>,\<value\_handle\>,\<hex\_data\> | Read response sent if the data read is found. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| hex\_data | byte\_array | Characteristic data in hexadecimal form. For example, 070809AABBCC |
###### **3.2.6 GATT Read characteristic by UUID AT+UBTGRU**
Read GATT characteristic values by UUID.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGRU=\<conn\_handle\>,\<start\>,\<end\>,\<uuid\> | Reads all the characteristics by UUID. It will read all the bytes in each characteristic. |

| Response | Description |
| ----------|----------|
| \+UBTGRU:\<conn\_handle\>,\<value\_handle\>,\<hex\_data\> | This response is sent if the read data is found. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| start | integer | Start handle. |
| end | integer | End handle. |
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| uuid | byte\_array | UUID of attribute. Either 16-bit or 128-bit. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| hex\_data | byte\_array | Characteristic data in hexadecimal form. For example, 070809AABBCC |
###### **3.2.7 GATT Write AT+UBTGW**
Writes a characteristic value.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGW=\<conn\_handle\>,\<value\_handle\>,\<hex\_data\> | Writes the characteristic value. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| hex\_data | byte\_array | Characteristic data in hexadecimal form. For example, 070809AABBCC |
###### **3.2.8 GATT Client Configuration Write AT+UBTGCCW**
Write characteristic configuration, in order to for example enable notifications or indications.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGCCW=\<conn\_handle\>,\<desc\_handle\>,\<config\> | Writes the client characteristic configuration. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| desc\_handle | integer | Handle of descriptor |
| config | enumerator | Valid values:<br>0: None<br>1: Enable notifications<br>2: Enable indications<br>3: Enable notifications and indications |
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
###### **3.2.9 GATT Write with No Response AT+UBTGWNR**
Writes the characteristic with no response message from the remote side.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGWNR=\<conn\_handle\>,\<value\_handle\>,\<hex\_data\> | Write characteristic. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
| hex\_data | byte\_array | Characteristic data in hexadecimal form. For example, 070809AABBCC |
###### **3.2.10 GATT Write long AT+UBTGWL**
Write a long characteristic.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGWL=\<conn\_handle\>,\<value\_handle\>,\<hex\_data\>,\<reliable\>,\<flag\>,\<offset\> | Writes long characteristic. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| hex\_data | string |  |
| reliable | enumerator | Valid values:<br>0: Not reliable<br>1: Reliable |
| flag | enumerator | Valid values:<br>0: Final data<br>1: More data<br>2: Cancel |
| offset | integer |  |
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| value\_handle | integer | Attribute handle of the characteristic value. |
## **4 WiFi**
Wi-Fi Commands
#### **4.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UEWLU:\<wlan\_handle\>,\<bssid\>,\<channel\> |  |
| \+UEWLD:\<wlan\_handle\>,\<reason\> |  |
| \+UEWSNU: |  |
| \+UEWSND: |  |
| \+UEWAPNU: |  |
| \+UEWAPND: |  |
| \+UEWAPU: |  |
| \+UEWAPD: |  |
| \+UEWAPSA:\<mac\> |  |
| \+UEWAPSDA:\<mac\> |  |
###### **4.1.1 +UEWLU**
Wi-Fi Link Up

**Syntax**<br>
```+UEWLU:<wlan_handle>,<bssid>,<channel>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bssid | byte\_array | BSSID of the connected AP |
| channel | integer | Connected channel |
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
###### **4.1.2 +UEWLD**
Wi-Fi Link Down

**Syntax**<br>
```+UEWLD:<wlan_handle>,<reason>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| reason | integer | Standard 802.11 reason codes |
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
###### **4.1.3 +UEWSNU**
Wi-Fi Station Network Up

**Syntax**<br>
```+UEWSNU```
###### **4.1.4 +UEWSND**
Wi-Fi Station Network Down

**Syntax**<br>
```+UEWSND```
###### **4.1.5 +UEWAPNU**
Wi-Fi Access Point Network Up

**Syntax**<br>
```+UEWAPNU```
###### **4.1.6 +UEWAPND**
Wi-Fi Access Point Network Down

**Syntax**<br>
```+UEWAPND```
###### **4.1.7 +UEWAPU**
Wi-Fi Access Point Up Event

**Syntax**<br>
```+UEWAPU```
###### **4.1.8 +UEWAPD**
Wi-Fi Access Point Down Event

**Syntax**<br>
```+UEWAPD```
###### **4.1.9 +UEWAPSA**
Wi-Fi AccessPiont Station Associated Event

**Syntax**<br>
```+UEWAPSA:<mac>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mac | byte\_array | Mac address of the connected Station |
###### **4.1.10 +UEWAPSDA**
Wi-Fi AccessPiont Station Disassociated Event

**Syntax**<br>
```+UEWAPSDA:<mac>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mac | byte\_array | MAc address of the connected Station |
#### **4.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+UWSS=\<wlan\_handle\> | Wi-Fi Security Config |
| AT\+UWSSW | Wi-Fi Station Security WPA |
| AT\+UWSSO | Wi-Fi Station Security Open |
| AT\+UWSCP | Network Connection Parameters |
| AT\+UWSIPS | Wi-Fi Station IP Static configuration |
| AT\+UWSIPD | Wi-Fi Station IP with DHCP |
| AT\+UWSIP=\<wlan\_handle\> | Wi-Fi Station IP configuration read |
| AT\+UWSC | Wi-Fi Station Connect |
| AT\+UWSDC | Wi-Fi Station Disconnect |
| AT\+UWSNST | Wi-Fi Station Network Status |
| AT\+UWSSC | Wi-Fi Station Scan |
| AT\+UWSST | Wi-Fi Station Status |
| AT\+UWAPA | Wi-Fi Access Point Activate |
| AT\+UWAPD | Wi-Fi Access Point Deactivate |
| AT\+UWAPCP | Wi-Fi AP Connection Parameters |
| AT\+UWAPSW | Wi-Fi AP Security WPA |
| AT\+UWAPSO | Wi-Fi AP Security Open |
| AT\+UWAPS? | Wi-Fi AP Security |
| AT\+UWAPCS? | Wi-Fi Access Point Connected Stations |
| AT\+UWAPNST | Wi-Fi Access Point Network Status |
###### **4.2.1 Wi-Fi Security Config AT+UWSS=<WLAN_HANDLE>**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSS=\<wlan\_handle\> | Get the current Wi-Fi Station security config |

| Response | Description |
| ----------|----------|
| \+UWSS:\<wlan\_handle\>,\<security\_mode\>,\<wpa\_threshold\> | Response if security mode is WPA |
| \+UWSS:\<wlan\_handle\>,\<security\_mode\> | Response if security mode is Open |
| \+UWSS:\<wlan\_handle\>,\<security\_mode\>,\<ca\_name\>,\<client\_cert\_name\>,\<client\_key\_name\> | Response if security mode is EAP-TLS |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| security\_mode | enumerator | The current security mode.<br><br>Valid values:<br>0: Open security<br>1: WPA security<br>2: EAP-TLS security |
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
| wpa\_threshold | enumerator | Lowest WPA version to connect to<br><br>Valid values:<br>0: Only connect to APs that support WPA2 or up<br>1: Only connect to APs that support WPA3<br><br>Default value: 0 |
| ca\_name | string | Name of the ca certificate to use (upload cert to module first)<br><br>Valid length: 0..32 |
| client\_cert\_name | string | Name of the client cert to use<br><br>Valid length: 0..32 |
| client\_key\_name | string | Name of the private key for client cert<br><br>Valid length: 0..32 |
###### **4.2.2 Wi-Fi Station Security WPA AT+UWSSW**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSSW=\<wlan\_handle\>,\<passphrase\>,\<wpa\_threshold\> | Set WPA connection params to use |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| passphrase | string | Passphrase to use for WPA connection<br><br>Valid length: 0..63 |
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
| wpa\_threshold | enumerator | Lowest WPA version to connect to<br><br>Valid values:<br>0: Only connect to APs that support WPA2 or up<br>1: Only connect to APs that support WPA3<br><br>Default value: 0 |
###### **4.2.3 Wi-Fi Station Security Open AT+UWSSO**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSSO=\<wlan\_handle\> | Sets security to open security |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
###### **4.2.4 Network Connection Parameters AT+UWSCP**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSCP=\<wlan\_handle\>\[,\<ssid\>] | Sets or Reads the connection parameters for the connection. If leaving out ssid this will read the parameters. |

| Response | Description |
| ----------|----------|
| AT\+UWSCP=\<wlan\_handle\>,\<ssid\> | Successfull read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| ssid | string | SSID to connect to<br><br>Valid length: 0..32 |
| bssid | byte\_array | BSSID for the specific AP to connect to, can be left empty to skip the param |
| channel | integer | Only scan this channel to find SSID or BSSID |
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
###### **4.2.5 Wi-Fi Station IP Static configuration AT+UWSIPS**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSIPS=\<wlan\_handle\>,\<ip\_addr\>,\<subnet\_mask\>,\<gateway\>\[,\<prim\_dns\>\[,\<sec\_dns\>]] | Sets ip configuration to use static ip |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
| ip\_addr | ip\_addr | Static IPv4 address<br><br>Default value: 0.0.0.0 |
| subnet\_mask | ip\_addr | subnet mask<br><br>Default value: 0.0.0.0 |
| gateway | ip\_addr | IPv4 gateway address<br><br>Default value: 0.0.0.0 |
| prim\_dns | ip\_addr | IPv4 primary dns address<br><br>Default value: 0.0.0.0 |
| sec\_dns | ip\_addr | IPv4 secondary dns address<br><br>Default value: 0.0.0.0 |
###### **4.2.6 Wi-Fi Station IP with DHCP AT+UWSIPD**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSIPD=\<wlan\_handle\> | Sets ip configuration to receive ip address via dhcp |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
###### **4.2.7 Wi-Fi Station IP configuration read AT+UWSIP=<WLAN_HANDLE>**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSIP=\<wlan\_handle\> | Read the current configuration for receiving an IP address |

| Response | Description |
| ----------|----------|
| \+UWSIP:\<wlan\_handle\>,\<ip\_mode\> | Response if IP mode is DHCP |
| \+UWSIP:\<wlan\_handle\>,\<ip\_mode\>,\<ip\_addr\>,\<subnet\_mask\>,\<gateway\>,\<prim\_dns\>,\<sec\_dns\> | Response if IP mode is set to be static |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| ip\_mode | enumerator | Current IP recipient mode<br><br>Valid values:<br>0: DHCP<br>1: Static IP configuration |
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
| ip\_addr | ip\_addr | Static IPv4 address<br><br>Default value: 0.0.0.0 |
| subnet\_mask | ip\_addr | subnet mask<br><br>Default value: 0.0.0.0 |
| gateway | ip\_addr | IPv4 gateway address<br><br>Default value: 0.0.0.0 |
| prim\_dns | ip\_addr | IPv4 primary dns address<br><br>Default value: 0.0.0.0 |
| sec\_dns | ip\_addr | IPv4 secondary dns address<br><br>Default value: 0.0.0.0 |
###### **4.2.8 Wi-Fi Station Connect AT+UWSC**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSC=\<wlan\_handle\> | Initiate connection to wlan network |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| wlan\_handle | integer | Handle to use for Wi-Fi config and connection<br><br>Valid values: 0..0 |
###### **4.2.9 Wi-Fi Station Disconnect AT+UWSDC**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSDC | Disconnect from wlan network |
###### **4.2.10 Wi-Fi Station Network Status AT+UWSNST**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSNST=\<status\_id\> | Show current status of Wifi Station network interface |
| AT\+UWSNST? | Show current status of Wifi Station network interface |

| Response | Description |
| ----------|----------|
| \+UWSNST:\<status\_id\>,\<status\_val\> | Send for every applicable status |
| \+UWSNST:\<status\_id\>,\<status\_val\> | Send for every applicable status |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| status\_id | enumerator | Valid values:<br>0: The current IPv4 address.<br>1: The current subnet mask<br>2: The current gateway<br>3: The current primary DNS server<br>4: The current secondary DNS server<br>5: The current IPv6 link local address |
| status\_val | ip\_addr |  |
###### **4.2.11 Wi-Fi Station Scan AT+UWSSC**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSSC | Initiate synchronous Wi-Fi scan (will lock AT interface until scan has finished) |
| AT\+UWSSC=\<scan\_mode\>\[,\<ssid\>] | Initiate synchronous Wi-Fi scan (will lock AT interface until scan has finished) |

| Response | Description |
| ----------|----------|
| \+UWSSC:\<bssid\>,\<op\_mode\>,\<ssid\>,\<channel\>,\<rssi\>,\<authentication\_suites\>,\<unicast\_ciphers\>,\<group\_ciphers\> | Successfull scan response |
| \+UWSSC:\<bssid\>,\<op\_mode\>,\<ssid\>,\<channel\>,\<rssi\>,\<authentication\_suites\>,\<unicast\_ciphers\>,\<group\_ciphers\> | Successfull scan response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| scan\_mode | enumerator | Choose how to scan<br><br>Valid values:<br>0: Active<br>1: Passive<br><br>Default value: Active |
| bssid | byte\_array | BSSID<br><br>Valid length: 0..6 |
| op\_mode | enumerator | op mode<br><br>Valid values:<br>1: Infrastructure<br>2: Ad-hoc |
| ssid | string | SSID |
| channel | integer | Channel |
| rssi | integer | RSSI |
| authentication\_suites | integer | Authentication suites. Bit 0 = shared secret, 1 = PSK, 2 = EAP, 3 = WPA, 4 = WPA2, 5 = WPA3 |
| unicast\_ciphers | integer | unicast ciphers. Bit 0 = WEP64, 1 = WEP128, 2 = TKIP, 3 = AES/CCMP |
| group\_ciphers | integer | group ciphers. Bit 0 = WEP64, 1 = WEP128, 2 = TKIP, 3 = AES/CCMP |
###### **4.2.12 Wi-Fi Station Status AT+UWSST**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWSST=\<wifi\_status\_id\> | Read status |
| AT\+UWSST | Read status |

| Response | Description |
| ----------|----------|
| \+UWSST:\<wifi\_status\_id\>,\<status\_val\> | Read response |
| \+UWSST:\<wifi\_status\_id\>,\<status\_val\> | Read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| wifi\_status\_id | enumerator | Valid values:<br>0: SSID of the connected AP<br>1: BSSID of the connected AP<br>2: Active channel<br>3: Connection status, 1 = not connected, 2 = Connected<br>4: RSSI value of the current connection; will return-32768, if not connected. |
| status\_val | string |  |
###### **4.2.13 Wi-Fi Access Point Activate AT+UWAPA**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPA | Start an Access Point with the current access point configuration. |
###### **4.2.14 Wi-Fi Access Point Deactivate AT+UWAPD**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPD | Brings down Wi-Fi access point and disconnect all connected stations |
###### **4.2.15 Wi-Fi AP Connection Parameters AT+UWAPCP**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPCP=\<ssid\>\[,\<channel\>] | Sets connection Parameters for the AP configuration |
| AT\+UWAPCP? | Read the current Connection Parameters |

| Response | Description |
| ----------|----------|
| \+UWAPCP:\<ssid\>,\<channel\> | Successfull read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| ssid | string | Ssid to use<br><br>Valid length: 0..32<br><br>Default value: UBXWifi |
| channel | enumerator | channel<br><br>Valid values:<br>1: 1<br>2: 2<br>3: 3<br>4: 4<br>5: 5<br>6: 6<br>7: 7<br>8: 8<br>9: 9<br>10: 10<br>11: 11<br>36: 36<br>40: 40<br>44: 44<br>48: 48<br><br>Default value: 6 |
###### **4.2.16 Wi-Fi AP Security WPA AT+UWAPSW**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPSW=\<passphrase\>\[,\<wpa\_version\>] | Sets WPA parameters for the AP config |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| passphrase | string | Passphrase to use<br><br>Valid length: 0..63 |
| wpa\_version | enumerator | Valid values:<br>0: WPA 2<br><br>Default value: WPA 2 |
###### **4.2.17 Wi-Fi AP Security Open AT+UWAPSO**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPSO | Sets Security level to open for the AP config |
###### **4.2.18 Wi-Fi AP Security AT+UWAPS?**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPS? | Get the current security configuration for Wi-Fi AP |

| Response | Description |
| ----------|----------|
| \+UWAPS:\<security\_mode\>,\<wpa\_version\> | Response if security mode is WPA |
| \+UWAPS:\<security\_mode\> | Response if security mode is Open |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| security\_mode | enumerator | The current security mode.<br><br>Valid values:<br>0: Open security<br>1: WPA security<br>2: EAP-TLS security |
| wpa\_version | enumerator | Valid values:<br>0: WPA 2<br><br>Default value: WPA 2 |
###### **4.2.19 Wi-Fi Access Point Connected Stations AT+UWAPCS?**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPCS? | Get a list of connected stations. One response per connected station will be sent |

| Response | Description |
| ----------|----------|
| \+UWAPCS:\<mac\> | A station that is connected to the access point |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mac | byte\_array | Mac address of the connected Station |
###### **4.2.20 Wi-Fi Access Point Network Status AT+UWAPNST**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UWAPNST=\<status\_id\> | Show current status of Wifi Station network interface |
| AT\+UWAPNST? | Show current status of Wifi Station network interface |

| Response | Description |
| ----------|----------|
| \+UWAPNST:\<status\_id\>,\<status\_val\> | Send for every applicable status |
| \+UWAPNST:\<status\_id\>,\<status\_val\> | Send for every applicable status |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| status\_id | enumerator | Valid values:<br>0: The current IPv4 address.<br>1: The current subnet mask<br>2: The current gateway<br>3: The current primary DNS server<br>4: The current secondary DNS server<br>5: The current IPv6 link local address |
| status\_val | ip\_addr |  |
## **5 Bluetooth**
Bluetooth commands
#### **5.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UEBTC:\<conn\_handle\>,\<bd\_addr\> |  |
| \+UEBTDC:\<conn\_handle\> |  |
| \+UEBTB:\<bd\_addr\>,\<bond\_status\> |  |
| \+UEBTUC:\<bd\_addr\>,\<nummeric\_value\> |  |
| \+UEBTUPD:\<bd\_addr\>,\<nummeric\_value\> |  |
| \+UEBTUPE:\<bd\_addr\> |  |
###### **5.1.1 +UEBTC**
Event indicating successful Bluetooth connection.

**Syntax**<br>
```+UEBTC:<conn_handle>,<bd_addr>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
###### **5.1.2 +UEBTDC**
Event indicating a disconnected Bluetooth connection.

**Syntax**<br>
```+UEBTDC:<conn_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
###### **5.1.3 +UEBTB**
Event indicates that a bonding procedure is completed.

**Syntax**<br>
```+UEBTB:<bd_addr>,<bond_status>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
| bond\_status | enumerator | Bonding status<br><br>Valid values:<br>0: Bonding procedure succeeded.<br>1: Bonding procedure failed due to page timeout.<br>2: Bonding failed because of authentication or pairing failed. This could be due to incorrect PIN/passkey.<br>3: Bonding failed becuase the protection against Man-In-The-Middle attack could not be guaranteed; the generated link key was too weak. |
###### **5.1.4 +UEBTUC**
This event is used while bonding with IO capability DisplayYesNo. This event indicates that the user confirmation of a numeric value is required.

**Syntax**<br>
```+UEBTUC:<bd_addr>,<nummeric_value>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
| nummeric\_value | integer | Nummeric value.<br><br>Valid values: 0..999999 |
###### **5.1.5 +UEBTUPD**
This event is used to indicate to the user that a passkey has to be entered on the remote device during a bonding procedure with the IO capability DisplayOnly.

**Syntax**<br>
```+UEBTUPD:<bd_addr>,<nummeric_value>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
| nummeric\_value | integer | Nummeric value.<br><br>Valid values: 0..999999 |
###### **5.1.6 +UEBTUPE**
This event is used during bonding with IO capability KeyboardOnly to indicate that a passkey is required from the user. User should respond to this event with the AT+UBTUPE command.

**Syntax**<br>
```+UEBTUPE:<bd_addr>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
#### **5.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+UBTC | Connect (ACL connection) |
| AT\+UBTDC | Disconnect (ACL disconnect) |
| AT\+UBTLN | Local Name |
| AT\+UBTD | Discovery |
| AT\+UBTBGD | Background Discovery |
| AT\+UBTRSS | Get RSSI |
| AT\+UBTCL | Connection List |
| AT\+UBTCST | Connection Status |
| AT\+UBTAD | Advertising Data |
| AT\+UBTA | Enable/Disable Advertisements. |
| AT\+UBTDA | Directed Advertisement |
| AT\+UBTCS | Connection Settings |
| AT\+UBTIOC | I/O Capabilities |
| AT\+UBTBSM | Bond security mode |
| AT\+UBTPM | Pairing mode |
| AT\+UBTUC | User confirmation |
| AT\+UBTUPE | User passkey entry |
| AT\+UBTB | Bond |
| AT\+UBTUB | Unbond |
| AT\+UBTBD | Read bonded devices |
| AT\+UBTDIS | Device Information Service |
###### **5.2.1 Connect (ACL connection) AT+UBTC**
Make an ACL connection to a remote device with defined protocol type. Unsolicited events +UUBTACLC or +UUBTACLD will be sent out to confirm the connection establishment.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTC=\<bd\_addr\> | Initiate connection. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
###### **5.2.2 Disconnect (ACL disconnect) AT+UBTDC**
Used to close a connection done with +UBTACLC.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTDC=\<conn\_handle\> | Close an existing ACL connection. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
###### **5.2.3 Local Name AT+UBTLN**
Set the local name used as device name for Bluetooth Classic, in the advertising data of the device and in the Device Information service for Bluetooth low energy.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTLN? | Reads the local Bluetooth device name. |
| AT\+UBTLN=\<device\_name\> | Writes the local Bluetooth device name. |

| Response | Description |
| ----------|----------|
| \+UBTLN:\<device\_name\> | Successful read response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| device\_name | string | For Bluetooth low energy the maximum size is 29 characters.<br><br>Valid length: 0..29 |
###### **5.2.4 Discovery AT+UBTD**
Performs a discovery procedure to find any advertising devices in the vicinity.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTD | Start discovery using default parameters |
| AT\+UBTD=\[\<discovery\_type\>\[,\<discovery\_mode\>\[,\<discovery\_length\>]]] | Start discovery. |

| Response | Description |
| ----------|----------|
| \+UBTD:\<bd\_addr\>,\<rssi\>,\<device\_name\>,\<data\_type\>,\<data\> | This response is sent for every found device. If no name is found, <device_name> is an empty string, if <mode> is set to Active, both Scan responses and Advertisements will be shown. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| discovery\_type | enumerator | Valid values:<br>0: All with no filter. Displays all found devices; devices can be displayed multiple times.<br>1: General inquiry. Displays devices in General or Limited discoverability mode; each device is displayed only once.<br>2: Discover all whitelisted devices.<br>3: Discover all whitelisted devices. Each device is displayed only once. |
| discovery\_mode | enumerator | Valid values:<br>0: (Default) Active discovery.<br>1: Passive, no scan reponse data will be recieved. |
| discovery\_length | integer | Timeout measured in milliseconds. Time range: 10 ms - 40 s, default 5000 ms<br><br>Valid values: 10..40000 |
| device\_name | string | Name of the discovered device. |
| data\_type | enumerator | Valid values:<br>0: Scan response data.<br>1: Advertise data. |
| data | byte\_array | Complete advertise/scan response data recieved from the remote device. |
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
| rssi | integer | Recieved signal strength in dBm. |
###### **5.2.5 Background Discovery AT+UBTBGD**
Start a background discovery.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTBGD=\<background\_discovery\_mode\> | Start/Stop background discovery |
| AT\+UBTBGD? | Read background discovery mode |

| Response | Description |
| ----------|----------|
| \+UBTBGD:\<background\_discovery\_mode\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| background\_discovery\_mode | enumerator | Valid values:<br>0: Set background discovery off<br>1: Set background discovery on |
###### **5.2.6 Get RSSI AT+UBTRSS**
Returns the current received RSSI for a specified Bluetooth connection.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTRSS=\<conn\_handle\> | Returns the current RSSI for a specified Bluetooth connection. |

| Response | Description |
| ----------|----------|
| \+UBTRSS:\<rssi\> | Successful response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| rssi | integer | Recieved signal strength in dBm. |
###### **5.2.7 Connection List AT+UBTCL**
List all active Bluetooth low energy ACl connections.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTCL | List all Bluetooth low energy ACL connections. |

| Response | Description |
| ----------|----------|
| \+UBTCL:\<conn\_handle\>,\<bd\_addr\> | Sent for every connection. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
###### **5.2.8 Connection Status AT+UBTCST**
Read negotiated properties of a Bluetooth low energy ACL connection.
 Some of the properties are a result of negotiation when a connections is set up, and this command gives the possibility to see what properties the connection actually uses.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTCST=\<conn\_handle\>\[,\<property\_id\>] | Read propertie(s) of an existing Bluetooth low energy ACL connection. If <property_id> is ommited all properties will be listed. |

| Response | Description |
| ----------|----------|
| \+UBTCST:\<property\_id\>,\<status\_val\> | Successful read response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| status\_val | integer | Value of the preceding property. |
| property\_id | enumerator | Valid values:<br>1: Connection inteval used on this connection. Range: 6 to 3200 \ Time = status_val * 1.25 ms \ Time range: 7.5 ms to 4000 ms<br>2: Peripheral latency for the connection in number of connection events. Range: 0 to 499<br>3: Supervision timeout (in ms) for this connections. Range: 100 ms to 32000 ms<br>4: MTU size for this connections.<br>5: Data Channel TX PDU Payload Length.<br>6: Data Channel RX PDU Payload Length.<br>7: Data Length Extension state. 0: Data Length Extension Off \ 1: Data Length Extension On<br>8: Local role in this connection. 1: Low Energy Central \ 2: Low Energy Peripheral<br>9: Current L2CAP mode. Possible values are: 1: Basic L2CAP mode \ 2: LE Credit Based Flow Control Mode |
| conn\_handle | integer | Connection handle of the Bluetooth low energy connection. |
###### **5.2.9 Advertising Data AT+UBTAD**
Command for using the custom advertising data in Bluetooth low energy. 
Any custom advertising data will be appended to the default mandatory flags field. 
Note that the AT command AT+UBTD supports scan modes that can be used to see the complete advertising data. 
This is useful when testing the advertising configurations set with the AT+UBTAD. 
By default, the service UUID for the u-blox Serial Port Service is part of the advertising data.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTAD=\<adv\_data\> | Write custom advertising data. |
| AT\+UBTAD? | Read custom advertising data. |

| Response | Description |
| ----------|----------|
| \+UBTAD:\<adv\_data\> | Successful read response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| adv\_data | byte\_array | Valid length: 2..255 |
###### **5.2.10 Enable/Disable Advertisements. AT+UBTA**
Command for enabling and disabling advertisements

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTA=\<mode\> | Set advertisements on or off. |
| AT\+UBTA? | Read advertisement mode. |

| Response | Description |
| ----------|----------|
| \+UBTA:\<mode\> | Successful read response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mode | enumerator | Valid values:<br>0: Set Bluetooth Advertisements off<br>1: Set Bluetooth Advertisements on |
###### **5.2.11 Directed Advertisement AT+UBTDA**
Start a directed advertisement to a given Bluetooth Address.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTDA=\<bd\_addr\> | Starts directed advertisements to Bluetooth Address. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
###### **5.2.12 Connection Settings AT+UBTCS**
Get and set connection related settings

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTCS0=\<connection\_interval\_minimum\> | Write connection interval minimum. |
| AT\+UBTCS0? | Read Connection Interval miniumum. |
| AT\+UBTCS1=\<connection\_interval\_maximum\> | Write connection interval maximum. |
| AT\+UBTCS1? | Read Connection Interval maximum. |
| AT\+UBTCS2=\<connection\_peripheral\_latency\> | Write connection peripheral latency. |
| AT\+UBTCS2? | Read connection peripheral latency. |
| AT\+UBTCS3=\<connection\_linkloss\_timeout\> | Write connection linkloss timeout. |
| AT\+UBTCS3? | Read connection linkloss timeout. |
| AT\+UBTCS? | Read all Bluetooth Configuration param values. |

| Response | Description |
| ----------|----------|
| \+UBTCS0:\<connection\_interval\_minimum\> | Successful read of connection interval minimum. |
| \+UBTCS1:\<connection\_interval\_maximum\> | Successful read of connection interval maximum. |
| \+UBTCS2:\<connection\_peripheral\_latency\> | Successful read of connection peripheral latency. |
| \+UBTCS3:\<connection\_linkloss\_timeout\> | Successful read of connection linkloss timeout. |
| \+UBTCS:\<param\>,\<value\> | Successful read response for AT+UBTCS. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| connection\_interval\_minimum | integer | Connection inteval minimum (must be <= Connection interval maximum). Final results will be a result of negotiation between devices.<br> Default: 24.<br> Calculation: connection_interval_minimum * 1.25. ms<br><br>Valid values: 6..3200 |
| connection\_interval\_maximum | integer | Connection inteval maximum (must be >= Connection interval minimum). Final results will be a result of negotiation between devices.<br> Default: 40.<br> Calculation: connection_interval_maximum * 1.25 ms.<br><br>Valid values: 6..3200 |
| connection\_peripheral\_latency | integer | Connection peripheral latency.<br> Default: 0<br> Calculation: Number of connection events.<br><br>Valid values: 0..500 |
| connection\_linkloss\_timeout | integer | Connection linkloss timeout.<br> Default: 2000<br> Calculation: connection_linkloss_timeout ms<br><br>Valid values: 100..32000 |
| param | enumerator | Connection parameter.<br><br>Valid values:<br>0: Connection interval minimum.<br>1: Connection interval maximum.<br>2: Connection peripheral latency.<br>3: Connection linkloss timeout. |
| value | integer | Value of connection parameter.<br><br>Valid values: 0..65535 |
###### **5.2.13 I/O Capabilities AT+UBTIOC**
Set Bluetooth I/O Capabilities, this impacts the possible bonding procedure between devices.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTIOC=\<io\_capabilities\> | Set I/O Capabilities |
| AT\+UBTIOC? | Read I/O Capabilities |

| Response | Description |
| ----------|----------|
| \+UBTIOC:\<io\_capabilities\> | Successful read response for AT+UBTIOC?. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| io\_capabilities | enumerator | Valid values:<br>0: Set I/O Capabilities to No Input No Output.<br>1: Set I/O Capabilities to Display Only.<br>2: Set I/O Capabilities to Display Yes/No<br>3: Set I/O Capabilities to Keyboard Only.<br>4: Set I/O Capabilities to Keyboard Display. |
###### **5.2.14 Bond security mode AT+UBTBSM**
Set the security mode of the device. This command works together with AT+UBTIOC to determine the bonding procedure used.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTBSM=\<bt\_security\_mode\> | Writes the security mode |
| AT\+UBTBSM? | Reads the security mode |

| Response | Description |
| ----------|----------|
| \+UBTBSM:\<bt\_security\_mode\> | Successful read response for AT+UBTBSM? |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bt\_security\_mode | enumerator | Valid values:<br>0: (Factory default) Security Disabled.<br>1: Allow unauthenticated bonding.<br>2: Only allow authenticated bonding.<br>3: Only allow authenticated bonding with encrypted Bluetooth link. Fallback to simple pairing if the remote side does not support secure connections.<br>4: Only allow authenticated bonding with encrypted Bluetooth link. Strictly uses secure connections. |
###### **5.2.15 Pairing mode AT+UBTPM**
Enable or disable pairing.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTPM=\<pairing\_mode\> | Writes the pairing mode. |
| AT\+UBTPM? | Read current pairing mode. |

| Response | Description |
| ----------|----------|
| \+UBTPM:\<pairing\_mode\> | Successful read response for AT+UBTPM? |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| pairing\_mode | enumerator | Valid values:<br>0: (Factory default) Disabled pairing mode.<br>1: Enable pairing mode. |
###### **5.2.16 User confirmation AT+UBTUC**
The user confirmation is used together with IO capability DisplayYesNo to repond to a user confirmation request (+UEBTUC). The command shall be used only after +UEUBTUC has been recieved.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTUC=\<bd\_addr\>,\<yes\_no\> | Respond to +UEUBTUC and confirm/deny bonding. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
| yes\_no | enumerator | Valid values:<br>0: Deny bonding.<br>1: Confirm bonding. |
###### **5.2.17 User passkey entry AT+UBTUPE**
The user passkey entry is used together with IO capability KeyboardOnly to respond on a user passkey entry request (+UEBTUPE). This command shall be used only after +UEBTUPE has been received.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTUPE=\<bd\_addr\>,\<yes\_no\>\[,\<passkey\>] | Respond to +UEBTUPE event and confirm/deny bonding. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| passkey | integer | Passkey used to confirm bonding, if yes_no is set to no, this can be omitted.<br><br>Valid values: 0..999999 |
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
| yes\_no | enumerator | Valid values:<br>0: Deny bonding.<br>1: Confirm bonding. |
###### **5.2.18 Bond AT+UBTB**
Performs a GAP bond procedure with another Bluetooth device. For some I/O Capabilities, user interaction is required during the bonding procedure. The procedure to use is determined by the I/O Capabilities and security mode.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTB=\<bd\_addr\> | Initiate bonding. To perform the bonding, the remote device must be in a pairable and connectable mode. Bond Event +UEBTB is genereated once the bond is complete. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
###### **5.2.19 Unbond AT+UBTUB**
Unbond from a previously bonded device. Note that this will remove the bond from the local device only.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTUB=\<bd\_addr\> | Removes a previously bonded device. The address FFFFFFFFFFFF will remove all the bonded devices. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
###### **5.2.20 Read bonded devices AT+UBTBD**
Reads the list of bonded devices.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTBD | Read list of bonded devices. |

| Response | Description |
| ----------|----------|
| \+UBTBD:\<bd\_addr\> | This response is sent for every found device. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| bd\_addr | bd\_addr | Bluetooth device address of the remote device. |
###### **5.2.21 Device Information Service AT+UBTDIS**
Write and read the module's Device Information Service (DIS) characteristics. The settings can be saved using AT&W.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTDIS=\<characteristic\_id\>\[,\<characteristic\_value\>] | Set a characterstic value. |
| AT\+UBTDIS? | Read all individual characterstic of the Device Information Service characteristics. |

| Response | Description |
| ----------|----------|
| \+UBTDIS:\<characteristic\_id\>,\<characteristic\_value\> | Successful read response. |
| \+UBTDIS:\<characteristic\_id\>,\<characteristic\_value\> | Successful read response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| characteristic\_id | enumerator | Valid values:<br>0: Manufacturer name string. Maximum length of the custom string is 31 characters.<br>1: Model name string. Maximum length of the custom string is 20 characters.<br>2: Firmware revision string. Maximum length of the custom string is 20 characters.<br>3: Software revision string. Maximum length of the custom string is 20 characters. |
| characteristic\_value | string | Value of Device Information Service characterstic. |
## **6 GATT Server**
GATT Server
#### **6.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UEBTGCW:\<conn\_handle\>,\<value\_handle\>,\<value\>,\<options\> |  |
| \+UEBTGRR:\<conn\_handle\>,\<value\_handle\> |  |
| \+UEBTGIC:\<conn\_handle\>,\<char\_handle\> |  |
###### **6.1.1 +UEBTGCW**
Unsolicited response code for GATT Client. This event is received when the remote side sends a notification.

**Syntax**<br>
```+UEBTGCW:<conn_handle>,<value_handle>,<value>,<options>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Handle of the connected device. |
| value\_handle | integer | Handle of the characteristic value. |
| value | byte\_array | The data as hex string. For example, 070809AABBCC |
| options | enumerator | Valid values:<br>0: Write without Response performed<br>1: Write with Response performed<br>2: Write long performed |
###### **6.1.2 +UEBTGRR**
Unsolicited response code for GATT Server. This event occurs when a remote client reads an attribute over the air. The event should be responded with AT+UBTGRR.

**Syntax**<br>
```+UEBTGRR:<conn_handle>,<value_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Handle of the connected device. |
| value\_handle | integer | Handle of the characteristic value. |
###### **6.1.3 +UEBTGIC**
Unsolicited response code for GATT Server. This event occurs when a remote GATT client confirms the receipt of an indication message made with +UBTGSI.

**Syntax**<br>
```+UEBTGIC:<conn_handle>,<char_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Handle of the connected device. |
| char\_handle | integer | Handle that identifies the characteristic value. |
#### **6.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+UBTGS | GATT Service define |
| AT\+UBTGC | GATT Characteristic define |
| AT\+UBTGHCC | GATT Host Controlled Characteristic |
| AT\+UBTGD | GATT Descriptor define |
| AT\+UBTGSA | GATT Service Acivate. |
| AT\+UBTGRRR | GATT Read Request Respond |
| AT\+UBTGNS | GATT Notification Send |
| AT\+UBTGIS | GATT Indication Send |
| AT\+UBTGAV | GATT Attribute Value |
| AT\+UBTGRRRE | GATT Read Request Respond with error code |
| AT\+UBTGWRE | GATT Write Respond with Error code |
| AT\+UBTGWRR | GATT Write Request Respond |
###### **6.2.1 GATT Service define AT+UBTGS**
Command to define a GATT service according to a 16-bit Service Assigned Number from Bluetooth SIG or a 128-bit user defined service number.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGS=\<uuid\> | Defines a service. |

| Response | Description |
| ----------|----------|
| \+UBTGS:\<ser\_handle\> | Successful write response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| uuid | byte\_array | UUID of service. This can be either 16 bit or 128 bit. |
| ser\_handle | integer | Handle of the created service. |
###### **6.2.2 GATT Characteristic define AT+UBTGC**
Command to add a GATT characteristic into the most recent GATT service record created with AT+UBTGS.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGC=\<uuid\>,\<properties\>,\<security\_read\>,\<security\_write\>,\<value\>\[,\<max\_length\>] | Creates a new characteristic into the GATT table for a GATT server. The CCCD for the characteristic, if applicable, is created here. Extended Properties such as CPFD, CUDD, and SCCD are not supported. |

| Response | Description |
| ----------|----------|
| \+UBTGC:\<value\_handle\>,\<cccd\_handle\> | Successful write response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| uuid | byte\_array | UUID of characteristic. This can be either 16 bit or 128 bit. |
| value | byte\_array | Default characteristic value before any value is pushed to the characteristic. A characteristic value can be 244 bytes long. |
| max\_length | integer | Maximum length of the characteristic in bytes. The maximum value is 244 bytes.<br><br>Valid values: 1..244 |
| value\_handle | integer | Handle of the added characteristic. |
| cccd\_handle | integer | Handle of the CCCD characteristic. This value is zero if there is no CCCD. |
| properties | byte\_array | Property value (a bit field): <br> Broadcast: 0x01 - If set, permits broadcasts of the Characteristic Value using Characteristic Configuration Descriptor. <br> Read: 0x02 - If set, permits reads of the Characteristic Value <br> Write Without Response: 0x04 - If set, permits Write of the Characteristic Value without response. <br> Write: 0x08 - If set, permits write of the Characteristic Value with response. <br> Notify: 0x10 - If set, permits notifications of a characteristic value. <br> Indicate: 0x20 - If set, permits indication of a characteristic value with acknoledgement. <br> Authenticated Signed Writes: 0x40 - If set, permits signed writes to the characteristic value. <br> Reserved Bit: 0x80 - Do not use. Reserved for future use.<br><br>Valid length: 1..1 |
| security\_read | enumerator | Valid values:<br>1: No encryption required.<br>2: Unauthenticated encryption required.<br>3: Authenticated encryption required. |
| security\_write | enumerator | Valid values:<br>1: No encryption required.<br>2: Unauthenticated encryption required.<br>3: Authenticated encryption required. |
###### **6.2.3 GATT Host Controlled Characteristic AT+UBTGHCC**
Creates a new host controlled characteristic into the GATT table for a GATT server. The CCCD for the characteristic, if applicable, is created here. Extended Properties such as CPFD, CUDD, and SCCD are not supported.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGHCC=\<uuid\>,\<properties\>,\<security\_read\>,\<security\_write\> | Define a characteristic. |

| Response | Description |
| ----------|----------|
| \+UBTGHCC:\<value\_handle\>,\<cccd\_handle\> | Successful write response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| uuid | byte\_array | UUID of characteristic. This can be either 16 bit or 128 bit. |
| value\_handle | integer | Handle of the added characteristic. |
| cccd\_handle | integer | Handle of the CCCD characteristic. This value is zero if there is no CCCD. |
| properties | byte\_array | Property value (a bit field): <br> Broadcast: 0x01 - If set, permits broadcasts of the Characteristic Value using Characteristic Configuration Descriptor. <br> Read: 0x02 - If set, permits reads of the Characteristic Value <br> Write Without Response: 0x04 - If set, permits Write of the Characteristic Value without response. <br> Write: 0x08 - If set, permits write of the Characteristic Value with response. <br> Notify: 0x10 - If set, permits notifications of a characteristic value. <br> Indicate: 0x20 - If set, permits indication of a characteristic value with acknoledgement. <br> Authenticated Signed Writes: 0x40 - If set, permits signed writes to the characteristic value. <br> Reserved Bit: 0x80 - Do not use. Reserved for future use.<br><br>Valid length: 1..1 |
| security\_read | enumerator | Valid values:<br>1: No encryption required.<br>2: Unauthenticated encryption required.<br>3: Authenticated encryption required. |
| security\_write | enumerator | Valid values:<br>1: No encryption required.<br>2: Unauthenticated encryption required.<br>3: Authenticated encryption required. |
###### **6.2.4 GATT Descriptor define AT+UBTGD**
Defines a vendor defined descriptor. Standard Bluetooth low energy descriptors such as CCCD are created while creating the characteristic in +UBTGC command.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGD=\<uuid\>,\<security\_read\>,\<security\_write\>,\<value\>\[,\<max\_length\>] | Define descriptor. |

| Response | Description |
| ----------|----------|
| \+UBTGD:\<desc\_handle\> | Successful write response. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| uuid | byte\_array | UUID of characteristic. This can be either 16 bit or 128 bit. |
| value | byte\_array | Descriptor value. This can be 23 bytes long. |
| max\_length | integer | Maximum length of the descriptor in bytes. The maximum value is 23 bytes.<br><br>Valid values: 1..23 |
| desc\_handle | integer | Handle of the created descriptor. |
| security\_read | enumerator | Valid values:<br>1: No encryption required.<br>2: Unauthenticated encryption required.<br>3: Authenticated encryption required. |
| security\_write | enumerator | Valid values:<br>1: No encryption required.<br>2: Unauthenticated encryption required.<br>3: Authenticated encryption required. |
###### **6.2.5 GATT Service Acivate. AT+UBTGSA**
Activates the service defined with the AT+UBTGS command. After this command is issued, it is not possible to add more characteristics or descriptors to the service.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGSA | Activate current defined service. |
###### **6.2.6 GATT Read Request Respond AT+UBTGRRR**
Responds to an unsolicited request to read (see +UEBTGRR) from a remote GATT client.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGRRR=\<conn\_handle\>,\<value\> | Responds to read request. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | GAP handle of the connected device. |
| value | byte\_array | Characteristic value. This can be 244 bytes long. |
###### **6.2.7 GATT Notification Send AT+UBTGNS**
Sends notifications to a remote client. This also updates the value of the characteristic.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGNS=\<conn\_handle\>,\<char\_handle\>,\<value\> | Send notification |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | GAP handle of the connected device. |
| char\_handle | integer | Characteristic value handle. |
| value | byte\_array | Characteristic value. The maximum length is the current MTU size - 3. |
###### **6.2.8 GATT Indication Send AT+UBTGIS**
Sends indication to a remote client. This also updates the value of the characteristic.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGIS=\<conn\_handle\>,\<char\_handle\>,\<value\> | Send notification |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | GAP handle of the connected device. |
| char\_handle | integer | Characteristic value handle. |
| value | byte\_array | Characteristic value. The maximum length is the current MTU size - 3. |
###### **6.2.9 GATT Attribute Value AT+UBTGAV**
Updates the value of an attribute. In case of characteristics which permit indications and notifications this command will update the value without sending any indications or notifications to the remote side.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGAV=\<attr\_handle\>,\<value\> | Set attribute value. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| attr\_handle | integer | Attribute handle. |
| value | byte\_array | Characterstic value. This can be 244 bytes long. |
###### **6.2.10 GATT Read Request Respond with error code AT+UBTGRRRE**
Responds to read request with application error code.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGRRRE=\<conn\_handle\>,\<error\_code\> | Respond with error code. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | GAP handle of connected device. |
| error\_code | byte\_array | Application error code. Allowed value range: 0x80-0x9F<br><br>Valid length: 1..1 |
###### **6.2.11 GATT Write Respond with Error code AT+UBTGWRE**
Responds to write operation with application error code.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGWRE=\<conn\_handle\>,\<error\_code\> | Respond with error code. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | GAP handle of connected device. |
| error\_code | byte\_array | Application error code. Allowed value range: 0x80-0x9F<br><br>Valid length: 1..1 |
###### **6.2.12 GATT Write Request Respond AT+UBTGWRR**
Accepts write request from peer.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UBTGWRR=\<conn\_handle\> | Respond to write request. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | GAP handle of connected device. |
## **7 Internet Protocols**
IP transport commands
Sockets are BSD sockets and their behaviour corresponds to this standard

#### **7.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UESOC:\<socket\_handle\> | Socket Connection Event |
| \+UESODA:\<socket\_handle\> | Socket Data Available event |
| \+UESOCL:\<socket\_handle\> | Socket Closed. |
| \+UESOIC:\<socket\_handle\>,\<remote\_ip\>,\<listening\_socket\_handle\> | Socket Incoming Connection event |
###### **7.1.1 +UESOC**
Event is sent out after a successfull connection to a remote peer (TCP only)

**Syntax**<br>
```+UESOC:<socket_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
###### **7.1.2 +UESODA**
Data is available to be read. This will be sent ou when using the buffered data mode

**Syntax**<br>
```+UESODA:<socket_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
###### **7.1.3 +UESOCL**
Event is sent out either when a socket was closed by the remote (or timed out) or when a connection to a remote peer has failed.
When this event is sent out the socket has been fully closed and cleaned up and the handle could be re-used.


**Syntax**<br>
```+UESOCL:<socket_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |

**Notes**<br>
If there is buffered data pending on the connection this event will not be sent out until all data is read.
###### **7.1.4 +UESOIC**
This event is sent when there is a incomming connection on the socket

**Syntax**<br>
```+UESOIC:<socket_handle>,<remote_ip>,<listening_socket_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| listening\_socket\_handle | integer | The handle of the new connected socket. Use this for any further operations on the connection |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
| remote\_ip | ip\_addr | The ip address of the remote peer |
#### **7.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+USOCR | Create Socket |
| AT\+USOC | Socket Connect |
| AT\+USOWS | Socket Write String |
| AT\+USOWH | Socket Write Hex |
| AT\+USOCL | Close socket |
| AT\+USORH | Socket Read Hex |
| AT\+USORS | Read Socket String |
| AT\+USOE | Socket Error |
| AT\+USOPA | Socket Peer Address |
| AT\+USOO | Socket Options |
###### **7.2.1 Create Socket AT+USOCR**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOCR=\<protocol\>\[,\<preferred\_protocol\_type\>] | Creates a socket and associates it with the specified protocol (TCP or UDP).<br> |

| Response | Description |
| ----------|----------|
| \+USOCR:\<socket\_handle\> | Successful creation of socket. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| protocol | enumerator | Protocol<br><br>Valid values:<br>6: TCP<br>17: UDP |
| preferred\_protocol\_type | enumerator | Selects the specific IP type.<br><br>Valid values:<br>0: IPv4<br>1: IPv6<br><br>Default value: 0 |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
###### **7.2.2 Socket Connect AT+USOC**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOC=\<socket\_handle\>,\<host\_address\>,\<remote\_port\> | Establish a peer-to-peer connection of the socket to the specified remote host on the given remote port<br><br>If the socket is a TCP socket, the command will perform the TCP negotiation<br>(3-way handshake) to open a connection.<br>If the socket is a UDP socket, this function will just declare the remote<br>host address and port for later use with other socket operations. This is important<br>to note because if <socket_handle> refers to a UDP socket, errors will not be reported prior to an attempt to write or<br>read data on the socket. This non blocking by default (unless socket is set to be blocking).<br>If a TCP socket is non blocking (default) a connection is not fully set up intil +UESOC URC is received<br>If socket is a UDP socket no +UESOC event will be sent since it is a connectionless protocol.<br> |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| host\_address | string | Remote host IP address or domain name of the remote host.<br><br>Valid length: 0..256 |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
| remote\_port | integer | The port of the remote peer<br><br>Valid values: 1..65535 |
###### **7.2.3 Socket Write String AT+USOWS**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOWS=\<socket\_handle\>,\<data\> | Writes the specified amount of data to the specified socket.<br>The command applies to UDP sockets (as well as TCP) after calling +USOCO. <br>This call is non blocking.<br>If socket is not ready to be written, generic negative error will be returned. <br>Check BSD errno (see BSD standard) by calling +USOE.<br> |

| Response | Description |
| ----------|----------|
| \+USOWS:\<socket\_handle\>,\<written\_length\> | Successful write response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| data | string | String to be written<br><br>Valid length: 1..1000 |
| written\_length | integer | Data length that was written. |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
###### **7.2.4 Socket Write Hex AT+USOWH**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOWH=\<socket\_handle\>,\<data\> | Writes the specified amount of data to the specified socket.<br><br>The command applies to UDP sockets (as wellas TCP) after calling +USOCO. <br>This call is non blocking.<br>If socket is not ready to be written, generic negative error will be returned. <br>Check BSD errno (see BSD standard) by calling +USOE.<br> |

| Response | Description |
| ----------|----------|
| \+USOWR:\<socket\_handle\>,\<written\_length\> | Successful write response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| data | byte\_array | Data bytes to be written.<br><br>Valid length: 1..500 |
| written\_length | integer | Data length that was actually written to socket. |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
###### **7.2.5 Close socket AT+USOCL**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOCL=\<socket\_handle\> | Closes the specified socket. <br>The command blocks the AT command interface until the completion of the socket close operation. <br>When this function returns OK the socket is cleaned up and fully closed. <br> |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
###### **7.2.6 Socket Read Hex AT+USORH**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USORH=\<socket\_handle\>,\<length\> | Reads the specified amount of data from the specified socket. <br>This call is non blocking.<br> |

| Response | Description |
| ----------|----------|
| \+USORH:\<socket\_handle\>,\<length\>,\<data\_bytes\> | Successful Read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| length | integer | Data bytes to to read.<br><br>Valid values: 1..500 |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
| data\_bytes | byte\_array | Raw data bytes |
###### **7.2.7 Read Socket String AT+USORS**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USORS=\<socket\_handle\>,\<length\> | Reads the specified amount of data from the specified socket. <br>This call is non blocking.<br>Note that the data should include no null terminator characters. <br> |

| Response | Description |
| ----------|----------|
| \+USORS:\<socket\_handle\>,\<length\>,\<string\_data\> | Successful Read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| length | integer | Data bytes to read.<br><br>Valid values: 1..1000 |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
| string\_data | string | Read data decoded as ascii chars |
###### **7.2.8 Socket Error AT+USOE**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOE | Retrieves the last error that occurred in any socket operation, stored in the socket errno. |

| Response | Description |
| ----------|----------|
| \+USOE:\<error\_code\> | Successful response. See BSD standard for error code definitions. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| error\_code | integer | Error code |
###### **7.2.9 Socket Peer Address AT+USOPA**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOPA=\<socket\_handle\> | Get the address of a connected peer. |

| Response | Description |
| ----------|----------|
| \+USOPA:\<socket\_handle\>,\<remote\_ip\>,\<remote\_port\> | The address |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
| remote\_ip | ip\_addr | The ip address of the remote peer |
| remote\_port | integer | The port of the remote peer<br><br>Valid values: 1..65535 |
###### **7.2.10 Socket Options AT+USOO**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USOO=\<socket\_handle\>,\<option\>,\<value\> | Set a socket option. See available options below. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| option | enumerator | Available options to set<br><br>Valid values:<br>0: Turn on/off No delay feature for TCP sockets. This will enable/disable the Nagle algorithm. This will make no difference if applied to UDP sockets. 0 = NO DELAY off (Nagle alg on), 1 = NO DELAY on (Nagle alg off)<br>1: Set socket to be blocking or non blocking. Sockets are non-blocking by default (Note that read/write will always be non-blocking). Can only be set while the socket is in a non connected state. 0 = off, 1 = on<br>2: Keep connections alive by sending keepalive probes. This specifies the time (in sec)  between keepalive packets. Only valid for TCP sockets<br>3: Set Keep Idle value for the socket. This specifies the amount of time (in sec) that the connection must be idle before sending keepalive probes (if keepalive is enabled). Only valid for TCP sockets<br>4: Set keep alive interval value for the socket. This is the time in seconds between two successive keepalive retransmissions. Only valid for TCP sockets<br>5: Set keep alive interval value for the socket. This is the time in seconds between two successive keepalive retransmissions. Only valid for TCP sockets |
| value | integer |  |
| socket\_handle | integer | Socket identifier to be used for any future operation on that socket. |
## **8 Mqtt**
Mqtt commands
#### **8.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UEMQC:\<mqtt\_id\> |  |
| \+UEMQDC:\<mqtt\_id\>,\<disconnect\_reason\> |  |
| \+UEMQD:\<mqtt\_id\>,\<message\_len\> |  |
###### **8.1.1 +UEMQC**
Connected to MQTT broker

**Syntax**<br>
```+UEMQC:<mqtt_id>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
###### **8.1.2 +UEMQDC**
Disconnected from MQTT Broker

**Syntax**<br>
```+UEMQDC:<mqtt_id>,<disconnect_reason>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| disconnect\_reason | integer | Disconnection reason. |
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
###### **8.1.3 +UEMQD**
MQTT Data available

**Syntax**<br>
```+UEMQD:<mqtt_id>,<message_len>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
| message\_len | integer | Lenght of the MQTT message |
#### **8.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+UMQCP | MQTT Connection Parameters |
| AT\+UMQC | MQTT Connect to broker |
| AT\+UMQLWT | MQTT Last Will and Testament |
| AT\+UMQTLS | MQTT TLS configuration |
| AT\+UMQDC | MQTT Disconnect |
| AT\+UMQP | MQTT Publish |
| AT\+UMQS | MQTT Subscribe |
| AT\+UMQR | Read MQTT message |
###### **8.2.1 MQTT Connection Parameters AT+UMQCP**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQCP=\<mqtt\_id\>,\<hostname\>,\<port\>\[,\<client\_id\>\[,\<keep\_alive\>\[,\<username\>\[,\<password\>]]]] | Sets the Mqtt login parameters |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| hostname | string | Hostname or ip address of the broker<br><br>Valid length: 0..128 |
| port | integer | The port of the broker<br><br>Valid values: 1..65535 |
| client\_id | string | Client id. Can be left empty to let the broker decide<br><br>Valid length: 0..128 |
| keep\_alive | integer | MQTT keepalive in seconds. If setting this to 0, no keepalive is used<br><br>Valid values: 0..65535<br><br>Default value: 60 |
| username | string | Valid length: 0..128 |
| password | string | Valid length: 0..128 |
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
###### **8.2.2 MQTT Connect to broker AT+UMQC**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQC=\<mqtt\_id\> | Connect to a broker using the mqtt config id. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
###### **8.2.3 MQTT Last Will and Testament AT+UMQLWT**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQLWT=\<mqtt\_id\>,\<topic\>,\<will\_msg\>\[,\<qos\>\[,\<retain\>]] | Add last will and testament configuration for client |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| will\_msg | string | Valid length: 0..256 |
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
| topic | string | Topic name or filter, (wildcard allowed)<br><br>Valid length: 0..256 |
| qos | enumerator | Qos for the message or topic<br><br>Valid values:<br>0: <br>1: <br>2: <br><br>Default value: 0 |
| retain | enumerator | Retain flag for messge<br><br>Valid values:<br>0: Do not retain message on broker<br><br>1: Retain message on broker<br><br>Default value: 0 |
###### **8.2.4 MQTT TLS configuration AT+UMQTLS**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQTLS=\<mqtt\_id\>,\<tls\_version\>,\<ca\_name\>\[,\<client\_cert\_name\>,\<client\_key\_name\>] | Setup mqtt tls config. Certs does not have to be uploaded untill connection |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| tls\_version | enumerator | Minimum TLS version to use<br><br>Valid values:<br>0: <br>12:  |
| ca\_name | string | Name of ca cert to use<br><br>Valid length: 1..32 |
| client\_cert\_name | string | Name of client cert to use<br><br>Valid length: 1..32 |
| client\_key\_name | string | Name of client private key to use<br><br>Valid length: 1..32 |
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
###### **8.2.5 MQTT Disconnect AT+UMQDC**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQDC=\<mqtt\_id\> | Disconnect the mqtt client form the broker. Note that the disconnection is not complete untill the +UEMQDC urc arrives |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
###### **8.2.6 MQTT Publish AT+UMQP**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQP=\<mqtt\_id\>,\<qos\>,\<retain\>,\<topic\>,\<message\> | Publish an MQTT message to the specified topic. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
| qos | enumerator | Qos for the message or topic<br><br>Valid values:<br>0: <br>1: <br>2: <br><br>Default value: 0 |
| retain | enumerator | Retain flag for messge<br><br>Valid values:<br>0: Do not retain message on broker<br><br>1: Retain message on broker<br><br>Default value: 0 |
| topic | string | Topic name or filter, (wildcard allowed)<br><br>Valid length: 0..256 |
| message | string | Mqtt message<br><br>Valid length: 0..730 |
###### **8.2.7 MQTT Subscribe AT+UMQS**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQS=\<mqtt\_id\>,\<subscribe\_action\>,\<topic\>\[,\<qos\>] | Subscribe or unsubscribe to/from MQTT topic |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| subscribe\_action | enumerator | Valid values:<br>0: Subscribe to topic<br>1: Unsubscribe from topic |
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
| topic | string | Topic name or filter, (wildcard allowed)<br><br>Valid length: 0..256 |
| qos | enumerator | Qos for the message or topic<br><br>Valid values:<br>0: <br>1: <br>2: <br><br>Default value: 0 |
###### **8.2.8 Read MQTT message AT+UMQR**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UMQR=\<mqtt\_id\>\[,\<all\>] | Read available MQTT message |

| Response | Description |
| ----------|----------|
| \+UMQR:\<mqtt\_id\>,\<num\_unread\>,\<topic\>,\<message\_len\>,\<message\> | Successful read response |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| all | enumerator | Valid values:<br>0: Read the oldest message<br>1: Read all available MQTT messsges, beginning with the oldest |
| num\_unread | integer | Number of available MQTT messages |
| mqtt\_id | integer | Mqtt config id<br><br>Valid values: 0..0 |
| topic | string | Topic name or filter, (wildcard allowed)<br><br>Valid length: 0..256 |
| message\_len | integer | Lenght of the MQTT message |
| message | string | Mqtt message<br><br>Valid length: 0..730 |
## **9 Security**
Security AT commands
#### **9.1 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+USECMNG | SSL/TLS certificates and private keys manager |
###### **9.1.1 SSL/TLS certificates and private keys manager AT+USECMNG**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USECMNG=\<op\_code\>\[,\<cert\_type\>\[,\<name\>\[,\<cert\>\[,\<password\>]]]] | Manages the X.509 certificates and private keys. Import, remove and list certificates and keys |

| Response | Description |
| ----------|----------|
| \+USECMNG:\<op\_code\>,\<cert\_type\>,\<name\> | Cert information |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| op\_code | enumerator | Valid values:<br>0: Upload cert in string form<br>2: Remove an uploaded certificates<br>3: List all the upploaded certificates |
| cert\_type | enumerator | Valid values:<br>0: Root certificate<br>1: Client certificate<br>2: Client private key |
| name | string | Valid length: 1..32 |
| cert | byte\_array | Valid length: 1..3072 |
| password | string | Decryption password; applicable only for PKCS8 encrypted client private keys.The maximum length is 64 characters.<br><br>Valid length: 1..64 |
## **10 SPS**
SPS
#### **10.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UESPSC:\<conn\_handle\> |  |
| \+UESPSDC:\<conn\_handle\> |  |
| \+UESPSDA:\<conn\_handle\>,\<data\> |  |
###### **10.1.1 +UESPSC**
Event response for SPS Connect. Upon a successful SPS connection, conn_handle will contain the connection handle of the remote peer.

**Syntax**<br>
```+UESPSC:<conn_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of remote peer |
###### **10.1.2 +UESPSDC**
Event response for SPS Connect. Upon a SPS disconnection, conn_handle will contain the connection handle of the remote peer.

**Syntax**<br>
```+UESPSDC:<conn_handle>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of remote peer |
###### **10.1.3 +UESPSDA**
Unsolicited event containing SPS data recieved from remote peer.

**Syntax**<br>
```+UESPSDA:<conn_handle>,<data>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of remote peer |
| data | byte\_array | SPS data |
#### **10.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+USPSC | SPS Connect |
| AT\+USPSE | SPS Enable |
| AT\+USPSW | SPS Write |
###### **10.2.1 SPS Connect AT+USPSC**
SPS connect on connected Bluetooth device

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USPSC=\<conn\_handle\>\[,\<flow\_control\>] | SPS connect on connected Bluetooth device |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of remote peer |
| flow\_control | integer | Flow control: 0 - no flow control, 1 - flow control |
###### **10.2.2 SPS Enable AT+USPSE**
Enables the SPS Service on the device, making it visible for remote peers.

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USPSE | Enables the SPS Service. |
###### **10.2.3 SPS Write AT+USPSW**
Write to a peer through SPS

**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+USPSW=\<conn\_handle\>,\<data\> | Write SPS data |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| conn\_handle | integer | Connection handle of remote peer which has SPS enabled |
| data | byte\_array | Data to send, max 244 bytes |
## **11 Diagnostics**
Diagnostics tools
#### **11.1 Unsolicited Response Codes**
| Unsolicited Response Code | Description |
| ----------|----------|
| \+UEDGP:\<transmitted\_packets\>,\<received\_packets\>,\<packet\_loss\_rate\>,\<avg\_response\_time\> |  |
###### **11.1.1 +UEDGP**
Ping complete event.

**Syntax**<br>
```+UEDGP:<transmitted_packets>,<received_packets>,<packet_loss_rate>,<avg_response_time>```

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| transmitted\_packets | integer | Total number of packets transmitted successfully. |
| received\_packets | integer | Total number of packets received successfully. |
| packet\_loss\_rate | integer | Packet loss rate in percentage between transmitted and received packets. |
| avg\_response\_time | integer | Average ping response time in milliseconds. |
#### **11.2 AT Commands**
| AT Command | Description |
| ----------|----------|
| AT\+UDGP | Send ping command. |
| AT\+UDGI | Diagnostics Iperf |
###### **11.2.1 Send ping command. AT+UDGP**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UDGP=\<destination\>,\<count\> | Sends a ping command to a destination address every second, repeating it (count) times. |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| destination | string | Destination host to send a ping call to in the form of IPv4 address (i.e. 192.168.1.10) or hostname (i.e. www.u-blox.com).<br><br>Valid length: 4..80 |
| count | integer | The number of pings (or packets) that will be transmitted.<br><br>Valid values: 1..65535 |
###### **11.2.2 Diagnostics Iperf AT+UDGI**


**Syntax**<br>
| AT Command | Description |
| ----------|----------|
| AT\+UDGI=\<iperf\_action\>,\<protocol\_type\>\[,\<role\>,\<port\>,\<report\_interval\>\[,\<time\_boundary\>,\<ip\_addr\>\[,\<bidirectional\>]]] | Start/stop IPERF 2 server/client |

**Defined values**<br>
| Parameter | Type | Description |
| ----------|----------|----------|
| iperf\_action | enumerator | Action<br><br>Valid values:<br>1: Start iperf<br>2: Stop iperf |
| protocol\_type | enumerator | IP protocol<br><br>Valid values:<br>1: TCP<br>2: UDP |
| role | enumerator | Role<br><br>Valid values:<br>1: Server<br>2: Client |
| port | integer | Port |
| report\_interval | integer | Report interval |
| time\_boundary | integer | Time boundary. Client only. Ignored if role is server |
| ip\_addr | ip\_addr | Ip address to connect to. Client only. Ignored if role is server |
| bidirectional | enumerator | Bidirectional flag. Client only. Ignored if role is server<br><br>Valid values:<br>0: Off<br>1: On<br>When starting biderectional tcp test, start server on both tester and dut, then start client with bidirectional flag on the dut.<br>If doing bidirectional UDP test, start server on both dut and tester and then start client with bidirectional flag on both<br> |

### Flags to use with yara

#### --no-warnings
- this flag will remove the warnings about certain strings slowing down scans when you scan with yara files, important if you just want the output
- example usage: **yara --no-warnings all_malware.yar mystery_php.php**

#### -s 
- this flag will provide the suspicious lines that caused the rule to be flagged when scanning a file
- typically, yara will only output the rule_name and the file_name but will not output the reason why the file was flagged, this is important if you would like to know what caused the file to be flagged as dangerous
- example usage: **yara -s test_rule.yar passwords.txt**
- example output without **-s**: 
	- `test_string passwords.txt`
- example output using **-s**: 
	- `test_string passwords.txt`
	- `0x9f62:$a: malware_test_string`
	
#### -r
- this flag is the recursive flag and will allow you to scan all files within a folder
- example usage: **yara -r all_malware.yar malware-samples/**
- this will use the rules provided in **all_malware.yar** to scan all files located within the **malware-samples** folder

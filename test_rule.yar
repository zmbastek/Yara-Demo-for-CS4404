rule malware_test_string
{
	strings:
		$a = "malware_test_string"
	
	condition:
		$a
}

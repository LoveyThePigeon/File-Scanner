from file_scanner import file_extension_check, file_scanner, contains_phrase, save_found, highlights
import pytest
import os
from termcolor import colored

def test_file_extension_check():
    assert file_extension_check("auth.log") == None
    with pytest.raises(ValueError) : file_extension_check("auth.l")


def test_file_scanner():
    assert file_scanner("auth.log", "authentication") == [{19: 'Jul 20 11:37:41 HOSTNAME lightdm[PID]: pam_unix(lightdm:auth): authentication failure; logname= uid=0 euid=0 tty=:0 ruser= rhost=  user=USERNAME'}, {24: 'Jul 20 11:37:36 HOSTNAME lightdm[PID]: pam_unix(lightdm:auth): authentication failure; logname= uid=0 euid=0 tty=:0 ruser= rhost=  user=USERNAME'}]


def test_contains_phrase():
    assert contains_phrase("'Jul 20 11:37:36 HOSTNAME lightdm[PID]: pam_unix(lightdm:auth): authentication failure; logname= uid=0 euid=0 tty=:0 ruser= rhost=  user=USERNAME'", "authentication failure") == True


def test_save_found():
    save_found([{19: 'Jul 20 11:37:41 HOSTNAME lightdm[PID]: pam_unix(lightdm:auth): authentication failure; logname= uid=0 euid=0 tty=:0 ruser= rhost=  user=USERNAME'}, {24: 'Jul 20 11:37:36 HOSTNAME lightdm[PID]: pam_unix(lightdm:auth): authentication failure; logname= uid=0 euid=0 tty=:0 ruser= rhost=  user=USERNAME'}],"test.json")
    assert os.path.exists("test.json")


def test_highlights():
    phrase_red = "10 Jul 20 11:37:53 HOSTNAME systemd[1]: session-c1.scope: "+ colored("Deactivated successfully","red") +"."
    assert highlights("10 Jul 20 11:37:53 HOSTNAME systemd[1]: session-c1.scope: Deactivated successfully.", "Deactivated successfully") == phrase_red

import subprocess

def windows_hello_auth():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-Command",
                "[Windows.Security.Credentials.UI.UserConsentVerifier]::RequestVerificationAsync('Secure File Access')"
            ],
            capture_output=True,
            text=True
        )
        return "Verified" in result.stdout
    except:
        return False

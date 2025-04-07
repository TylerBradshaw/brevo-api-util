from pkg import *
import brevo_python
import config

"""Utility package based on Brevo's API v3 Python Library. Found @ https://github.com/getbrevo/brevo-python/tree/main"""


configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = config.apiKey

def main():
    brevo_api_writer.SmsWriter.create_brevo_sms_campaign(configuration, "test", "test", "test", [2],None,None,"#TESTPFX","STOP")
    #brevo_api_writer.SmsWriter.delete_brevo_sms_campaign(configuration,5)
    #brevo_api_reader.ContactReader.get_brevo_contacts(configuration)
    #brevo_api_reader.AccountReader.get_brevo_account_activity(configuration)
    #brevo_api_writer.ContactWriter.create_brevo_contact(configuration, "test1@testorg.com", {'FIRSTNAME': 'TestF', 'LASTNAME': 'TestL1', 'SMS': '+10000000000'}, [2])
    #brevo_api_writer.ContactWriter.create_brevo_contact_list(configuration, "test_list", 3)

if __name__ == '__main__':
    main()

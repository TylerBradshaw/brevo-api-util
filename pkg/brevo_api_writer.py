import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint


class ContactWriter:

    @staticmethod
    def create_brevo_contact(configuration,
                             email = None,
                             attributes = None,
                             list_ids = None,
                             update_enabled = None,
                             ext_id = None,
                             email_blacklisted = None,
                             sms_blacklisted = None
                             ):
        """
            Creates new contact(s).

            :param configuration: The configuration object for the Brevo API.
            :param email: str | Email address of the user. Mandatory if SMS field is not passed in attributes.
                Example: 'test@testorg.com'
            :param attributes: dict(str, object) | The set of attributes and their values. These attributes must
                be present in the Brevo account.
                Example: {'FIRSTNAME': 'Test', 'LASTNAME': 'TestL', 'SMS': '+10000000000'}
            :param list_ids: list[int] | Ids of the lists to add the contact to.
                Example: [2] (Optional)
            :param update_enabled: bool | Facilitate updating the existing contact in the same request.
                Example: True (Optional)
            :param ext_id: str | Pass custom id to contact. (Optional)
            :param email_blacklisted: bool | Set this field to blacklist the contact for emails. (Optional)
            :param sms_blacklisted: bool | Set this field to blacklist the contact for SMS. (Optional)
            """
        api_instance = brevo_python.ContactsApi(brevo_python.ApiClient(configuration))

        kwargs = {}
        if email is not None:
            kwargs['email'] = email
        if attributes is not None:
            kwargs['attributes'] = attributes
        if list_ids is not None:
            kwargs['list_ids'] = list_ids
        if update_enabled is not None:
            kwargs['update_enabled'] = update_enabled
        if ext_id is not None:
            kwargs['ext_id'] = ext_id
        if email_blacklisted is not None:
            kwargs['email_blacklisted'] = email_blacklisted
        if sms_blacklisted is not None:
            kwargs['sms_blacklisted'] = sms_blacklisted

        create_contact = brevo_python.CreateContact(**kwargs)

        try:
            api_response = api_instance.create_contact(create_contact)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactsApi->create_contact: %s\n" % e)

    @staticmethod
    def delete_brevo_contact(configuration, identifier):
        """
            Deletes a contact.

            :param configuration: The configuration object for the Brevo API.
            :param identifier: str | Email (urlencoded) OR ID of the contact
                Example: 'test%40testorg.com'
            """
        api_instance = brevo_python.ContactsApi(brevo_python.ApiClient(configuration))

        try:
            api_instance.delete_contact(identifier)
        except ApiException as e:
            print("Exception when calling ContactsApi->delete_contact: %s\n" % e)


    @staticmethod
    def create_brevo_contact_list(configuration,
                                  name,
                                  folder_id):
        """
            Creates new contact list.

            :param configuration: The configuration object for the Brevo API.
            :param name: str | Name of the list.
                Example: 'test_list'
            :param folder_id: int | ID of the parent folder in which this list is to be created.
            """
        api_instance = brevo_python.ContactsApi(brevo_python.ApiClient(configuration))

        kwargs = {}

        if name is not None:
            kwargs['name'] = name
        if folder_id is not None:
            kwargs['folder_id'] = folder_id

        create_list = brevo_python.CreateList(**kwargs)

        try:
            api_response = api_instance.create_list(create_list)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactsApi->create_list: %s\n" % e)

    @staticmethod
    def create_brevo_contact_folder(configuration, name):
        """
            Creates new contact folder.

            :param configuration: The configuration object for the Brevo API.
            :param name: str | Name of the folder.
                Example: 'test_folder'
            """
        api_instance = brevo_python.ContactsApi(brevo_python.ApiClient(configuration))
        create_folder =brevo_python.CreateUpdateFolder(name)
        try:
            api_response = api_instance.create_folder(create_folder)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactsApi->create_folder: %s\n" % e)

    @staticmethod
    def import_brevo_contacts(configuration,
                                file_url = None,
                                file_body = None,
                                json_body = None,
                                list_ids = None,
                                notify_url = None,
                                new_list = None,
                                email_blacklist = False,
                                disable_notification = False,
                                sms_blacklist = False,
                                update_existing_contacts = True,
                                empty_contacts_attributes = False):
        """
            Imports Brevo contacts.

            :param configuration: The configuration object for the Brevo API.
            :param file_url: str | (Optional) Mandatory if fileBody or jsonBody is not defined. URL of the file to be imported (no local file).
                Possible file formats: .txt, .csv, .json
            :param file_body: str | (Optional)Mandatory if fileUrl and jsonBody is not defined. CSV content to be imported.
                Use semicolon to separate multiple attributes. Maximum allowed file body size is 10MB .
                However, we recommend a safe limit of around 8 MB to avoid the issues caused due to increase of file body size
                while parsing. Please use fileUrl instead to import bigger files.
            :param json_body: str| (Optional) Mandatory if fileUrl and fileBody is not defined. JSON content to be imported. Maximum allowed json body size is 10MB .
                However, we recommend a safe limit of around 8 MB to avoid the issues caused due to increase of json body size while parsing.
                Please use fileUrl instead to import bigger files.
            :param list_ids: list[int] | (Optional) Mandatory if newList is not defined. Ids of the lists in which the contacts shall be imported. For example, [2, 4, 7].
            :param notify_url: str | (Optional) URL that will be called once the import process is finished. For reference, https://help.brevo.com/hc/en-us/articles/360007666479
            :param new_list: RequestContactImportNewList | (Optional) Parameters: list_name: str | (Optional) List with listName will be created first and users will be imported in it (Mandatory if listIds is empty).
                folder_id int | (Optional) ID of the folder where this new list shall be created (Mandatory if listName is not empty).
            :param email_blacklist: bool | (Optional) Set this field to blacklist the contacts for emails. Defaults to False.
            :param disable_notification: bool | (Optional) Set this field to disable email notifications. Defaults to False.
            :param sms_blacklist: bool | (Optional) Set this field to blacklist the contacts for sms. Defaults to False.
            :param update_existing_contacts: bool | (Optional) Set this field to update existing contacts. Defaults to True.
            :param empty_contacts_attributes: bool | (Optional) To facilitate the choice to erase any attribute of the existing contacts with empty value.
                emptyContactsAttributes = true means the empty fields in your import will erase any attribute that currently contain data in Brevo, &
                emptyContactsAttributes = false means the empty fields will not affect your existing data ( only available if `updateExistingContacts` set to true )
            :return:
        """
        api_instance = brevo_python.ContactsApi(brevo_python.ApiClient(configuration))
        kwargs = {}
        if file_url is not None:
            kwargs['file_url'] = file_url
        if file_body is not None:
            kwargs['file_body'] = file_body
        if json_body is not None:
            kwargs['json_body'] = json_body
        if list_ids is not None:
            kwargs['list_ids'] = list_ids
        if notify_url is not None:
            kwargs['notify_url'] = notify_url
        if new_list is not None:
            kwargs['new_list'] = new_list
        if email_blacklist is not False:
            kwargs['email_blacklist'] = email_blacklist
        if disable_notification is not False:
            kwargs['disable_notification'] = disable_notification
        if sms_blacklist is not False:
            kwargs['sms_blacklist'] = sms_blacklist
        if update_existing_contacts is not True:
            kwargs['update_existing_contacts'] = update_existing_contacts
        if empty_contacts_attributes is not False:
            kwargs['empty_contacts_attributes'] = empty_contacts_attributes


        request_contact_import = brevo_python.RequestContactImport(**kwargs)

        try:
            api_response = api_instance.import_contacts(request_contact_import)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactsApi->import_contacts: %s\n" % e)


class SmsWriter:

    @staticmethod
    def create_brevo_sms_campaign(configuration,
                                  name = None,
                                  sender = None,
                                  content = None,
                                  list_ids = None,
                                  scheduled_at = None,
                                  unicode_enabled = None,
                                  organisation_prefix = None,
                                  unsubscribe_instruction = None):
        """
           Creates new SMS campaign

           :param configuration: The configuration object for the Brevo API.
           :param name: str | Name of the campaign.
               Example: "Test Alert Campaign"
           :param sender: str | Name of the sender. Up to 11 characters (alphanumeric) or 15 (numeric).
               Example: "Test"
           :param content: str | Content of the message. 160 characters per SMS. Longer will count as multiple SMS.
               Example: "This is a test campaign. Please Ignore"
           :param list_ids: list[int] | Lists Ids to send the campaign to. REQUIRED if scheduledAt is not empty
               Example: [2]
           :param scheduled_at: str | (Optional) UTC date-time on which the campaign will run (YYYY-MM-DDTHH:mm:ss.SSSZ).
               Example: "2025-01-31T17:00:00.000Z"
           :param unicode_enabled: bool | (Optional) Indicates whether the content should be treated as unicode.
               Example: False
           :param organisation_prefix: str | (Optional) A recognizable prefix (your Brand Name) before the message.
               Example: "#TESTPFIX"
           :param unsubscribe_instruction: str | (Optional) Instructions to unsubscribe (must include STOP).
               Example: "Reply STOP to unsubscribe"
           """
        api_instance = brevo_python.SMSCampaignsApi(brevo_python.ApiClient(configuration))
        kwargs = {}
        if name is not None:
            kwargs['name'] = name
        if sender is not None:
            kwargs['sender'] = sender
        if content is not None:
            kwargs['content'] = content
        if list_ids is not None:
            kwargs['recipients'] = brevo_python.CreateSmsCampaignRecipients(list_ids)
        if scheduled_at is not None:
            kwargs['scheduled_at'] = scheduled_at
        if unicode_enabled is not None:
            kwargs['unicode_enabled'] = unicode_enabled
        if organisation_prefix is not None:
            kwargs['organisation_prefix'] = organisation_prefix
        if unsubscribe_instruction is not None:
            kwargs['unsubscribe_instruction'] = unsubscribe_instruction
        create_sms_campaign = brevo_python.CreateSmsCampaign(**kwargs)

        try:
            api_response = api_instance.create_sms_campaign(create_sms_campaign)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SMSCampaignsApi->create_sms_campaign: %s\n" % e)

    @staticmethod
    def delete_brevo_sms_campaign(configuration, campaign_id):
        """
        Deletes an SMS campaign

        :param configuration: The configuration object for the Brevo API.
        :param campaign_id: int | The ID of the SMS campaign to be deleted.
            Example: 3
        """
        api_instance = brevo_python.SMSCampaignsApi(brevo_python.ApiClient(configuration))

        try:
            api_instance.delete_sms_campaign(campaign_id)
            print("Successfully deleted SMS Campaign %s" % campaign_id)
        except ApiException as e:
            print("Exception when calling SMSCampaignsApi->delete_sms_campaign: %s\n" % e)

    @staticmethod
    def get_brevo_sms_campaign(configuration, campaign_id):
        """
        Fetches an SMS campaign

        :param configuration: The configuration object for the Brevo API.
        :param campaign_id: int | The ID of the SMS campaign to be fetched.
            Example: 3
        """
        api_instance = brevo_python.SMSCampaignsApi(brevo_python.ApiClient(configuration))

        try:
            api_instance.get_sms_campaign(campaign_id)
            pprint(api_instance)
        except ApiException as e:
            print("Exception when calling SMSCampaignsApi->get_sms_campaign: %s\n" % e)

    @staticmethod
    def send_brevo_sms_report(configuration,
                              campaign_id = None,
                              send_report = None):

        api_instance = brevo_python.SMSCampaignsApi(brevo_python.ApiClient(configuration))

        kwargs = {}

        if campaign_id is not None:
            kwargs['campaign_id'] = campaign_id
        if send_report is not None:
            kwargs['send_report'] = send_report

        try:
            api_instance.send_sms_report(**kwargs)
            pprint(api_instance)
        except ApiException as e:
            print("Exception when calling SMSCampaignsApi->send_sms_report: %s\n" % e)

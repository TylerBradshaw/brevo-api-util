import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint


class AccountReader:

    @staticmethod
    def get_brevo_account(configuration):
        """
        Fetches account, plan, and credit information.

        :param configuration: The configuration object for the Brevo API.
        """
        api_instance = brevo_python.AccountApi(brevo_python.ApiClient(configuration))
        try:
            api_response = api_instance.get_account()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AccountApi->get_accounts: %s\n" % e)

    @staticmethod
    def get_brevo_account_activity(configuration,
        start_date = None,
        end_date = None,
        limit = None,
        offset = None
    ):
        """
            Fetches account activity based on optional filter criteria. Requires Enterprise account to use.

            :param configuration: The configuration object for the Brevo API.
            :param start_date: str | (Optional) Start date in UTC (YYYY-MM-DD) for filtering activity.
                Mandatory if end_date is used. Maximum range is one month.
                Example: "2025-01-01"
            :param end_date: str | (Optional) End date in UTC (YYYY-MM-DD) for filtering activity.
                Mandatory if start_date is used. Maximum range is one month.
                Example: "2025-01-31"
            :param limit: int | (Optional) Number of documents per page. Default is 10.
                Example: 10
            :param offset: int | (Optional) Index of the first document in the page. Default is 0.
                Example: 0
            """
        api_instance = brevo_python.AccountApi(brevo_python.ApiClient(configuration))

        kwargs = {}
        if start_date is not None:
            kwargs['start_date'] = start_date
        if end_date is not None:
            kwargs['end_date'] = end_date
        if limit is not None:
            kwargs['limit'] = limit
        if offset is not None:
            kwargs['offset'] = offset

        try:
            api_response = api_instance.get_account_activity(**kwargs)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AccountApi->get_account_activity: %s\n" % e)


class ContactReader:

    @staticmethod
    def get_brevo_contacts(configuration,
        limit=None,
        offset=None,
        modified_since=None,
        created_since=None,
        sort=None,
        segment_id=None,
        list_ids=None,
        filter=None
    ):
        """
        Fetches contacts based on optional filter criteria

        :param configuration: The configuration object for the Brevo API.
        :param limit: int | (Optional) Number of documents per page. Default is 50.
            Example: 50
        :param offset: int | (Optional) Index of the first document of the page. Default is 0.
            Example: 0
        :param sort: str | (Optional) Sort in ascending ('asc') or descending ('desc') order. Default is 'desc'.
            Example: 'desc'
        :param list_ids: list[int] | (Optional) Ids of the list. Either list_ids or segment_id can be passed.
            Example: [2]
        :param modified_since: str | (Optional) Filter contacts modified after a given UTC date-time
            (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
            Example: "2025-01-01T00:00:00.000Z"
        :param created_since: str | (Optional) Filter contacts created after a given UTC date-time
            (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
            Example: "2025-01-01T00:00:00.000Z"
        :param segment_id: int | (Optional) Id of the segment. Either list_ids or segment_id can be passed.
            Example: 789
        :param filter_str: str | (Optional) Filter contacts by attributes using the equals operator.
            e.g., `filter=equals(FIRSTNAME,"Tyler")`
            Example: 'equals(FIRSTNAME,"Test")'
        """
        api_instance = brevo_python.ContactsApi(brevo_python.ApiClient(configuration))

        kwargs={}
        if limit is not None:
            kwargs['limit'] = limit
        if offset is not None:
            kwargs['offset'] = offset
        if modified_since is not None:
            kwargs['modified_since'] = modified_since
        if created_since is not None:
            kwargs['created_since'] = created_since
        if sort is not None:
            kwargs['sort'] = sort
        if segment_id is not None:
            kwargs['segment_id'] = segment_id
        if list_ids is not None:
            kwargs['list_ids'] = list_ids
        if filter is not None:
            kwargs['filter'] = filter
        try:
            api_response = api_instance.get_contacts(**kwargs)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AccountApi->get_accounts: %s\n" % e)
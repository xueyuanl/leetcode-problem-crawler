from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def query(problem, query_str):
    url = 'https://leetcode.com/graphql'
    _transport = RequestsHTTPTransport(
        url=url,
        use_json=True,
        headers={"Content-type": "application/json"},
        verify=False

    )
    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,
    )
    params = {'titleSlug': problem}
    result = client.execute(gql(query_str), params)
    return result

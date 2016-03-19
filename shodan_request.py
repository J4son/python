import shodan,sys

SHODAN_API_KEY = "nKQx5VGqgryRvTNBbfg9SCAuQSs66IS2"
api = shodan.Shodan(SHODAN_API_KEY)
api.host('88.190.253.248')
try:
        # Search Shodan
        results = api.search('cisco page=1')

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
except shodan.APIError, e:
        print 'Error: %s' % e

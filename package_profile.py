#!/usr/bin/env python
"""
App to compare two Content Hosts
"""

import sys

try:
    import requests
except ImportError:
    print ("Please install the python-requests module.")
    sys.exit(-1)

# URL to your Satellite 6 server
URL = "https://sat64.local.domain"
SAT_API = "%s/api/v2/" % URL
# Default credentials to login to Satellite 6
USERNAME = "admin"
PASSWORD = "redhat"
# Ignore SSL for now
SSL_VERIFY = False


def get_json(location):
    """
    Performs a GET using the passed URL location
    """

    req = requests.get(location, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)

    return req.json()


def main():
    """
    Main Code
    """

    final_list = []

    # print("Type the First CH fqdn: ")
    first_fqdn = raw_input("Type the First CH fqdn: ")
    # first_fqdn = "node005.local.domain"
    # print("Type the Second CH fqdn: ")
    second_fqdn = raw_input("Type the Second CH fqdn: ")
    # second_fqdn = "refnode01.local.domain"
    ch1_id = get_json(SAT_API + "hosts/?search=" + first_fqdn)['results'][0]['id']
    ch1_pkg = get_json(SAT_API + "hosts/" + str(ch1_id) + "/packages?per_page=100000")

    ch2_id = get_json(SAT_API + "hosts/?search=" + second_fqdn)['results'][0]['id']
    ch2_pkg = get_json(SAT_API + "hosts/" + str(ch2_id) + "/packages?per_page=100000")

    # print("Package,Fist System,Second System,Difference")
    for pkg_ch1 in ch1_pkg['results']:
        for pkg_ch2 in ch2_pkg['results']:
            if(pkg_ch1['name'] == pkg_ch2['name']):
                # cont=cont+1
                # print("found package {}".format(pkg_ch1['name']))
                # print("CH1: {}, CH2: {}".format(pkg_ch1['nvra'],pkg_ch2['nvra']))
                # input("press ...")
                if(pkg_ch1['nvra'] != pkg_ch2['nvra']):
                    try:
                        ch1_v = pkg_ch1['nvra'].split(pkg_ch1['name'])[1].split("-")[1].replace(".", "").replace("k", "")
                        ch1_v_pretty = pkg_ch1['nvra'].split(pkg_ch1['name'])[1].split("-")[1]
                    except IndexError:
                        pass

                    try:
                        ch1_r = pkg_ch1['nvra'].split(pkg_ch1['name'])[1].split("-")[2].split(".")[0]
                    except IndexError:
                        pass

                    try:
                        ch2_v = pkg_ch2['nvra'].split(pkg_ch1['name'])[1].split("-")[1].replace(".", "").replace("k", "")
                        ch2_v_pretty = pkg_ch2['nvra'].split(pkg_ch2['name'])[1].split("-")[1]
                    except IndexError:
                        pass

                    try:
                        ch2_r = pkg_ch2['nvra'].split(pkg_ch1['name'])[1].split("-")[2].split(".")[0]
                    except IndexError:
                        pass

                    if(int(ch1_v) > int(ch2_v)):
                        # print("ch1 > ch2")
                        # print("greater on {}".format(first_fqdn))
                        # print("{},{},{},greater on {}".format(pkg_ch1['name'],ch1_v_pretty+"-"+ch1_r,ch2_v_pretty+"-"+ch2_r,first_fqdn))
                        stage = [pkg_ch1['name'], ch1_v_pretty+"-"+ch1_r, ch2_v_pretty+"-"+ch2_r, "greater on {}".format(first_fqdn)]
                        final_list.append(stage)
                    elif(int(ch1_v) < int(ch2_v)):
                        # print("ch1 < ch2")
                        # print("lower on {}".format(first_fqdn))
                        # print("{},{},{},lower on {}".format(pkg_ch1['name'],ch1_v_pretty+"-"+ch1_r,ch2_v_pretty+"-"+ch2_r,first_fqdn))
                        stage = [pkg_ch1['name'], ch1_v_pretty+"-"+ch1_r, ch2_v_pretty+"-"+ch2_r, "lower on {}".format(first_fqdn)]
                        final_list.append(stage)

                    elif(int(ch1_v) == int(ch2_v)):
                        # print("ch1 == ch2")
                        # print("## similar version on {} and {}".format(first_fqdn,second_fqdn))
                        if(int(ch1_r) > int(ch2_r)):
                            # print("greater on {}".format(first_fqdn))
                            # print("{},{},{},greater on {}".format(pkg_ch1['name'],ch1_v_pretty+"-"+ch1_r,ch2_v_pretty+"-"+ch2_r,first_fqdn))
                            stage = [pkg_ch1['name'], ch1_v_pretty+"-"+ch1_r, ch2_v_pretty+"-"+ch2_r, "greater on {}".format(first_fqdn)]
                            final_list.append(stage)

                        elif(int(ch1_r) < int(ch2_r)):
                            # print("lower on {}".format(first_fqdn))
                            # print("{},{},{},lower on {}".format(pkg_ch1['name'],ch1_v_pretty+"-"+ch1_r,ch2_v_pretty+"-"+ch2_r,first_fqdn))
                            stage = [pkg_ch1['name'], ch1_v_pretty+"-"+ch1_r, ch2_v_pretty+"-"+ch2_r, "lower on {}".format(first_fqdn)]
                            final_list.append(stage)

                    # ch2_v = pkg_ch2['nvra'].split("-")
                    # print("they are diff, {}: {}, {}: {}".format(first_fqdn,pkg_ch1['nvra'],second_fqdn,pkg_ch2['nvra']))
                    # print("")
                    # input("press ...")
            # if(cont==0):
                # print("Package {} only on CH1".format(pkg_ch1['name']))

    for pkg_ch1 in ch1_pkg['results']:
        count = 0
        for pkg_ch2 in ch2_pkg['results']:
            if(pkg_ch1['name'] == pkg_ch2['name']):
                count = count+1
                continue
                # input("here")

        if(count == 0):
            # print("package {} only on {}".format(pkg_ch1['name'],first_fqdn))
            ch1_v_pretty = pkg_ch1['nvra'].split(pkg_ch1['name'])[1].split("-")[1]
            ch1_r = pkg_ch1['nvra'].split(pkg_ch1['name'])[1].split("-")[2].split(".")[0]
            # print("{},{},-,only on {}".format(pkg_ch1['name'],ch1_v_pretty+"-"+ch1_r,first_fqdn))
            stage = [pkg_ch1['name'], ch1_v_pretty+"-"+ch1_r, "-", "only on {}".format(first_fqdn)]
            final_list.append(stage)

    for pkg_ch2 in ch2_pkg['results']:
        count = 0
        for pkg_ch1 in ch1_pkg['results']:
            if(pkg_ch2['name'] == pkg_ch1['name']):
                count = count+1
                continue
                # input("here")

        if(count == 0):
            # print("package {} only on {}".format(pkg_ch1['name'],first_fqdn))
            ch2_v_pretty = pkg_ch2['nvra'].split(pkg_ch2['name'])[1].split("-")[1]
            ch2_r = pkg_ch2['nvra'].split(pkg_ch2['name'])[1].split("-")[2].split(".")[0]
            # print("{},{},-,only on {}".format(pkg_ch2['name'],ch2_v_pretty+"-"+ch2_r,second_fqdn))
            stage = [pkg_ch2['name'], ch2_v_pretty+"-"+ch2_r, "-", "only on {}".format(second_fqdn)]
            final_list.append(stage)

    print("Package,Fist System,Second System,Difference")
    for result in final_list:
        print("{},{},{},{}".format(result[0], result[1], result[2], result[3]))

    # pass


if __name__ == "__main__":
    main()

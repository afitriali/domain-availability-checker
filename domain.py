#!/usr/bin/env python3

import sys
import whois

def find_available_domains(min_chars, max_chars, charset, tlds):
    domains = ['']
    for character in range(max_chars):
        domains = build_domain_list(domains, charset)
    check_availability(clean_list(domains,min_chars),tlds)

def build_domain_list(domains, charset):
    result = domains[:]
    for domain in domains:
        for index in range(len(charset)):
            result.append(domain + charset[index])
    return list(set(result))

def clean_list(list_items, min_chars):
    del list_items[list_items.index('')]
    list_items.sort()
    for list_item in list_items:
        if len(list_item) < min_chars:
            del list_items[list_items.index(list_item)]
    return list_items

def check_availability(domains, tlds):
    for tld in tlds:
        for domain in domains:
            domain = domain + '.' + tld
            sys.stdout.write('checking: ' + domain + '          ')
            sys.stdout.flush()
            sys.stdout.write('\r')
            sys.stdout.flush()
            if (domain_available(domain)):
                print(domain + ' might be available.')

# Can be more reliable if checking through an API.
def domain_available(domain):
    try:
        w = whois.whois(domain)
        if w['status'] == None:
            return True
    except:
        return False

try:
    min_chars = int(input("Enter the Min number of characters (int): "))
    max_chars = int(input("Enter the Max number of characters (int): "))
except:
    print("Error: Must be a number, try again. Exiting script.")
    sys.exit()
charset = input("Enter the character sets (string or alphabets if left empty): ")
tlds = input("Enter the TLDs (strings separated with space - e.g:- io com co): ")
tlds = tlds.split()
find_available_domains(min_chars, max_chars, charset if charset != '' else 'abcdefghijklmopqrstuvwxyz', tlds)

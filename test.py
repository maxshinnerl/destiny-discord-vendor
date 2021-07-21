import os
import requests

from enums import *
from EatYoWaffles import *

def get_headers():
    """
    Return headers dictionary with api key from .bash_profile
    """
    key = os.environ.get('DDV_API_KEY')
    headers = {"X-API-Key":key}
    return headers


def make_request(endpoint):
    """
    Given an endpoint, make request and return json
    """
    headers = get_headers()
    url = "https://www.bungie.net/platform/"
    url += endpoint

    r = requests.get(url, headers=headers)

    print(r)
    
    return r.json()

def get_vendor_inventory(vendor):
    """
    Given a vendor name, get current inventory
    """
    # NOTE: probably just gonna implement like one vendor for now but

if __name__=='__main__':


    # GOAL:
    #endpoint=Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/
    # GET VENDORS:
    #endpoint=Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/
    membershipType = membership_types['TigerSteam']
    xbox_membtype = membership_types['TigerXbox']
    destinyMembershipId = 6597792  # EatYoWaffles id


    #endpoint = f"User/GetMembershipsById/{destinyMembershipId}/{membershipType}"
    #endpoint = f"Destiny2/1/Profile/{xbox_membershipId}/?components=200"

    #endpoint=f"Destiny2/{xbox_membtype}/Profile/{xbox_membershipId}/Character/{hunter_characterId}/Vendors/?components=200,400,401,402"
    # I don't know why this gives an error sadly

    # TODO:
    """
    So we have an API key, but it's different from an access token (bearer).
    If I can figure out how to get that then it's gg
    but I'm over it right now
    """

    print(endpoint)
    res = make_request(endpoint)
    print(res)



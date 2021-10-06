# I hate this API.  ZERO examples ANYWHERE. Makes NO sense.

import os
import requests

from enums import *
from EatYoWaffles import *
from basics import *

def get_vendor_inventory(vendor):
    """
    Given a vendor name, get current inventory
    """
    # NOTE: probably just gonna implement like one vendor for now but


def get_weapon_stats(weapon=None):
    
    if weapon is None:
        # shouldn't need this, just for testing
        weapon = "The Palindrome"  # weapon name here

    endpoint = "Destiny2/Manifest" #/DestinyInventoryItemDefinition"
    r = make_request(endpoint)

    print(r['Response'].keys())

if __name__=='__main__':

    # get_weapon_stats()

   
    
    # NOTE: everything here down is the vendor stuff

    # GOAL:
    #endpoint=Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/
    # GET VENDORS:
    #endpoint=Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/
    #membershipType = membership_types['TigerSteam']
    #xbox_membtype = membership_types['TigerXbox']
    #destinyMembershipId = 6597792  # EatYoWaffles id


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

    #print(endpoint)
    #res = make_request(endpoint)
    #print(res)



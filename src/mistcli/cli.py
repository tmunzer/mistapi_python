import mistcli as mistcli
import sys


def _search_org(orgs, org_id):
    i = 0
    for org in orgs:
        if org['org_id'] == org_id:
            return i
        i+=1
    return None

def _test_choice(val, val_max):
    try:
        val_int = int(val)
        if val_int >= 0 and val_int <= val_max:
            return val_int
        else:
            return -1
    except:
        return -2

def select_org(mist_session:mistcli.Session, allow_many=False):
    i=-1
    org_ids = []
    resp_ids=[]
    data = mist_session.privileges
    data=sorted(data, key=lambda x: x["name"].lower())
    print("\r\nAvailable organizations:")
    for privilege in data:
        if privilege["scope"] == "org" and not privilege["org_id"] in org_ids:
            i+=1
            org_ids.append(privilege["org_id"])
            print(f"{i}) {privilege['name']} (id: {privilege['org_id']})")

    orgs_with_sites = []
    for privilege in data:
        if privilege["scope"] == "site" and not privilege["org_id"] in org_ids:
            index = _search_org(orgs_with_sites, privilege["org_id"])
            if index is None:
                i+=1
                org_ids.append(privilege["org_id"])
                print(f"{i}) {privilege['name']} (id: {privilege['org_id']})")
                orgs_with_sites.append({
                    "org_id": privilege["org_id"], 
                    "name": privilege["name"], 
                    "sites": [
                        {"site_id": privilege["site_id"], "name": privilege["name"]}
                        ]
                    })
            else:
                orgs_with_sites[index]["sites"].append({"site_id": privilege["site_id"], "name": privilege["name"]})

    if allow_many: resp = input(f"\r\nSelect an Org (0 to {i}, \"0,1\" for sites 0 and 1, \"a\" for all, or q to exit): ")
    else: resp = input(f"\r\nSelect an Org (0 to {i}, or q to exit): ")
    if resp == "q":
        sys.exit(0)
    elif resp.lower() == "a" and allow_many:
        return org_ids
    else:            
        resp = resp.split(",")
        if not allow_many and len(resp) > 1 :
            print(f"Only one org is allowed, you selected {len(resp)}")
            return select_org(mist_session, allow_many)
        for num in resp:
            tested_val = _test_choice(num, i)
            if tested_val >= 0:
                resp_ids.append(org_ids[tested_val])
            if tested_val == -1:
                print(f"{num} is not part of the possibilities.")
                return select_org(mist_session, allow_many)
            if tested_val == -2:
                print("Only numbers are allowed.")
                return select_org(mist_session, allow_many)
        return resp_ids


def select_site(mist_session:mistcli.Session, org_id=None, allow_many=False):
    i=-1
    site_ids=[]
    site_choices = []
    resp_ids=[]
    org_access = False

    if org_id is None:
        org_id = select_org(mist_session)[0]

    for privilege in mist_session.privileges:
        if privilege["scope"] == "org" and privilege["org_id"] == org_id:
            org_access = True
        if privilege["scope"] == "site" and privilege["org_id"] == org_id:
            site_choices.append({"id": privilege["site_id"], "name": privilege["name"]})

    if site_choices == [] or org_access == True:
        site_choices = mistcli.apis.orgs.sites.get(mist_session, org_id)['result']


    
    site_choices=sorted(site_choices, key=lambda x: x["name"].lower())
    print("\r\nAvailable sites:")
    for site in site_choices:        
        i+=1
        site_ids.append(site["id"])
        print(f"{i}) {site['name']} (id: {site['id']})")
    if allow_many: resp = input(f"\r\nSelect a Site (0 to {i}, \"0,1\" for sites 0 and 1, \"a\" for all, or q to exit): ")
    else: resp = input(f"\r\nSelect a Site (0 to {i}, or q to exit): ")

    if resp.lower() == "q":
        sys.exit(0)
    elif resp.lower() == "a" and allow_many:
        return site_ids
    else:                
        resp = resp.split(",")
        if not allow_many and len(resp) > 1 :
            print(f"Only one site is allowed, you selected {len(resp)}")
            return select_site(mist_session, org_id, allow_many)
        for num in resp:
            tested_val = _test_choice(num, i)
            if tested_val >= 0:
                resp_ids.append(site_choices[tested_val]["id"])
            if tested_val == -1:
                print(f"{num} is not part of the possibilities.")
                return select_site(mist_session, org_id, allow_many)
            if tested_val == -2:
                print("Only numbers are allowed.")
                return select_site(mist_session, org_id, allow_many)
        return resp_ids


    
def extract_field(json_data, field):   
    split_field = field.split(".")
    cur_field = split_field[0]
    next_fields = ".".join(split_field[1:])
    if cur_field in json_data:
        if len(split_field) > 1:
            return extract_field(json_data[cur_field], next_fields)
        else:
            return json_data[cur_field] 
    else:
        return "N/A"

def save_to_csv(csv_file, array_data, fields, csv_separator=","):
    print("saving to file...")
    with open(csv_file, "w") as f:
        for column in fields:
            f.write(f"{column},")
        f.write('\r\n')
        for row in array_data:
            for field in row:
                if field is None:
                    f.write("")
                else:
                    f.write(field)
                f.write(csv_separator)
            f.write('\r\n')



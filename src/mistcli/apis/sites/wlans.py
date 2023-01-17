from mistcli import Session

def get(mist_session:Session, site_id, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/wlans"
    resp = mist_session.mist_et(uri, page=page, limit=limit)
    return resp


def create(mist_session:Session, site_id, wlan_settings):
    uri = f"/api/v1/sites/{site_id}/wlans"
    resp = mist_session.mist_ost(uri, body=wlan_settings)
    return resp


def delete(mist_session:Session, site_id, wlan_id):
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}"
    resp = mist_session.mist_elete(uri)
    return resp


def add_portal_image(mist_session:Session, site_id, wlan_id, image_path):
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}/portal_image"
    f = open(image_path, 'rb')
    files = {'file': f.read()}
    resp = mist_session.mist_ost_file(uri, files=files)
    f.close()
    return resp


def delete_portal_image(mist_session:Session, site_id, wlan_id):
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}/portal_image"
    resp = mist_session.mist_elete(uri)
    return resp


def set_portal_template(mist_session:Session, site_id, wlan_id, portal_template_body):
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}/portal_template"
    body = portal_template_body
    resp = mist_session.mist_ut(uri, body=body)
    return resp


def report(mist_session:Session, site_id, fields):
    wlans = get(mist_session, site_id)
    result = []
    for wlan in wlans['result']:
        temp = []
        for field in fields:
            if field not in wlan:
                temp.append("")
            elif field == "auth":
                temp.append(str(wlan["auth"]["type"]))
            elif field == "auth_servers":
                string = ""
                for server_num, server_val in enumerate(wlan["auth_servers"]):
                    if "host" in server_val:
                        string += f"{server_val['host']}:{server_val['port']}"
                    else:
                        string += f"{server_val['ip']}:{server_val['port']}" 
                    if server_num < len(wlan["auth_servers"]) - 1:
                        string += " - "
                temp.append(string)
            elif field == "acct_servers":
                string = ""
                for server_num, server_val in enumerate(wlan["auth_servers"]):
                    if "host" in server_val:
                        string += f"{server_val['host']}:{server_val['port']}"
                    else:
                        string += f"{server_val['ip']}:{server_val['port']}" 
                    if server_num < len(wlan["acct_servers"]) - 1:
                        string += " - "
                temp.append(string)
            elif field == "dynamic_vlan":
                string = "Disabled"
                if wlan.get("dynamic_vlan", {"enabled": False})["enabled"] == True:
                    string = "default: "
                    if "default_vlan_id" in wlan["dynamic_vlan"]:
                        string += f"{wlan['dynamic_vlan']['default_vlan_id']} | others: " 
                    else:
                        string += "N/A | others: "
                    if wlan["dynamic_vlan"]["vlans"]:
                        for vlan_num, vlan_val in enumerate(wlan["dynamic_vlan"]["vlans"]):
                            string += f"{vlan_val}"
                            if vlan_num < len(wlan["dynamic_vlan"]["vlans"]) - 1:
                                string += " - "
                    else:
                        string += "None"
                temp.append(string)
            else:
                temp.append(f"{wlan[field]}")
        result.append(temp)
    return result

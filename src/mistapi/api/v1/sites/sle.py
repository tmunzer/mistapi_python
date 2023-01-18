from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteSleClassifierDetails(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, classifier:str, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleClassifierDetails
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics
    :param str classifier        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/classifier/{classifier}/summary"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleMetricClassifiers(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleMetricClassifiers
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric -  values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/classifiers"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleHistogram(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleHistogram
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/histogram"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactSummary(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", fields:str=None, classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactSummary
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str fields(wlan, device_type, device_os, band, ap, server, mxedge, switch, client, vlan, interface, chassis, gateway, peer_path, gateway_zones)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impact-summary"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if fields: query_params["fields"]=fields
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedApplications(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedApplications
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-applications"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedAps(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedAps
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-aps"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedChassis(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedChassis
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-chassis"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedWiredClients(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedWiredClients
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-clients"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedGateways(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedGateways
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-gateways"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedInterfaces(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedInterfaces
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-interfaces"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedSwitches(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedSwitches
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-switches"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleImpactedWirelessClients(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleImpactedWirelessClients
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str classifier        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-users"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleSummary(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleSummary
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/summary"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSleThreshold(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSleThreshold
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/threshold"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def replaceSiteSleThreshold(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/replaceSiteSleThreshold
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/threshold"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateSiteSleThreshold(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteSleThreshold
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id
    :param str metric - values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/threshold"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def getSiteSlesMetrics(mist_session:_APISession, site_id:str, scope:str, scope_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSlesMetrics
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str scope
    :param str scope_id        
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
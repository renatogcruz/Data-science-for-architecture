import json
import operator

try:
    import urllib2
    urlopen = urllib2.urlopen
except:
    import urllib.request
    urlopen = urllib.request.urlopen

class api:
    """
    A minimal BIMserver.org API client. Interfaces are obtained from the server
    and can be retrieved as attributes from an API instance. The interfaces 
    expose their methods as functions with keyword arguments.
    
    Example:
    import bimserver
    client = bimserver.api(server_address, username, password)
    client.Bimsie1ServiceInterface.addProject(projectName="My new project")
    """
    
    class interface:
        def __init__(self, api, name):
            self.api, self.name = api, name
            
        def make_request(self, method, **kwargs):
            request = urlopen(self.api.url, data=json.dumps(dict({
                "request": {
                    "interface": self.name,
                    "method": method,
                    "parameters": kwargs
                }
            }, **({"token":self.api.token} if self.api.token else {}))).encode("utf-8"))
            response = json.loads(request.read().decode("utf-8"))
            exception = response.get("response", {}).get("exception", None)
            if exception:
                raise Exception(exception['message'])
            else: return response["response"]["result"]
            
        def __getattr__(self, method):
            return lambda **kwargs: self.make_request(method, **kwargs)
            
            
    token = None
    interfaces = None
    
    def __init__(self, hostname, username=None, password=None):
        self.url = "%s/json" % hostname
        if not hostname.startswith('http://') and not hostname.startswith('https://'):
            self.url = "http://%s" % self.url
            
        self.interfaces = set(map(
            operator.itemgetter("simpleName"), 
            self.MetaInterface.getServiceInterfaces()
        ))
        
        self.version = "1.4" if "Bimsie1AuthInterface" in self.interfaces else "1.5"
        
        if username is not None and password is not None:
            auth_interface = getattr(self, "Bimsie1AuthInterface", getattr(self, "AuthInterface"))
            self.token = auth_interface.login(
                username=username,
                password=password
            )            
            
    def __getattr__(self, interface):
        if self.interfaces is not None and interface not in self.interfaces:
        
            # Some form of compatibility:
            if self.version == "1.4" and not interface.startswith("Bimsie1"):
                return self.__getattr__("Bimsie1" + interface)
            elif self.version == "1.5" and interface.startswith("Bimsie1"):
                return self.__getattr__(interface[len("Bimsie1"):])
                
            raise AttributeError("'%s' is does not name a valid interface on this server" % interface)
        return api.interface(self, interface)
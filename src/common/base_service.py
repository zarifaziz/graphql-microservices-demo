from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseService(ABC):
    """
    Abstract base class for microservices.
    
    Parameters
    ----------
    host : str
        The host address of the service
    port : int
        The port number the service runs on
    """
    
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
    
    @abstractmethod
    def health_check(self) -> Dict[str, Any]:
        """
        Health check endpoint for the service.
        
        Returns
        -------
        Dict[str, Any]
            Service health status
        """
        pass 
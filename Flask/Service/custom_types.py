from enum import (StrEnum)

class Status(StrEnum):

    received = "received" 

    diagnosing = "diagnosing" 

    repairing = "repairing" 

    ready = "ready" 

    delivered = "delivered" 
    
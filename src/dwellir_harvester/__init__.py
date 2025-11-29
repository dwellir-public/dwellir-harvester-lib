"""Collectors for gathering node metadata.

This package provides base classes for creating collectors and specific collector
implementations for different blockchain clients and system information.
"""
# Base classes
from .collector_base import (
    BlockchainCollector,
    GenericCollector,
    CollectorError,
)

# Re-export collectors so the framework can discover them by import.
from .collectors.null import NullCollector
from .collectors.dummychain import DummychainCollector
from .collectors.host import HostCollector
from .collectors.juju import JujuCollector
# from .collectors.substrate import SubstrateCollector

# What this package exports
__all__ = [
    # Base classes
    "BlockchainCollector",
    "GenericCollector",
    "CollectorError",
    
    # Concrete collectors
    "NullCollector",
    "DummychainCollector",
#    "PolkadotCollector",
    "HostCollector",
    "JujuCollector"
]
